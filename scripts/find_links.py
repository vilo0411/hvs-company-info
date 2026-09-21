#!/usr/bin/env python3
"""Query the internal-link registry without loading anchor-index.md into the LLM.

Modes:
  python scripts/find_links.py "từ khóa" [--top 8] [--exclude slug] [--json]
      → best published articles to link TO from a draft (+ 1 conversion page /thuc-tap-so).
  python scripts/find_links.py --backfill <slug> [--top 5] [--json]
      → finalized articles that should link TO <slug> but don't yet, with the line to edit.
  python scripts/find_links.py --add-row <slug> --anchor "..." [--partial "a, b"] --cluster "CLUSTER C"
      → register a newly published article (one row) — used by finalize.py.

Sources: seo-strategy/content-plan/anchor-index.md · scripts/sitemap-cache.json ·
         content/blog/3-finalized/*.md (backfill only)
Only rows marked ✅ AND present in sitemap-cache are safe to insert. ⚠️ rows = not live yet.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (ANCHOR_INDEX, SITEMAP_CACHE, FINAL_DIR, HOST, CTA_PREFIX, setup_utf8, unaccent,  # noqa: E402
                     read_text, write_text, split_frontmatter, body_end)

setup_utf8()

STOPWORDS = {
    "la", "gi", "va", "cua", "cho", "cac", "nhung", "co", "khong", "duoc", "trong", "khi", "voi", "de",
    "mot", "nay", "nao", "nhu", "the", "cach", "nen", "hay", "ve", "tu", "den", "theo", "tai", "bi", "se",
    "da", "dang", "hon", "nhat", "huong", "dan", "chi", "tiet", "nguoi", "moi", "f0", "hvs", "bai", "viet",
    "2024", "2025", "2026", "cap", "top", "dieu", "can", "biet", "ma", "hieu", "qua", "tot", "nhanh",
    "an", "toan", "phuong", "phap", "buoc", "chung", "khoan",
}


def tokens(s: str) -> set[str]:
    return {t for t in re.split(r"[^a-z0-9]+", unaccent(s)) if t and t not in STOPWORDS and len(t) > 1}


@dataclass
class Entry:
    cluster: str
    url: str
    anchor: str
    partial: str
    live: bool
    line: int

    @property
    def slug(self) -> str:
        return self.url.rstrip("/").rsplit("/", 1)[-1].removesuffix(".md").removeprefix("Final-")

    @property
    def is_cta(self) -> bool:
        return self.url.startswith(CTA_PREFIX)


def load_index() -> list[Entry]:
    entries, cluster = [], ""
    text, _ = read_text(ANCHOR_INDEX)
    for i, line in enumerate(text.split("\n"), 1):
        if line.startswith("## "):
            cluster = line[3:].strip()
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].startswith("URL") or set(cells[0]) <= set(":- "):
            continue
        live = cells[0].startswith("✅")
        url = cells[0].lstrip("✅⚠️ ").strip().strip("`")
        entries.append(Entry(cluster, url, cells[1], cells[2] if len(cells) > 2 else "", live, i))
    return entries


def load_sitemap() -> set[str]:
    if not SITEMAP_CACHE.exists():
        return set()
    return {u.rstrip("/") for u in json.loads(SITEMAP_CACHE.read_text(encoding="utf-8")).get("urls", [])}


def score(q: set[str], e: Entry) -> float:
    if not q:
        return 0.0
    a, p, s = tokens(e.anchor), tokens(e.partial), tokens(e.slug.replace("-", " "))
    sc = 3.0 * len(q & a) / len(q) + 2.0 * len(q & s) / len(q) + 1.0 * len(q & p) / len(q)
    if unaccent(e.anchor) == unaccent(" ".join(sorted(q))):
        sc += 1.0
    return round(sc, 3)


# ───────────── search ─────────────

def mode_search(args, entries, sitemap):
    q = tokens(args.keyword)
    ranked = []
    for e in entries:
        if e.is_cta or (args.exclude and args.exclude in e.url):
            continue
        sc = score(q, e)
        if sc > 0:
            ranked.append((sc, e))
    ranked.sort(key=lambda x: (-x[0], not x[1].live, x[1].anchor))
    top = ranked[: args.top]
    # Conversion page: pick by keyword overlap, default to the hub
    ctas = [e for e in entries if e.is_cta]
    cta = max(ctas, key=lambda e: score(q, e), default=None) if ctas else None
    if cta and score(q, cta) == 0:
        cta = next((e for e in ctas if e.url.rstrip("/") == CTA_PREFIX), ctas[0])

    def ok(e):
        return e.live and e.url.rstrip("/") in sitemap

    if args.json:
        out = [{**asdict(e), "score": sc, "in_sitemap": ok(e)} for sc, e in top]
        if cta:
            out.append({**asdict(cta), "score": "cta", "in_sitemap": ok(cta)})
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return
    print(f"# Internal link candidates for “{args.keyword}” (top {len(top)}/{len(ranked)})\n")
    print("| # | Anchor gợi ý | URL | Cluster | Sitemap |")
    print("|---|---|---|---|---|")
    for n, (sc, e) in enumerate(top, 1):
        mark = "✓" if ok(e) else ("✗ chưa live" if not e.live else "✗ không có trong cache")
        print(f"| {n} | {e.anchor} | {e.url} | {e.cluster} | {mark} |")
    if cta:
        print(f"| CTA | {cta.anchor} | {cta.url} | conversion | {'✓' if ok(cta) else '✗'} |")
    if not top:
        print("Không có bài liên quan trong anchor-index. Link về hub cluster hoặc bỏ qua.")
    print("\nChỉ chèn URL có Sitemap ✓. Anchor đặt tự nhiên trong câu (partial match ưu tiên), không dùng 'xem thêm'.")


# ───────────── backfill ─────────────

def mode_backfill(args, entries, sitemap):
    target = next((e for e in entries if e.slug == args.backfill), None)
    if target is None:
        matches = [e for e in entries if args.backfill in e.url]
        if len(matches) == 1:
            target = matches[0]
        else:
            print(f"Không tìm thấy slug '{args.backfill}' trong anchor-index"
                  + (f" ({len(matches)} URL gần giống)" if matches else "") + ". Dùng --add-row trước.", file=sys.stderr)
            sys.exit(1)
    if not target.live:
        print(f"⚠️ {target.url} chưa live (⚠️ trong anchor-index) — backfill sau khi sitemap có URL.", file=sys.stderr)
    q = tokens(target.anchor) | tokens(target.partial)
    core = re.sub(r"\s+(la gi|la sao|nhu the nao|co nen khong)\s*$", "", unaccent(target.anchor)).strip()
    results = []
    for path in sorted(FINAL_DIR.glob("Final-*.md")):
        text, _ = read_text(path)
        if target.url.rstrip("/") in text or target.slug == path.stem.removeprefix("Final-"):
            continue
        _, start, lines = split_frontmatter(text)
        end = body_end(lines, start)
        best = None
        for ln in range(start, end):
            s = lines[ln].strip()
            if not s or s.startswith(("#", "|", "!", ">", "```", "---")):
                continue
            plain = unaccent(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)).replace("-", " ")
            hit = 2.0 if core and core in plain else 0.0
            hit += len(q & tokens(plain)) / max(1, len(q))
            if hit >= 1.0 and (best is None or hit > best[0]):
                best = (hit, ln + 1, s)
        if best:
            results.append((best[0], path.name, best[1], best[2]))
    results.sort(key=lambda r: (-r[0], r[1]))
    top = results[: args.top]
    if args.json:
        print(json.dumps([{"file": f, "line": ln, "score": sc, "excerpt": ex} for sc, f, ln, ex in top],
                         ensure_ascii=False, indent=2))
        return
    print(f"# Backfill candidates → {target.url}\n")
    print(f"Target anchor: **{target.anchor}** · {len(results)} bài có đoạn liên quan, chưa link tới bài này\n")
    print("| # | Bài nguồn | Dòng | Đoạn gợi ý chèn link |")
    print("|---|---|---:|---|")
    for n, (sc, f, ln, ex) in enumerate(top, 1):
        ex = ex.replace("|", "\\|")
        print(f"| {n} | {f} | {ln} | {ex[:160]}{'…' if len(ex) > 160 else ''} |")
    if top:
        print("\nAnchor lấy từ chính câu trong bài nguồn (partial match). Chỉ sửa đúng dòng đã nêu, chạy qa_lint sau khi sửa.")


# ───────────── add-row ─────────────

def mode_add_row(args, entries, sitemap):
    slug = args.add_row
    if any(e.slug == slug for e in entries):
        print(f"Đã có row cho {slug} trong anchor-index — bỏ qua.")
        return
    text, nl = read_text(ANCHOR_INDEX)
    lines = text.split("\n")
    live_url = next((u for u in sitemap if u.rsplit("/", 1)[-1] == slug), None)
    cell = f"✅ `{live_url}`" if live_url else f"⚠️ `Final-{slug}.md`"
    row = f"| {cell} | {args.anchor} | {args.partial or ''} |"
    hdr = next((i for i, l in enumerate(lines) if l.startswith("## ") and args.cluster.lower() in l.lower()), None)
    if hdr is None:
        print(f"Không có section '{args.cluster}'. Section hiện có:", file=sys.stderr)
        for l in lines:
            if l.startswith("## "):
                print("  " + l[3:], file=sys.stderr)
        sys.exit(1)
    j = hdr + 1
    last = None
    while j < len(lines) and not lines[j].startswith("## "):
        if lines[j].startswith("|"):
            last = j
        j += 1
    lines.insert((last or hdr + 3) + 1, row)
    write_text(ANCHOR_INDEX, "\n".join(lines), nl)
    print(f"Đã thêm vào {lines[hdr][3:]}: {row}")
    if not live_url:
        print("⚠️ URL chưa có trong sitemap-cache — chạy `python scripts/fetch_sitemap.py --refresh` sau khi bài live rồi cập nhật row này.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("keyword", nargs="?")
    ap.add_argument("--backfill", metavar="SLUG")
    ap.add_argument("--add-row", dest="add_row", metavar="SLUG")
    ap.add_argument("--anchor")
    ap.add_argument("--partial")
    ap.add_argument("--cluster")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--exclude")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if not ANCHOR_INDEX.exists():
        print(f"Không tìm thấy {ANCHOR_INDEX}", file=sys.stderr)
        sys.exit(2)
    entries, sitemap = load_index(), load_sitemap()
    if args.add_row:
        if not (args.anchor and args.cluster):
            ap.error("--add-row cần --anchor và --cluster")
        mode_add_row(args, entries, sitemap)
    elif args.backfill:
        if args.top == 8:
            args.top = 5
        mode_backfill(args, entries, sitemap)
    elif args.keyword:
        mode_search(args, entries, sitemap)
    else:
        ap.error("cần keyword, --backfill <slug> hoặc --add-row <slug>")


if __name__ == "__main__":
    main()
