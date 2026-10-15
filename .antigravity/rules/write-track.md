---
name: Write Track — HVS SEO Content Pipeline
description: Quy trình 6 phase (0–5) từ keyword đến Final. Kích hoạt bởi /write. Gate & boundary xem workflow-integrity.md.
---

# Write Track — HVS SEO Content Pipeline

Kiến trúc: **Main Agent** (bộ não, viết bài) · **SEO Collector** (cảm biến SERP) · **Quality Guardian** (kiểm định) · **Brand Guardian** (chỉ Mode B/C — audit optimize & cập nhật kiến thức, không tham gia `/write`).
Rule hình thức: `seo-formatting.md` · Gate/Mode/Boundary: `workflow-integrity.md` · Học: `learning-loop.md`.

---

## Phase 0: Pre-flight

```
python scripts/topic_status.py --find "<keyword>"     # đã có bài? Pillar hay Cluster? slug chuẩn?
python scripts/sprint_status.py "<keyword>"            # có trong sprint không (nếu có → dùng persona/cluster đó)
```
- Đã có `Final-<slug>.md` → dừng, đề xuất `/optimize`.
- Chưa có trong topic-clusters → `topic_status.py --add "<kw>" --cluster "<tên cluster>"`.
- `topic_status.py <slug> --set "In Progress"`.

## Phase 1: Context (Sensing)

Load context bắt buộc theo `workflow-integrity.md §2` (1 lần / session).

**SERP (mặc định):**
```
python .antigravity/skills/seo-research/scripts/serp_research.py "<keyword>" --top 10 --extract 5
```
→ SEO Collector tổng hợp theo `.antigravity/agents/seo-collector.md` (competitor outline, PAA, gap, lexicon SSI/VNDirect). Không có API key → Collector dùng WebSearch + WebFetch top 5, cùng format output.

**`--no-serp`:** bỏ Collector; YAML ghi `SERP_Research: false`.

**Internal (song song):** `grep -n "<slug>" seo-strategy/content-plan/revision-log.md` → "Don'ts" của bài/chủ đề tương tự.

## Phase 2: Outline (Planning)

1. Chọn `Word_Count_Target` theo bảng `seo-formatting.md §3` **hoặc** theo đối thủ thực tế từ SERP. Không dùng 1 độ dài mặc định cho mọi bài.
2. Viết Outline theo `.antigravity/skills/seo-research/examples/brief-template.md`:
   - Mỗi H2 (kể cả Kết luận) có `Word_Count`; MAIN 55–65%, HVS Bridge ≥250–300, Kết luận 150–200; Σ ≥ `Word_Count_Target`.
   - `PAA_Questions:` từ SERP, mỗi câu `placement: body | faq`.
   - `Internal_Links:` từ `python scripts/find_links.py "<keyword>" --top 6` — chỉ URL Sitemap ✓ + 1 conversion link.
   - H2 cuối: `## Kết luận` (có thể thêm `: <góc nhìn>`), không rập khuôn "Checklist 4 bước".
3. Lưu `content/blog/1-outlines/Outline-<slug>.md`. Copy `## Revision Log` nếu có.

> 🚧 **GATE 1** — Express/Guided: DỪNG, chờ `/approve`. Auto: tiếp tục.

## Phase 3: Draft + Lint + Quality Guardian + Link

1. **Viết Draft** `content/blog/2-user-review/Draft-<slug>.md` theo đúng Outline, YAML schema `seo-formatting.md §4`.
   - Viết từng section đúng `Word_Count`; thiếu → thêm ví dụ/kịch bản/bảng MỚI (chống padding).
   - Kịch bản "Nếu A → …, Nếu B → …" + cảnh báo rủi ro; HVS Bridge nêu nỗi đau trước sản phẩm, Thực tập số là phễu chính.
   - Công thức Unicode/inline code, không LaTeX; không `---`; không `file:///`.
2. **Lint (BLOCKING):**
   ```
   python scripts/qa_lint.py content/blog/2-user-review/Draft-<slug>.md --fix
   ```
   (Outline tự detect ở `1-outlines/`.) Exit 1 → sửa đúng dòng báo → chạy lại. **Tối đa 2 vòng.**
2a. **Fact check dữ liệu (advisory — không chặn khi mất mạng):**
   ```
   python scripts/market_facts.py --verify content/blog/2-user-review/Draft-<slug>.md
   ```
   `FACT-index-wrong` = số liệu chỉ số sai → sửa bắt buộc. `FACT-ticker` = mã không niêm yết → sửa bắt buộc. `FACT-stale` = mọi mốc cũ hơn 18 tháng → thêm 1 mốc hiện tại. Exit 3 = nguồn dữ liệu chết, bỏ qua bước này.
2b. **Slop check (BLOCKING):**
   ```
   python scripts/slop_check.py content/blog/2-user-review/Draft-<slug>.md -v
   ```
   Tầng thống kê — bắt cái lint không thấy: nhịp câu phẳng, mật độ bằng chứng thấp, câu sáo rỗng, khung H2 trùng bài cũ. Exit 1 → sửa theo rule `SLOP-*` được báo. **Tối đa 2 vòng.**
   Cách sửa theo rule: `SLOP-rhythm`/`burstiness`/`uniform-run` → chèn câu 3–7 từ, gộp/cắt câu · `SLOP-evidence`/`anchor` → thêm mã CP + mốc Tháng M/YYYY + % thật · `SLOP-vague` → thay cụm sáo rỗng bằng số hoặc tiêu chí · `SLOP-template` → đổi khung H2.
3. **Internal link:** chèn theo `Internal_Links` của Outline; thiếu → `find_links.py`. Anchor partial match tự nhiên, không ép "là gì".
4. **Quality Guardian** (`.antigravity/agents/quality-guardian.md`): chỉ khi lint PASS. FAIL → sửa → tối đa 2 vòng. Copy `## Revision Log` từ Outline sang cuối Draft.
5. Vẫn FAIL sau 2 vòng → trình bày kèm `⚠️ Remaining issues`.

> 🚧 **GATE 2** — Guided: DỪNG, chờ `/approve`. Express (đã approve Outline) / Auto: sang Phase 5.

## Phase 4: User review

- User feedback qua chat hoặc ghi cuối file Draft.
- Sửa **đúng section** được nêu (Content Edit Rule); ghi 1 dòng `revision-log.md` trước khi sửa; lint lại.

## Phase 5: Finalize + Learn

Thực hiện `.antigravity/workflows/approve.md` (nhánh Draft):
```
python scripts/finalize.py <slug>          # move → Final, xóa Draft+Outline, status, backlog, progress-log, anchor-index, qa_lint --log
```
Rồi vòng học theo `learning-loop.md` (`/learn` nếu có Revision Log).
