"""
fetch_sitemap.py — Tải sitemap và build slug→URL map cho internal linking

Usage:
    python .antigravity/scripts/fetch_sitemap.py
    python .antigravity/scripts/fetch_sitemap.py --slug co-phieu-penny-la-gi
    python .antigravity/scripts/fetch_sitemap.py --refresh

Output:
    .antigravity/scripts/sitemap-cache.json  (được cập nhật tự động)

Cách dùng trong internal linking workflow:
    1. Chạy script để refresh cache (nếu cache > 1 ngày hoặc cần bài mới)
    2. Tra slug → lấy full URL chính xác
    3. Dùng URL đó trong bài viết
"""

import json
import sys
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


def fetch_sitemap() -> list[str]:
    """Tải sitemap XML và trả về list URL."""
    print(f"Fetching sitemap: {SITEMAP_URL}")
    try:
        with urllib.request.urlopen(SITEMAP_URL, timeout=15) as resp:
            xml_content = resp.read()
    except Exception as e:
        print(f"ERROR: Cannot fetch sitemap — {e}")
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
        # Lấy phần cuối của path làm slug
        path = url.rstrip("/").split("https://taichinhso.hvsvn.com", 1)[-1]
        slug = path.rstrip("/").split("/")[-1]
        if slug and slug not in slug_map:
            slug_map[slug] = url
        elif slug and slug in slug_map:
            # Nếu trùng slug, ưu tiên URL dài hơn (path cụ thể hơn)
            pass  # giữ URL đầu tiên, log conflict

    cache = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_urls": len(urls),
        "slug_map": slug_map,
    }
    return cache


def load_cache() -> dict | None:
    """Load cache từ file nếu tồn tại và còn mới."""
    if not CACHE_FILE.exists():
        return None
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        cache = json.load(f)

    fetched_at = datetime.fromisoformat(cache.get("fetched_at", "2000-01-01T00:00:00+00:00"))
    age_hours = (datetime.now(timezone.utc) - fetched_at).total_seconds() / 3600
    if age_hours > CACHE_MAX_AGE_HOURS:
        print(f"Cache is {age_hours:.1f}h old (> {CACHE_MAX_AGE_HOURS}h). Will refresh.")
        return None
    return cache


def save_cache(cache: dict):
    """Lưu cache ra file JSON."""
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    print(f"Cache saved: {CACHE_FILE} ({cache['total_urls']} URLs)")


def lookup_slug(slug: str, cache: dict) -> str | None:
    """Tra slug → full URL từ cache."""
    return cache["slug_map"].get(slug)


def main():
    args = sys.argv[1:]
    force_refresh = "--refresh" in args
    lookup_mode = "--slug" in args

    # Load or fetch cache
    cache = None
    if not force_refresh:
        cache = load_cache()

    if cache is None:
        urls = fetch_sitemap()
        cache = build_cache(urls)
        save_cache(cache)
    else:
        print(f"Using cached sitemap ({cache['total_urls']} URLs, fetched at {cache['fetched_at']})")

    # Lookup mode: tra 1 slug cụ thể
    if lookup_mode:
        idx = args.index("--slug")
        if idx + 1 < len(args):
            slug = args[idx + 1]
            url = lookup_slug(slug, cache)
            if url:
                print(f"\nSlug: {slug}")
                print(f"URL:  {url}")
            else:
                print(f"\nSlug '{slug}' NOT FOUND in sitemap.")
                print("Possible matches:")
                for s in cache["slug_map"]:
                    if slug[:10] in s:
                        print(f"  {s} → {cache['slug_map'][s]}")
        return

    # Default: in ra toàn bộ map (dạng gọn)
    print("\n=== SLUG -> URL MAP ===")
    for slug, url in sorted(cache["slug_map"].items()):
        print(f"  {slug:55s} -> {url}")


if __name__ == "__main__":
    main()
