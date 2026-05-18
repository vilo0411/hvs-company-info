---
name: content-feedback-loop
description: Tự động phân tích phản hồi của người dùng và nhật ký chỉnh sửa để cập nhật quy tắc Anti-AI và cải thiện chất lượng nội dung theo thời gian.
---

# Skill: Content Feedback Learning Loop (Vòng lặp Phản hồi Nội dung)

## Tổng quan
Skill này đóng vai trò là "trí nhớ dài hạn" và "kiểm toán viên chất lượng" cho Agent. Nó được kích hoạt sau khi một bài viết được hoàn tất để đảm bảo các ưu tiên của người dùng được ghi nhận, đồng thời cung cấp khung cấu trúc để kiểm định nội dung dựa trên bộ quy tắc Anti-AI.

## Quy trình thực hiện (Workflow)

### Giai đoạn 0: Hiệu chỉnh Dàn ý & Khởi tạo Nhật ký (Outline Iteration)
**Kích hoạt khi:** Người dùng đưa ra phản hồi trực tiếp sau khi xem Outline hoặc Draft qua bất kỳ kênh nào (Chat hoặc Comment trong file).

**Trách nhiệm của Agent:**
1.  **Chủ động khởi tạo:** Nếu file chưa có section `## Revision Log`, Agent phải tự động tạo ở cuối file ngay khi nhận được phản hồi đầu tiên.
2.  **Hợp nhất phản hồi:**
    *   Nếu phản hồi qua **Chat**: Tóm tắt các ý chính và ghi vào Log.
    *   Nếu phản hồi qua **Comment/Nhận xét** trong file: Di chuyển (migrate) nội dung đó vào Log để đảm bảo tính chuẩn hóa.
3.  **Phân tích yêu cầu:** Xác định chính xác Heading nào, Entity nào hoặc logic nào cần thay đổi.
4.  **Tái cấu trúc (Regeneration):** Cập nhật lại các yêu cầu chi tiết (Key points, Entities, Word count) cho các Heading bị ảnh hưởng. Đảm bảo tính nhất quán với Knowledge Base.

### Giai đoạn 1: Kiểm định cấu trúc & Anti-AI (Kích hoạt trong mọi lệnh /write hoặc /optimize)
Khi chỉnh sửa hoặc kiểm định nội dung, Agent BẮT BUỘC phải thực hiện và hiển thị **Bảng Kiểm định Anti-AI (Audit Table)** trong phản hồi cho người dùng theo cấu trúc sau:

| Bước Kiểm soát | Nội dung thực hiện | Kết quả (PASS/FAIL) |
| :--- | :--- | :--- |
| **1. Issues Found** | Liệt kê các lỗi AI-vibe, ngoặc kép nhấn mạnh (Quy tắc 3.79), từ cấm. | |
| **2. Second-Pass Audit** | Đọc lại bản viết để tìm các cụm từ sáo rỗng hoặc câu bị động còn sót. | |
| **3. Persona Check** | Xác nhận nội dung đã đúng giọng Senior Mentor và sát nỗi đau của Persona. | |
| **4. HVS Bridge Check** | Xác nhận cấu trúc Vấn đề - Giải pháp khi lồng ghép sản phẩm HVS. | |

**Tuyệt đối không được bỏ qua bảng này. Nếu kết quả có mục FAIL, Agent phải tự sửa lại trước khi trình bày.**

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
5.  **Cập nhật (2 files — theo thứ tự):**
    - **Bước 1** — Cập nhật `seo-strategy/resources/content-strategy/anti-ai-rules.md`:
      - Thêm rule mới vào Section 0 — QUICK SCAN (FORBIDDEN_STRINGS hoặc FORBIDDEN_PATTERNS hoặc REQUIRED).
      - Thêm Full Rationale vào phần tương ứng (Mục 1, 2 hoặc 3).
      - Thêm dòng vào Mục 4 — Feedback Learning Log với ngày và context bài viết.
    - **Bước 2** — Cập nhật `.antigravity/rules/anti-ai-digest.md` để phản ánh rule mới (đây là file compact mà skills/QA đọc khi audit).

## Tiêu chuẩn Hiệu suất & Chất lượng
- **Zero-Tolerance (Không khoan nhượng):** Tuyệt đối không có dấu vết của Chatbot ("Tôi hy vọng thông tin này hữu ích", "Chắc chắn rồi").
*   **Đúng Persona:** Nội dung phải đánh thẳng vào nỗi đau và nhu cầu của Persona mục tiêu.
*   **Dựa trên dữ liệu (Data-Driven):** Mọi khẳng định phải có dữ liệu hoặc ví dụ cụ thể đi kèm, không viết dựa trên cảm giác hoặc tính từ sáo rỗng.
*   **Kiểm tra nhịp điệu (Rhythm Check):** Đảm bảo độ dài các câu đa dạng. Nếu có 3 câu liên tiếp có độ dài tương đương, Agent phải viết lại.
