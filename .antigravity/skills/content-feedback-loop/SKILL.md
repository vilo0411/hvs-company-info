---
name: content-feedback-loop
description: Tự động phân tích phản hồi của người dùng và nhật ký chỉnh sửa để cập nhật quy tắc Anti-AI và cải thiện chất lượng nội dung theo thời gian.
---

# Skill: Content Feedback Learning Loop (Vòng lặp Phản hồi Nội dung)

## Tổng quan
Skill này đóng vai trò là "trí nhớ dài hạn" và "kiểm toán viên chất lượng" cho Agent. Nó được kích hoạt sau khi một bài viết được hoàn tất để đảm bảo các ưu tiên của người dùng được ghi nhận, đồng thời cung cấp khung cấu trúc để kiểm định nội dung dựa trên bộ quy tắc Anti-AI.

## Quy trình thực hiện (Workflow)

### Giai đoạn 0: Hiệu chỉnh Dàn ý (Outline Iteration)
**Kích hoạt khi:** Người dùng đưa ra phản hồi trực tiếp sau khi xem Outline (Cách 1).

1.  **Phân tích yêu cầu:** Xác định chính xác Heading nào, Entity nào hoặc logic nào cần thay đổi.
2.  **Cập nhật Nhật ký (Revision Log):** Ghi nhận yêu cầu của người dùng vào phần cuối của file Outline để theo dõi lịch sử thay đổi.
3.  **Tái cấu trúc (Regeneration):** Cập nhật lại các yêu cầu chi tiết (Key points, Entities, Word count) cho các Heading bị ảnh hưởng. Đảm bảo tính nhất quán với Knowledge Base.

### Giai đoạn 1: Kiểm định cấu trúc & Anti-AI (Kích hoạt trong khi dùng /write hoặc /optimize)
Khi chỉnh sửa hoặc kiểm định nội dung, Agent BẮT BUỘC phải tuân theo cấu trúc 4 bước sau:

1.  **Issues Found (Lỗi phát hiện):** Liệt kê mọi "AI-ism" (dấu vết AI) được xác định (từ `anti-ai-rules.md`), trích dẫn văn bản cụ thể và gọi tên nhóm pattern.
2.  **Rewritten Version (Bản viết lại):** Cung cấp phiên bản sạch đã loại bỏ toàn bộ dấu vết AI và có nhịp điệu câu đa dạng.
3.  **What Changed (Thay đổi chính):** Tóm tắt các chỉnh sửa quan trọng và lý do (ví dụ: "Loại bỏ thổi phồng tầm quan trọng", "Đa dạng hóa độ dài câu").
4.  **Second-Pass Audit (Kiểm định lần 2):** Đọc lại bản viết lại để phát hiện bất kỳ dấu vết nào còn sót (các cụm chuyển đoạn lặp lại, sự thổi phồng còn sót lại, v.v.).

### Giai đoạn 2: Vòng lặp học hỏi (Kích hoạt sau khi dùng /approve)
1.  **Trigger:** Tự động kích hoạt sau khi lệnh `/approve` đưa file vào thư mục `3-finalized/`.
2.  **Phân tích:**
    - Đọc TOÀN BỘ **Revision Log (Nhật ký chỉnh sửa)** tích lũy ở cuối file đã hoàn tất.
    - Xác định các mẫu (patterns) trong các lần sửa đổi của người dùng:
        - Các từ cụ thể mà người dùng không thích.
        - Điều chỉnh tông giọng (ví dụ: "quá trang trọng", "quá máy móc").
        - Các ưu tiên về cấu trúc bài viết.
3.  **Hợp nhất:**
    - So sánh kết quả với `seo-strategy/resources/content-strategy/anti-ai-rules.md`.
    - Đề xuất quy tắc mới hoặc chuyển đổi vị trí từ vựng giữa các Tiers.
4.  **Xác nhận với người dùng:**
    - Trình bày các mẫu đã học được để người dùng phê duyệt.
5.  **Cập nhật:**
    - Cập nhật file `anti-ai-rules.md` và thêm một mục vào phần **Feedback Learning Log** của file đó.

## Tiêu chuẩn Hiệu suất & Chất lượng
- **Zero-Tolerance (Không khoan nhượng):** Tuyệt đối không có dấu vết của Chatbot ("Tôi hy vọng thông tin này hữu ích", "Chắc chắn rồi").
*   **Đúng Persona:** Nội dung phải đánh thẳng vào nỗi đau và nhu cầu của Persona mục tiêu.
*   **Dựa trên dữ liệu (Data-Driven):** Mọi khẳng định phải có dữ liệu hoặc ví dụ cụ thể đi kèm, không viết dựa trên cảm giác hoặc tính từ sáo rỗng.
*   **Kiểm tra nhịp điệu (Rhythm Check):** Đảm bảo độ dài các câu đa dạng. Nếu có 3 câu liên tiếp có độ dài tương đương, Agent phải viết lại.
