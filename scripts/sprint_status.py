#!/usr/bin/env python3
"""Single writer for sprint-backlog.md and the Dashboard / Active Pipeline blocks of progress-log.md.

Usage:
  python scripts/sprint_status.py "<keyword|slug>"                       → show row
  python scripts/sprint_status.py "<keyword|slug>" --set Outline-Pending → change Status
  python scripts/sprint_status.py "<keyword|slug>" --remove              → drop row (after finalize)
  python scripts/sprint_status.py --list [STATUS]                        → list rows
  python scripts/sprint_status.py --add "kw" --cluster C --persona P [--type "Priority 1"]
  python scripts/sprint_status.py --sync                                 → recount Dashboard, mirror Active
                                                                            Pipeline, report stale rows
  python scripts/sprint_status.py --log-publish "<kw>" --persona P --mode Express --file <path>
                                                                         → prepend Publication Log row

Status flow: Planned → Outline-Pending → Outline-Approved → Writing → (removed at finalize)
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import BACKLOG_FILE, PROGRESS_FILE, FINAL_DIR, setup_utf8, unaccent, slugify, read_text, write_text  # noqa: E402

setup_utf8()

VALID_STATUS = ["Planned", "Outline-Pending", "Outline-Approved", "Writing"]
HEADER = "| # | Keyword | Cluster | Persona | Loại | Status |"


@dataclass
class Row:
    idx: int
    num: int
    keyword: str
    cluster: str
    persona: str
    kind: str
    status: str

    def line(self) -> str:
        return f"| {self.num} | {self.keyword} | {self.cluster} | {self.persona} | {self.kind} | {self.status} |"


def parse(lines: list[str]) -> list[Row]:
    rows = []
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or not cells[0].isdigit():
            continue
        rows.append(Row(i, int(cells[0]), *cells[1:]))
    return rows


def match(rows: list[Row], q: str) -> list[Row]:
    u, s = unaccent(q), slugify(q)
    return [r for r in rows if unaccent(r.keyword) == u or slugify(r.keyword) == s] \
        or [r for r in rows if u in unaccent(r.keyword)]


def stale_rows(rows: list[Row]) -> list[Row]:
    return [r for r in rows if (FINAL_DIR / f"Final-{slugify(r.keyword)}.md").exists()]


# ───────────── progress-log.md ─────────────

def update_progress(rows: list[Row]) -> None:
    text, nl = read_text(PROGRESS_FILE)
    published = len(list(FINAL_DIR.glob("Final-*.md")))
    text = re.sub(r"(- \*\*Published:\*\* )\d+", rf"\g<1>{published}", text, count=1)
    text = re.sub(r"(- \*\*Active Pipeline:\*\* )\d+", rf"\g<1>{len(rows)}", text, count=1)
    # Rebuild the Active Pipeline table from the backlog
    table = ["| Keyword | Persona | Mode | Status |", "| :--- | :--- | :--- | :--- |"]
    table += [f"| {r.keyword} | {r.persona} | Express | {r.status} |" for r in rows]
    text = re.sub(r"(## Active Pipeline\n\n)(?:\|.*\n)+", lambda m: m.group(1) + "\n".join(table) + "\n", text, count=1)
    write_text(PROGRESS_FILE, text, nl)


def log_publish(keyword: str, persona: str, mode: str, file: str) -> None:
    text, nl = read_text(PROGRESS_FILE)
    row = f"| {date.today().isoformat()} | {keyword} | {persona} | {mode} | `{file}` |"
    if row in text:
        return
    text = re.sub(r"(## Publication Log\n\n\|.*\n\|[ :\-|]+\n)", lambda m: m.group(1) + row + "\n", text, count=1)
    write_text(PROGRESS_FILE, text, nl)


# ───────────── main ─────────────

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?")
    ap.add_argument("--set", metavar="STATUS")
    ap.add_argument("--remove", action="store_true")
    ap.add_argument("--list", nargs="?", const="*", metavar="STATUS")
    ap.add_argument("--add", metavar="KEYWORD")
    ap.add_argument("--cluster")
    ap.add_argument("--persona")
    ap.add_argument("--type", default="Priority 1")
    ap.add_argument("--sync", action="store_true")
    ap.add_argument("--log-publish", metavar="KEYWORD")
    ap.add_argument("--mode", default="Express")
    ap.add_argument("--file")
    args = ap.parse_args()

    text, nl = read_text(BACKLOG_FILE)
    lines = text.split("\n")
    rows = parse(lines)

    def save():
        write_text(BACKLOG_FILE, "\n".join(lines), nl)
        update_progress(parse(lines))

    if args.log_publish:
        if not (args.persona and args.file):
            ap.error("--log-publish cần --persona và --file")
        log_publish(args.log_publish, args.persona, args.mode, args.file)
        print(f"Đã ghi Publication Log: {args.log_publish}")
        return 0

    if args.sync:
        update_progress(rows)
        stale = stale_rows(rows)
        print(f"Dashboard: Published={len(list(FINAL_DIR.glob('Final-*.md')))} · Active={len(rows)}")
        if stale:
            print(f"⚠️ {len(stale)} row đã có Final nhưng còn trong backlog (chạy --remove hoặc pipeline_audit.py --fix):")
            for r in stale:
                print(f"  #{r.num} {r.keyword} → Final-{slugify(r.keyword)}.md")
            return 1
        return 0

    if args.list:
        hits = rows if args.list == "*" else [r for r in rows if r.status.lower() == args.list.lower()]
        print(HEADER + "\n|---|---|---|---|---|---|")
        for r in hits:
            print(r.line())
        return 0

    if args.add:
        if not (args.cluster and args.persona):
            ap.error("--add cần --cluster và --persona")
        if match(rows, args.add):
            print(f"Đã có trong backlog: {args.add}", file=sys.stderr)
            return 1
        num = max((r.num for r in rows), default=0) + 1
        new = Row(-1, num, args.add, args.cluster, args.persona, args.type, "Planned")
        insert_at = rows[-1].idx + 1 if rows else next(i for i, l in enumerate(lines) if l.startswith("| :---")) + 1
        lines.insert(insert_at, new.line())
        save()
        print(f"Đã thêm #{num}: {args.add}")
        return 0

    if not args.query:
        ap.error("cần <keyword|slug>, --list, --add, --sync hoặc --log-publish")
    hits = match(rows, args.query)
    if not hits:
        print(f"Không có '{args.query}' trong sprint-backlog.md", file=sys.stderr)
        return 1
    if len(hits) > 1 and (args.set or args.remove):
        print(f"{len(hits)} row khớp — dùng keyword đầy đủ:", file=sys.stderr)
        for r in hits:
            print("  " + r.keyword, file=sys.stderr)
        return 1
    r = hits[0]

    if args.remove:
        del lines[r.idx]
        save()
        print(f"Đã xóa #{r.num} {r.keyword} khỏi backlog")
        return 0
    if args.set:
        if args.set not in VALID_STATUS:
            print(f"'{args.set}' không hợp lệ. Chọn: {', '.join(VALID_STATUS)}", file=sys.stderr)
            return 1
        old = r.status
        r.status = args.set
        lines[r.idx] = r.line()
        save()
        print(f"#{r.num} {r.keyword}: {old} → {args.set}")
        return 0
    print(HEADER + "\n|---|---|---|---|---|---|")
    for r in hits:
        print(r.line())
    return 0


if __name__ == "__main__":
    sys.exit(main())
