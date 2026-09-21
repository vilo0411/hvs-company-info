#!/usr/bin/env python3
"""Read or update one article's status in topic-clusters.md without loading the file into the LLM.

Usage:
  python scripts/topic_status.py <slug>                      → print matching row(s)
  python scripts/topic_status.py <slug> --set "In Progress"  → change status of exactly one row
  python scripts/topic_status.py --find "từ khóa"            → accent-insensitive keyword search
  python scripts/topic_status.py --list Planned              → list rows with a status
  python scripts/topic_status.py --recount                   → recompute cluster headers + summary line
  python scripts/topic_status.py --add "kw" --cluster "Tên cluster" [--slug s]  → append a Planned row

Statuses: Planned · In Progress · Outline-Approved · Optimizing · Finalized
Row format (kept exactly as the file already uses it):
  - ⭕ kw *(Planned)*
  - 🔄 kw *(In Progress)*  |  *(Outline-Approved)*  |  *(Optimizing — Final-<slug>.md)*
  - ✅ kw *(Published — Final-<slug>.md)*
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import TOPIC_FILE, FINAL_DIR, setup_utf8, unaccent, slugify, read_text, write_text  # noqa: E402

setup_utf8()

VALID_STATUS = ["Planned", "In Progress", "Outline-Approved", "Optimizing", "Finalized"]
ROW_RE = re.compile(r"^(?P<prefix>\*\*Pillar:\*\* |- )(?P<icon>✅|🔄|⭕) (?P<kw>.+?) \*\((?P<paren>.+?)\)\*(?P<tail>.*)$")
CLUSTER_RE = re.compile(r"^### Cluster: (?P<name>.+?) \((?P<n>\d+) articles \| ✅ \d+ \| 🔄 \d+ \| ⭕ \d+\)\s*$")
GROUP_RE = re.compile(r"^## Group: (?P<name>.+?) \((?P<n>\d+) articles\)\s*$")
SUMMARY_RE = re.compile(r"^> ✅ Published: \d+ \| 🔄 In Progress: \d+ \| ⭕ Planned: \d+\s*$")
FINAL_RE = re.compile(r"Final-([a-z0-9-]+)\.md", re.I)


@dataclass
class Row:
    idx: int
    cluster: str
    group: str
    keyword: str
    slug: str
    status: str
    pillar: bool
    file: str


def paren_to_status(paren: str) -> str:
    p = paren.strip()
    if p.startswith("Published"):
        return "Finalized"
    for s in VALID_STATUS:
        if p.startswith(s):
            return s
    return p


def status_to_line(prefix: str, keyword: str, status: str, slug: str, tail: str = "") -> str:
    if status == "Finalized":
        return f"{prefix}✅ {keyword} *(Published — Final-{slug}.md)*{tail}"
    if status == "Optimizing":
        return f"{prefix}🔄 {keyword} *(Optimizing — Final-{slug}.md)*{tail}"
    if status == "Planned":
        return f"{prefix}⭕ {keyword} *(Planned)*{tail}"
    return f"{prefix}🔄 {keyword} *({status})*{tail}"


def parse(lines: list[str]) -> list[Row]:
    rows, cluster, group = [], "", ""
    for i, line in enumerate(lines):
        g = GROUP_RE.match(line)
        if g:
            group = g.group("name")
            continue
        c = CLUSTER_RE.match(line)
        if c:
            cluster = c.group("name")
            continue
        m = ROW_RE.match(line)
        if not m:
            continue
        paren = m.group("paren")
        fm = FINAL_RE.search(paren)
        file = fm.group(0) if fm else ""
        slug = fm.group(1).lower() if fm else slugify(m.group("kw"))
        rows.append(Row(i, cluster, group, m.group("kw"), slug, paren_to_status(paren),
                        m.group("prefix").startswith("**"), file))
    return rows


def recount(lines: list[str]) -> list[str]:
    """Rewrite '(N articles | ✅ a | 🔄 b | ⭕ c)' in cluster headers, group totals and the summary line."""
    out = list(lines)
    cluster_idx: list[int] = []
    group_idx: list[int] = []
    counts: dict[int, list[int]] = {}
    cur_c = cur_g = -1
    for i, line in enumerate(lines):
        if GROUP_RE.match(line):
            cur_g = i
            group_idx.append(i)
            counts[i] = [0, 0, 0]
            continue
        if CLUSTER_RE.match(line):
            cur_c = i
            cluster_idx.append(i)
            counts[i] = [0, 0, 0]
            continue
        m = ROW_RE.match(line)
        if not m or cur_c < 0:
            continue
        k = {"✅": 0, "🔄": 1, "⭕": 2}[m.group("icon")]
        counts[cur_c][k] += 1
        if cur_g >= 0:
            counts[cur_g][k] += 1
    for i in cluster_idx:
        a, b, c = counts[i]
        name = CLUSTER_RE.match(lines[i]).group("name")
        out[i] = f"### Cluster: {name} ({a + b + c} articles | ✅ {a} | 🔄 {b} | ⭕ {c})"
    for i in group_idx:
        a, b, c = counts[i]
        name = GROUP_RE.match(lines[i]).group("name")
        out[i] = f"## Group: {name} ({a + b + c} articles)"
    tot = [sum(counts[i][k] for i in cluster_idx) for k in range(3)]
    for i, line in enumerate(lines):
        if SUMMARY_RE.match(line):
            out[i] = f"> ✅ Published: {tot[0]} | 🔄 In Progress: {tot[1]} | ⭕ Planned: {tot[2]}"
            break
    return out


def print_rows(rows: list[Row], as_json: bool):
    if as_json:
        print(json.dumps([asdict(r) for r in rows], ensure_ascii=False, indent=2))
        return
    print("| Slug | Keyword | Trạng thái | Cluster | Pillar |\n|---|---|---|---|---|")
    for r in rows:
        print(f"| {r.slug} | {r.keyword} | {r.status} | {r.cluster} | {'✓' if r.pillar else ''} |")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--set", metavar="STATUS")
    ap.add_argument("--find", metavar="TEXT")
    ap.add_argument("--list", metavar="STATUS")
    ap.add_argument("--recount", action="store_true")
    ap.add_argument("--add", metavar="KEYWORD", help="Append a Planned row to --cluster")
    ap.add_argument("--cluster", metavar="NAME")
    ap.add_argument("--slug-override", dest="slug_override", metavar="SLUG")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not TOPIC_FILE.exists():
        print(f"Không tìm thấy {TOPIC_FILE}", file=sys.stderr)
        return 2
    text, nl = read_text(TOPIC_FILE)
    lines = text.split("\n")
    rows = parse(lines)

    if args.list:
        hits = [r for r in rows if r.status.lower() == args.list.lower()]
        if not args.json:
            print(f"# {len(hits)} bài ở trạng thái {args.list}\n")
        print_rows(hits, args.json)
        return 0

    if args.find:
        q = unaccent(args.find)
        hits = [r for r in rows if q in unaccent(r.keyword) or q.replace(" ", "-") in r.slug]
        if not args.json:
            print(f"# {len(hits)} dòng khớp “{args.find}”\n")
        print_rows(hits[:20], args.json)
        return 0

    if args.add:
        if not args.cluster:
            ap.error("--add cần --cluster")
        target = next((i for i, l in enumerate(lines) if CLUSTER_RE.match(l) and CLUSTER_RE.match(l).group("name") == args.cluster), None)
        if target is None:
            print(f"Không có cluster '{args.cluster}'. Cluster hiện có:", file=sys.stderr)
            for l in lines:
                m = CLUSTER_RE.match(l)
                if m:
                    print("  " + m.group("name"), file=sys.stderr)
            return 1
        # insert after the last row of this cluster (before the next blank+header)
        j = target + 1
        last_row = target
        while j < len(lines) and not lines[j].startswith("### ") and not lines[j].startswith("## "):
            if ROW_RE.match(lines[j]):
                last_row = j
            j += 1
        new_line = status_to_line("- ", args.add, "Planned", args.slug_override or slugify(args.add))
        lines.insert(last_row + 1, new_line)
        lines = recount(lines)
        write_text(TOPIC_FILE, "\n".join(lines), nl)
        print(f"Đã thêm: {new_line} (cluster {args.cluster})")
        return 0

    if args.recount and not args.slug:
        new = recount(lines)
        changed = sum(1 for a, b in zip(lines, new) if a != b)
        write_text(TOPIC_FILE, "\n".join(new), nl)
        print(f"Recount xong — {changed} dòng header cập nhật.")
        return 0

    if not args.slug:
        ap.error("cần <slug>, --find, --list, --add hoặc --recount")

    slug = args.slug.strip("/").split("/")[-1].lower()
    slug = re.sub(r"^(final|draft|outline)-", "", slug).removesuffix(".md")
    hits = [r for r in rows if r.slug == slug] or [r for r in rows if slug in r.slug]
    if not hits:
        print(f"Không có dòng nào cho slug '{slug}' trong topic-clusters.md. "
              f"Dùng --add \"<keyword>\" --cluster \"<tên>\" để thêm.", file=sys.stderr)
        return 1

    if args.set is None:
        print_rows(hits, args.json)
        return 0

    if len(hits) > 1:
        print(f"{len(hits)} dòng khớp '{slug}' — không thể --set. Dùng slug đầy đủ:", file=sys.stderr)
        for r in hits:
            print(f"  {r.slug}  ({r.status})", file=sys.stderr)
        return 1

    new_status = args.set.strip()
    if new_status not in VALID_STATUS:
        print(f"'{new_status}' không hợp lệ. Chọn: {', '.join(VALID_STATUS)}", file=sys.stderr)
        return 1
    r = hits[0]
    if r.status == new_status:
        print(f"Không đổi: {r.slug} đã ở trạng thái {r.status}")
        return 0
    if new_status in ("Finalized", "Optimizing") and not (FINAL_DIR / f"Final-{r.slug}.md").exists():
        print(f"Cảnh báo: chưa có content/blog/3-finalized/Final-{r.slug}.md", file=sys.stderr)
    m = ROW_RE.match(lines[r.idx])
    lines[r.idx] = status_to_line(m.group("prefix"), r.keyword, new_status, r.slug, m.group("tail"))
    lines = recount(lines)
    write_text(TOPIC_FILE, "\n".join(lines), nl)
    print(f"Đã cập nhật {r.slug}: {r.status} → {new_status} (dòng {r.idx + 1}, {r.cluster})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
