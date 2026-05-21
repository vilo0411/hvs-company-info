---
name: qa-qc
description: Verify checklist bài viết SEO HVS. Brief đã có writing spec — QA chỉ confirm, không phát hiện lại từ đầu.
---

# Skill: QA/QC — Verify Checklist

Brief/Outline đã embed đủ writing spec (persona, tone, anti-AI flags, HVS products, linking obligations). QA chỉ cần verify từng item Yes/No và fix targeted nếu có Fail.

## Workflow

1. **[OPTIONAL] Word Count Script:** Chạy `python .antigravity/skills/qa-qc/scripts/wordcount.py [draft_path]`
   - Script tự parse section, đếm từ, so sánh Outline target ±10%
   - Nếu có section FAIL: **chỉ sửa/bổ sung nội dung tại đúng section bị FAIL đó** (Targeted Fix), tuyệt đối không sửa đổi hay viết lại toàn bộ bài viết.
2. **Verify** từng item trong checklist bên dưới — đánh Yes/No
3. **Fix targeted**: item nào Fail → sửa đúng chỗ đó, không rewrite toàn bài
4. **Re-verify** item vừa fix
5. **PASS** khi tất cả Yes → trình bày cho user

Mục tiêu: PASS trong ≤2 vòng. Nếu cần >2 vòng → vấn đề ở Brief, không phải QA.

> **⛔ Word Count là NON-NEGOTIABLE:** Đếm số từ từng section, so sánh với `Word_Count` trong Outline. Nếu thiếu: bổ sung ví dụ/kịch bản trước khi vào bước QA khác.

---

## Checklist

### SEO Structure & Holistic (Koray Gübür)
- [ ] H1 chứa keyword chính xác & ≤65 ký tự?
- [ ] Sapo: keyword xuất hiện trong 100 từ đầu & ≤150 từ?
- [ ] **Formatting Diversity (BẮT BUỘC):**
  - [ ] Không có đoạn văn nào dài >4 câu hoặc >80 từ?
  - [ ] Không có quá 2 đoạn văn bản thông thường nằm liền kề nhau mà không có danh sách hoặc bảng ngắt quãng?
  - [ ] Toàn bộ các quy trình, bước thực hiện bắt buộc phải viết dưới dạng danh sách (bullet/numbered lists)?
  - [ ] Có ít nhất một bảng so sánh hoặc đối chiếu dữ liệu (Markdown Table) cho mỗi 1000 từ?
  - [ ] Các công thức tính toán hoặc minh họa số liệu được trình bày bằng ký hiệu toán học ($...$ hoặc $$...$$)?
- [ ] **Word Sequence:** Thực thể quan trọng nằm ở 5-7 từ đầu câu? (Rule 1)
- [ ] **Direct Answers:** Câu đầu tiên dưới mỗi H2 trả lời trực tiếp cho Heading? (Rule 9/12)
- [ ] **Bolding:** Chỉ bôi đậm câu trả lời/giá trị cốt lõi (không bold keyword)? (Rule 13)
- [ ] **Entity Enrichment:** Sử dụng các thực thể từ `Entities_Gap_Analysis` trong Outline? (Rule 14)
- [ ] **Bảo chứng SERP:** Outline có liệt kê các Entities/Ý tưởng từ Top 10 đối thủ? (YAML `SERP_Research: true`)?
- [ ] **Content Gap:** Có điểm khác biệt/nâng cấp rõ rệt so với đối thủ?

### Anti-AI & Syntax
- [ ] **Anti-AI scan:** Đọc `.antigravity/rules/anti-ai-digest.md` → loop qua FORBIDDEN_STRINGS, FORBIDDEN_PATTERNS → flag mọi match; verify tất cả REQUIRED items
- [ ] **Certainty:** Không sử dụng các từ "nên", "có lẽ", "cần"? (Rule 2)
- [ ] **If-Logic:** Mệnh đề chính đứng trước mệnh đề "Nếu"? (Rule 10)
- [ ] Câu chủ động là chính (không quá 2 câu bị động/đoạn)?
- [ ] Không có >3 câu liên tiếp cùng cấu trúc S+V+O?
- [ ] Không có danh từ hóa kiểu Anh ("việc thực hiện" → "thực hiện")?

### Specificity & Context
- [ ] **Plural Examples:** Có ví dụ cụ thể ngay sau các danh từ số nhiều? (Rule 7)
- [ ] **Niche Verbs:** Sử dụng đúng hệ động từ của ngành tài chính (giải ngân, tất toán...)? (Rule 6)
- [ ] **Numeric Values:** Sử dụng con số chính xác (%, phí, mã cổ phiếu) thay vì từ mơ hồ? (Rule 4)

### Brand & Persona
- [ ] Persona chuẩn "HVS Senior Mentor" (theo `tone-and-voice.md`)?
- [ ] **Product Hierarchy (BẮT BUỘC):** Lồng ghép HVS tuân thủ đúng phân tầng: **HVS Tài Chính Số** (lộ trình **HVS Thực tập số**) làm trọng tâm chính, các công cụ **HVS Demo** và **HVS Forum** làm bổ trợ phía dưới?
- [ ] Product mentions theo dạng benefit, không phải feature list (theo `financial-logic.md`)?
- [ ] CTA phù hợp Persona & Xưng hô đúng chuẩn: "bạn", "HVS"?

### Terminology & Technical
- [ ] **Professional Lexicon:** Tuyệt đối không dùng từ Amateur (dựa dẫm, chơi chứng...) theo `glossary.md`?
- [ ] **Scenario-based (BẮT BUỘC):** Có kịch bản thực tế đúng công thức "Nếu [Biến số A] -> [Kịch bản 1]. Nếu [Biến số B] -> [Kịch bản 2]" cho các nhận định/giao dịch?
- [ ] **Risk-Reward:** Mọi claim lợi nhuận hoặc hành động đặt lệnh đều đi kèm cảnh báo rủi ro/điều kiện cụ thể?
- [ ] Thuật ngữ đúng theo `glossary.md` & Tên sản phẩm HVS đúng?
- [ ] YAML metadata đủ fields, HVS_Products là danh sách chuỗi phẳng & Anchor text khớp với Title bài đích? (Rule 11)
- [ ] Markdown format chuẩn & Không có typo?

### Word Count (NON-NEGOTIABLE)
- [ ] Tổng số từ toàn bài ≥ `Word_Count_Target` trong YAML?
- [ ] Từng MAIN section đạt `Word_Count` đã ghi trong Outline? (đếm thực tế, không ước lượng)
- [ ] Nếu bất kỳ section nào thiếu từ: bổ sung ví dụ, kịch bản, bảng so sánh TRƯỚC khi PASS?
