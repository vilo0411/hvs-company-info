#!/usr/bin/env python3
"""Normalize content/blog/0-raw/: rename `<Title>.md` → `Raw-<slug>.md` and ensure YAML frontmatter.

Usage:  python scripts/normalize_raw.py [--apply]
Dry-run by default. Idempotent. Never overwrites an existing Raw-<slug>.md (reports conflict instead).

Slug source (in order): YAML Target_Keyword → H1 → file name (part before "_" / ":").
YAML added/filled: Author, Status: Raw, Source_Title, Imported (YYYY-MM-DD), Target_Keyword (if missing).
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import RAW_DIR, ROOT, setup_utf8, slugify, read_text, write_text, split_frontmatter  # noqa: E402

setup_utf8()


def guess_keyword(fm: dict, lines: list[str], start: int, stem: str) -> str:
    if fm.get("Target_Keyword"):
        return fm["Target_Keyword"]
    for l in lines[start:start + 40]:
        m = re.match(r"^#\s+\**(.+?)\**\s*$", l.strip())
        if m:
            return re.split(r"[?:_|–—]", m.group(1))[0].strip("* ").strip()
    return re.split(r"[_:]", stem)[0].strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    plan = []
    for p in sorted(RAW_DIR.glob("*.md")):
        if p.name.startswith("Raw-"):
            continue
        text, nl = read_text(p)
        fm, start, lines = split_frontmatter(text)
        kw = guess_keyword(fm, lines, start, p.stem)
        slug = slugify(kw)[:80].strip("-") or slugify(p.stem)[:80]
        target = RAW_DIR / f"Raw-{slug}.md"
        if target.exists():  # second import of the same keyword → numbered suffix
            n = 2
            while (RAW_DIR / f"Raw-{slug}-{n}.md").exists():
                n += 1
            target = RAW_DIR / f"Raw-{slug}-{n}.md"
        updates = {"Author": fm.get("Author", "Import"), "Status": "Raw" if fm.get("Status") in (None, "", "Review") else fm["Status"],
                   "Source_Title": p.stem, "Imported": date.today().isoformat(), "Target_Keyword": kw}
        plan.append((p, target, updates, fm, start, lines, nl))
    if not plan:
        print("Không có file cần chuẩn hóa.")
        return 0
    for p, target, up, *_ in plan:
        flag = "⚠️ trùng" if target.exists() else ""
        print(f"{p.name}\n   → {target.name}  [kw: {up['Target_Keyword']}] {flag}")
    if not a.apply:
        print(f"\n{len(plan)} file. Dry-run — thêm --apply để đổi tên.")
        return 0
    done = 0
    for p, target, up, fm, start, lines, nl in plan:
        if target.exists():
            print(f"bỏ qua {p.name}: {target.name} đã tồn tại")
            continue
        head = lines[:start] if start else ["---", "---"]
        body = lines[start:]
        out = [head[0]]
        keys = set()
        for l in head[1:-1]:
            m = re.match(r"^([A-Za-z_]+)\s*:", l)
            if m and m.group(1) in up:
                out.append(f"{m.group(1)}: {up[m.group(1)]}")
                keys.add(m.group(1))
            else:
                out.append(l)
        for k, v in up.items():
            if k not in keys:
                out.append(f"{k}: {v}")
        out.append("---")
        write_text(target, "\n".join(out + body), nl)
        p.unlink()
        done += 1
    print(f"Đã chuẩn hóa {done}/{len(plan)} file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
