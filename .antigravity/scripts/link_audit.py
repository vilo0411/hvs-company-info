import json
import os
import re
import sys
from pathlib import Path

# Force UTF-8 encoding for standard output to avoid UnicodeEncodeErrors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Configuration
CONTENT_DIR = Path("content/blog/3-finalized")
OUTPUT_FILE = Path("seo-strategy/content-plan/internal-link-dashboard.md")
INDEX_FILE = Path("seo-strategy/content-plan/anchor-index.md")
SITEMAP_CACHE_FILE = Path(__file__).parent / "sitemap-cache.json"

# Regex
LINK_REGEX = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
YAML_REGEX = re.compile(r'^---\s*(.*?)\s*---\s*', re.DOTALL)
# Matches a "Final-xxx.md" filename embedded anywhere in a broken/legacy-style URL
# (file:///..., relative content/blog/..., ../..., or a bare Final-xxx.md)
LEGACY_TARGET_REGEX = re.compile(r'(Final-[a-z0-9\-]+)\.md')


def load_sitemap_cache() -> dict:
    """Load slug_map từ sitemap-cache.json (nếu có)."""
    if not SITEMAP_CACHE_FILE.exists():
        return {}
    with open(SITEMAP_CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)
    return cache.get("slug_map", {})


def resolve_dest_file(url: str, slug_map: dict) -> tuple[str | None, bool]:
    """
    Xác định file đích (Final-slug.md) mà 1 link trỏ tới, bất kể format URL.
    Trả về (dest_file, is_broken_format).
    - Absolute production URL đúng chuẩn (https://taichinhso.hvsvn.com/.../slug) -> not broken.
    - file://, relative path, hoặc URL không có trong sitemap -> broken (cần sửa).
    """
    # Case 1: legacy/broken formats that embed "Final-xxx.md" directly
    legacy_match = LEGACY_TARGET_REGEX.search(url)
    if legacy_match:
        dest_file = f"{legacy_match.group(1)}.md"
        is_absolute_prod_url = url.startswith("https://taichinhso.hvsvn.com/")
        return dest_file, not is_absolute_prod_url

    # Case 2: absolute production URL -> reverse-lookup slug in sitemap cache
    if url.startswith("https://taichinhso.hvsvn.com/"):
        slug = url.rstrip("/").split("/")[-1]
        if slug in slug_map:
            return f"Final-{slug}.md", False
        # Slug not in sitemap: dest article likely not published, or slug mismatch
        return None, False

    return None, False

def get_anchor_index():
    index = {} # filename -> {exact: "", partial: []}
    if not INDEX_FILE.exists():
        return index
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if "|" in line and "[" in line:
                # Basic table row parsing
                cells = [c.strip() for c in line.split("|")]
                if len(cells) >= 4:
                    # Cell 1: [Filename](Path)
                    file_match = re.search(r'\[(.*?)\]', cells[1])
                    if file_match:
                        filename = file_match.group(1)
                        exact = cells[2].lower()
                        partials = [p.strip().lower() for p in cells[3].split(",")]
                        index[filename] = {"exact": exact, "partial": partials}
    return index

def classify_anchor(anchor, filename, index):
    anchor_clean = anchor.lower().strip()
    entry = index.get(filename, {})
    
    if anchor_clean == entry.get("exact", ""):
        return "Exact"
    if anchor_clean in entry.get("partial", []):
        return "Partial"
    
    # Fallback: simple keyword check if not in index
    exact_fallback = entry.get("exact", "")
    if exact_fallback and exact_fallback in anchor_clean:
        return "Partial"
        
    return "Generic/Title"

def audit():
    index = get_anchor_index()
    slug_map = load_sitemap_cache()
    files = list(CONTENT_DIR.glob("*.md"))
    data = {}
    broken_links = []  # [(source_file, anchor, url)]

    for file_path in files:
        rel_path = file_path.name
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if rel_path not in data:
            data[rel_path] = {"out_links": [], "in_links": []}

        links = LINK_REGEX.findall(content)
        for anchor, url in links:
            dest_file, is_broken = resolve_dest_file(url, slug_map)
            if dest_file is None:
                continue

            data[rel_path]["out_links"].append({"anchor": anchor, "dest": dest_file})

            if dest_file not in data:
                data[dest_file] = {"out_links": [], "in_links": []}
            data[dest_file]["in_links"].append({"anchor": anchor, "source": rel_path})

            if is_broken:
                broken_links.append((rel_path, anchor, url))

    # Generate Report
    from datetime import datetime
    report = "# Internal Linking Dashboard\n"
    report += "> Tự động cập nhật bởi `link_audit.py` | " + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n"
    report += "> Dựa trên quy tắc tại `anchor-index.md` (Exact / Partial / Title)\n\n"
    report += "| Bài viết (File) | Out | In | Phân bổ In-links (E/P/T) | Tình trạng |\n"
    report += "| :--- | :---: | :---: | :--- | :--- |\n"

    for file_name in sorted(data.keys()):
        stats = data[file_name]
        out_count = len(stats["out_links"])
        in_count = len(stats["in_links"])
        
        exact = 0
        partial = 0
        title = 0
        
        for il in stats["in_links"]:
            cls = classify_anchor(il["anchor"], file_name, index)
            if cls == "Exact": exact += 1
            elif cls == "Partial": partial += 1
            else: title += 1
            
        total_in = exact + partial + title
        ratio_str = "0/0/0"
        if total_in > 0:
            ratio_str = f"{exact/total_in:.0%}/{partial/total_in:.0%}/{title/total_in:.0%}"
            
        health = "✅ Healthy"
        if total_in > 0 and (exact/total_in) > 0.15:
            health = "⚠️ Over-opt"
        elif total_in < 3 and total_in > 0:
            health = "🔍 Needs more"
        elif total_in == 0:
            health = "⭕ New"

        report += f"| `{file_name}` | {out_count} | {in_count} | {ratio_str} | {health} |\n"

    if broken_links:
        report += f"\n## ⚠️ Broken-format links ({len(broken_links)})\n"
        report += "> Link không dùng URL tuyệt đối chuẩn (`https://taichinhso.hvsvn.com/...`) — sẽ hỏng khi publish. Cần sửa lại bằng `fetch_sitemap.py --slug [slug]`.\n\n"
        report += "| Bài nguồn | Anchor | URL hiện tại |\n"
        report += "| :--- | :--- | :--- |\n"
        for source, anchor, url in broken_links:
            report += f"| `{source}` | {anchor} | `{url}` |\n"

    os.makedirs(OUTPUT_FILE.parent, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Audit completed. Report saved to {OUTPUT_FILE}")
    if broken_links:
        print(f"WARNING: {len(broken_links)} broken-format internal links found (see report).")

if __name__ == "__main__":
    audit()
