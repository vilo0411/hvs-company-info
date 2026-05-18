---
description: "Tối ưu bài viết cũ (anti-AI + SEO + linking). Args: [đường dẫn file]"
---

Tối ưu bài viết.

**Cách dùng:**
```
/optimize content/blog/3-finalized/Final-chung-khoan-la-gi.md
/optimize content/blog/2-user-review/Draft-co-phieu-penny-la-gi.md
```

Nếu không có args → hỏi user đường dẫn file cần tối ưu.

Đọc `.antigravity/rules/content-optimization.md` để nắm toàn bộ quy trình.

1. **Phân tích hiện trạng:** Đọc nội dung file + `.antigravity/rules/anti-ai-digest.md` + `glossary.md` + `tone-and-voice.md` + `financial-logic.md`.
2. **Khởi tạo Revision Log:** Nếu file chưa có section `## Revision Log`, Agent phải tự động tạo ở cuối file để ghi nhận các yêu cầu tối ưu.
3. **Brand Guardian Mode B (Sub-Agent) Audit:**
   - Scan bài hiện tại theo `.antigravity/rules/anti-ai-digest.md`.
   - Liệt kê vi phạm cụ thể (dấu ngoặc kép nhấn mạnh, FORBIDDEN_STRINGS...).
   - Đề xuất Persona/tone và cấu trúc HVS Bridge (Vấn đề → Giải pháp).
4. **Rewrite & Strict Audit (BẮT BUỘC):** 
   - Agent thực hiện sửa bài.
   - Hiển thị **Bảng Kiểm định Anti-AI (Audit Table)** theo `content-feedback-loop/SKILL.md` trong phản hồi.
5. **User Review:** Trình bày bản tối ưu + Bảng Kiểm định cho người dùng.
6. **Lưu & Hoàn tất:** Sau khi `/approve Final`, di chuyển vào `3-finalized/` và cập nhật tri thức vào Knowledge Base.
