---
name: Internal Linking Suggestion (Optimized)
description: Gắn link SEO tại Phase 5. Kích hoạt bởi lệnh `/link` hoặc tự động trước khi Finalize.
---
# Skill: Internal Linking Suggestion (Optimized)

Kỹ năng này giúp xây dựng mạng lưới liên kết nội bộ (Internal Links) một cách tự nhiên và chính xác về mặt ngữ nghĩa.

---

## 🛠️ Công cụ sử dụng
- `list_dir`: Quét thư mục `content/blog/3-finalized/`.
- `grep_search`: Tìm kiếm từ khóa chính xác trong các bài cũ.

---

## 📝 Quy trình thực hiện (Chuẩn SEO HVS)

### 1. Phân tích Ngữ nghĩa (Semantic Check)
- Chỉ đặt link khi từ khóa (Anchor Text) mang tính đặc thù của bài đích.
- **Ví dụ:** 
  - ✅ Link keyword "DCA" tới bài "Chiến lược trung bình giá (DCA)".
  - ❌ KHÔNG link "F0" tới bài "Chứng khoán là gì" (trừ khi không còn bài nào khác phù hợp hơn).

### 2. Chống trùng lặp (No Duplicates)
- Trong một bài viết, mỗi URL đích chỉ được xuất hiện **DUY NHẤT 1 LẦN**. 
- Nếu đã có link ngữ nghĩa trong đoạn văn, không thêm "Xem thêm" cho cùng URL đó.

### 3. Cấu trúc hiển thị
Hệ thống ưu tiên 2 dạng:
1.  **Link ngữ nghĩa:** `[Anchor Text](URL)` lồng trực tiếp vào câu văn.
2.  **Link Wheel (Xem thêm):** `>> Xem thêm: [Tên bài viết/Từ khóa](URL)` đặt ở cuối đoạn văn hoặc cuối mục H2.

### 4. Hiển thị Preview cho User
Trước khi thực hiện, Agent phải báo cáo danh sách link dự kiến:
- `[Từ khóa] -> [Tên file đích]`

---

## 🛡️ Ràng buộc kỹ thuật
- Luôn sử dụng đường dẫn tương đối hoặc link file nội bộ: `file:///e:/project/hvs-company-info/content/blog/3-finalized/[slug].md`.
- Tuyệt đối không tự ý tạo link đến các trang web bên ngoài (External Link) trừ khi có yêu cầu đặc biệt.
