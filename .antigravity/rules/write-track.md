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

## Giới hạn Giai đoạn theo Lệnh (Execution Boundaries)

Để tránh việc agent tự động viết tiếp (over-automation) vượt quá yêu cầu của lệnh, agent phải tuân thủ nghiêm ngặt các điểm dừng sau:
- **Lệnh `/write --sprint` hoặc `/write --sprint --with-serp`:** Chỉ chạy đến hết **Phase 2 (Tạo Outline)**. Sau khi lưu các file Outline và cập nhật backlog sang `Outline-Pending`, **BẮT BUỘC PHẢI DỪNG LẠI** và báo cáo. KHÔNG được chạy tiếp sang Phase 3 (Draft) hay các phase sau.
- **Lệnh `/write [keyword] --step` (Guided Mode):** Chỉ chạy đến hết **Phase 2 (Tạo Outline)** và dừng lại chờ lệnh `/approve` tiếp theo từ user. Sau khi user duyệt Outline bằng `/approve`, agent mới chuyển sang viết Draft và **BẮT BUỘC PHẢI DỪNG LẠI** ở cuối Phase 3 (Draft) để chờ duyệt lần 2.
- **Lệnh `/write --sprint --flush`:** Chỉ chạy đối với các item có status `Outline-Approved`, bắt đầu từ **Phase 3 (Draft)** cho đến **Phase 5 (Finalize)**.
- **Lệnh `/write [keyword]` (Express Mode):** Chạy từ Phase 0 đến Phase 2, dừng lại báo cáo Outline. Sau khi user chạy `/approve`, agent sẽ chạy một mạch từ Phase 3 đến Phase 5 (Auto-finalize).
- **Lệnh `/write [keyword] --auto` (Auto Mode):** Chạy một mạch không dừng từ Phase 0 đến Phase 5.

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
2.  **Định lượng & Phân loại bài viết (Word Count Target):**
    Tuyệt đối KHÔNG sử dụng một độ dài mặc định (ví dụ: 1.200 từ) cho tất cả bài viết. Độ dài mục tiêu (`Word_Count_Target`) phải được xác định dựa trên phân tích đối thủ thực tế từ SERP (hoặc theo phân loại nội dung dưới đây nếu ở chế độ `--no-serp`):
    - **Bài phân tích chuỗi giá trị ngành sâu (Deep Industry Value Chain):** 1.800 – 2.500 từ (Mục tiêu tối thiểu: 2.000 từ để bao quát toàn bộ các mắt xích, doanh nghiệp niêm yết lớn và yếu tố vĩ mô).
    - **Bài hướng dẫn tỷ số tài chính / định lượng (Financial Ratio Guides):** 1.200 – 1.500 từ (Mục tiêu: 1.400 từ để có đủ không gian cho công thức toán học, ví dụ tính toán số liệu cụ thể và lọc cổ phiếu).
    - **Bài khái niệm tài chính chiến lược / chu kỳ (Strategic & Market Concepts):** 1.200 từ (Mục tiêu: 1.200 từ để phân tích chi tiết các giai đoạn thị trường, ma trận chiến lược).
    - **Bài định nghĩa thuật ngữ cơ bản (Basic Term Definitions):** 1.100 – 1.200 từ (Mục tiêu: 1.200 từ để đảm bảo độ sâu chi tiết, Sapo dài 80-100 từ, HVS Bridge dài 250-300 từ, và Kết luận dài 150-200 từ).
3.  **Thiết kế Outline:** Tạo Content Brief theo @.antigravity/skills/seo-research/examples/brief-template.md.
    - **Cấu trúc bắt buộc:** Outline BẮT BUỘC phải có tiêu đề Kết luận ở cuối (H2: Kết luận...). Tiêu đề kết luận phải tùy biến theo từ khóa (Ví dụ: "Kết luận rủi ro doanh nghiệp...").
    - **Word Count per Heading (BẮT BUỘC):** Mỗi H2 (bao gồm cả H2 Kết luận) phải có trường `Word_Count` riêng.
      - MAIN sections (phần xương sống): chiếm 55-65% tổng từ — viết đầy đủ ví dụ, số liệu, kịch bản thực tế.
      - SUPPLEMENTAL sections (giải pháp HVS/CTA) & Conclusion (Kết luận): chiếm 35-45% tổng từ — phải được viết chi tiết, sâu sắc, tránh viết chung chung hay quá ngắn. Section giải pháp HVS phải đạt tối thiểu 250-300 từ để nêu bật đầy đủ nỗi đau/bẫy tâm lý và cách HVS giải quyết. Section Kết luận phải đạt tối thiểu 150-200 từ để tóm tắt trọn vẹn bài học và checklist hành động.
      - Tổng cộng các section phải ≥ `Word_Count_Target` trong YAML.
    - **Kiểm tra trước khi lưu:** Σ Word_Count các H2 ≥ Word_Count_Target?
4.  **Lưu file & Review:** Lưu `content/blog/1-outlines/Outline-[slug].md`.
5.  **User Loop:** Main Agent đọc nhận xét trực tiếp trong file Outline (nếu có) -> Tự điều chỉnh dàn ý -> Duyệt qua `/approve`.

---

## Phase 3: Viết Draft & Kiểm định Nội bộ (Internal Loop)
1.  **Main Agent** viết Draft dựa trên Outline đã duyệt.

    > **⛔ ENFORCEMENT — Đọc trước khi viết:**
    > - Viết từng section theo đúng `Word_Count` đã ghi trong Outline. Kiểm tra số từ section đó TRƯỚC khi viết section tiếp theo.
    > - Nếu một section chưa đạt số từ: bổ sung ví dụ cụ thể, kịch bản thực tế, bảng so sánh, hoặc tính toán minh họa.
    > - **Anti-AI:** Đọc `.antigravity/rules/anti-ai-digest.md` → loop qua FORBIDDEN_STRINGS, FORBIDDEN_PATTERNS, verify REQUIRED trước khi bắt đầu viết.
    > - **⛔ CHỐNG PADDING:** KHÔNG chuyển danh sách bullet/numbered đã viết thành các đoạn văn "Nguyên nhân thứ 1 là...; Nguyên nhân thứ 2 là...;" để tăng số từ. Nếu section thiếu từ: thêm ví dụ cụ thể MỚI, kịch bản thực tế MỚI, bảng so sánh MỚI — không viết lại nội dung đã có dưới dạng list. Danh sách ngắn gọn là intentional, không phải lỗi cần "sửa".
    > - **Conclusion (Kết luận):** Bắt buộc phải viết phần Kết luận (H2) ở cuối bài theo đúng Outline. Tuyệt đối không dùng các từ khóa cấm trong TIER 1 như "Tóm lại,", "Kết luận là,".
    > - **Formatting Diversity (Lists & Tables):** Bắt buộc chèn danh sách liệt kê (bullet/numbered lists) cho các bước quy trình và ít nhất một bảng Markdown so sánh/đối chiếu để tránh các mảng chữ dài (walls of text).
    > - **Financial Logic (Scenarios & Risk-Reward):** Bắt buộc tích hợp công thức kịch bản "Nếu [Biến số A] -> [Kịch bản 1]. Nếu [Biến số B] -> [Kịch bản 2]" và ghi nhận cảnh báo rủi ro thực tế đi kèm mọi khuyến nghị.
    > - **HVS Product Hierarchy:** Khi lồng ghép thương hiệu HVS, luôn đặt **HVS Thực tập số** (chương trình đào tạo thực chiến trọng tâm của **HVS Tài chính số**) làm phễu chuyển đổi chính cho tất cả các đối tượng (kể cả F0, F1 hay Sinh viên). Các sản phẩm **HVS Demo** (giao dịch mô phỏng) và **HVS Forum** (cộng đồng) chỉ đóng vai trò là công cụ bổ trợ thực hành và thảo luận nằm trong hệ sinh thái hỗ trợ cho chương trình **HVS Thực tập số**.
    > - **Word Count:** Sau khi hoàn thành Draft, chạy `python .antigravity/skills/qa-qc/scripts/wordcount.py [draft_path]` để xác nhận từng section đạt target ±10%.

2.  **Audit Nội bộ (BLOCKING):** Main Agent gửi Draft cho **Quality Guardian**.
3.  **Vòng lặp Pass/Fail:**
    - Nếu Quality Guardian báo `FAILED` -> Main Agent tự sửa dựa trên báo cáo lỗi chi tiết.
    - Nếu fail về word count: bổ sung nội dung cụ thể vào đúng section thiếu.
    - Chỉ khi đạt trạng thái `PASSED`, bài viết mới được trình bày cho User.
- **Outline Retention Rule (BẮT BUỘC):** Giữ nguyên file Outline tại `content/blog/1-outlines/Outline-[slug].md` trong suốt các giai đoạn Draft và User Review — cần để script `wordcount.py` đối chiếu target. **Sau khi bài được Finalize: xóa file Outline ngay.**
- **Bảo toàn Revision Log (BẮT BUỘC):** Khi chuyển đổi/viết từ Outline sang Draft, Agent BẮT BUỘC phải sao chép phần `## Revision Log` (hoặc `## Nhật ký chỉnh sửa (Revision Log)`) từ Outline sang cuối file Draft để tiếp tục lưu vết và kích hoạt learning feedback loop sau này.
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
2.  **Finalize:** Chuyển sang `3-finalized/Final-[slug].md`, cập nhật metadata/log liên quan, xóa Draft (`2-user-review/Draft-[slug].md`) và xóa Outline (`1-outlines/Outline-[slug].md`).
3.  **Learning** (nếu có Revision Log):
    - **Content Feedback Loop**: chạy `.antigravity/skills/content-feedback-loop/SKILL.md` → cập nhật `anti-ai-rules.md` + `anti-ai-digest.md`
    - **Brand Guardian Mode C**: đề xuất cập nhật `glossary.md`, `financial-logic.md`, `hvs-profile.md` dựa trên pattern lỗi trong Revision Logs → chờ user xác nhận trước khi ghi
