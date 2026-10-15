#!/usr/bin/env python3
"""Deterministic QA linter for HVS SEO articles.

Runs the machine-checkable subset of the Quality Guardian checklist so the LLM only
reasons about semantics (persona, market facts, So-What / Prove-It, product bridge).

Usage:
    python scripts/qa_lint.py <draft.md> [--outline Outline-x.md] [--original Final-x.md]
                              [--keyword "..."] [--fix] [--json] [--log] [--no-sitemap]
    python scripts/qa_lint.py --dump-rules

Exit:   0 = PASS (0 CRITICAL, 0 MAJOR)   1 = FAIL   2 = usage / IO error

Rule sources (parsed at runtime — edit the .md, not this file):
    seo-strategy/resources/content-strategy/anti-ai-rules.md §0
        FORBIDDEN_STRINGS → CL2-hard · RESTRICTED_STRINGS → CL2-soft · HEDGE_WORDS → CL2-hedge
    seo-strategy/resources/content-strategy/glossary.md
        "Thuật ngữ Thị trường & Phân tích" col Amateur → CL3-amateur · "Tone & Xưng hô" TRÁNH → CL3-address
    resources/confirm-with-leadership.md  LINT_BLOCK / FEE_TERMS → BRAND-regulatory / BRAND-fee
    scripts/sitemap-cache.json → LINK-sitemap
    <outline>.md  Word_Count per H2 (via wordcount.py) → WC-section · PAA_Questions → PAA-missing
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (ROOT, ANTI_AI_RULES, GLOSSARY_FILE, LEADERSHIP_FILE, SITEMAP_CACHE, REVISION_LOG,  # noqa: E402
                     WORDCOUNT_DIR, OUTLINES_DIR, HOST, CTA_PREFIX, setup_utf8, split_frontmatter, body_end,
                     slug_from_path)

setup_utf8()

MAX_H1 = 65
META_RANGE = (140, 160)
MAX_PARA_SENTENCES = 4
MAX_PARA_WORDS = 80
MAX_SENTENCE_WORDS = 35
MAX_PROSE_RUN = 2
TABLE_PER_WORDS = 1000
MIN_INTERNAL_LINKS = 3
MAX_HEDGE = 3
SAPO_RANGE = (60, 130)
CONCLUSION_MIN = 120

REQUIRED_FM = ["Author", "Status", "Pipeline_Mode", "Persona", "Target_Keyword", "Search_Intent",
               "Word_Count_Target", "Meta_Description"]

WEIGHTS = {"anti_ai": 30, "seo": 25, "readability": 20, "link": 15, "brand": 10}
PENALTY = {"CRITICAL": 25, "MAJOR": 10, "MINOR": 3}
MINOR_CAP = 30

HIDDEN_UNICODE = re.compile("[​‌‍⁠﻿­]")
VAGUE_TEMPORAL = ["gần đây,", "hiện nay,", "trong những năm qua", "thời gian gần đây", "trong thời gian qua",
                  "những năm gần đây"]
TEMPORAL_MARKER = re.compile(
    r"(tính đến tháng \d{1,2}/\d{4}|tháng \d{1,2}/\d{4}|quý \d/\d{4}|q[1-4][/–-]?\d{4}|năm 20\d{2}|\b\d{1,2}/20\d{2}\b)", re.I)
DATA_POINT = re.compile(r"\d+(?:[.,]\d+)?\s*(?:%|tỷ|triệu|nghìn|điểm)", re.I)
GENERIC_ANCHORS = {"xem thêm", "tại đây", "click vào đây", "ở đây", "bài viết này", "link", "đây"}
LATEX = re.compile(r"(\$\$[^$\n]+\$\$|(?<![\w$])\$[^$\s][^$\n]{0,80}?\$(?![\w$])|\\frac|\\times|\\sum)")
EM_DASH_CONNECTOR = re.compile(r"\S\s+—\s+\S")


@dataclass
class Finding:
    check: str
    category: str
    severity: str
    line: int
    message: str
    excerpt: str = ""


@dataclass
class Report:
    file: str
    findings: list[Finding] = field(default_factory=list)
    fixes: list[str] = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    def add(self, check, category, severity, line, message, excerpt=""):
        self.findings.append(Finding(check, category, severity, line, message, excerpt.strip()[:120]))

    def count(self, sev):
        return sum(1 for f in self.findings if f.severity == sev)

    def score(self) -> tuple[int, dict]:
        per_cat = {}
        for cat, w in WEIGHTS.items():
            s, minor = 100, 0
            for f in self.findings:
                if f.category != cat:
                    continue
                if f.severity == "MINOR":
                    minor += PENALTY["MINOR"]
                else:
                    s -= PENALTY[f.severity]
            per_cat[cat] = max(0, s - min(minor, MINOR_CAP))
        return round(sum(per_cat[c] * WEIGHTS[c] for c in WEIGHTS) / 100), per_cat

    def passed(self) -> bool:
        return self.count("CRITICAL") == 0 and self.count("MAJOR") == 0


# ─────────────────────────── Rule loading ───────────────────────────

def _yaml_list_blocks(path: Path, keys: tuple[str, ...]) -> dict[str, list[str]]:
    """Parse `KEY:` + `  - "value"` lines inside fenced blocks of a markdown file."""
    out: dict[str, list[str]] = {k: [] for k in keys}
    if not path.exists():
        return out
    cur = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([A-Z_]+):\s*$", line.strip())
        if m:
            cur = m.group(1) if m.group(1) in keys else None
            continue
        if cur is None:
            continue
        if not line.startswith("  ") or not line.strip().startswith("- "):
            if line.strip() and not line.startswith(" "):
                cur = None
            continue
        item = line.strip()[2:].split("→")[0].strip()
        q = re.match(r"""^["'](.+?)["']""", item)
        val = (q.group(1) if q else item).replace("...", "").strip().rstrip(".,")
        if val and "[" not in val:
            out[cur].append(val)
    return out


def load_rules() -> dict:
    ai = _yaml_list_blocks(ANTI_AI_RULES, ("FORBIDDEN_STRINGS", "RESTRICTED_STRINGS", "HEDGE_WORDS"))
    lead = _yaml_list_blocks(LEADERSHIP_FILE, ("LINT_BLOCK", "FEE_TERMS"))
    amateur, address = [], []
    if GLOSSARY_FILE.exists():
        sec = ""
        for line in GLOSSARY_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                sec = line
                continue
            if not line.startswith("|") or line.startswith("| :---") or line.startswith("| Bối cảnh") or line.startswith("| Tình huống"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if "Professional vs Amateur" in sec and len(cells) >= 2:
                amateur += [t.strip().strip('"') for t in cells[1].split(",") if t.strip()]
            elif "Xưng hô" in sec and len(cells) >= 3 and cells[0].startswith("Gọi người đọc"):
                address += re.findall(r'"([^"]+)"', cells[2])
    return {
        "hard": ai["FORBIDDEN_STRINGS"], "soft": ai["RESTRICTED_STRINGS"], "hedge": ai["HEDGE_WORDS"],
        "amateur": [a for a in amateur if len(a) > 3], "address": address,
        "regulatory": lead["LINT_BLOCK"], "fee_terms": lead["FEE_TERMS"],
    }


def load_sitemap() -> set[str]:
    if not SITEMAP_CACHE.exists():
        return set()
    return {u.rstrip("/") for u in json.loads(SITEMAP_CACHE.read_text(encoding="utf-8")).get("urls", [])}


# ─────────────────────────── Parsing ───────────────────────────

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s.lower())).strip()


def strip_md(s: str) -> str:
    s = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"`[^`]*`", "", s)
    s = re.sub(r"[*_]", "", s)
    return s.strip()


def split_sentences(text: str) -> list[str]:
    t = re.sub(r"(\d)[.,](\d)", r"\1<d>\2", text)
    t = re.sub(r"\b(TP|Tp|TS|ThS|PGS|GS|Q|P|vs|VD|Ví dụ)\.", r"\1<a>", t)
    parts = re.split(r"(?<=[.!?…])\s+(?=[^\s])", t)
    return [p.replace("<d>", ",").replace("<a>", ".").strip() for p in parts if p.strip()]


def classify(line: str) -> str:
    s = line.strip()
    if not s:
        return "blank"
    if s.startswith("```"):
        return "fence"
    if re.match(r"^#{1,6}\s", s):
        return "heading"
    if re.match(r"^(\*|-|\+|\d+[.)])\s", s):
        return "list"
    if s.startswith("|"):
        return "table"
    if s.startswith(">"):
        return "quote"
    if re.match(r"^!\[", s) or re.match(r"^\[!\[", s):
        return "image"
    if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
        return "hr"
    if s.startswith("<"):
        return "html"
    return "text"


def iter_body(lines, start, end):
    """Yield (index, line) for body lines outside code fences."""
    in_fence = False
    for i in range(start, end):
        s = lines[i].strip()
        if s.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield i, lines[i]


# ─────────────────────────── Checks ───────────────────────────

def check_frontmatter(rep: Report, fm: dict, keyword: str, raw_fm_lines: list[str]):
    if not fm:
        rep.add("FM-missing", "seo", "CRITICAL", 1, "Không có YAML front matter")
        return
    missing = [k for k in REQUIRED_FM if k not in fm]
    if missing:
        rep.add("FM-required", "seo", "MAJOR", 1, "Thiếu field YAML: " + ", ".join(missing))
    if "Mode" in fm and "Pipeline_Mode" not in fm:
        rep.add("FM-mode-legacy", "seo", "MAJOR", 1, "Dùng `Mode:` (cũ) — đổi thành `Pipeline_Mode:`", f"Mode: {fm['Mode']}")
    if fm.get("Pipeline_Mode") and fm["Pipeline_Mode"] not in ("Express", "Guided", "Auto", "Optimized"):
        rep.add("FM-mode-value", "seo", "MINOR", 1, "Pipeline_Mode phải là Express | Guided | Auto | Optimized", fm["Pipeline_Mode"])
    if fm.get("SERP_Research", "").lower() == "false":
        rep.add("SERP-off", "seo", "MINOR", 1, "Bài viết không qua SERP research (SERP_Research: false)")
    # HVS_Products must be a flat list of strings, not {product, benefit} objects
    if any(re.match(r"^\s+-\s+product\s*:", l) for l in raw_fm_lines):
        rep.add("FM-products-shape", "seo", "MAJOR", 1, "HVS_Products phải là list chuỗi phẳng `[\"HVS Thực tập số\", ...]`, không phải object {product, benefit}")
    meta = fm.get("Meta_Description", "")
    if meta:
        lo, hi = META_RANGE
        if not (lo <= len(meta) <= hi):
            rep.add("CL1-meta", "seo", "MAJOR", 1, f"Meta description dài {len(meta)} ký tự (cần {lo}–{hi})", meta)
        if keyword and norm(keyword) not in norm(meta):
            rep.add("CL1-meta", "seo", "MAJOR", 1, "Meta description không chứa target keyword", meta)
    for k, v in fm.items():
        if k not in ("aliases", "HVS_Products") and v.startswith('"') and v.endswith('"'):
            rep.add("FM-quotes", "seo", "MINOR", 1, f"Front matter `{k}` bọc trong ngoặc kép", v)


def check_headings(rep: Report, lines, start, end, keyword):
    h1s, h2s, prev = [], [], 0
    for i, raw in iter_body(lines, start, end):
        m = re.match(r"^(#{1,6})\s+(.*)", raw.strip())
        if not m:
            continue
        lvl, text = len(m.group(1)), m.group(2).strip()
        if lvl == 1:
            h1s.append((i + 1, text))
        if lvl == 2:
            h2s.append((i + 1, text))
        if prev and lvl > prev + 1:
            rep.add("CL1-hierarchy", "seo", "MAJOR", i + 1, f"Nhảy cấp heading H{prev} → H{lvl}", text)
        if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", text):
            rep.add("FMT-heading-icon", "readability", "MINOR", i + 1, "Icon/emoji trong heading", text)
        if lvl == 2 and text.startswith("**") and text.endswith("**"):
            rep.add("FMT-heading-bold", "readability", "MINOR", i + 1, "Heading bọc trong **bold** — bỏ dấu *", text)
        prev = lvl
    if len(h1s) != 1:
        rep.add("CL1-h1", "seo", "CRITICAL", h1s[0][0] if h1s else start + 1, f"Bài có {len(h1s)} H1 (cần đúng 1)")
    else:
        ln, t = h1s[0]
        if len(t) > MAX_H1:
            rep.add("CL1-h1", "seo", "MAJOR", ln, f"H1 dài {len(t)} ký tự (tối đa {MAX_H1})", t)
        if keyword and norm(keyword) not in norm(t):
            rep.add("CL1-h1", "seo", "CRITICAL", ln, "H1 không chứa target keyword", t)
        if re.search(r"\s[|–-]\s*(HVS|Tài chính số)\s*$", t, re.I):
            rep.add("CL1-h1-suffix", "seo", "MINOR", ln, "H1 có hậu tố thương hiệu — bỏ", t)
    rep.stats["h1"] = h1s[0][1] if h1s else ""
    rep.stats["h2"] = len(h2s)
    # Conclusion must be the last H2 and start with "Kết luận"
    if h2s:
        ln, t = h2s[-1]
        if not re.match(r"^\**\s*Kết luận", t, re.I):
            rep.add("BRAND-conclusion", "brand", "MAJOR", ln, "H2 cuối phải là `## Kết luận` (có thể thêm ': ...')", t)
    return h1s, h2s


def check_sapo_and_conclusion(rep: Report, lines, start, end, keyword, h2s):
    first_h2 = h2s[0][0] - 1 if h2s else end
    sapo = [strip_md(lines[i]) for i in range(start, first_h2) if classify(lines[i]) == "text"]
    sapo_text = " ".join(sapo)
    n = len(sapo_text.split())
    rep.stats["sapo_words"] = n
    if not sapo:
        rep.add("CL1-sapo", "seo", "MAJOR", start + 1, "Không có sapo (đoạn mở đầu) trước H2 đầu tiên")
    else:
        if "hvs" not in sapo_text.lower():
            rep.add("BRAND-sapo", "brand", "MAJOR", start + 1, "Sapo không nhắc \"HVS\" (REQUIRED brand_in_sapo)")
        if not (SAPO_RANGE[0] <= n <= SAPO_RANGE[1]):
            rep.add("CL1-sapo-length", "seo", "MINOR", start + 1, f"Sapo {n} từ (chuẩn 80–100, chấp nhận {SAPO_RANGE[0]}–{SAPO_RANGE[1]})")
        if keyword:
            core = re.sub(r"\s+(là gì|là sao|như thế nào|có nên không)\s*$", "", norm(keyword)).strip() or norm(keyword)
            if core not in norm(sapo_text):
                rep.add("CL1-sapo", "seo", "MAJOR", start + 1, f"Target keyword “{core}” không xuất hiện trong sapo")
    if h2s and re.match(r"^\**\s*Kết luận", h2s[-1][1], re.I):
        c_start = h2s[-1][0]
        body = " ".join(strip_md(lines[i]) for i in range(c_start, end) if classify(lines[i]) in ("text", "list"))
        n = len(body.split())
        rep.stats["conclusion_words"] = n
        if "hvs" not in body.lower():
            rep.add("BRAND-conclusion", "brand", "MAJOR", c_start, "Kết luận không nhắc \"HVS\" (REQUIRED brand_in_conclusion)")
        if n < CONCLUSION_MIN:
            rep.add("BRAND-conclusion-length", "brand", "MINOR", c_start, f"Kết luận {n} từ (chuẩn 150–200)")


def check_anti_ai(rep: Report, lines, start, end, rules: dict):
    hedge_hits, soft_hits = [], {}
    in_official_footer = False
    for i, raw in iter_body(lines, start, end):
        low = raw.lower()
        if "về hvs tài chính số:" in low or "thông tin liên hệ:" in low:
            in_official_footer = True
        if in_official_footer:
            if "info@hvsvn.com" in low:
                in_official_footer = False
            continue
        kind = classify(raw)
        if kind in ("table", "image", "html"):
            continue
        for p in rules["hard"]:
            if p.lower() in low:
                rep.add("CL2-hard", "anti_ai", "CRITICAL", i + 1, f"Từ cấm Tier 1: “{p}”", raw)
        for p in rules["soft"]:
            if p.lower() in low:
                soft_hits.setdefault(p, []).append(i + 1)
        if kind == "text":
            for p in rules["hedge"]:
                if re.search(r"(?<!\w)" + re.escape(p.lower()) + r"(?!\w)", low):
                    hedge_hits.append((i + 1, p))
        for t in rules["amateur"]:
            if re.search(r"(?<!\w)" + re.escape(t.lower()) + r"(?!\w)", low):
                rep.add("CL3-amateur", "brand", "MAJOR", i + 1, f"Từ nghiệp dư (glossary): “{t}” — dùng từ chuyên nghiệp", raw)
        for t in rules["address"]:
            if t.lower() in low:
                rep.add("CL3-address", "brand", "MAJOR", i + 1, f"Xưng hô sai: “{t}” — dùng \"bạn\"", raw)
        # Emphatic quotes around ordinary words (not citations / legal titles / after ':')
        for m in re.finditer(r"[\"“]([^\"”\n]{1,60})[\"”]", raw):
            inner = m.group(1).strip()
            nw = len(inner.split())
            before = raw[max(0, m.start() - 14):m.start()].lower()
            if 1 <= nw <= 4 and not inner[0].isupper() and not re.search(r"\d", inner) \
                    and not re.search(r"(:|nói|rằng|gọi là|từ khóa|lệnh|nút|tab|mục|thuật ngữ|chữ|từ)\s*$", before):
                rep.add("FMT-quotes", "anti_ai", "MAJOR", i + 1, f"Ngoặc kép nhấn mạnh quanh từ thường: “{inner}”", raw)
        if HIDDEN_UNICODE.search(raw):
            rep.add("SCRUB-unicode", "anti_ai", "MINOR", i + 1, "Ký tự unicode ẩn (zero-width/BOM)")
        if re.match(r"^\s*>\s*\[!\w+\]", raw):
            rep.add("FMT-callout", "readability", "MAJOR", i + 1, "Callout `> [!NOTE]` không render trên CMS", raw)
        for vt in VAGUE_TEMPORAL:
            if vt in low:
                rep.add("GEO-vague-time", "seo", "MINOR", i + 1, f"Mốc thời gian mơ hồ “{vt.strip(',')}” — dùng Tháng M/Y", raw)
        if kind in ("text", "list", "quote") and LATEX.search(raw) and "VNĐ" not in raw and "USD" not in raw:
            rep.add("FMT-latex", "readability", "CRITICAL", i + 1, "Công thức LaTeX `$...$` — dùng blockquote in đậm hoặc `code`", raw)
        if kind in ("text", "list") and EM_DASH_CONNECTOR.search(strip_md(raw)):
            rep.add("FMT-emdash", "anti_ai", "MAJOR", i + 1, "Dấu — làm từ nối câu — thay bằng dấu phẩy / 'vì' / tách câu", raw)
    for p, lns in soft_hits.items():
        if len(lns) > 1:
            rep.add("CL2-soft", "anti_ai", "MAJOR", lns[0], f"Từ hạn chế Tier 2 “{p}” dùng {len(lns)} lần (tối đa 1)")
    rep.stats["tier2_used"] = len(soft_hits)
    if len(hedge_hits) > MAX_HEDGE:
        rep.add("CL2-hedge", "anti_ai", "MAJOR", hedge_hits[0][0],
                f"Hedge words {len(hedge_hits)} lần (>{MAX_HEDGE}): " + ", ".join(sorted({h for _, h in hedge_hits})) + " — viết khẳng định")
    rep.stats["hedge"] = len(hedge_hits)


def check_brand_facts(rep: Report, lines, start, end, rules: dict):
    """CL5 — sentences naming HVS must not quote fee % or regulatory history."""
    for i, raw in iter_body(lines, start, end):
        if "hvs" not in raw.lower():
            continue
        for sent in split_sentences(strip_md(raw)):
            sl = sent.lower()
            if "hvs" not in sl:
                continue
            if re.search(r"\d+(?:[.,]\d+)?\s*%", sent) and any(t in sl for t in rules["fee_terms"]):
                rep.add("BRAND-fee", "brand", "CRITICAL", i + 1, "Câu nhắc HVS kèm % phí — lãnh đạo yêu cầu KHÔNG nêu con số phí", sent)
            for t in rules["regulatory"]:
                if t in sl:
                    rep.add("BRAND-regulatory", "brand", "CRITICAL", i + 1, f"Câu nhắc HVS kèm “{t}” — không nhắc lịch sử xử lý", sent)
        if re.search(r"\bVN\s?Index\b", raw) and "VN-Index" not in raw:
            rep.add("CL3-vnindex", "seo", "MINOR", i + 1, "Viết `VN-Index` (có gạch ngang)", raw)
    body = "\n".join(lines[start:end]).lower()
    if "thực tập số" in body and re.search(r"\d[\d.,]*\s*(vnđ|vnd|đồng|triệu)", body):
        if "1.500.000" not in body and "1,5 triệu" not in body:
            rep.add("BRAND-fee-amount", "brand", "MINOR", start + 1,
                    "Bài nêu giá tiền và nhắc Thực tập số nhưng không có mức chuẩn \"từ 1.500.000 VNĐ\" — kiểm tra lại")


def check_structure(rep: Report, lines, start, end):
    kinds = [classify(l) for l in lines]
    prose_run = 0
    long_sent, long_para, hr_lines = [], [], []
    in_fence, fence_lines = False, []
    tables, words = 0, 0
    in_table = False
    for i in range(start, end):
        k = kinds[i]
        if k == "fence":
            in_fence = not in_fence
            if in_fence:
                fence_lines.append(i + 1)
            continue
        if in_fence:
            continue
        if k == "table":
            if not in_table:
                tables += 1
            in_table = True
        else:
            in_table = False
        if k == "hr":
            hr_lines.append(i + 1)
        if k == "text":
            prose_run += 1
            txt = strip_md(lines[i])
            sents = split_sentences(txt)
            nw = len(txt.split())
            words += nw
            if len(sents) > MAX_PARA_SENTENCES or nw > MAX_PARA_WORDS:
                long_para.append((i + 1, len(sents), nw))
            for s in sents:
                n = len(s.split())
                if n > MAX_SENTENCE_WORDS:
                    long_sent.append((i + 1, n, s))
        elif k == "list":
            item = strip_md(re.sub(r"^\s*(\*|-|\+|\d+[.)])\s+", "", lines[i]))
            words += len(item.split())
            for s in split_sentences(item):
                if len(s.split()) > MAX_SENTENCE_WORDS:
                    long_sent.append((i + 1, len(s.split()), s))
        if k in ("heading", "list", "table", "image", "quote", "html"):
            prose_run = 0
        if prose_run > MAX_PROSE_RUN:
            rep.add("FMT-prose-run", "readability", "MINOR", i + 1, f"> {MAX_PROSE_RUN} đoạn văn liên tiếp — chèn list/bảng/ảnh/blockquote")
            prose_run = 0
    for ln in hr_lines:
        rep.add("FMT-hr", "readability", "MINOR", ln, "Đường kẻ `---` giữa các phần — xóa (CMS tự tách section)")
    for ln in fence_lines:
        rep.add("FMT-codeblock", "readability", "MAJOR", ln, "Code block ``` trong bài — CMS không render, dùng bảng/blockquote")
    for ln, n, s in long_sent:
        rep.add("CL6-sentence", "readability", "MINOR", ln, f"Câu dài {n} từ (>{MAX_SENTENCE_WORDS})", s)
    for ln, ns, nw in long_para:
        rep.add("FMT-para", "readability", "MINOR", ln, f"Đoạn {ns} câu / {nw} từ (tối đa {MAX_PARA_SENTENCES} câu, {MAX_PARA_WORDS} từ)")
    if len(long_para) > 3:
        rep.add("FMT-para", "readability", "MAJOR", long_para[0][0], f"{len(long_para)} đoạn vượt chuẩn — vi phạm nhiều")
    if len(long_sent) > 5:
        rep.add("CL6-sentence", "readability", "MAJOR", long_sent[0][0], f"{len(long_sent)} câu vượt {MAX_SENTENCE_WORDS} từ — vi phạm nhiều")
    if words >= TABLE_PER_WORDS and tables < words // TABLE_PER_WORDS:
        rep.add("FMT-table-density", "readability", "MINOR", start + 1, f"{tables} bảng cho ~{words} từ (chuẩn ≥1 bảng / {TABLE_PER_WORDS} từ)")
    rep.stats.update({"long_sentences": len(long_sent), "long_paragraphs": len(long_para), "tables": tables})


def check_links(rep: Report, lines, start, end, sitemap: set[str], use_sitemap: bool):
    internal, has_cta = [], False
    for i, raw in iter_body(lines, start, end):
        for m in re.finditer(r"(!?)\[([^\]]*)\]\(([^)\s]+)[^)]*\)", raw):
            is_img, text, url = m.group(1) == "!", m.group(2), m.group(3)
            if is_img:
                if url.startswith("file:///"):
                    rep.add("LINK-file", "link", "CRITICAL", i + 1, f"Ảnh dùng file:/// — dùng path repo-relative content/blog/assets/images/...", raw)
                continue
            if url.startswith("file:///"):
                rep.add("LINK-file", "link", "CRITICAL", i + 1, f"Link file:/// — thay bằng URL sitemap: {url[-60:]}", raw)
                continue
            if url.endswith(".md") or "Final-" in url:
                rep.add("LINK-final", "link", "CRITICAL", i + 1, f"Link tới file .md — thay bằng URL sitemap: {url}", raw)
                continue
            if url.startswith(("../", "./")):
                rep.add("LINK-relative", "link", "CRITICAL", i + 1, f"Link relative: {url}", raw)
                continue
            if url.startswith("/"):
                rep.add("LINK-relative", "link", "CRITICAL", i + 1, f"URL tương đối `{url}` — dùng {HOST}{url}", raw)
                continue
            if url.startswith(HOST):
                clean = url.split("?")[0].split("#")[0].rstrip("/")
                if clean.startswith(CTA_PREFIX):
                    has_cta = True
                else:
                    internal.append((i + 1, text, url))
                if use_sitemap and sitemap and clean not in sitemap:
                    close = difflib.get_close_matches(clean, sitemap, n=1, cutoff=0.8)
                    hint = f" → gần nhất: {close[0]}" if close else " (chạy fetch_sitemap.py --refresh nếu cache cũ)"
                    rep.add("LINK-sitemap", "link", "CRITICAL", i + 1, f"URL không có trong sitemap: {url}{hint}", raw)
                if norm(text) in GENERIC_ANCHORS:
                    rep.add("LINK-anchor-generic", "link", "MINOR", i + 1, f"Anchor chung chung: “{text}”", raw)
            elif "hvsvn.com" in url:
                rep.add("LINK-host", "link", "MAJOR", i + 1, f"URL HVS không chuẩn host `{HOST}`: {url}", raw)
    if not has_cta:
        rep.add("LINK-cta", "link", "MAJOR", start + 1, f"Thiếu conversion link {CTA_PREFIX}…")
    if len(internal) < MIN_INTERNAL_LINKS:
        rep.add("LINK-count", "link", "MAJOR", start + 1, f"Chỉ có {len(internal)} internal link (cần ≥ {MIN_INTERNAL_LINKS}, dùng find_links.py)")
    rep.stats["internal_links"] = len(internal)


def check_geo(rep: Report, lines, start, end):
    body = "\n".join(lines[start:end])
    markers = len(TEMPORAL_MARKER.findall(body))
    data_points = len(DATA_POINT.findall(body))
    rep.stats.update({"temporal_markers": markers, "data_points": data_points})
    if data_points >= 8 and markers == 0:
        rep.add("GEO-no-marker", "seo", "MINOR", start + 1, f"{data_points} data point nhưng 0 mốc thời gian (Tháng M/Y)")


def check_images(rep: Report, lines, start, end, original: Path):
    try:
        orig = original.read_text(encoding="utf-8-sig")
    except OSError as e:
        rep.add("CL1-images", "seo", "MAJOR", 1, f"Không đọc được bài gốc: {e}")
        return
    body = "\n".join(lines[start:end])
    orig_imgs = re.findall(r"!\[[^\]]*\]\(([^)\s]+)", orig)
    missing = [u for u in orig_imgs if u not in body and Path(u).name not in body]
    for u in missing:
        rep.add("CL1-images", "seo", "CRITICAL", start + 1, f"Mất ảnh gốc: {u}")
    rep.stats.update({"images_original": len(orig_imgs), "images_missing": len(missing)})


def check_word_count(rep: Report, draft: Path, outline: Path | None, fm: dict):
    sys.path.insert(0, str(WORDCOUNT_DIR))
    try:
        import wordcount as wc  # type: ignore
    except ImportError:
        rep.add("WC", "seo", "MINOR", 1, "Không import được wordcount.py — bỏ qua word count")
        return
    res = wc.check_file(draft, outline)
    rep.stats["total_words"] = res["total_words"]
    rep.stats["outline"] = Path(res["outline_used"]).name if res["outline_used"] else None
    if res["total_status"] == "FAIL":
        rep.add("WC-total", "seo", "MAJOR", 1,
                f"Tổng {res['total_words']} từ vs target {res['yaml_target']} ({res['total_diff_pct']:+.0f}%, dung sai ±10%)")
    for s in res["sections"]:
        if s["status"] == "FAIL":
            rep.add("WC-section", "seo", "MAJOR", 1,
                    f"[{s['heading'][:50]}] {s['words']}/{s['target']} từ ({s['diff_pct']:+.0f}%) — {s['type']}")
    if not res["outline_used"] and not fm.get("Section_Targets"):
        rep.add("WC-no-outline", "seo", "MINOR", 1, "Không có Outline / Section_Targets — chỉ check tổng từ")


# ─────────────────────────── PAA / FAQ ───────────────────────────

FAQ_HEADING = re.compile(r"^##\s+.*(faq|câu hỏi thường gặp)", re.I)
FAQ_ITEM = re.compile(r"^(?:#{3,4}\s+(.+)|[-*+]\s+\*\*(.+?)\*\*\s*\??)")
_PAA_STOP = {"la", "gi", "co", "cua", "va", "cac", "nhung", "de", "khi", "nao", "the", "thi", "nen", "bao", "nhieu",
             "cach", "lam", "sao", "o", "dau", "toi", "ban", "can", "muon", "khong", "phai", "hay", "voi", "cho", "ve"}


def _ascii_words(text: str) -> list[str]:
    t = unicodedata.normalize("NFD", strip_md(text).lower().replace("đ", "d"))
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return [w for w in re.split(r"[^a-z0-9]+", t) if len(w) > 1 and w not in _PAA_STOP]


def _paa_match(q: str, cand: str) -> bool:
    qw, cw = _ascii_words(q), set(_ascii_words(cand))
    return bool(qw) and sum(w in cw for w in qw) / len(qw) >= 0.7


def parse_outline_paa(text: str) -> list[dict]:
    out, cur, inside = [], None, False
    for line in text.split("\n"):
        if re.match(r"^PAA_Questions\s*:", line):
            inside = True
            continue
        if inside:
            if re.match(r"^[A-Za-z_]+\s*:", line) or line.strip() in ("---", "```"):
                break
            m = re.match(r"""^\s*-\s*(?:q\s*:\s*)?["']?(.+?)["']?\s*$""", line)
            if m and not re.match(r"^\s*placement", line):
                cur = {"q": m.group(1).strip(), "placement": "faq"}
                out.append(cur)
                continue
            m = re.match(r"^\s*placement\s*:\s*(\w+)", line)
            if m and cur:
                cur["placement"] = m.group(1).lower()
    return [q for q in out if q["q"] and not q["q"].startswith("[")]


def faq_items(lines, start, end):
    items, in_faq, i = [], False, start
    while i < end:
        s = lines[i].strip()
        if re.match(r"^##\s", s):
            in_faq = bool(FAQ_HEADING.match(s))
            i += 1
            continue
        m = FAQ_ITEM.match(s) if in_faq else None
        if m:
            if m.group(1):
                ans, j = [], i + 1
                while j < end and not re.match(r"^#{2,4}\s", lines[j].strip()):
                    if lines[j].strip():
                        ans.append(lines[j].strip())
                    j += 1
                items.append((i + 1, m.group(1), " ".join(ans)))
                i = j
                continue
            items.append((i + 1, m.group(2), s[m.end():].lstrip("? ").strip()))
        i += 1
    return items


def check_paa(rep: Report, lines, start, end, outline: Path):
    try:
        paa = parse_outline_paa(outline.read_text(encoding="utf-8-sig"))
    except OSError:
        return
    rep.stats["paa_questions"] = len(paa)
    if not paa:
        return
    headings = [strip_md(l.strip().lstrip("#").strip()) for l in lines[start:end] if re.match(r"^#{2,4}\s", l.strip())]
    faq_qs = [q for _, q, _ in faq_items(lines, start, end)]
    missing = [it for it in paa if not any(_paa_match(it["q"], c) for c in headings + faq_qs)]
    for it in missing:
        where = "H2/H3 thân bài" if it["placement"] == "body" else "FAQ"
        rep.add("PAA-missing", "seo", "MAJOR", start + 1, f"Câu PAA chưa xuất hiện làm {where}: “{it['q']}”")
    rep.stats["paa_covered"] = len(paa) - len(missing)


# ─────────────────────────── Fix (safe, idempotent) ───────────────────────────

def apply_fixes(text: str, sitemap_map: dict[str, str]) -> tuple[str, list[str]]:
    fixes = []
    lines = text.split("\n")
    fm_end = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_end = i + 1
                break
    head, body = "\n".join(lines[:fm_end]), "\n".join(lines[fm_end:])

    def sub_head(pattern, repl, label, flags=0):
        nonlocal head
        new, n = re.subn(pattern, repl, head, flags=flags)
        if n:
            fixes.append(f"{label} ×{n}")
            head = new

    def sub(pattern, repl, label, flags=0):
        nonlocal body
        new, n = re.subn(pattern, repl, body, flags=flags)
        if n:
            fixes.append(f"{label} ×{n}")
            body = new

    sub_head(r"^Mode:\s*(Detailed|Fast|Guided|Express|Auto|Optimized)\s*$",
             lambda m: "Pipeline_Mode: " + {"Detailed": "Guided", "Fast": "Express"}.get(m.group(1), m.group(1)),
             "Mode → Pipeline_Mode", re.M)
    sub(HIDDEN_UNICODE.pattern, "", "Xóa unicode ẩn")
    sub(r"\bVN\s?Index\b", "VN-Index", "VN Index → VN-Index")
    sub(r"^[ \t]*>[ \t]*\[!(?:NOTE|TIP|INFO|WARNING|IMPORTANT)\][ \t]*\n[ \t]*>[ \t]*", "> **Lưu ý:** ", "Callout → > **Lưu ý:**", re.M | re.I)
    sub(r"^[ \t]*(-{3,}|\*{3,}|_{3,})[ \t]*\n", "", "Xóa --- giữa các phần", re.M)
    sub(r"^##\s+\*\*(.+?)\*\*\s*$", r"## \1", "Bỏ bold trong H2", re.M)
    # file:/// image paths → repo-relative
    sub(r"\]\(file:///[^)]*?/(content/blog/assets/[^)]+)\)", r"](\1)", "file:/// ảnh → relative")
    # file:///…/Final-<slug>.md and Final-<slug>.md links → sitemap URL when resolvable
    def link_repl(m):
        slug = m.group(2).lower()
        url = sitemap_map.get(slug)
        return f"[{m.group(1)}]({url})" if url else m.group(0)
    new, n = re.subn(r"\[([^\]]+)\]\((?:file:///[^)]*?/)?Final-([A-Za-z0-9-]+)\.md\)", link_repl, body)
    if n and new != body:
        fixes.append(f"Link Final-*.md → URL sitemap ×{sum(1 for a, b in zip(body.split('\n'), new.split('\n')) if a != b)}")
        body = new
    # Single-line LaTeX $...$ (no $$) → inline code
    sub(r"(?<![\w$])\$([^$\n]{1,60}?)\$(?![\w$])", r"`\1`", "LaTeX $x$ → `x`")
    sub(r"\$\$([^$\n]{1,120}?)\$\$", r"> **\1**", "LaTeX $$x$$ → blockquote")
    sub(r"[ \t]+$", "", "Xóa khoảng trắng cuối dòng", re.M)
    sub(r"\n{3,}", "\n\n", "Gộp dòng trống thừa")
    return ((head + "\n" + body) if head else body), fixes


# ─────────────────────────── Output ───────────────────────────

def render(rep: Report) -> str:
    comp, cats = rep.score()
    out = [f"# QA LINT — {rep.file}", ""]
    out.append(f"**Kết quả:** {'PASS' if rep.passed() else 'FAIL'} · CRITICAL {rep.count('CRITICAL')} · "
               f"MAJOR {rep.count('MAJOR')} · MINOR {rep.count('MINOR')} · **Score {comp}/100** ("
               + ", ".join(f"{k} {v}" for k, v in cats.items()) + ")")
    if rep.stats:
        out.append("Stats: " + ", ".join(f"{k}={v}" for k, v in rep.stats.items() if k != "h1"))
    if rep.fixes:
        out += ["", "Auto-fix đã áp dụng: " + "; ".join(rep.fixes)]
    for sev in ("CRITICAL", "MAJOR", "MINOR"):
        items = [f for f in rep.findings if f.severity == sev]
        if not items:
            continue
        out += ["", f"## {sev} ({len(items)})", "", "| Dòng | Check | Vấn đề | Trích |", "|---:|---|---|---|"]
        for f in sorted(items, key=lambda x: (x.line, x.check)):
            out.append(f"| {f.line} | {f.check} | {f.message.replace('|', '\\|')} | {f.excerpt.replace('|', '\\|')} |")
    if rep.passed():
        out += ["", "Lint PASS. Quality Guardian chỉ cần kiểm tra ngữ nghĩa: CL4 Persona, CL5 số liệu, So-What / Prove-It, HVS Bridge, Holistic SEO."]
    else:
        out += ["", "Sửa các dòng CRITICAL/MAJOR rồi chạy lại. Tối đa 2 vòng — vẫn FAIL thì trình bày kèm ⚠️ Remaining issues."]
    return "\n".join(out)


def append_log(rep: Report, slug: str):
    comp, cats = rep.score()
    header = "## QA Score Log (auto — qa_lint.py)"
    raw = REVISION_LOG.read_bytes() if REVISION_LOG.exists() else b""
    nl = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8") if raw else "# Revision Log — HVS Content\n\n> Append-only. `/approve`, `/learn`, `/revise` ghi feedback; `qa_lint.py --log` ghi điểm.\n"
    row = (f"| {date.today().isoformat()} | {slug} | {comp} | {rep.count('CRITICAL')}/{rep.count('MAJOR')}/{rep.count('MINOR')} | "
           + " ".join(f"{k[:5]}={v}" for k, v in cats.items()) + " |")
    body = text.rstrip("\r\n")
    if header not in text:
        body += f"{nl}{nl}{header}{nl}{nl}| Ngày | Slug | Score | C/M/m | Theo nhóm |{nl}|---|---|---:|---|---|"
    body += nl + row + nl
    REVISION_LOG.write_bytes(body.encode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft", nargs="?")
    ap.add_argument("--outline")
    ap.add_argument("--original")
    ap.add_argument("--keyword")
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--log", action="store_true")
    ap.add_argument("--no-sitemap", action="store_true")
    ap.add_argument("--dump-rules", action="store_true")
    args = ap.parse_args()

    rules = load_rules()
    if args.dump_rules:
        for k, v in rules.items():
            print(f"{k}: {len(v)} — {', '.join(v[:6])}{' …' if len(v) > 6 else ''}")
        return 0
    if not args.draft:
        ap.error("cần <draft.md>")

    path = Path(args.draft)
    try:
        raw = path.read_bytes()
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    nl = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8-sig").replace("\r\n", "\n")  # strip BOM (legacy files)

    sitemap = set() if args.no_sitemap else load_sitemap()
    rep = Report(file=str(path))
    if args.fix:
        smap = json.loads(SITEMAP_CACHE.read_text(encoding="utf-8")).get("slug_map", {}) if SITEMAP_CACHE.exists() else {}
        fixed, fixes = apply_fixes(text, smap)
        if fixed != text:
            path.write_bytes(fixed.replace("\n", nl).encode("utf-8"))
            text = fixed
        rep.fixes = fixes

    fm, start, lines = split_frontmatter(text)
    end = body_end(lines, start)
    keyword = args.keyword or fm.get("Target_Keyword", "")
    slug = slug_from_path(path)
    rep.stats["keyword"] = keyword

    outline = Path(args.outline) if args.outline else None
    if outline is None:
        cand = OUTLINES_DIR / f"Outline-{slug}.md"
        outline = cand if cand.exists() else None

    check_frontmatter(rep, fm, keyword, lines[:start])
    h1s, h2s = check_headings(rep, lines, start, end, keyword)
    check_sapo_and_conclusion(rep, lines, start, end, keyword, h2s)
    check_anti_ai(rep, lines, start, end, rules)
    check_brand_facts(rep, lines, start, end, rules)
    check_structure(rep, lines, start, end)
    check_links(rep, lines, start, end, sitemap, not args.no_sitemap)
    check_geo(rep, lines, start, end)
    if args.original:
        check_images(rep, lines, start, end, Path(args.original))
    check_word_count(rep, path, outline, fm)
    if outline:
        check_paa(rep, lines, start, end, outline)

    if args.log:
        append_log(rep, slug)
    if args.json:
        comp, cats = rep.score()
        print(json.dumps({"file": rep.file, "pass": rep.passed(), "score": comp, "categories": cats,
                          "stats": rep.stats, "fixes": rep.fixes, "findings": [asdict(f) for f in rep.findings]},
                         ensure_ascii=False, indent=2))
    else:
        print(render(rep))
    return 0 if rep.passed() else 1


if __name__ == "__main__":
    sys.exit(main())
