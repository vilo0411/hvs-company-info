---
name: workflow-router
description: Tự động kích hoạt workflow từ ngôn ngữ tự nhiên. Dùng skill này khi người dùng yêu cầu tối ưu (optimize), viết bài (write), duyệt (approve), gắn link (link), gom nhóm (cluster) hoặc lên kế hoạch (plan) mà không dùng slash command.
---

# Skill: Workflow Router

Skill này chịu trách nhiệm thu hẹp khoảng cách giữa yêu cầu bằng ngôn ngữ tự nhiên và các workflow kỹ thuật được định nghĩa trong `.agents/workflows/`.

## Hướng dẫn thực thi

1. **Phân tích Intent**: Xác định yêu cầu của người dùng khớp với workflow nào nhất.
   - "tối ưu", "nâng cấp", "sửa bài" → `.agents/workflows/optimize.md`
   - "viết bài", "tạo bài", "lên bài" → `.agents/workflows/write.md`
   - "duyệt", "approve", "xong rồi" → `.agents/workflows/approve.md`
   - "gắn link", "internal link" → `.agents/workflows/link.md`
   - "gom nhóm", "cluster" → `.agents/workflows/cluster.md`
   - "lên kế hoạch", "sprint plan" → `.agents/workflows/keyword-plan.md`
   - "xử lý raw", "chuyển markdown" → `.agents/workflows/raw.md`
   - "setup", "cài đặt" → `.agents/workflows/setup.md`

2. **Xác nhận**: Thông báo cho người dùng biết workflow nào sẽ được kích hoạt.
   - Ví dụ: "Tôi hiểu bạn muốn tối ưu bài viết này. Tôi sẽ kích hoạt workflow `/optimize` để thực hiện."

3. **Thực hiện**: 
   - Đọc nội dung file workflow tương ứng.
   - Thực hiện từng bước (Step) được mô tả trong workflow đó.
   - Nếu workflow yêu cầu tham số (như [slug] hoặc [path]), hãy tự động trích xuất từ context hoặc hỏi người dùng nếu không rõ.

## Quy tắc ưu tiên
- Nếu người dùng dùng slash command trực tiếp, hãy thực hiện workflow đó ngay lập tức.
- Skill này chỉ dùng để "bắt" các câu lệnh tự nhiên để đảm bảo hệ thống luôn chạy đúng quy trình (Pipeline).
