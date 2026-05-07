# 🚀 HVS SEO Content Agent System

Hệ thống Agent AI được thiết lập riêng cho **HVS Securities**, tối ưu hóa quy trình sản xuất nội dung SEO chất lượng cao, thực chiến và loại bỏ hoàn toàn "AI-vibe".

---

## 🏗️ Tổng quan Hệ thống (System Architecture)

Hệ thống hoạt động dựa trên sự kết hợp giữa **Workflows** (Quy trình cứng) và **Skills** (Trí tuệ linh hoạt), đảm bảo mọi bài viết đều đi qua bộ lọc chất lượng nghiêm ngặt trước khi đến tay người dùng.

### 1. Luồng xử lý Nội dung (Workflows)
Hệ thống hỗ trợ 4 chế độ vận hành chính thông qua các Slash Commands:

| Command | Workflow | Mục tiêu |
| :--- | :--- | :--- |
| `/fast` | **Fast Track** | Lên bản thảo nhanh cho các chủ đề đơn giản, tin tức. |
| `/detailed` | **Detailed Track** | Quy trình 3 bước (Chiến lược -> Dàn ý -> Bản thảo) cho bài Pillar. |
| `/optimize` | **Content Optimization** | Làm mới, tối ưu SEO và cập nhật brand cho bài viết cũ/thô. |
| `/raw` | **Raw Processing** | Chuyển đổi dữ liệu thô (HTML, Text hỗn tạp) sang Markdown chuẩn. |

### 2. Bộ kỹ năng Đặc thù (Specialized Skills)
*   **Keyword Management:** Tự động theo dõi và quản lý từ khóa từ file CSV, tránh trùng lặp nội dung.
*   **QA-QC Loop:** Bộ kiểm tra tự động đối chiếu bài viết với `anti-ai-rules.md` và tiêu chuẩn thương hiệu HVS.
*   **Dashboard Logging:** Hệ thống tự động cập nhật tiến độ tại `progress-log.md` sau mỗi hành động, giúp quản lý kho nội dung theo thời gian thực.
*   **Semantic Internal Linking:** Tự động quét kho dữ liệu `3-finalized/` để gợi ý liên kết nội bộ tự nhiên, tối ưu cấu trúc Link Wheel cho SEO.
*   **Content Feedback Loop:** Tự động phân tích nhật ký sửa đổi (Revision Logs) để "học" gu thẩm mỹ và lỗi sai từ người dùng.

---

## 🧠 Nguyên tắc "Con người hóa" (Anti-AI Philosophy)

Điểm khác biệt cốt lõi của Agent này là bộ lọc **Anti-AI Rules**, đảm bảo văn phong chuyên nghiệp, thực chiến:
- **Cấm sáo rỗng:** Loại bỏ các cụm từ "Trong thế giới...", "Hành trình...", "Mở khóa tiềm năng...".
- **Thực chiến (Actionable):** Luôn lấy ví dụ từ thị trường Việt Nam (HOSE, HNX, mã chứng khoán cụ thể).
- **Hệ sinh thái Persona:** Dẫn dắt sản phẩm HVS (Thực tập số, Đào tạo) dựa trên nhu cầu thực tế của từng đối tượng (F0, Sinh viên, Pro).

---

## 📂 Vòng đời Bài viết (Content Lifecycle)

Mọi tệp tin di chuyển qua các giai đoạn nghiêm ngặt:
1.  `0-raw/`: Tiếp nhận nguyên liệu thô.
2.  `1-outlines/`: Lên khung chiến lược (User cần duyệt tại đây).
3.  `2-user-review/`: Bản thảo hoàn chỉnh đã qua QA nội bộ (Kèm **Revision Log** ở cuối file).
4.  `3-finalized/`: Nội dung đã sẵn sàng đăng tải.

---

## 🔍 Điểm có thể Tối ưu (Potential Optimizations)

Dựa trên cấu trúc hiện tại, đây là các hướng có thể nâng cấp hệ thống:

### ⚡ Tối ưu Quy trình (Efficiency)
1.  **WordPress/Ghost Integration:** Kết nối Agent trực tiếp với CMS để đẩy bài viết từ `3-finalized/` lên bản nháp trên website chỉ bằng một lệnh `/publish`.
2.  **Image Generation Workflow:** Tự động hóa việc tạo Prompts cho Designer hoặc dùng AI tạo ảnh minh họa chuẩn brand ngay trong bản Draft.

### 🧠 Tối ưu Trí tuệ (Intelligence)
3.  **Real-time Market Data Integration:** Tích hợp công cụ lấy dữ liệu thị trường thời gian thực (Giá cổ phiếu, tin vĩ mô mới nhất) để các ví dụ trong bài viết luôn mang tính thời sự cao nhất.
4.  **Automatic SEO Audit (Simulation):** Tích hợp kỹ năng giả lập Google Bot để chấm điểm SEO (Headline, Meta, Keyword Density) ngay trong bước QA-QC.
5.  **Multi-Agent Coordination:** Nâng cấp hệ thống Sub-Agents (SEO Collector, Quality Guardian) để hoạt động độc lập và báo cáo định kỳ.

---

> [!TIP]
> Hệ thống Agent này không chỉ viết bài, nó **học** cách viết của bạn thông qua `Revision Log`. Hãy tích cực để lại nhận xét ở cuối file để Agent ngày càng thông minh hơn.

---
**Author:** Antigravity AI Agent  
**Project:** HVS Securities Content SEO Framework
