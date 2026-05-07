---
name: Automated Dashboard Logging
description: Cập nhật tiến độ sau mỗi Phase. Kích hoạt tự động hoặc qua lệnh `/log`.
---
# Skill: Automated Dashboard Logging

Kỹ năng này giúp tự động cập nhật tiến độ công việc vào file `seo-strategy/content-plan/progress-log.md` hoặc các file theo dõi dự án.

---

## 🛠️ Công cụ sử dụng
- `view_file`: Đọc trạng thái hiện tại của log.
- `replace_file_content`: Cập nhật dòng trạng thái mới.

---

## 📝 Quy trình thực hiện

1.  **Identify Entry:** Tìm dòng tương ứng với bài viết đang xử lý trong `progress-log.md`.
2.  **Update Status:** Thay đổi tag trạng thái (ví dụ: `Draft` -> `QC Pending` -> `Finalized`).
3.  **Timestamping:** Ghi nhận thời gian thực hiện bước đó.

---

## 🚀 Cách kích hoạt
Được gọi tự động bởi Main Agent sau khi một Sub-agent hoàn thành nhiệm vụ hoặc sau khi User phê duyệt một giai đoạn.
