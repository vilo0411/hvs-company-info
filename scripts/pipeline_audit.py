#!/usr/bin/env python3
"""Pipeline health check. Exit 1 when any issue remains.

Usage:
  python scripts/pipeline_audit.py            → report
  python scripts/pipeline_audit.py --fix      → safe fixes only: delete stale Outline/Draft whose Final is newer,
                                                remove stale backlog rows, recount dashboards
  python scripts/pipeline_audit.py --wrappers → only check .claude/commands ↔ .agents/workflows ↔ .antigravity/workflows

Checks:
  A. Outline/Draft stale (Final already exists)      B. Drafts without Outline (wordcount can't check sections)
  C. Backlog rows already published                  D. Dashboard counts vs disk
  E. topic-clusters ✅ rows whose Final is missing / Finals not in topic-clusters
  F. 0-raw files without Raw- prefix                 G. Finals not in anchor-index / not in sitemap cache
  H. Backticked paths in CLAUDE.md + .antigravity/** that don't exist
  I. Wrapper drift
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (ROOT, RAW_DIR, OUTLINES_DIR, DRAFTS_DIR, FINAL_DIR, TOPIC_FILE, PROGRESS_FILE,  # noqa: E402
                     ANCHOR_INDEX, SITEMAP_CACHE, setup_utf8, slugify, read_text)
import topic_status as ts  # noqa: E402
import sprint_status as ss  # noqa: E402

setup_utf8()
SOP_DIR = ROOT / ".antigravity/workflows"
WRAPPER_DIRS = [ROOT / ".claude/commands", ROOT / ".agents/workflows"]
PATH_SCAN = [ROOT / "CLAUDE.md", *(ROOT / ".antigravity").rglob("*.md")]
PATH_RE = re.compile(r"`((?:\.antigravity|\.claude|\.agents|scripts|content|seo-strategy|resources)/[^`\s<>\[\]|]+)`")


class Audit:
    def __init__(self):
        self.issues: list[tuple[str, str, str]] = []  # (section, item, hint)

    def add(self, sec, item, hint=""):
        self.issues.append((sec, item, hint))


def finals() -> dict[str, Path]:
    return {p.stem.removeprefix("Final-").lower(): p for p in FINAL_DIR.glob("Final-*.md")}


def check_stages(a: Audit, fix: bool):
    fin = finals()
    for d, prefix in ((OUTLINES_DIR, "Outline-"), (DRAFTS_DIR, "Draft-"), (DRAFTS_DIR, "Optimize-"), (DRAFTS_DIR, "Proposal-")):
        for p in d.glob(f"{prefix}*.md"):
            slug = p.stem.removeprefix(prefix).lower()
            f = fin.get(slug)
            if f and f.stat().st_mtime >= p.stat().st_mtime:
                if fix:
                    p.unlink()
                    print(f"  [fix] xóa {p.relative_to(ROOT)} (Final mới hơn)")
                else:
                    a.add("A stale", str(p.relative_to(ROOT)), f"Final-{slug}.md đã có, mới hơn → --fix xóa")
            elif f:
                a.add("A stale?", str(p.relative_to(ROOT)), f"Final-{slug}.md có nhưng CŨ hơn — đang optimize? kiểm tra tay")
    for p in DRAFTS_DIR.glob("Draft-*.md"):
        slug = p.stem.removeprefix("Draft-")
        if not (OUTLINES_DIR / f"Outline-{slug}.md").exists():
            a.add("B no-outline", str(p.relative_to(ROOT)), "wordcount không check được từng H2 — tạo Outline hoặc thêm Section_Targets")


def check_backlog(a: Audit, fix: bool):
    text, nl = read_text(ss.BACKLOG_FILE)
    lines = text.split("\n")
    rows = ss.parse(lines)
    stale = ss.stale_rows(rows)
    if fix and stale:
        for r in sorted(stale, key=lambda r: -r.idx):
            del lines[r.idx]
            print(f"  [fix] bỏ backlog #{r.num} {r.keyword}")
        ss.write_text(ss.BACKLOG_FILE, "\n".join(lines), nl)
        ss.update_progress(ss.parse(lines))
    else:
        for r in stale:
            a.add("C backlog", f"#{r.num} {r.keyword}", "đã có Final → --fix")
    # D dashboard
    ptext, _ = read_text(PROGRESS_FILE)
    m = re.search(r"\*\*Published:\*\* (\d+)", ptext)
    n_final = len(finals())
    if m and int(m.group(1)) != n_final:
        if fix:
            ss.update_progress(ss.parse(lines))
            print(f"  [fix] Dashboard Published → {n_final}")
        else:
            a.add("D dashboard", f"Published {m.group(1)} ≠ {n_final} file Final", "--fix")


def check_clusters(a: Audit, fix: bool):
    text, nl = read_text(TOPIC_FILE)
    rows = ts.parse(text.split("\n"))
    fin = finals()
    seen = set()
    for r in rows:
        seen.add(r.slug)
        if r.status == "Finalized" and r.slug not in fin:
            a.add("E cluster", f"✅ {r.keyword} → {r.file or r.slug}", "Final không tồn tại (External? đổi tên?)")
    missing = sorted(set(fin) - seen)
    for s in missing[:40]:
        a.add("E cluster", f"Final-{s}.md", "không có trong topic-clusters → topic_status.py --add \"<kw>\" --cluster …")
    if len(missing) > 40:
        a.add("E cluster", f"… +{len(missing) - 40} Final khác", "")
    if fix:
        new = ts.recount(text.split("\n"))
        ts.write_text(TOPIC_FILE, "\n".join(new), nl)


def check_raw(a: Audit):
    for p in RAW_DIR.glob("*.md"):
        if not p.name.startswith("Raw-"):
            a.add("F raw", p.name, "python scripts/normalize_raw.py --apply")


def check_links(a: Audit):
    idx, _ = read_text(ANCHOR_INDEX)
    cache = json.loads(SITEMAP_CACHE.read_text(encoding="utf-8")) if SITEMAP_CACHE.exists() else {}
    slug_map = cache.get("slug_map", {})
    missing_live, missing_offline, stale_mark = [], [], []
    for slug in sorted(finals()):
        in_idx = f"/{slug}`" in idx or f"Final-{slug}.md" in idx
        live = slug in slug_map
        if not in_idx:
            (missing_live if live else missing_offline).append(slug)
        elif live and f"⚠️ `Final-{slug}.md`" in idx:
            stale_mark.append(slug)
    for s in stale_mark:
        a.add("G anchor-index", f"Final-{s}.md", f"đã live ({slug_map[s]}) — đổi ⚠️ → ✅ URL")
    if missing_live:
        a.add("G anchor-index", f"{len(missing_live)} Final đã live nhưng chưa có trong anchor-index",
              "find_links.py --add-row từng bài (ưu tiên) — vd: " + ", ".join(missing_live[:5]))
    if missing_offline:
        a.add("G anchor-index", f"{len(missing_offline)} Final chưa live, chưa có trong anchor-index",
              "thêm ⚠️ row khi cần link — vd: " + ", ".join(missing_offline[:5]))


def check_paths(a: Audit):
    for f in PATH_SCAN:
        if "archive" in f.parts:
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        for m in PATH_RE.finditer(text):
            p = m.group(1).rstrip("/").split("#")[0]
            if any(ch in p for ch in "<>[]*") or p.endswith((".md`",)):
                continue
            if "api-keys.md" in p or "secrets" in p or "serp-opportunities.md" in p:  # gitignored / generated
                continue
            if not (ROOT / p).exists():
                a.add("H path", f"{f.relative_to(ROOT)} → `{p}`", "file không tồn tại")


def check_wrappers(a: Audit):
    sops = {p.stem for p in SOP_DIR.glob("*.md")}
    for d in WRAPPER_DIRS:
        names = {p.stem for p in d.glob("*.md")}
        for extra in sorted(names - sops):
            a.add("I wrapper", f"{d.relative_to(ROOT)}/{extra}.md", "không có SOP tương ứng trong .antigravity/workflows/")
        for missing in sorted(sops - names):
            a.add("I wrapper", f"{d.relative_to(ROOT)}/{missing}.md", "thiếu wrapper")
        for p in d.glob("*.md"):
            body = p.read_text(encoding="utf-8")
            n = len([l for l in body.splitlines() if l.strip()])
            if n > 12:
                a.add("I wrapper", str(p.relative_to(ROOT)), f"{n} dòng — wrapper phải ≤12, logic để trong SOP")
            if f".antigravity/workflows/{p.stem}.md" not in body:
                a.add("I wrapper", str(p.relative_to(ROOT)), "không trỏ tới SOP cùng tên")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--wrappers", action="store_true")
    args = ap.parse_args()
    a = Audit()
    if args.wrappers:
        check_wrappers(a)
    else:
        check_stages(a, args.fix)
        check_backlog(a, args.fix)
        check_clusters(a, args.fix)
        check_raw(a)
        check_links(a)
        check_paths(a)
        check_wrappers(a)
    if not a.issues:
        print("✅ Pipeline sạch.")
        return 0
    cur = None
    for sec, item, hint in sorted(a.issues):
        if sec != cur:
            print(f"\n## {sec} ({sum(1 for s, _, _ in a.issues if s == sec)})")
            cur = sec
        print(f"- {item}" + (f"  → {hint}" if hint else ""))
    print(f"\n{len(a.issues)} vấn đề.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
