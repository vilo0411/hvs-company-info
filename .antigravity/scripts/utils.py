#!/usr/bin/env python3
"""
utils.py — HVS Content Pipeline Utilities
==========================================
Các hàm tái sử dụng dùng chung cho các script trong pipeline.
Không chạy trực tiếp — import vào các script khác.

Import: from utils import setup_utf8, check_forbidden_words, update_clusters_status, ...
"""

import os
import re
import sys
from pathlib import Path


# ─── UTF-8 Setup ─────────────────────────────────────────────────────────────

def setup_utf8():
    """Force UTF-8 for stdout/stderr on Windows — gọi ngay đầu mọi script."""
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')


# ─── File Helpers ─────────────────────────────────────────────────────────────

def read_file(path) -> str:
    """Đọc file với UTF-8, trả về nội dung string."""
    return Path(path).read_text(encoding='utf-8')


def write_file(path, content: str):
    """Ghi nội dung vào file với UTF-8."""
    Path(path).write_text(content, encoding='utf-8')


def remove_files(*paths):
    """Xóa nhiều file cùng lúc, bỏ qua nếu không tồn tại."""
    for p in paths:
        fp = Path(p)
        if fp.exists():
            fp.unlink()
            print(f"Removed: {fp.name}")
        else:
            print(f"Not found (skip): {fp.name}")


# ─── Anti-AI Word Check ───────────────────────────────────────────────────────

FORBIDDEN_WORDS = ['cần', 'nên', 'có lẽ']

def check_forbidden_words(filepath, words=None) -> list[tuple[int, str, str]]:
    """
    Kiểm tra từ bị cấm trong file.
    Trả về: [(line_num, word, line_text), ...]
    """
    if words is None:
        words = FORBIDDEN_WORDS
    content = read_file(filepath)
    results = []
    for i, line in enumerate(content.split('\n'), 1):
        # Bỏ qua lines trong YAML frontmatter và Revision Log
        for w in words:
            if re.search(rf'\b{re.escape(w)}\b', line, re.IGNORECASE):
                results.append((i, w, line.strip()))
    return results


def print_forbidden_report(filepath, words=None):
    """In báo cáo từ bị cấm ra console."""
    setup_utf8()
    results = check_forbidden_words(filepath, words)
    if not results:
        print(f"PASS — Không tìm thấy từ bị cấm trong {Path(filepath).name}")
    else:
        print(f"FAIL — Tìm thấy {len(results)} vi phạm trong {Path(filepath).name}:")
        for ln, word, text in results:
            print(f"  Line {ln}: [{word}] → {text[:100]}")
    return results


# ─── Topic Cluster Updater ────────────────────────────────────────────────────

TOPIC_CLUSTERS_PATH = Path("seo-strategy/content-plan/topic-clusters.md")


def mark_published_in_clusters(keyword: str, slug: str) -> bool:
    """
    Đánh dấu keyword từ ⭕ Planned → ✅ Published trong topic-clusters.md.
    
    Args:
        keyword: Từ khóa (ví dụ: 'chính sách tài khóa là gì')
        slug: Tên file không có 'Final-' và '.md' (ví dụ: 'chinh-sach-tai-khoa-la-gi')
    
    Returns:
        True nếu thay thế thành công, False nếu không tìm thấy.
    """
    content = read_file(TOPIC_CLUSTERS_PATH)
    
    # Pattern để tìm dòng keyword trong topic clusters
    planned_pattern = rf'- ⭕ {re.escape(keyword)} \*\(Planned\)\*'
    replacement = f'- ✅ {keyword} *(Published — Final-{slug}.md)*'
    
    if re.search(planned_pattern, content):
        new_content = re.sub(planned_pattern, replacement, content)
        write_file(TOPIC_CLUSTERS_PATH, new_content)
        print(f"Cluster updated: '{keyword}' → Published")
        return True
    else:
        print(f"WARNING: '{keyword}' không tìm thấy dạng ⭕ Planned trong topic-clusters.md")
        return False


# ─── Batch URL Fixer ──────────────────────────────────────────────────────────

OLD_BASE = "https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/"

def fix_urls_in_file(filepath: str, url_map: dict) -> bool:
    """
    Thay thế các URL cũ theo url_map trong file Markdown.
    url_map: {old_url: new_url}
    """
    content = read_file(filepath)
    modified = False
    for old_url, new_url in url_map.items():
        if old_url in content:
            content = content.replace(old_url, new_url)
            print(f"  Fixed: ...{old_url.split('/')[-1]} → ...{new_url.split('/')[-1]}")
            modified = True
    if modified:
        write_file(filepath, content)
        print(f"  Saved: {Path(filepath).name}")
    return modified


# ─── Standalone CLI ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    setup_utf8()

    parser = argparse.ArgumentParser(description="HVS Pipeline Utilities CLI")
    parser.add_argument('--check-words', metavar='FILE', help='Kiểm tra từ bị cấm trong file')
    args = parser.parse_args()

    if args.check_words:
        print_forbidden_report(args.check_words)
    else:
        parser.print_help()
