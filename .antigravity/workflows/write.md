---
name: write
description: Viết bài SEO chuẩn HVS. Args: "<keyword>" [--step] [--auto] [--no-serp] | --sprint [N] [--with-serp] | --sprint --flush
---

# /write — Full Pipeline (Outline → Draft → Finalize)

Quy trình chi tiết: `.antigravity/rules/write-track.md`. Gate/mode: `.antigravity/rules/workflow-integrity.md §1`.

## Options

| Lệnh | Pipeline_Mode | Gate |
|---|---|---|
| `/write "ETF là gì"` | Express | 1 (sau Outline) |
| `/write "ETF là gì" --step` | Guided | 2 (Outline, Draft) |
| `/write "ETF là gì" --auto` | Auto | 0 |
| `… --no-serp` | (giữ mode) | bỏ SERP, YAML `SERP_Research: false` |
| `/write --sprint [N]` | Express | tạo Outline cho N item `Planned` rồi DỪNG |
| `/write --sprint --with-serp` | Express | như trên, có SERP |
| `/write --sprint --flush` | Express | viết Draft→Final cho mọi item `Outline-Approved` |

`$ARGUMENTS` trống → hỏi keyword. Alias cũ: `/fast` = `--no-serp`, `/detailed` = `--step`.

## 🔄 Bước 0: Context Load (BẮT BUỘC, 1 lần/session)

1. `resources/company/hvs-profile.md`
2. `seo-strategy/resources/content-strategy/anti-ai-rules.md` — **chỉ §0**
3. `seo-strategy/resources/content-strategy/glossary.md`
4. `seo-strategy/resources/content-strategy/tone-and-voice.md`
5. `.antigravity/memory/instincts.md` (+ scope file nếu topic khớp)
6. Persona: đúng 1 section trong `resources/audience/personas-deep.md` + 1–2 file `resources/products/`

Rồi:
```
python scripts/topic_status.py --find "<keyword>"
python scripts/topic_status.py <slug> --set "In Progress"       # sau khi chốt slug
```
Đã có `Final-<slug>.md` → dừng, gợi ý `/optimize`.

## Phase 1 — Context (SERP)

```
python .antigravity/skills/seo-research/scripts/serp_research.py "<keyword>" --top 10 --extract 5
```
→ SEO Collector (`.antigravity/agents/seo-collector.md`) tổng hợp gap/PAA/entities. Không có key → Collector fallback WebSearch+WebFetch.
Song song: `grep -n "<slug>" seo-strategy/content-plan/revision-log.md`.

## Phase 2 — Outline

- Theo `.antigravity/skills/seo-research/examples/brief-template.md`; `Word_Count` từng H2; `PAA_Questions`; `Internal_Links` từ `python scripts/find_links.py "<keyword>" --top 6`.
- Lưu `content/blog/1-outlines/Outline-<slug>.md`. Trình bày tóm tắt (H2 + Word_Count + PAA).

> 🚧 **APPROVAL GATE 1** — Express/Guided: DỪNG LẠI. Chờ người dùng gõ `/approve`. Auto: tiếp tục.

## Phase 3 — Draft + Lint + QG + Link

1. Viết `content/blog/2-user-review/Draft-<slug>.md` (YAML schema `seo-formatting.md §4`, copy `## Revision Log` từ Outline).
2. `python scripts/qa_lint.py content/blog/2-user-review/Draft-<slug>.md --fix` → exit 0 (≤2 vòng).
2a. `python scripts/market_facts.py --verify content/blog/2-user-review/Draft-<slug>.md` → sửa `FACT-index-wrong` / `FACT-ticker` / `FACT-stale`. Exit 3 (nguồn chết) → bỏ qua.
2b. `python scripts/slop_check.py content/blog/2-user-review/Draft-<slug>.md` → exit 0 (≤2 vòng). FAIL = nhịp phẳng / thiếu bằng chứng; sửa theo đúng rule `SLOP-*` được báo, không viết lại cả bài.
3. Chèn internal link theo Outline; thiếu → `find_links.py`.
4. Quality Guardian (`.antigravity/skills/qa-qc/SKILL.md` Bước 1) → PASSED (≤2 vòng).
5. Vẫn FAIL → trình bày kèm `⚠️ Remaining issues`.

> 🚧 **APPROVAL GATE 2** — Guided: DỪNG LẠI, chờ `/approve`. Express/Auto: sang Phase 5.

## Phase 5 — Finalize

Thực hiện `.antigravity/workflows/approve.md` (nhánh Draft) → `python scripts/finalize.py <slug>`.

---

## Sprint Mode — `/write --sprint [N]`

1. `python scripts/sprint_status.py --list Planned` → lấy N item đầu (mặc định tất cả).
2. Không có → "Chạy `/keyword-plan N` để thêm." → DỪNG.
3. Với mỗi item (tuần tự): Bước 0 (rút gọn) → Phase 1 (`--no-serp` trừ khi `--with-serp`) → Phase 2 → lưu Outline → `sprint_status.py "<kw>" --set Outline-Pending` → log `✅ [i/N] Outline-<slug>.md`.
4. **DỪNG** sau item cuối. Không sang Phase 3. Báo: "Review `1-outlines/` → `sprint_status.py "<kw>" --set Outline-Approved` → `/write --sprint --flush`".

## Sprint Flush — `/write --sprint --flush`

1. `python scripts/sprint_status.py --list Outline-Approved`. Không có → DỪNG.
2. Với mỗi item: `sprint_status.py "<kw>" --set Writing` → Phase 3 (lint + QG + link) → `python scripts/finalize.py <slug>` → log `✅ [i/N] Final-<slug>.md (<words> từ · Score <n>)`.
3. Bài FAIL sau 2 vòng → giữ ở `2-user-review/`, ghi `⚠️`, tiếp tục item sau.
4. Summary + gợi ý `/learn` nếu có Revision Log.
