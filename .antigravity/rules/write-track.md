---
name: Write Track — HVS SEO Content Pipeline
description: Quy trình viết bài SEO 3 modes. Kích hoạt bởi lệnh /write. Thay thế detailed-track và fast-track.
---

# Write Track — HVS SEO Content Pipeline

## Modes & Flags

| Mode | Cách gọi | Human Gates | Dùng khi |
|------|---------|------------|---------|
| **Express** | `/write [keyword]` | Outline only | Mặc định — BẮT BUỘC nghiên cứu SERP, AI tự hoàn thiện Draft sau khi Outline được duyệt |
| **Guided** | `/write [keyword] --step` | Outline + Draft | Cần kiểm soát chặt chẽ từng bước (SERP → Outline → Draft) |
| **Auto** | `/write [keyword] --auto` | Không | Batch content, tin tưởng hoàn toàn vào quy trình SERP-first |

**Lưu ý:** Flag `--no-serp` đã bị loại bỏ để đảm bảo chất lượng nội dung theo quy định mới. Mọi bài viết phải bắt đầu bằng Phase 1: Context Collection (SERP Research).

Mode được lưu vào YAML Outline → `/approve` đọc để biết dừng hay chạy tiếp.

---

## Resource Priority (Fallback)

Trước khi chạy pipeline, xác định files nào tồn tại theo thứ tự ưu tiên:

```
Company:
  1. resources/company/hvs-profile.md       ← /setup company
  2. resources/company/identity.md          ← fallback
     resources/company/usps.md

Personas:
  1. resources/audience/personas-deep.md
     → Tồn tại: sử dụng
     → Không tồn tại: spawn Research Agent (scope: audience, mode: quick)
       → BLOCKING — chờ output → tiếp tục với personas-deep.md vừa tạo
  2. resources/audience/icp.md              ← bổ sung nếu có
  3. resources/audience/hvs-target-audience.csv
     ← fallback cuối nếu Research Agent cũng fail

Market:
  1. resources/market/market-landscape.md
     → Tồn tại: SEO Collector đọc Competitor section trước khi WebSearch
     → Không tồn tại + SERP enabled: spawn Research Agent (scope: market, mode: quick)
       NON-BLOCKING — chạy song song với SEO Collector
       (SEO Collector không cần chờ — market context chỉ cải thiện Competitor section)
     → Không tồn tại + --no-serp: bỏ qua hoàn toàn
  2. Live SERP research                     ← always fallback (trừ --no-serp)

Products:
  → Sau khi xác định Persona → đọc 1-2 file liên quan trong resources/products/
  → Chỉ đọc file phù hợp, không đọc hết folder
  → Persona → Product map:
    F0 / NV VP mới đầu tư    → hvs-demo.md, hvs-forum.md
    Sinh viên tài chính       → hvs-thuc-tap-so-nha-phan-tich-chung-khoan.md, hvs-demo.md
    Sinh viên không tài chính → hvs-thuc-tap-so.md, hvs-tai-chinh-so.md
    F1+ / Đã đầu tư           → hvs-forum.md, hvs-tai-chinh-so.md
```

---

## Phase 0: Pre-flight

**Duplicate check:**
- Đọc `seo-strategy/content-plan/progress-log.md`
- Keyword đã có bài Published hoặc In Progress → DỪNG, thông báo cho user

**Cluster check:**
- Đọc `seo-strategy/content-plan/topic-clusters.md` (nếu tồn tại)
- Xác định: bài này là **Pillar** hay **Cluster article**?
- Nếu **Cluster article**:
  - Pillar đã Published → ghi nhận file vào `Internal_Links` YAML (link bắt buộc)
  - Pillar chưa Published → ghi nhận tên Pillar vào YAML (note only, không tạo link bắt buộc). Sẽ dùng `/link` để back-fill khi Pillar được publish.
- Nếu **Pillar**: Cluster articles nào đã Published? → ghi nhận để embed vào Linking Plan

---

## Phase 1: Context Collection (SERP-First Mandatory)
Mọi bài viết đều phải thực hiện nghiên cứu SERP. Không có ngoại lệ.

Chạy **song song**:

**Luồng A — SEO Collector** (spawn Agent theo `.antigravity/agents/seo-collector.md`):
- Nếu `resources/market/market-landscape.md` tồn tại → đọc Competitor section trước để biết đối thủ cần focus
- WebSearch top 5 kết quả cho keyword (ưu tiên site:vn)
- WebFetch từng URL → extract H1/H2/H3, PAA, Featured Snippet, content length, keyword variations
- Output: SERP Intelligence report (format chuẩn trong brief-template.md)

**Luồng B — Main Agent** đọc brand + persona files song song với Luồng A:
- Đọc company file (priority order)
- Đọc persona file (priority order)
- Xác định Persona phù hợp keyword → đọc 1-2 product files tương ứng
- Đọc `seo-strategy/resources/content-strategy/anti-ai-rules.md`

---

## Phase 2: Tạo Outline
1. Kết hợp output Phase 1 + Cluster info từ Phase 0.
2. **BẮT BUỘC**: Tạo Content Brief theo ĐÚNG template tại `.antigravity/skills/seo-research/examples/brief-template.md`.
3. Kiểm tra lại với `anti-ai-rules.md` để đảm bảo không dùng từ cấm trong Outline.
4. **BẮT BUỘC**: Outline file phải chứa section `SERP Intelligence (Audit Proof)` trong YAML frontmatter, liệt kê ít nhất 3 đối thủ và 1 khoảng trống nội dung (Gap Analysis) tìm được qua việc truy cập trực tiếp URL.
5. Lưu: `content/blog/1-outlines/Outline-[slug].md`

**→ Express / Guided: DỪNG — chờ `/approve`**
**→ Auto: tiếp tục Phase 3**

---

## Phase 3: Viết Draft

Đọc: **Outline** (YAML + Content Brief sections)
Không cần đọc lại brand files — đã embedded trong Outline YAML.

Viết từng section theo đúng Key Points trong Brief:
- Mỗi H2/H3: bám sát key points, đưa vào ví dụ cụ thể (mã cổ phiếu / con số / tên sàn)
- H2 đầu tiên của bài Informational: có Definition Block ≤50 từ
- HVS section: dùng Writing Method đã chọn (PAS/AIDA/...), benefit-first
- Kết bài: không dùng "Tóm lại" / "Kết luận" — dùng H2 thay thế

Lưu: `content/blog/2-user-review/Draft-[slug].md` (Status: Draft)

---

## Phase 4: QA/QC

Chạy `.antigravity/skills/qa-qc/SKILL.md` — verify checklist Yes/No.

Nếu có item No → fix targeted (không rewrite toàn bài), verify lại item đó.
Mục tiêu: PASS toàn bộ checklist trong ≤2 vòng.

---

## Phase 5: Internal Linking

Chạy `.antigravity/skills/internal-linking/SKILL.md`:
- Mode: Mặc định `--cluster`. Có thể tùy chỉnh thành `--silo`, `--power`, `--conversion` theo yêu cầu.
- Primary source: `topic-clusters.md` (đã trong context từ Phase 0).
- Verify slug: scan `content/blog/3-finalized/` để confirm file tồn tại.
- Logic: Tuân thủ quy tắc của từng mode đã chọn (Pillar link, Group-silo, Power authority, hoặc Conversion-led).
- Chèn link theo đề xuất của workflow `/link`.

**→ Guided: DỪNG — chờ `/approve`**
**→ Express / Auto: tiếp tục Phase 6**

---

## Phase 6: Finalize

1. Move: `2-user-review/Draft-[slug].md` → `3-finalized/Final-[slug].md`
2. Update YAML: `Status: Finalized`
3. Xóa Draft cũ tại `2-user-review/`
4. Sync 3 files:
   - `progress-log.md`: xóa khỏi Active Pipeline, thêm lên đầu Publication Log, cập nhật count
   - `topic-clusters.md`: ⭕/🔄 → ✅ + filename + cập nhật cluster header count
   - `sprint-backlog.md`: xóa bài vừa finalize (nếu có)
5. **Trigger Back-filling Prompt**:
   - Agent hỏi user: *"Bài [Slug] đã finalize. Bạn có muốn quét các bài cũ để trỏ link về bài mới này không?"*
   - Nếu user đồng ý: Chạy `/link --backfill [slug]`.
6. **Trigger Content Feedback Loop**: đọc Revision Log cuối file (nếu có) → chạy `.antigravity/skills/content-feedback-loop/SKILL.md` → đề xuất cập nhật `anti-ai-rules.md` nếu phát hiện pattern mới
6. Báo cáo: keyword | word count | file path | files updated
