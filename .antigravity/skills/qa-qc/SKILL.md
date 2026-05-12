---
name: qa-qc
description: Verify checklist bài viết SEO HVS. Brief đã có writing spec — QA chỉ confirm, không phát hiện lại từ đầu.
---

# Skill: QA/QC — Verify Checklist

Brief/Outline đã embed đủ writing spec (persona, tone, anti-AI flags, HVS products, linking obligations). QA chỉ cần verify từng item Yes/No và fix targeted nếu có Fail.

## Workflow

1. **Verify** từng item trong checklist bên dưới — đánh Yes/No
2. **Fix targeted**: item nào Fail → sửa đúng chỗ đó, không rewrite toàn bài
3. **Re-verify** item vừa fix
4. **PASS** khi tất cả Yes → trình bày cho user

Mục tiêu: PASS trong ≤2 vòng. Nếu cần >2 vòng → vấn đề ở Brief, không phải QA.

---

## Checklist

### SEO Structure & Holistic (Koray Gübür)
- [ ] H1 chứa keyword chính xác & ≤65 ký tự?
- [ ] Sapo: keyword xuất hiện trong 100 từ đầu & ≤150 từ?
- [ ] **Word Sequence:** Thực thể quan trọng nằm ở 5-7 từ đầu câu? (Rule 1)
- [ ] **Direct Answers:** Câu đầu tiên dưới mỗi H2 trả lời trực tiếp cho Heading? (Rule 9/12)
- [ ] **Bolding:** Chỉ bôi đậm câu trả lời/giá trị cốt lõi (không bold keyword)? (Rule 13)
- [ ] **Entity Enrichment:** Sử dụng các thực thể từ `Entities_Gap_Analysis` trong Outline? (Rule 14)
- [ ] **Bảo chứng SERP:** Outline có liệt kê các Entities/Ý tưởng từ Top 10 đối thủ? (YAML `SERP_Research: true`)?
- [ ] **Content Gap:** Có điểm khác biệt/nâng cấp rõ rệt so với đối thủ?

### Anti-AI & Syntax
- [ ] Không có forbidden phrases từ `anti-ai-rules.md`?
- [ ] **Certainty:** Không sử dụng các từ "nên", "có lẽ", "cần"? (Rule 2)
- [ ] **If-Logic:** Mệnh đề chính đứng trước mệnh đề "Nếu"? (Rule 10)
- [ ] Câu chủ động là chính (không quá 2 câu bị động/đoạn)?
- [ ] Không có >3 câu liên tiếp cùng cấu trúc S+V+O?
- [ ] Không có danh từ hóa kiểu Anh ("việc thực hiện" → "thực hiện")?
- [ ] Tuyệt đối không dùng ngoặc kép để nhấn mạnh từ ngữ/thuật ngữ?

### Specificity & Context
- [ ] **Plural Examples:** Có ví dụ cụ thể ngay sau các danh từ số nhiều? (Rule 7)
- [ ] **Niche Verbs:** Sử dụng đúng hệ động từ của ngành tài chính (giải ngân, tất toán...)? (Rule 6)
- [ ] **Numeric Values:** Sử dụng con số chính xác (%, phí, mã cổ phiếu) thay vì từ mơ hồ? (Rule 4)

### Brand & Persona
- [ ] Tone phù hợp Persona & HVS Products nhắc đúng loại theo YAML?
- [ ] Product mentions theo dạng benefit, không phải feature list?
- [ ] CTA phù hợp Persona & Xưng hô đúng chuẩn: "bạn", "HVS"?

### Terminology & Technical
- [ ] Thuật ngữ đúng theo `glossary.md` & Tên sản phẩm HVS đúng?
- [ ] YAML metadata đủ fields, HVS_Products là danh sách chuỗi phẳng & Anchor text khớp với Title bài đích? (Rule 11)
- [ ] Markdown format chuẩn & Không có typo?
