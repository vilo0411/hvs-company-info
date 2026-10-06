#!/usr/bin/env python3
"""Shared helpers for HVS pipeline scripts. Import only — do not run directly.

    from _common import ROOT, setup_utf8, unaccent, split_frontmatter, read_text, write_text
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Canonical project paths (single place to change if the layout moves)
CONTENT = ROOT / "content/blog"
RAW_DIR = CONTENT / "0-raw"
OUTLINES_DIR = CONTENT / "1-outlines"
DRAFTS_DIR = CONTENT / "2-user-review"
FINAL_DIR = CONTENT / "3-finalized"
PLAN_DIR = ROOT / "seo-strategy/content-plan"
TOPIC_FILE = PLAN_DIR / "topic-clusters.md"
BACKLOG_FILE = PLAN_DIR / "sprint-backlog.md"
PROGRESS_FILE = PLAN_DIR / "progress-log.md"
ANCHOR_INDEX = PLAN_DIR / "anchor-index.md"
REVISION_LOG = PLAN_DIR / "revision-log.md"
STRATEGY_DIR = ROOT / "seo-strategy/resources/content-strategy"
ANTI_AI_RULES = STRATEGY_DIR / "anti-ai-rules.md"
GLOSSARY_FILE = STRATEGY_DIR / "glossary.md"
LEADERSHIP_FILE = ROOT / "resources/confirm-with-leadership.md"
SITEMAP_CACHE = ROOT / "scripts/sitemap-cache.json"
WORDCOUNT_DIR = ROOT / ".antigravity/skills/qa-qc/scripts"
MEMORY_DIR = ROOT / ".antigravity/memory"

HOST = "https://taichinhso.hvsvn.com"
CTA_PREFIX = f"{HOST}/thuc-tap-so"


def setup_utf8() -> None:
    """Force UTF-8 on stdout/stderr (Windows consoles default to cp1252)."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def unaccent(s: str) -> str:
    s = s.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def slugify(s: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", unaccent(s))).strip("-")


def slug_from_path(p: Path | str) -> str:
    stem = Path(p).stem
    return re.sub(r"^(Final|Draft|Outline|Optimize|Proposal|Raw)-", "", stem)


def read_text(p: Path) -> tuple[str, str]:
    """Return (text with LF endings, original newline) so writers can preserve CRLF/LF."""
    raw = p.read_bytes()
    nl = "\r\n" if b"\r\n" in raw else "\n"
    return raw.decode("utf-8-sig").replace("\r\n", "\n"), nl  # utf-8-sig: 169 legacy Finals carry a BOM


def write_text(p: Path, text: str, nl: str = "\n") -> None:
    p.write_bytes(text.replace("\r\n", "\n").replace("\n", nl).encode("utf-8"))


def split_frontmatter(text: str) -> tuple[dict, int, list[str]]:
    """Return (frontmatter dict, body_start_line_index, all_lines). Nested YAML values are kept raw."""
    lines = text.split("\n")
    fm: dict[str, str] = {}
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return fm, i + 1, lines
            m = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", lines[i])
            if m:
                fm[m.group(1)] = m.group(2).strip()
    return fm, 0, lines


def body_end(lines: list[str], start: int = 0) -> int:
    """Index of the Revision Log heading (content after it is not article body), or len(lines)."""
    for i in range(start, len(lines)):
        if re.match(r"^##\s+\**\s*(Revision Log|Nhật ký chỉnh sửa)", lines[i].strip(), re.I):
            return i
    return len(lines)
