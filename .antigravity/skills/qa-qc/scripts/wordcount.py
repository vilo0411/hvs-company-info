#!/usr/bin/env python3
"""
HVS Word Count Checker
======================
Đếm từ chính xác từng H2 section trong Draft/Final,
so sánh với Word_Count target trong Outline tương ứng.

Dùng:
    python .antigravity/skills/qa-qc/scripts/wordcount.py content/blog/2-user-review/Draft-[slug].md
    python .antigravity/skills/qa-qc/scripts/wordcount.py [draft] --outline [outline]
    python .antigravity/skills/qa-qc/scripts/wordcount.py content/blog/  # scan thư mục
    python .antigravity/skills/qa-qc/scripts/wordcount.py content/blog/  --fail-only
"""

import re
import sys
import argparse
from pathlib import Path

# Force UTF-8 encoding for standard output to avoid UnicodeEncodeErrors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

TOLERANCE = 0.10  # ±10%
SECTION_MARKER_MAIN = "MAIN"
SECTION_MARKER_SUP = "SUPPLEMENTAL"


# ─── Helpers ────────────────────────────────────────────────────────────────

def count_words_vn(text: str) -> int:
    """
    Đếm từ tiếng Việt: tách theo khoảng trắng, loại bỏ ký tự markdown
    (**, *, #, [], (), ---) và YAML frontmatter.
    """
    # Bỏ YAML frontmatter ở đầu file (chỉ khớp ở đầu chuỗi)
    text = re.sub(r'^---[\s\S]*?---\r?\n', '', text)
    # Bỏ markdown links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Bỏ ký tự markdown còn lại
    text = re.sub(r'[*_#>\-`|]', ' ', text)
    # Bỏ URL thuần
    text = re.sub(r'https?://\S+', '', text)
    # Tách từ
    words = text.split()
    return len(words)


def extract_yaml_field(content: str, field: str):
    """Lấy giá trị field từ YAML frontmatter."""
    pattern = rf'^{field}:\s*(.+)$'
    m = re.search(pattern, content, re.MULTILINE)
    return m.group(1).strip() if m else None


def split_into_sections(content: str) -> list[dict]:
    """
    Tách content thành list sections theo H2 (##).
    Trả về: [{"heading": str, "body": str, "line_start": int}]
    """
    lines = content.split('\n')
    sections = []
    current_heading = None
    current_body_lines = []
    current_start = 0
    in_yaml = False

    for i, line in enumerate(lines):
        if i == 0 and line.strip() == '---':
            in_yaml = True
            continue
        if in_yaml:
            if line.strip() == '---':
                in_yaml = False
            continue

        if re.match(r'^#{2,3} ', line):
            if current_heading is not None:
                sections.append({
                    "heading": current_heading,
                    "body": '\n'.join(current_body_lines),
                    "line_start": current_start
                })
            current_heading = line.lstrip('# ').strip()
            current_body_lines = []
            current_start = i + 1
        else:
            if current_heading is not None:
                current_body_lines.append(line)

    if current_heading is not None:
        sections.append({
            "heading": current_heading,
            "body": '\n'.join(current_body_lines),
            "line_start": current_start
        })

    return sections


def parse_outline_targets(outline_path: Path) -> dict[str, dict]:
    """
    Đọc Outline, trích xuất Word_Count và loại (MAIN/SUPPLEMENTAL) của từng H2.
    Trả về: {"Heading text": {"target": int, "type": "MAIN"|"SUPPLEMENTAL"|"UNKNOWN"}}
    """
    if not outline_path.exists():
        return {}

    content = outline_path.read_text(encoding='utf-8')
    targets = {}
    blocks = re.split(r'\n(?=#{2,5} )', content)

    for block in blocks:
        heading_match = re.match(r'^#{2,5} (.+)', block)
        if not heading_match:
            continue
        heading = heading_match.group(1).strip()

        wc_match = re.search(r'[-*]\s*\*{0,2}Word_Count\*{0,2}(?::\*{0,2}|\*{0,2}:)\s*(\d+)', block)
        if not wc_match:
            continue
        target = int(wc_match.group(1))

        section_type = "UNKNOWN"
        if SECTION_MARKER_MAIN in block:
            section_type = SECTION_MARKER_MAIN
        if SECTION_MARKER_SUP in block:
            section_type = SECTION_MARKER_SUP

        targets[heading] = {"target": target, "type": section_type}

    return targets


def find_best_match(heading: str, targets: dict) -> tuple[str | None, dict | None]:
    """Fuzzy match heading với targets (exact → lowercase → contains)."""
    if heading in targets:
        return heading, targets[heading]
    heading_lower = heading.lower()
    for k, v in targets.items():
        if k.lower() == heading_lower:
            return k, v
    for k, v in targets.items():
        if heading_lower in k.lower() or k.lower() in heading_lower:
            return k, v
    return None, None


# ─── Report ─────────────────────────────────────────────────────────────────

def check_file(draft_path: Path, outline_path: Path | None = None) -> dict:
    """Kiểm tra một file Draft/Final. Trả về dict kết quả."""
    content = draft_path.read_text(encoding='utf-8')

    total_words = count_words_vn(content)

    yaml_target_str = extract_yaml_field(content, 'Word_Count_Target')
    yaml_target = None
    if yaml_target_str:
        m = re.search(r'\d+', yaml_target_str)
        if m:
            yaml_target = int(m.group())

    sections = split_into_sections(content)

    # Auto-detect Outline: content/blog/2-user-review/ → content/blog/1-outlines/
    if outline_path is None:
        slug = draft_path.stem
        for prefix in ('Draft-', 'Final-', 'Outline-'):
            slug = slug.replace(prefix, '')
        candidate = draft_path.parent.parent / '1-outlines' / f'Outline-{slug}.md'
        if candidate.exists():
            outline_path = candidate

    targets = parse_outline_targets(outline_path) if outline_path else {}

    section_results = []
    any_fail = False

    for sec in sections:
        wc = count_words_vn(sec['body'])
        _, target_info = find_best_match(sec['heading'], targets)

        result = {
            "heading": sec['heading'],
            "words": wc,
            "target": None,
            "type": "UNKNOWN",
            "status": "NO_TARGET",
            "diff_pct": None,
        }

        if target_info:
            t = target_info['target']
            low = int(t * (1 - TOLERANCE))
            high = int(t * (1 + TOLERANCE))
            diff_pct = (wc - t) / t * 100

            result.update({
                "target": t,
                "type": target_info['type'],
                "low": low,
                "high": high,
                "diff_pct": diff_pct,
                "status": "PASS" if low <= wc <= high else "FAIL",
            })
            if result["status"] == "FAIL":
                any_fail = True

        section_results.append(result)

    # Kiểm tra tổng
    total_status = "NO_TARGET"
    total_diff_pct = None
    if yaml_target:
        low_t = int(yaml_target * (1 - TOLERANCE))
        high_t = int(yaml_target * (1 + TOLERANCE))
        total_diff_pct = (total_words - yaml_target) / yaml_target * 100
        total_status = "PASS" if low_t <= total_words <= high_t else "FAIL"
        if total_status == "FAIL":
            any_fail = True

    return {
        "file": str(draft_path),
        "total_words": total_words,
        "yaml_target": yaml_target,
        "total_status": total_status,
        "total_diff_pct": total_diff_pct,
        "sections": section_results,
        "overall": "FAIL" if any_fail else "PASS",
        "outline_used": str(outline_path) if outline_path else None,
    }


def print_report(result: dict, verbose: bool = True):
    """In báo cáo ra console."""
    GREEN  = '\033[92m'
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    RESET  = '\033[0m'
    BOLD   = '\033[1m'

    def color(text, c):
        return f"{c}{text}{RESET}"

    file_name = Path(result['file']).name
    overall = result['overall']
    overall_color = GREEN if overall == "PASS" else RED

    print(f"\n{'='*60}")
    print(f"{BOLD}FILE:{RESET} {file_name}")
    if result['outline_used']:
        print(f"{BOLD}OUTLINE:{RESET} {Path(result['outline_used']).name}")
    else:
        print(f"{BOLD}OUTLINE:{RESET} {color('Không tìm thấy — chỉ kiểm tra tổng từ', YELLOW)}")
    print(f"{'='*60}")

    total = result['total_words']
    target = result['yaml_target']
    ts = result['total_status']
    if target:
        ts_color = GREEN if ts == "PASS" else RED
        print(f"\n{BOLD}TỔNG TỪ:{RESET} {total} / target {target}  [{color(ts, ts_color)}]  ({result['total_diff_pct']:+.1f}%)")
        print(f"  Cho phép: {int(target*0.9)} – {int(target*1.1)} từ")
    else:
        print(f"\n{BOLD}TỔNG TỪ:{RESET} {total}  [{color('Không có Word_Count_Target trong YAML', YELLOW)}]")

    if verbose:
        print(f"\n{BOLD}CHI TIẾT TỪNG SECTION:{RESET}")
        print(f"{'─'*60}")
        for sec in result['sections']:
            h = sec['heading'][:45] + '...' if len(sec['heading']) > 45 else sec['heading']
            wc = sec['words']
            status = sec['status']

            if status == "PASS":
                print(f"  {color('✓ PASS', GREEN)}  ## {h}")
                print(f"         {wc} từ / target {sec['target']}  ({sec['diff_pct']:+.1f}%)  [{sec['type']}]")
            elif status == "FAIL":
                needed = sec['target'] - wc if sec['diff_pct'] < 0 else 0
                print(f"  {color('✗ FAIL', RED)}  ## {h}")
                print(f"         {wc} từ / target {sec['target']}  ({sec['diff_pct']:+.1f}%)  [{sec['type']}]")
                if needed > 0:
                    print(f"         {color(f'→ Cần thêm ~{needed} từ', RED)}")
            else:
                print(f"  {color('? N/A ', YELLOW)}  ## {h}")
                print(f"         {wc} từ  [Không có target trong Outline]")

        print(f"{'─'*60}")

    print(f"\n{BOLD}KẾT QUẢ:{RESET} {color(overall, overall_color)}")
    print(f"{'='*60}\n")


# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='HVS Word Count Checker — kiểm tra số từ per-section ±10%'
    )
    parser.add_argument('path', help='Đường dẫn file Draft/Final hoặc thư mục')
    parser.add_argument('--outline', help='Đường dẫn Outline tương ứng (tùy chọn)')
    parser.add_argument('--quiet', action='store_true', help='Chỉ in tổng, không in per-section')
    parser.add_argument('--fail-only', action='store_true', help='Chỉ in các file/section FAIL')
    args = parser.parse_args()

    target_path = Path(args.path)
    outline_path = Path(args.outline) if args.outline else None

    if target_path.is_dir():
        md_files = (
            list(target_path.rglob('Draft-*.md')) +
            list(target_path.rglob('Final-*.md'))
        )
        if not md_files:
            print(f"Không tìm thấy file Draft-*.md hoặc Final-*.md trong {target_path}")
            sys.exit(1)
        all_pass = True
        for f in sorted(md_files):
            result = check_file(f)
            if args.fail_only and result['overall'] == 'PASS':
                continue
            print_report(result, verbose=not args.quiet)
            if result['overall'] == 'FAIL':
                all_pass = False
        sys.exit(0 if all_pass else 1)

    if not target_path.exists():
        print(f"File không tồn tại: {target_path}")
        sys.exit(1)

    result = check_file(target_path, outline_path)
    print_report(result, verbose=not args.quiet)
    sys.exit(0 if result['overall'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
