---
name: Internal Quality Audit (QC Loop)
description: Soát lỗi tự động tại Phase 4. Kích hoạt bởi `/qa` hoặc tự động sau khi viết.
---
# Skill: Internal Quality Audit (QC Loop)

Kỹ năng này thực hiện việc kiểm tra chất lượng bản thảo cuối cùng dựa trên các tiêu chuẩn SEO và Brand của HVS.

---

## 🛠️ Công cụ sử dụng
- `view_file`: Đọc bản thảo và các file quy tắc.
- `multi_replace_file_content`: (Nếu cần) để Agent tự động sửa các lỗi nhỏ ngay trong quá trình Audit.

---

## 📝 Quy trình Kiểm soát (Checklist)

### 1. SEO Checklist
- [ ] Từ khóa chính xuất hiện trong H1 và ít nhất một thẻ H2.
- [ ] Meta Description chứa từ khóa chính và CTA.
- [ ] Cấu trúc heading (H2, H3) logic, không nhảy cấp.

### 2. Brand & Anti-AI Checklist
- [ ] Không chứa từ khóa cấm (Trong thế giới, Hành trình...).
- [ ] Dẫn dắt sản phẩm HVS đúng Persona.
- [ ] Sử dụng đúng thuật ngữ từ `glossary.md`.

---

## 🚀 Cách kích hoạt
Skill này được gọi bởi **Quality Guardian** sau khi Main Agent hoàn thành bài viết. Nếu không đạt 100% Pass, Agent phải lặp lại vòng sửa lỗi.
