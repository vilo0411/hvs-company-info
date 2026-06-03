# Strategic Decisions & Lessons Learned (DECISIONS.md)

Tệp này lưu trữ các quyết định quan trọng đã được thống nhất giữa User và Agent để đảm bảo tính nhất quán lâu dài.

---

## 🏛️ Quyết định Kiến trúc
- **[2026-05-07]:** Chuyển từ Single-Agent sang **Multi-Agent (Sub-agent) Framework**.
- **[2026-05-07]:** Áp dụng cấu trúc thư mục GSD (Agents, Docs, Scripts).
- **[2026-05-07]:** Quy trình phê duyệt 2 lớp (Outline & Draft) là bắt buộc.

## ✍️ Quyết định Nội dung
- **[2026-05-07]:** Tất cả bài viết F0 bắt buộc phải dẫn dắt đến sản phẩm **HVS Demo** và **HVS Forum**.
- **[2026-05-07]:** Naming convention bắt buộc dùng tiền tố `Outline-`, `Draft-`, `Final-`.
- **[2026-05-07]:** Hoàn tất thiết lập bộ nhận diện thương hiệu tại `resources/company/` (Identity, USPs) để làm giàu Context cho Brand Guardian.
- **[2026-05-07]:** Content Brief phải tuân thủ mẫu chuẩn của `content-brief-example.md` (H1, Sapo, Heading Details, Conclusion).
- **[2026-05-25]:** Đối với các đoạn phân tích kỹ thuật hoặc liệt kê nguyên nhân/rủi ro dài, ưu tiên chuyển đổi thành định dạng danh mục (bullet points/numbered lists) kèm bôi đậm từ khóa tiêu điểm để tối ưu độ scannability cho người đọc.

## 💡 Bài học kinh nghiệm (Retrospective)
- Tránh sử dụng lệnh `dir /s /b` trong terminal trên Windows, thay bằng đường dẫn tuyệt đối.
- Luôn gắn link nội bộ theo ngữ nghĩa thay vì gắn link đại trà vào các từ khóa chung như "F0".
