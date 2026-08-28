"""
fetch_sitemap.py — Tải sitemap và build slug→URL map cho internal linking HVS Tài chính số

Usage:
    python .antigravity/scripts/fetch_sitemap.py
    python .antigravity/scripts/fetch_sitemap.py --refresh
    python .antigravity/scripts/fetch_sitemap.py --slug ty-gia-la-gi
    python .antigravity/scripts/fetch_sitemap.py --search "chứng khoán"
    python .antigravity/scripts/fetch_sitemap.py --suggest "dxy"
    python .antigravity/scripts/fetch_sitemap.py --validate content/blog/3-finalized/Final-ty-gia-la-gi.md

Output:
    .antigravity/scripts/sitemap-cache.json  (được cập nhật tự động)
"""

import json
import re
import sys
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

# Force UTF-8 encoding for standard output to avoid UnicodeEncodeErrors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

SITEMAP_URL = "https://taichinhso.hvsvn.com/sitemap.xml"
CACHE_FILE = Path(__file__).parent / "sitemap-cache.json"
CACHE_MAX_AGE_HOURS = 24  # Tự động refresh nếu cache > 24h


def remove_accents(input_str: str) -> str:
    """Chuyển chuỗi tiếng Việt có dấu thành không dấu dạng kebab/token."""
    nfkd = unicodedata.normalize('NFKD', input_str)
    no_accent = ''.join([c for c in nfkd if not unicodedata.combining(c)])
    no_accent = re.sub(r'[đĐ]', 'd', no_accent)
    return no_accent.lower()


def fetch_sitemap() -> list[str]:
    """Tải sitemap XML và trả về list URL."""
    print(f"Fetching sitemap: {SITEMAP_URL}")
    try:
        req = urllib.request.Request(
            SITEMAP_URL,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) HVS-LinkAuditor/1.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_content = resp.read()
    except Exception as e:
        print(f"ERROR: Cannot fetch sitemap — {e}")
        # If cache exists, fall back to cache
        if CACHE_FILE.exists():
            print("Falling back to existing cache file.")
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return list(json.load(f).get("slug_map", {}).values())
        sys.exit(1)

    # Parse XML (namespace-aware)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(xml_content)
    urls = [loc.text.strip() for loc in root.findall(".//sm:loc", ns) if loc.text]
    print(f"Found {len(urls)} URLs in sitemap.")
    return urls


def build_cache(urls: list[str]) -> dict:
    """Build slug→URL map từ danh sách URL."""
    slug_map = {}
    for url in urls:
        path = url.rstrip("/").split("https://taichinhso.hvsvn.com", 1)[-1]
        slug = path.rstrip("/").split("/")[-1]
        if slug and slug not in slug_map:
            slug_map[slug] = url

    cache = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_urls": len(urls),
        "slug_map": slug_map,
        "urls": sorted(urls),
    }
    return cache


def load_cache(force_refresh: bool = False) -> dict:
    """Load cache từ file nếu còn mới, hoặc fetch mới nếu cần."""
    if not force_refresh and CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cache = json.load(f)
            fetched_at = datetime.fromisoformat(cache.get("fetched_at", "2000-01-01T00:00:00+00:00"))
            age_hours = (datetime.now(timezone.utc) - fetched_at).total_seconds() / 3600
            if age_hours <= CACHE_MAX_AGE_HOURS:
                return cache
            print(f"Cache is {age_hours:.1f}h old (> {CACHE_MAX_AGE_HOURS}h). Refreshing...")
        except Exception:
            pass

    urls = fetch_sitemap()
    cache = build_cache(urls)
    save_cache(cache)
    return cache


def save_cache(cache: dict):
    """Lưu cache ra file JSON."""
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    print(f"Cache saved: {CACHE_FILE} ({cache['total_urls']} URLs)")


def lookup_slug(slug: str, cache: dict) -> str | None:
    """Tra slug chính xác → full URL từ cache."""
    return cache["slug_map"].get(slug.strip().lower())


def search_links(query: str, cache: dict, limit: int = 10) -> list[tuple[str, str, float]]:
    """
    Tìm kiếm và gợi ý các link phù hợp từ sitemap dựa trên query.
    Trả về [(slug, full_url, score)]
    """
    raw_q = query.strip().lower()
    clean_q = remove_accents(raw_q)
    tokens = [t for t in re.split(r'[\s\-_]+', clean_q) if len(t) > 1 and t not in ["la", "gi", "cua", "va", "cho", "cac", "nhung", "trong"]]

    results = []
    for slug, url in cache["slug_map"].items():
        score = 0.0
        slug_clean = remove_accents(slug)

        # Exact slug match
        if slug_clean == clean_q or slug_clean == raw_q:
            score += 100.0
        # Substring match
        elif clean_q in slug_clean:
            score += 50.0 + (len(clean_q) / max(len(slug_clean), 1)) * 20.0
        elif slug_clean in clean_q:
            score += 40.0
        else:
            # Token match
            matched_tokens = 0
            for token in tokens:
                if token in slug_clean:
                    matched_tokens += 1
            if tokens:
                token_ratio = matched_tokens / len(tokens)
                if token_ratio > 0:
                    score += token_ratio * 30.0

        if score > 0:
            results.append((slug, url, score))

    results.sort(key=lambda x: x[2], reverse=True)
    return results[:limit]


def validate_markdown_file(file_path: Path, cache: dict):
    """Quét toàn bộ internal link trong file Markdown và kiểm tra với sitemap."""
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    link_regex = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)')
    links = link_regex.findall(content)

    print(f"\n🔍 VALIDATING INTERNAL LINKS: {file_path.name}")
    print("=" * 70)

    valid_count = 0
    broken_count = 0

    for anchor, url in links:
        # Check if it's an internal link
        if "hvsvn.com" in url or url.startswith("file://") or url.endswith(".md") or url.startswith("/"):
            # Check absolute URL in sitemap
            if url in cache.get("urls", []):
                print(f"✅ VALID: [{anchor}] -> {url}")
                valid_count += 1
            else:
                broken_count += 1
                print(f"\n❌ BROKEN/NOT IN SITEMAP: [{anchor}] -> {url}")
                # Try to suggest correct URL
                slug = url.rstrip("/").split("/")[-1].replace(".md", "").replace("Final-", "").replace("Draft-", "")
                suggestions = search_links(slug, cache, limit=3)
                if not suggestions:
                    suggestions = search_links(anchor, cache, limit=3)

                if suggestions:
                    print("   💡 Gợi ý URL đúng từ Sitemap:")
                    for s_slug, s_url, _ in suggestions:
                        print(f"      - [{s_slug}] -> {s_url}")
                else:
                    print("   ⚠️ Không tìm thấy URL tương ứng trong sitemap (chưa publish).")

    print("\n" + "=" * 70)
    print(f"Tổng kết: {valid_count} link hợp lệ, {broken_count} link cần sửa.")


def main():
    args = sys.argv[1:]
    force_refresh = "--refresh" in args
    cache = load_cache(force_refresh=force_refresh)

    if "--slug" in args:
        idx = args.index("--slug")
        if idx + 1 < len(args):
            slug = args[idx + 1]
            url = lookup_slug(slug, cache)
            if url:
                print(f"\nSlug: {slug}\nURL:  {url}")
            else:
                print(f"\nSlug '{slug}' NOT FOUND in sitemap.")
                suggestions = search_links(slug, cache, limit=5)
                if suggestions:
                    print("Possible matches:")
                    for s, u, _ in suggestions:
                        print(f"  {s} -> {u}")
        return

    if "--search" in args or "--suggest" in args:
        flag = "--search" if "--search" in args else "--suggest"
        idx = args.index(flag)
        if idx + 1 < len(args):
            query = args[idx + 1]
            results = search_links(query, cache, limit=8)
            print(f"\n🔎 Gợi ý link sitemap cho từ khóa '{query}':")
            if results:
                for slug, url, score in results:
                    print(f"  - [{slug}] ({score:.0f} pts)\n    URL: {url}")
            else:
                print("  Không tìm thấy URL phù hợp trong sitemap.")
        return

    if "--validate" in args:
        idx = args.index("--validate")
        if idx + 1 < len(args):
            target_file = Path(args[idx + 1])
            validate_markdown_file(target_file, cache)
        return

    # Default overview
    print("\n=== SITEMAP STATS ===")
    print(f"Total live URLs: {cache['total_urls']}")
    print(f"Last fetched:    {cache['fetched_at']}")
    print("Dùng --search <từ khóa> hoặc --suggest <từ khóa> để tìm link nhanh.")


if __name__ == "__main__":
    main()

