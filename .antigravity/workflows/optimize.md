---
name: optimize
description: Tối ưu bài cũ — SERP gap, Information Gain, anti-AI, link 2 chiều, bảo toàn ảnh. Args: <path Final-*.md | slug>
---

# /optimize

Rule chi tiết: `.antigravity/rules/content-optimization.md`. Không có path → hỏi user.

## 🔄 Bước 0: Context Load

Như `write.md` Bước 0 (1 lần/session). Thêm: `grep -n "<slug>" seo-strategy/content-plan/revision-log.md`.

## Bước 1 — Intake

```
python scripts/topic_status.py <slug> --set Optimizing
python scripts/qa_lint.py content/blog/3-finalized/Final-<slug>.md --no-sitemap   # baseline lỗi cơ học
```
- Copy `Final-<slug>.md` → `content/blog/2-user-review/Optimize-<slug>.md`. **Không sửa Final trực tiếp.**
- Ghi **Intent & Persona Declaration** đầu phiên (không lưu vào bài): TARGET KEYWORD · SEARCH INTENT · PERSONA · PRODUCT BRIDGE (Thực tập số).
- Lập danh sách ảnh gốc (`![…](…)`) — cấm xóa.

## Bước 2 — SERP & Audit

```
python .antigravity/skills/seo-research/scripts/serp_research.py "<keyword>" --top 10 --extract 5
python scripts/find_links.py "<keyword>" --exclude <slug>
python scripts/find_links.py --backfill <slug>
```
- SEO Collector: heading đối thủ, PAA mới (`[THÊM MỚI]` / `[XÓA BỎ]`), content gap.
- Brand Guardian **Mode B**: audit phân tầng sản phẩm, xưng hô, USP.

## Bước 3 — Proposal

Tạo `content/blog/2-user-review/Proposal-<slug>.md`: heading-by-heading `[GIỮ NGUYÊN] / [CẬP NHẬT] / [XÓA BỎ] / [THÊM MỚI]`, Unique Value Block (case study VN, kịch bản Nếu A→…, bảng), link outbound/backfill, ảnh giữ + vị trí mới.

> 🚧 **APPROVAL GATE** — DỪNG LẠI, chờ `/approve` proposal (user gõ "ok proposal" hoặc `/approve`).

## Bước 4 — Rewrite (chỉ trên `Optimize-<slug>.md`)

- Sweep: anti-AI → clarity → So-What → Prove-It → specificity → HVS Bridge → link.
- YAML: `Pipeline_Mode: Optimized`, `Status: Draft`; bỏ `Mode:` cũ.
- Thêm entry `## Revision Log` `(vX - Optimized)`.

## Bước 5 — Lint + QG

```
python scripts/qa_lint.py content/blog/2-user-review/Optimize-<slug>.md --original content/blog/3-finalized/Final-<slug>.md --fix
```
exit 0 → Quality Guardian → PASSED (≤2 vòng). Trình bày Indexation Audit Table (trước/sau).

> 🚧 **APPROVAL GATE 2** — DỪNG LẠI. **KHÔNG TỰ FINALIZE.** Chờ `/approve` → nhánh C của `approve.md`.
