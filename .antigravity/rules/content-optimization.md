---
name: Content Optimization
description: Nâng cấp bài cũ/bài thô sang chuẩn HVS. Kích hoạt bằng lệnh `/optimize [path]` khi cần sửa văn phong Anti-AI, phân tích SERP đối thủ và tăng chỉ số Information Gain để giải quyết lỗi "crawled but not indexed".
---

# Workflow: Content Optimization (/optimize)

Quy trình này tập trung vào nâng cấp chất lượng bài viết cũ, bài viết thô (raw) nhằm tăng chất lượng nội dung, loại bỏ "AI-vibe", tạo tính độc bản (Information Gain) thông qua phân tích SERP đối thủ và tối ưu cấu trúc liên kết nội bộ để giải quyết triệt để tình trạng **"Crawled - currently not indexed"** (Đã thu thập dữ liệu - hiện chưa được chỉ mục) trên Google Search Console.

## Nguyên lý cốt lõi để bài viết được Index

Google không index trang web nếu nội dung đó là một bản dịch hoặc xào xáo lại (rewrite) thông tin chung chung đã có trên mạng mà không mang lại giá trị gia tăng nào cho người dùng. Để được index, bài viết phải đạt 3 tiêu chuẩn sau:

1. **SERP Gap & Information Gain (Phân tích đối thủ & Bứt phá thông tin):** Bắt buộc phải cào/tìm kiếm SERP cho `Target_Keyword` để phân tích Top 10 đối thủ đang đứng top. Xác định các lỗ hổng nội dung (Content Gaps) của đối thủ để bổ sung dữ liệu thực tế tại Việt Nam, case study thực tế (ví dụ: chu kỳ lãi suất năm 2022-2024, các đợt hút tín phiếu của SBV), hoặc ví dụ cụ thể kèm mã cổ phiếu cụ thể (HPG, VCB, VNM) mà các bài viết top 10 SERP hiện tại chưa đề cập hoặc chỉ đề cập hời hợt.
2. **Bi-directional Link Wheel (Liên kết 2 chiều):** Một trang web mồ côi (orphan page) hoặc có quá ít liên kết trỏ đến sẽ có nguy cơ cao bị "crawled but not indexed". Bài viết tối ưu bắt buộc phải có cả link đi (outbound) và đề xuất link trỏ về (inbound/backfill) từ các trang Pillar hoặc bài viết cùng cluster đã published.
3. **User Experience & Clean Formats:** Định dạng trực quan sinh động (xen kẽ Bullet List, Markdown Table sau mỗi 2 đoạn văn thường), trả lời trực tiếp ý định tìm kiếm ngay câu đầu tiên dưới H2 (Answer First), và tuyệt đối sạch bóng các dấu vết AI-slop.

---

## Các bước thực hiện chi tiết

### 1. Phân tích Hiện trạng & Nghiên cứu SERP (Phase 1 — Audit & SERP Research)
- **Hành động:** 
  - Đọc trường `Target_Keyword` trong YAML của bài viết hiện tại.
  - **Bảo toàn hình ảnh (Image Audit):** Lập danh sách toàn bộ ảnh (`![alt](url)` hoặc `[![alt](img_url)](target_url)`) từ bài gốc. Nghiêm cấm xóa ảnh khi viết lại; chuẩn bị vị trí tái phân bổ và tối ưu hóa Alt-text/Caption chuẩn SEO.
  - Sử dụng `search_web` hoặc gọi `SEO Collector` để tìm kiếm thông tin Top 10 đối thủ đang hiển thị trên SERP cho từ khóa đó.
  - Trích xuất: Cấu trúc heading, các ý chính đối thủ khai thác, và xác định lỗ hổng nội dung (Content Gaps).
  - Đối soát bài viết hiện tại với `.antigravity/rules/anti-ai-digest.md` để liệt kê các từ cấm ("hành trình", "mở khóa tiềm năng", ngoặc kép nhấn mạnh...).
- **Đầu ra:** Bản đánh giá hiện trạng gồm:
  - Danh sách ảnh gốc cần bảo toàn.
  - Phân tích SERP đối thủ và các lỗ hổng nội dung được tìm thấy.
  - Danh sách lỗi AI-vibe hiện có trong bài viết cần tối ưu.
  - Đánh giá độ nông sâu: Xác định các đoạn lý thuyết chung chung thiếu số liệu hoặc thiếu ví dụ thực tế.

### 2. Thiết lập Section Độc bản (Phase 2 — Information Gain Injecting)
- **Hành động:** 
  - Thiết kế **Section Độc quyền (Unique Value Block)**: Dựa trên lỗ hổng nội dung đối thủ, bổ sung 1 Case Study thực tế, kịch bản giao dịch (Nếu [Biến số A] -> [Kịch bản 1]...), hoặc 1 bảng phân tích dữ liệu thực tế tại thị trường Việt Nam mà đối thủ bỏ sót.

### 3. Thực thi Nâng cấp & Bố trí Hình ảnh (Phase 3 — Rewrite & Polish)
- **Hành động:** Main Agent thực hiện sửa đổi và viết lại bài viết:
  - **Giữ trọn vẹn và tối ưu hình ảnh gốc:** Tái phân bổ ảnh vào đúng section phù hợp, bổ sung Alt-text và Caption chất lượng cao (chứa thực thể/từ khóa ngữ cảnh, không AI-vibe).
  - Loại bỏ hoàn toàn các lỗi AI-vibe, câu bị động, danh từ hóa ("việc thực hiện", "sự phát triển").
  - Đan xen nhịp điệu câu linh hoạt (xen kẽ câu ngắn ≤7 từ).
  - Lồng ghép tinh tế giải pháp sản phẩm HVS theo đúng phân tầng: **HVS Tài chính số** (chương trình **HVS Thực tập số**) làm trọng tâm chính giải quyết nỗi đau của nhà đầu tư; **HVS Demo** và **HVS Forum** đóng vai trò bổ trợ đắc lực.
  - Đảm bảo YAML metadata chính xác, đúng định dạng và có đầy đủ các thông tin SEO (Title, Meta Description, Target Keyword).

### 4. Thiết lập Liên kết nội bộ chuẩn Sitemap (Phase 4 — Sitemap-verified Linking)
- **Hành động:**
  - **Nguồn chân lý URL:** Sử dụng `fetch_sitemap.py` (`python .antigravity/scripts/fetch_sitemap.py --suggest "[keyword]"`) tra cứu URL thực tế từ `https://taichinhso.hvsvn.com/sitemap.xml`.
  - **Outbound Links:** Đề xuất chèn 2-4 internal links từ bài đang tối ưu đến bài Pillar và các bài cluster khác đã published (sử dụng anchor text tự nhiên/partial match).
  - **Inbound Links (Backfill):** Quét các bài viết cùng cluster đã published trên sitemap để tìm đoạn phù hợp chèn link trỏ ngược lại bài viết vừa tối ưu này.
  - **Validation:** Bắt buộc chạy `python .antigravity/scripts/fetch_sitemap.py --validate [filepath]` để xác nhận 100% link chuẩn xác.

### 5. Kiểm định Chất lượng & Báo cáo (Phase 5 — QA & Audit Table)
- **Hành động:** 
  - Kích hoạt Quality Guardian để tự động chạy checklist QA/QC trên bài viết mới.
  - Yêu cầu bắt buộc tạo hoặc cập nhật phần `## Revision Log` ở cuối file để ghi nhận các chỉnh sửa.
  - Trình bày cho người dùng bản so sánh Đối chiếu trước/sau, kèm theo bảng kiểm định chất lượng:

| Tiêu chuẩn Index | Hiện trạng trước tối ưu | Cải tiến sau tối ưu | Kết quả QA |
| :--- | :--- | :--- | :--- |
| **SERP & Information Gain** | Lý thuyết chung, thiếu ví dụ cụ thể | Phân tích lỗ hổng SERP; Bổ sung Case Study thực tế [Tên case] | `PASSED` |
| **Image Retention & UX** | [Số lượng ảnh gốc] | Giữ nguyên 100% ảnh gốc, tối ưu Alt-text & Caption chuẩn SEO | `PASSED` |
| **Anti-AI Rules** | Có từ cấm "..."; lạm dụng ngoặc kép | Loại bỏ 100% từ cấm; sửa câu bị động | `PASSED` |
| **Internal Linking (Sitemap)** | Không có liên kết nội bộ / sai URL | Outbound: [X] link (100% Khớp Sitemap); Inbound (Backfill): [Y] bài | `PASSED` |
| **UX & Formatting** | Đoạn văn quá dài, thiếu bảng biểu | Chia nhỏ đoạn văn; thêm bảng so sánh | `PASSED` |

---
*Lệnh kích hoạt: `/optimize [đường dẫn tệp]`*
