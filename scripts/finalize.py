#!/usr/bin/env python3
"""Finalize an approved Draft (or Optimize) in one deterministic step.

Usage:
  python scripts/finalize.py <slug> [--optimize] [--dry-run] [--force]
        [--anchor "..."] [--partial "a, b"] [--cluster "CLUSTER X"] [--persona P] [--mode Express]

Steps (all-or-nothing after the lint gate):
  1. Lint source (qa_lint) — refuse if CRITICAL unless --force
  2. Snapshot per-H2 Word_Count from Outline → YAML `Section_Targets`
  3. YAML: Status: Finalized, Pipeline_Mode kept (Optimized when --optimize), drop legacy Mode:
  4. Move → content/blog/3-finalized/Final-<slug>.md  (--optimize: backup old Final to archive/optimize-backups/)
  5. Delete Draft/Optimize/Proposal + Outline
  6. topic_status --set Finalized · sprint_status --remove · Publication Log row + Dashboard recount
  7. find_links --add-row (skipped if already registered)
  8. qa_lint --log (score row in revision-log.md)
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (ROOT, OUTLINES_DIR, DRAFTS_DIR, FINAL_DIR, setup_utf8, read_text, write_text,  # noqa: E402
                     split_frontmatter, slug_from_path)

setup_utf8()
PY = sys.executable
BACKUP_DIR = ROOT / "archive/optimize-backups"


def run(args: list[str], check=False) -> subprocess.CompletedProcess:
    return subprocess.run([PY, *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", check=check)


def outline_targets(outline: Path) -> dict[str, int]:
    sys.path.insert(0, str(ROOT / ".antigravity/skills/qa-qc/scripts"))
    try:
        import wordcount as wc  # type: ignore
        return {k: v["target"] for k, v in wc.parse_outline_targets(outline).items()}
    except Exception:
        return {}


def set_yaml(text: str, updates: dict[str, str], drop: tuple[str, ...] = ()) -> str:
    fm, start, lines = split_frontmatter(text)
    if start == 0:
        block = ["---"] + [f"{k}: {v}" for k, v in updates.items()] + ["---", ""]
        return "\n".join(block + lines)
    head = lines[:start]
    out, seen = [], set()
    for l in head:
        m = re.match(r"^([A-Za-z_]+)\s*:", l)
        k = m.group(1) if m else None
        if k in drop:
            continue
        if k in updates:
            out.append(f"{k}: {updates[k]}")
            seen.add(k)
        else:
            out.append(l)
    for k, v in updates.items():
        if k not in seen:
            out.insert(len(out) - 1, f"{k}: {v}")  # before closing ---
    return "\n".join(out + lines[start:])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--optimize", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--anchor")
    ap.add_argument("--partial", default="")
    ap.add_argument("--cluster")
    ap.add_argument("--persona")
    ap.add_argument("--mode")
    a = ap.parse_args()
    slug = slug_from_path(a.slug).lower()

    src = DRAFTS_DIR / (f"Optimize-{slug}.md" if a.optimize else f"Draft-{slug}.md")
    if not src.exists():
        alt = DRAFTS_DIR / f"Draft-{slug}.md"
        if a.optimize and alt.exists():
            src = alt
        else:
            print(f"Không có {src.relative_to(ROOT)}", file=sys.stderr)
            return 1
    final = FINAL_DIR / f"Final-{slug}.md"
    outline = OUTLINES_DIR / f"Outline-{slug}.md"
    proposal = DRAFTS_DIR / f"Proposal-{slug}.md"
    if final.exists() and not a.optimize:
        print(f"{final.relative_to(ROOT)} đã tồn tại — dùng --optimize nếu là bản tối ưu.", file=sys.stderr)
        return 1

    text, nl = read_text(src)
    fm, _, _ = split_frontmatter(text)
    keyword = fm.get("Target_Keyword", slug.replace("-", " "))
    persona = a.persona or fm.get("Persona", "Lan Newbie / Nhà đầu tư F0")
    mode = a.mode or ("Optimized" if a.optimize else fm.get("Pipeline_Mode") or {"Detailed": "Guided", "Fast": "Express"}.get(fm.get("Mode", ""), "Express"))

    # 1. Lint gate
    lint_args = ["scripts/qa_lint.py", str(src), "--json"]
    if a.optimize and final.exists():
        lint_args += ["--original", str(final)]
    r = run(lint_args)
    try:
        rep = json.loads(r.stdout)
    except json.JSONDecodeError:
        print("qa_lint lỗi:\n" + r.stdout + r.stderr, file=sys.stderr)
        return 2
    crit = [f for f in rep["findings"] if f["severity"] == "CRITICAL"]
    print(f"Lint: {'PASS' if rep['pass'] else 'FAIL'} · Score {rep['score']}/100 · CRITICAL {len(crit)} · MAJOR {sum(1 for f in rep['findings'] if f['severity']=='MAJOR')}")
    if crit and not a.force:
        for f in crit:
            print(f"  [{f['check']}] dòng {f['line']}: {f['message']}")
        print("Còn CRITICAL — sửa rồi chạy lại, hoặc --force khi user đồng ý.", file=sys.stderr)
        return 1

    # 2. Section targets snapshot
    targets = outline_targets(outline) if outline.exists() else {}
    updates = {"Status": "Finalized", "Pipeline_Mode": mode}
    if targets and "Section_Targets" not in fm:
        updates["Section_Targets"] = json.dumps(targets, ensure_ascii=False)
    new_text = set_yaml(text, updates, drop=("Mode",))

    plan = [
        f"lint OK ({rep['score']}/100)",
        f"YAML → Status: Finalized, Pipeline_Mode: {mode}" + (f", Section_Targets ({len(targets)} H2)" if targets else ""),
        (f"backup {final.name} → archive/optimize-backups/ và ghi đè" if a.optimize and final.exists() else f"move → {final.relative_to(ROOT)}"),
        "xóa " + ", ".join(p.name for p in (src, outline, proposal) if p.exists()),
        f"topic_status {slug} --set Finalized",
        f"sprint_status \"{keyword}\" --remove (nếu có)",
        f"progress-log: Publication Log + Dashboard",
        "find_links --add-row" if a.anchor or not a.optimize else "anchor-index: giữ nguyên (optimize)",
        "qa_lint --log",
    ]
    print("Kế hoạch:\n  " + "\n  ".join(f"{i + 1}. {s}" for i, s in enumerate(plan)))
    if a.dry_run:
        return 0

    # 3–5. Write Final, backup, delete stage files
    if a.optimize and final.exists():
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy2(final, BACKUP_DIR / f"Final-{slug}.{date.today().isoformat()}.md")
    write_text(final, new_text, nl)
    for p in (src, outline, proposal):
        if p.exists():
            p.unlink()

    # 6. Status / sprint / progress-log
    r = run(["scripts/topic_status.py", slug, "--set", "Finalized"])
    print(r.stdout.strip() or r.stderr.strip())
    if "Không có dòng nào" in r.stderr and a.cluster:
        run(["scripts/topic_status.py", "--add", keyword, "--cluster", a.cluster, "--slug-override", slug])
        run(["scripts/topic_status.py", slug, "--set", "Finalized"])
    r = run(["scripts/sprint_status.py", keyword, "--remove"])
    print(r.stdout.strip() or "sprint: không có trong backlog")
    run(["scripts/sprint_status.py", "--log-publish", keyword, "--persona", persona, "--mode", mode,
         "--file", str(final.relative_to(ROOT)).replace("\\", "/")])
    run(["scripts/sprint_status.py", "--sync"])

    # 7. anchor-index
    if not a.optimize or a.anchor:
        anchor = a.anchor or keyword
        cluster = a.cluster or "CLUSTER"
        r = run(["scripts/find_links.py", "--add-row", slug, "--anchor", anchor, "--partial", a.partial, "--cluster", cluster])
        print(r.stdout.strip() or r.stderr.strip())

    # 8. score log
    run(["scripts/qa_lint.py", str(final), "--log", "--no-sitemap"])
    print(f"\n✅ Finalized: {final.relative_to(ROOT)} · Score {rep['score']}/100")
    print("Tiếp: /learn (nếu có Revision Log) · sau khi bài live: fetch_sitemap.py --refresh → /link --backfill")
    return 0


if __name__ == "__main__":
    sys.exit(main())
