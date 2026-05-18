---
name: Write Track — HVS SEO Content Pipeline
description: Quy trình viết bài SEO 3 modes (Express/Guided/Auto). Kích hoạt bởi lệnh /write. Kiến trúc Cảm biến - Bộ não - Tiến hóa.
---

# Write Track — HVS SEO Content Pipeline

## Kiến trúc Hệ thống (Sensor-Brain Architecture)
- **Main Agent (The Brain):** Điều phối, tổng hợp dữ liệu và đưa ra quyết định cuối cùng về nội dung.
- **SEO Collector (External Sensor):** Thu thập dữ liệu thực tế từ thị trường và đối thủ trên SERP. Xem @.antigravity/agents/seo-collector.md.
- **Brand Guardian (Internal Sensor & Memory):** Cung cấp bản sắc thương hiệu, USPs và quản lý "Ký ức" hệ thống. Xem @.antigravity/agents/brand-guardian.md.
- **Quality Guardian (Senior Editor):** Chốt chặn kiểm định nội bộ khắt khe. Xem @.antigravity/agents/quality-guardian.md.

---

## Phase 0: Pre-flight

1. Đọc `seo-strategy/content-plan/progress-log.md` → duplicate check (keyword đã có bài chưa?)
2. Đọc `seo-strategy/content-plan/topic-clusters.md` (nếu có) → xác định Pillar/Cluster role + linking obligations

---

## Phase 1: Context Collection (Sensing Phase)

**Nếu `--no-serp`:**
Main Agent đọc trực tiếp: `resources/audience/personas-deep.md` (fallback: `hvs-target-audience.csv`) → `resources/products/` (1-2 file phù hợp) → `.antigravity/rules/anti-ai-digest.md` + `glossary.md` + `tone-and-voice.md` + `financial-logic.md`. Bỏ qua SEO Collector.

**Nếu SERP (mặc định):** Chạy song song:

1. **Luồng External (SEO Collector Agent):**
   - Cào SERP cho keyword mục tiêu.
   - Trích xuất: Heading đối thủ, Keywords, Thực thể (Entities), Lexicon chuyên môn từ SSI/VNDirect.
   - Output: JSON theo `.antigravity/skills/seo-research/SKILL.md`
2. **Luồng Internal (Main Agent):**
   - Đọc: `resources/audience/personas-deep.md` + `resources/products/` + `hvs-profile.md`
   - Đọc **Past Revision Logs** trong các file Draft/Final gần nhất → thu thập "Don'ts" list
   - Tài nguyên chủ đạo: `glossary.md`, `tone-and-voice.md`, `financial-logic.md`
   - Output: Brand Spec (Tone, Persona, USPs, "Don'ts" list) → embed vào YAML của Outline

---

## Phase 2: Lên Chiến lược & Outline (Planning Phase)
Main Agent thực hiện vai trò "Bộ não":

1.  **Synthesis (Tổng hợp):** Kết hợp dữ liệu từ Collector (Thị trường) + Brand Guardian (Bản sắc) + ICP/Audience.
2.  **Thiết kế Outline:** Tạo Content Brief theo @.antigravity/skills/seo-research/examples/brief-template.md.
    - **Word Count per Heading (BẮT BUỘC):** Mỗi H2 phải có trường `Word_Count` riêng.
      - MAIN sections (phần xương sống): chiếm 60-70% tổng từ — viết đầy đủ ví dụ, số liệu, kịch bản thực tế.
      - SUPPLEMENTAL sections (giải pháp HVS/CTA): chiếm 30-40% tổng từ — ngắn gọn, focus CTA.
      - Tổng cộng các section phải ≥ `Word_Count_Target` trong YAML.
    - **Kiểm tra trước khi lưu:** Σ Word_Count các H2 ≥ Word_Count_Target?
3.  **Lưu file & Review:** Lưu `content/blog/1-outlines/Outline-[slug].md`.
4.  **User Loop:** Main Agent đọc nhận xét trực tiếp trong file Outline (nếu có) -> Tự điều chỉnh dàn ý -> Duyệt qua `/approve`.

---

## Phase 3: Viết Draft & Kiểm định Nội bộ (Internal Loop)
1.  **Main Agent** viết Draft dựa trên Outline đã duyệt.

    > **⛔ ENFORCEMENT — Đọc trước khi viết:**
    > - Viết từng section theo đúng `Word_Count` đã ghi trong Outline. Kiểm tra số từ section đó TRƯỚC khi viết section tiếp theo.
    > - Nếu một section chưa đạt số từ: bổ sung ví dụ cụ thể, kịch bản thực tế, bảng so sánh, hoặc tính toán minh họa.
    > - **Anti-AI:** Đọc `.antigravity/rules/anti-ai-digest.md` → loop qua FORBIDDEN_STRINGS, FORBIDDEN_PATTERNS, verify REQUIRED trước khi bắt đầu viết.
    > - **Formatting Diversity (Lists & Tables):** Bắt buộc chèn danh sách liệt kê (bullet/numbered lists) cho các bước quy trình và ít nhất một bảng Markdown so sánh/đối chiếu để tránh các mảng chữ dài (walls of text).
    > - **Financial Logic (Scenarios & Risk-Reward):** Bắt buộc tích hợp công thức kịch bản "Nếu [Biến số A] -> [Kịch bản 1]. Nếu [Biến số B] -> [Kịch bản 2]" và ghi nhận cảnh báo rủi ro thực tế đi kèm mọi khuyến nghị.
    > - **HVS Product Hierarchy:** Khi lồng ghép thương hiệu HVS, luôn đặt **HVS Tài Chính Số** (với chương trình đào tạo **HVS Thực tập số**) làm giải pháp cốt lõi, các công cụ **HVS Demo** và **HVS Forum** làm bổ trợ phía dưới.
    > - **Word Count:** Sau khi hoàn thành Draft, chạy `python .antigravity/skills/qa-qc/scripts/wordcount.py [draft_path]` để xác nhận từng section đạt target ±10%.

2.  **Audit Nội bộ (BLOCKING):** Main Agent gửi Draft cho **Quality Guardian**.
3.  **Vòng lặp Pass/Fail:**
    - Nếu Quality Guardian báo `FAILED` -> Main Agent tự sửa dựa trên báo cáo lỗi chi tiết.
    - Nếu fail về word count: bổ sung nội dung cụ thể vào đúng section thiếu.
    - Chỉ khi đạt trạng thái `PASSED`, bài viết mới được trình bày cho User.
- **Outline Retention Rule (BẮT BUỘC):** Luôn giữ nguyên file Outline tại `content/blog/1-outlines/Outline-[slug].md` trong suốt các giai đoạn Draft và User Review. KHÔNG được xóa Outline trước khi bài viết được chuyển sang trạng thái Finalized để làm gốc đối chiếu từ cho script `wordcount.py`.
4.  **Lưu file:** `content/blog/2-user-review/Draft-[slug].md`.

---

## Phase 4: User Feedback & Sửa bài
1.  User cung cấp feedback (qua Chat hoặc ghi trực tiếp vào cuối file Draft).
2.  **Main Agent** trực tiếp xử lý feedback và sửa bài.
    - **Targeted Sửa bài (QA-QC & Word Count):** Khi sửa Draft theo ý kiến User hoặc theo báo cáo từ script `wordcount.py`, Agent chỉ được phép sửa/thêm/bớt nội dung tập trung vào ĐÚNG các section bị lỗi hoặc được chỉ định. Tuyệt đối không viết lại hoặc làm xáo trộn các section đã đạt trạng thái PASS.
3.  Mọi nhận xét của User phải được lưu lại trong mục `Revision_Log` ở cuối file hoặc YAML metadata.

---

## Phase 5: Phê duyệt & Tiến hóa (Evolution Phase)
1.  User dùng lệnh `/approve` (khi file hiện tại là Draft).
2.  **Finalize:** Chuyển sang `3-finalized/Final-[slug].md`, cập nhật metadata/log liên quan, xóa đồng thời Outline (`1-outlines/`) và Draft (`2-user-review/`).
3.  **Learning** (nếu có Revision Log):
    - **Content Feedback Loop**: chạy `.antigravity/skills/content-feedback-loop/SKILL.md` → cập nhật `anti-ai-rules.md` + `anti-ai-digest.md`
    - **Brand Guardian Mode C**: đề xuất cập nhật `glossary.md`, `financial-logic.md`, `hvs-profile.md` dựa trên pattern lỗi trong Revision Logs → chờ user xác nhận trước khi ghi
