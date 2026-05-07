---
name: Brand & Style Compliance
description: Trích xuất quy tắc HVS tại Phase 2. Kích hoạt bởi lệnh `/detailed` hoặc `/optimize`.
---
# Skill: Brand & Style Compliance

Kỹ năng này cho phép Agent đối chiếu nội dung với bộ quy tắc thương hiệu HVS, Persona người dùng và các bài học từ feedback cũ.

---

## 🛠️ Công cụ sử dụng
- `view_file`: Đọc các tệp quy tắc (`anti-ai-rules.md`, `glossary.md`).
- `grep_search`: Tìm kiếm các mẫu feedback cũ trong thư mục `2-user-review`.

---

## 📝 Quy trình trích xuất Context

1.  **Persona Filter:** Dựa trên Intent (ví dụ: Informational), Agent sẽ lọc ra các sản phẩm HVS phù hợp (F0 cần HVS Demo, Sinh viên cần HVS Thực tập số).
2.  **Anti-AI Filter:** Chỉ trích xuất các "từ cấm" liên quan đến chủ đề bài viết.
3.  **Terminology Sync:** Luôn lấy dữ liệu từ `glossary.md` để đảm bảo dùng đúng thuật ngữ (ví dụ: dùng "HVS Demo" thay vì "App chơi thử").

---

## 🚀 Cách kích hoạt
Skill này được gọi bởi **Brand & Style Guardian** ngay sau khi nhận được dữ liệu từ SEO Collector.
