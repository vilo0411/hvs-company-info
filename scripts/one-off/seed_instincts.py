#!/usr/bin/env python3
"""One-off: seed .antigravity/memory/instincts-archive.md from historical feedback.

Sources:
  - anti-ai-rules.md §4 lines:  - [YYYY-MM-DD]: Cập nhật từ "<source>" ...: <text>
  - DECISIONS.md "Bài học kinh nghiệm" bullets (--from-decisions)

Usage:  python scripts/one-off/seed_instincts.py [--apply] [--from-decisions]
Dry-run by default. Idempotent: entries whose title already exists in the archive are skipped.
Entries that are purely system/refactor notes (no content rule) are ignored.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _common import ANTI_AI_RULES, MEMORY_DIR, ROOT, setup_utf8, unaccent, slugify  # noqa: E402

setup_utf8()
ARCHIVE = MEMORY_DIR / "instincts-archive.md"
DECISIONS = MEMORY_DIR / "DECISIONS.md"

SKIP_PAT = re.compile(r"tái cấu trúc file|refactor hệ thống|tối ưu toàn bộ rules|avoid-ai-writing", re.I)
TOPIC_PAT = re.compile(r"toplist|comprehensive stock directory|danh mục (5|top \d) mã|ngành", re.I)
HEADER = """# Instincts Archive — HVS (append-only, nguồn chân lý)

> Mọi bản năng (judgment call) học được từ feedback của user. `scripts/optimize_instincts.py` sinh `instincts.md` từ file này — **không sửa `instincts.md` tay**.
> Format entry: xem `.antigravity/rules/learning-loop.md`. Trạng thái: Active | Deprecated.

"""


def title_from(text: str) -> str:
    t = re.split(r"[;.]\s", text, 1)[0].strip()
    t = re.sub(r"^(Thêm|Cấm|Bổ sung|Ép|Yêu cầu|Chuẩn hóa|Sử dụng|Loại bỏ|Đính chính|Làm rõ|Triệt tiêu|Đồng bộ hóa|Xây dựng|Tiếp tục củng cố|Tối ưu hóa|Thay đổi|Gỡ bỏ)\s+", "", t)
    return t[:90].rstrip(",:")


def parse_learning_log() -> list[dict]:
    out = []
    text = ANTI_AI_RULES.read_text(encoding="utf-8")
    sec = text.split("## 4. Nhật ký học hỏi", 1)[-1]
    for line in sec.splitlines():
        m = re.match(r"^- \[(\d{4}-\d{2}-\d{2})\]:\s*(.+)$", line.strip())
        if not m:
            continue
        date, body = m.groups()
        if SKIP_PAT.search(body):
            continue
        src = re.search(r'từ ["“]([^"”]+)["”]', body)
        rule = re.split(r"(?:feedback|Revision Log(?: \(v[\d.]+\))?)\s*:\s*", body, 1)[-1].strip()
        out.append({
            "title": title_from(rule),
            "date": date,
            "source": slugify(src.group(1)) if src else "anti-ai-rules-log",
            "feedback": body,
            "instinct": rule,
            "scope": "Chỉ topic: phan-tich-nganh" if TOPIC_PAT.search(rule) else "Global",
        })
    return out


def parse_decisions() -> list[dict]:
    out = []
    if not DECISIONS.exists():
        return out
    sec = DECISIONS.read_text(encoding="utf-8").split("## 💡 Bài học kinh nghiệm", 1)[-1]
    for line in sec.splitlines():
        if line.startswith("- ") and "dir /s" not in line:
            rule = line[2:].strip()
            out.append({"title": title_from(rule), "date": "2026-09-21", "source": "DECISIONS.md",
                        "feedback": rule, "instinct": rule, "scope": "Global"})
    return out


def render(e: dict) -> str:
    return (f"### {e['title']}\n- **Trạng thái:** Active\n- **Nguồn:** {e['source']} · {e['date']}\n"
            f"- **Phản hồi từ User:** \"{e['feedback']}\"\n- **Bản năng:** {e['instinct']}\n- **Phạm vi:** {e['scope']}\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--from-decisions", action="store_true")
    a = ap.parse_args()

    entries = parse_learning_log() + (parse_decisions() if a.from_decisions else [])
    existing = ARCHIVE.read_text(encoding="utf-8") if ARCHIVE.exists() else ""
    have = {unaccent(t) for t in re.findall(r"^### (.+)$", existing, re.M)}
    new = [e for e in entries if unaccent(e["title"]) not in have]
    print(f"{len(entries)} candidate · {len(new)} new · {len(entries) - len(new)} đã có")
    for e in new:
        print(f"  [{e['date']}] {e['title']}  ({e['scope']})")
    if not a.apply:
        print("\nDry-run. Thêm --apply để ghi.")
        return 0
    MEMORY_DIR.mkdir(exist_ok=True)
    body = existing or HEADER
    body = body.rstrip("\n") + "\n\n" + "\n".join(render(e) for e in sorted(new, key=lambda x: x["date"]))
    ARCHIVE.write_text(body.rstrip("\n") + "\n", encoding="utf-8")
    print(f"Đã ghi {len(new)} entry vào {ARCHIVE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
