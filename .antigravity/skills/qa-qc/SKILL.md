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

### SEO Structure
- [ ] H1 chứa keyword chính xác?
- [ ] H1 ≤65 ký tự?
- [ ] Sapo: keyword xuất hiện trong 100 từ đầu?
- [ ] Sapo ≤150 từ?
- [ ] H2 đầu tiên (Informational): có Definition Block ≤50 từ?
- [ ] Meta description có keyword + CTA, 120–155 ký tự?
- [ ] Heading hierarchy logic (H1→H2→H3, không nhảy cấp)?

### Anti-AI
- [ ] Không có forbidden phrases từ `seo-strategy/resources/content-strategy/anti-ai-rules.md`?
- [ ] Không có phrases trong `Anti_AI_Flags` YAML của Outline?
- [ ] Câu chủ động là chính (passive voice không quá 2 câu/đoạn)?
- [ ] Không có >3 câu liên tiếp cùng cấu trúc S+V+O?
- [ ] Không có danh từ hóa kiểu Anh ("việc thực hiện" → "thực hiện")?

### Specificity
- [ ] Mỗi H2 có ít nhất 1 ví dụ cụ thể (mã cổ phiếu / con số / tên sàn)?
- [ ] Claim không chung chung: không "một doanh nghiệp lớn", phải "VCB", "HPG", v.v.?

### Brand & Persona
- [ ] Tone phù hợp Persona trong YAML?
- [ ] HVS Products đã nhắc đúng loại theo `HVS_Products` YAML?
- [ ] Product mentions theo dạng benefit, không phải feature list?
- [ ] CTA cuối bài phù hợp Persona?
- [ ] Xưng hô đúng chuẩn: "bạn", "HVS" / "chúng tôi"?

### Terminology
- [ ] Thuật ngữ đúng chuẩn theo `seo-strategy/resources/content-strategy/glossary.md`?
- [ ] Tên sản phẩm HVS đúng (HVS Demo, không phải "tài khoản ảo")?

### Technical
- [ ] YAML metadata đủ fields bắt buộc?
- [ ] Markdown format chuẩn (heading, bullet indent)?
- [ ] Không có typo rõ ràng?
