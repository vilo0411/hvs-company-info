import os
import re
from pathlib import Path

# Configuration
CONTENT_DIR = Path("content/blog/3-finalized")
OUTPUT_FILE = Path("seo-strategy/content-plan/internal-link-dashboard.md")
INDEX_FILE = Path("seo-strategy/content-plan/anchor-index.md")

# Regex
LINK_REGEX = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
YAML_REGEX = re.compile(r'^---\s*(.*?)\s*---\s*', re.DOTALL)

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
    files = list(CONTENT_DIR.glob("*.md"))
    data = {}

    for file_path in files:
        rel_path = file_path.name
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if rel_path not in data:
            data[rel_path] = {"out_links": [], "in_links": []}

        links = LINK_REGEX.findall(content)
        for anchor, url in links:
            if "Final-" in url:
                dest_file = os.path.basename(url)
                data[rel_path]["out_links"].append({"anchor": anchor, "dest": dest_file})
                
                if dest_file not in data:
                    data[dest_file] = {"out_links": [], "in_links": []}
                data[dest_file]["in_links"].append({"anchor": anchor, "source": rel_path})

    # Generate Report
    report = "# Internal Linking Dashboard\n"
    report += "> Tự động cập nhật bởi `link_audit.py` | " + os.popen("date /t").read().strip() + "\n"
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

    os.makedirs(OUTPUT_FILE.parent, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Audit completed. Report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    audit()
