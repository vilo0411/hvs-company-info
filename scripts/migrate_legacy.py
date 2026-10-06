#!/usr/bin/env python3
"""Batch-migrate legacy Final articles to the current standard. DRY-RUN by default.

Usage:
  python scripts/migrate_legacy.py [paths…] [--apply] [--only yaml,file-links,final-links,image-paths,latex,hr]
                                   [--collect-revision-logs] [--report seo-strategy/content-plan/migration-report.md]

Transforms (idempotent, applied only with --apply):
  yaml         Mode: → Pipeline_Mode: (Detailed→Guided, Fast→Express) · add Status: Finalized if missing
               · HVS_Products {product, benefit} objects → flat string list
  file-links   [text](file:///…/Final-<slug>.md) → sitemap URL when slug resolves (else report)
  final-links  [text](Final-<slug>.md) / (…/Final-<slug>.md) → sitemap URL when slug resolves
  image-paths  ![alt](file:///…/content/blog/assets/…) → repo-relative path
  latex        $x$ single-line → `x` ; $$x$$ → > **x**
  hr           remove `---` rules between sections (frontmatter untouched)
Report-only (need rewriting by hand): Tier-1 phrases (qa_lint CL2-hard), em-dash connectors, remaining file:/// links.

--collect-revision-logs  copy each Final's `## Revision Log` into seo-strategy/content-plan/revision-log.md
                         under `### [legacy] <slug>` (skips slugs already present).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import ROOT, FINAL_DIR, REVISION_LOG, SITEMAP_CACHE, setup_utf8, read_text, write_text, split_frontmatter, body_end  # noqa: E402
import qa_lint  # noqa: E402

setup_utf8()
ALL = ["yaml", "file-links", "final-links", "image-paths", "latex", "hr"]
MODE_MAP = {"Detailed": "Guided", "Fast": "Express", "Guided": "Guided", "Express": "Express", "Auto": "Auto", "Optimized": "Optimized"}


def slug_map() -> dict[str, str]:
    return json.loads(SITEMAP_CACHE.read_text(encoding="utf-8")).get("slug_map", {}) if SITEMAP_CACHE.exists() else {}


def migrate_yaml(head: list[str]) -> tuple[list[str], Counter]:
    c = Counter()
    out, i = [], 0
    has_status = any(re.match(r"^Status\s*:", l) for l in head)
    while i < len(head):
        l = head[i]
        m = re.match(r"^Mode\s*:\s*(\w+)", l)
        if m and not any(re.match(r"^Pipeline_Mode\s*:", x) for x in head):
            out.append(f"Pipeline_Mode: {MODE_MAP.get(m.group(1), 'Express')}")
            c["yaml:mode"] += 1
            i += 1
            continue
        if m:  # both present → drop legacy
            c["yaml:mode-dup"] += 1
            i += 1
            continue
        if re.match(r"^HVS_Products\s*:\s*$", l) and i + 1 < len(head) and re.match(r"^\s+-\s+product\s*:", head[i + 1]):
            names = []
            j = i + 1
            while j < len(head) and head[j].startswith("  "):
                pm = re.match(r"^\s+-\s+product\s*:\s*(.+?)\s*$", head[j])
                if pm:
                    names.append(pm.group(1).strip('"'))
                j += 1
            out.append("HVS_Products: " + json.dumps(names, ensure_ascii=False))
            c["yaml:products"] += 1
            i = j
            continue
        out.append(l)
        i += 1
    if not has_status:
        out.insert(len(out) - 1, "Status: Finalized")
        c["yaml:status"] += 1
    return out, c


def migrate_body(body: str, only: set[str], smap: dict[str, str]) -> tuple[str, Counter, list[str]]:
    c, notes = Counter(), []

    def link_repl(m):
        slug = m.group(2).lower()
        url = smap.get(slug)
        if url:
            c["links:resolved"] += 1
            return f"[{m.group(1)}]({url})"
        c["links:unresolved"] += 1
        notes.append(f"link chưa live: {slug}")
        return m.group(0)

    if "image-paths" in only:
        body, n = re.subn(r"\]\(file:///[^)]*?/(content/blog/assets/[^)]+)\)", r"](\1)", body)
        c["image-paths"] += n
    if "file-links" in only:
        body = re.sub(r"\[([^\]]+)\]\(file:///[^)]*?/Final-([A-Za-z0-9-]+)\.md\)", link_repl, body)
    if "final-links" in only:
        body = re.sub(r"\[([^\]]+)\]\((?:[^)]*?/)?Final-([A-Za-z0-9-]+)\.md\)", link_repl, body)
    if "latex" in only:
        body, n = re.subn(r"\$\$([^$\n]{1,120}?)\$\$", r"> **\1**", body)
        c["latex:block"] += n
        body, n = re.subn(r"(?<![\w$])\$([^$\n]{1,60}?)\$(?![\w$])", r"`\1`", body)
        c["latex:inline"] += n
    if "hr" in only:
        body, n = re.subn(r"^[ \t]*(-{3,}|\*{3,}|_{3,})[ \t]*\n", "", body, flags=re.M)
        c["hr"] += n
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body, c, notes


def report_only(text: str, rules: dict) -> list[str]:
    fm, start, lines = split_frontmatter(text)
    end = body_end(lines, start)
    hits = []
    for i in range(start, end):
        low = lines[i].lower()
        for p in rules["hard"]:
            if p.lower() in low:
                hits.append(f"L{i + 1} từ cấm “{p}”")
        if qa_lint.EM_DASH_CONNECTOR.search(qa_lint.strip_md(lines[i])) and not lines[i].strip().startswith("|"):
            hits.append(f"L{i + 1} em-dash")
        if "file:///" in lines[i]:
            hits.append(f"L{i + 1} file:/// còn lại")
    return hits


def collect_revision_logs(files: list[Path], apply: bool) -> int:
    existing = REVISION_LOG.read_text(encoding="utf-8") if REVISION_LOG.exists() else ""
    chunks, n = [], 0
    for p in files:
        slug = p.stem.removeprefix("Final-")
        if f"### [legacy] {slug}" in existing:
            continue
        text, _ = read_text(p)
        _, start, lines = split_frontmatter(text)
        i = body_end(lines, start)
        if i >= len(lines):
            continue
        log = "\n".join(l for l in lines[i + 1:] if l.strip())
        chunks.append(f"### [legacy] {slug}\n{log}\n")
        n += 1
    if apply and chunks:
        raw = REVISION_LOG.read_bytes() if REVISION_LOG.exists() else b""
        nl = "\r\n" if b"\r\n" in raw else "\n"
        marker = "## QA Score Log"
        text = raw.decode("utf-8") if raw else "# Revision Log — HVS Content\n\n"
        block = "\n## Legacy Revision Logs (migrate_legacy.py, " + date.today().isoformat() + ")\n\n" + "\n".join(chunks)
        text = text.replace(marker, block + "\n" + marker, 1) if marker in text else text.rstrip("\n") + "\n" + block
        REVISION_LOG.write_bytes(text.replace("\r\n", "\n").replace("\n", nl).encode("utf-8"))
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", default=",".join(ALL))
    ap.add_argument("--collect-revision-logs", action="store_true")
    ap.add_argument("--report", default="seo-strategy/content-plan/migration-report.md")
    a = ap.parse_args()
    only = {x.strip() for x in a.only.split(",") if x.strip()}
    files = [Path(p) for p in a.paths] if a.paths else sorted(FINAL_DIR.glob("Final-*.md"))
    smap = slug_map()
    rules = qa_lint.load_rules()
    total, per_file = Counter(), []

    for p in files:
        text, nl = read_text(p)
        fm, start, lines = split_frontmatter(text)
        head, body = lines[:start], "\n".join(lines[start:])
        c = Counter()
        if start and "yaml" in only:
            head, cy = migrate_yaml(head)
            c += cy
        body, cb, notes = migrate_body(body, only, smap)
        c += cb
        manual = report_only(text, rules)
        new_text = "\n".join(head + [body]) if start else body
        changed = new_text != text
        if changed and a.apply:
            write_text(p, new_text, nl)
        total += c
        total["files:changed"] += int(changed)
        total["files:manual"] += int(bool(manual))
        per_file.append((p.name, c, manual, notes))

    n_logs = collect_revision_logs(files, a.apply) if a.collect_revision_logs else 0

    L = [f"# Migration report — {date.today().isoformat()} ({'APPLIED' if a.apply else 'DRY-RUN'})", "",
         f"Files: {len(files)} · thay đổi: {total['files:changed']} · cần sửa tay: {total['files:manual']}", "",
         "| Transform | Số lần |", "|---|---:|"]
    L += [f"| {k} | {v} |" for k, v in sorted(total.items()) if not k.startswith("files:")]
    if a.collect_revision_logs:
        L += ["", f"Revision Log gom: {n_logs} bài"]
    L += ["", "## Cần sửa tay (report-only)", ""]
    for name, c, manual, notes in per_file:
        if manual or notes:
            L.append(f"### {name}")
            L += [f"- {h}" for h in manual[:12]] + [f"- {n}" for n in notes[:6]]
            if len(manual) > 12:
                L.append(f"- … +{len(manual) - 12}")
            L.append("")
    rep = "\n".join(L)
    Path(ROOT / a.report).write_text(rep, encoding="utf-8")
    print("\n".join(L[:8 + len([k for k in total if not k.startswith('files:')])]))
    print(f"\nBáo cáo đầy đủ: {a.report}")
    if not a.apply:
        print("Dry-run — không ghi file bài viết. Thêm --apply để áp dụng.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
