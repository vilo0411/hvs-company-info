#!/usr/bin/env python3
"""
fix_urls.py - Batch fix wrong internal link URLs in finalized articles.
Replaces /dau-tu/danh-cho-nguoi-moi-bat-dau/ pattern with correct sitemap paths.
For slugs NOT in sitemap, removes the hyperlink and keeps plain text.
"""

import os
import re
import sys
import json

# Force UTF-8 encoding for standard output to avoid UnicodeEncodeErrors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Map slug -> correct sitemap path
SLUG_TO_URL = {
    # Chinh sach tai khoa cluster
    "chinh-sach-tai-khoa-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tai-khoa/chinh-sach-tai-khoa-la-gi",
    "dau-tu-cong-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tai-khoa/dau-tu-cong-la-gi",
    "ngan-sach-nha-nuoc-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tai-khoa/ngan-sach-nha-nuoc-la-gi",
    "thue-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tai-khoa/thue-la-gi",
    "luat-va-chinh-sach-cong-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tai-khoa/luat-va-chinh-sach-cong-la-gi",
    # Chinh sach cong - dung slug thuc te tren sitemap
    "chinh-sach-cong-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tai-khoa/luat-va-chinh-sach-cong-la-gi",
    # Chinh sach tien te cluster
    "chinh-sach-tien-te-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tien-te/chinh-sach-tien-te-la-gi",
    "cung-tien-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tien-te/cung-tien-la-gi",
    "ngan-hang-nha-nuoc-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tien-te/ngan-hang-nha-nuoc-la-gi",
    "du-tru-ngoai-hoi-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tien-te/du-tru-ngoai-hoi-la-gi",
    "tin-phieu-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tien-te/tin-phieu-la-gi",
    "lien-ngan-hang-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chinh-sach-tien-te/lien-ngan-hang-la-gi",
    # Chi tieu kinh te
    "lai-suat-la-gi": "https://taichinhso.hvsvn.com/kinh-te-vi-mo/chi-tieu-kinh-te/lai-suat-la-gi",
    # Co phieu dau tu cong - trong cluster danh-cho-nguoi-moi-bat-dau
    "co-phieu-dau-tu-cong": "https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/co-phieu-dau-tu-cong",
    # Slugs NOT in sitemap (remove hyperlink)
    "trai-phieu-chinh-phu-la-gi": None,
    "chu-ky-kinh-te-la-gi": None,
    "tang-truong-tin-dung-la-gi": None,
    "he-so-thanh-toan-la-gi": None,
    # These slugs are in the correct path already
    "chung-khoan-la-gi": "https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/chung-khoan-la-gi",
    "margin-la-gi": "https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/margin-la-gi",
    "dau-tu-ngan-han": "https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/dau-tu-ngan-han",
    "mo-tai-khoan-chung-khoan-co-mat-phi-khong": "https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/mo-tai-khoan-chung-khoan-co-mat-phi-khong",
    "co-phieu-la-gi": "https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/co-phieu-la-gi",
}

# Regex pattern to find markdown links with wrong base path
WRONG_PATH_PATTERN = re.compile(
    r'\[([^\]]+)\]\(https://taichinhso\.hvsvn\.com/dau-tu/danh-cho-nguoi-moi-bat-dau/([^\)]+)\)'
)


def fix_link(match):
    """Replace wrong URL or remove hyperlink if slug not in sitemap."""
    anchor_text = match.group(1)
    slug = match.group(2).rstrip('/')

    if slug in SLUG_TO_URL:
        correct_url = SLUG_TO_URL[slug]
        if correct_url is None:
            # Remove hyperlink, keep plain text
            print(f"  [REMOVED LINK] slug='{slug}' not in sitemap")
            return anchor_text
        else:
            # Check if URL already correct (co-phieu-la-gi etc)
            old_url = f"https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/{slug}"
            if correct_url == old_url:
                return match.group(0)  # No change needed
            print(f"  [FIXED] slug '{slug}' -> {correct_url}")
            return f'[{anchor_text}]({correct_url})'
    else:
        # Slug not in our map - check if it belongs to another cluster
        # For safety, leave unchanged and report
        print(f"  [UNKNOWN] slug='{slug}' - leaving unchanged")
        return match.group(0)


def process_file(filepath):
    """Process a single markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count matches before
    matches = WRONG_PATH_PATTERN.findall(content)
    if not matches:
        return False
    
    print(f"\nProcessing: {os.path.basename(filepath)}")
    new_content = WRONG_PATH_PATTERN.sub(fix_link, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  -> File updated.")
        return True
    return False


def main():
    finalized_dir = r"e:\project\hvs-company-info\content\blog\3-finalized"
    
    # Focus on macroeconomic cluster articles
    target_files = [
        "Final-chinh-sach-cong-la-gi.md",
        "Final-ngan-sach-nha-nuoc-la-gi.md",
        "Final-dau-tu-cong-la-gi.md",
        "Final-thue-la-gi.md",
        "Final-chinh-sach-tien-te-la-gi.md",
        "Final-ngan-hang-nha-nuoc-la-gi.md",
        "Final-cung-tien-la-gi.md",
        "Final-du-tru-ngoai-hoi-la-gi.md",
        "Final-lien-ngan-hang-la-gi.md",
    ]
    
    updated_count = 0
    for filename in target_files:
        filepath = os.path.join(finalized_dir, filename)
        if os.path.exists(filepath):
            if process_file(filepath):
                updated_count += 1
        else:
            print(f"File not found: {filename}")
    
    print(f"\n=== Done: {updated_count} files updated ===")


if __name__ == "__main__":
    main()
