---
description: "Tối ưu bài viết cũ (Phân tích SERP + Chống lỗi Crawled but not Indexed + Sạch bóng Anti-AI + Gắn link 2 chiều). Args: [đường dẫn file]"
---

# Workflow: Content Optimization (/optimize)

Workflow này giúp tối ưu hóa bài viết cũ hoặc bài nháp thô lên tiêu chuẩn E-E-A-T và UX cao nhất của HVS thông qua việc **nghiên cứu đối thủ trên SERP**, nhằm mục đích giải quyết triệt để lỗi **"Crawled - currently not indexed"** (Đã thu thập dữ liệu - hiện chưa được chỉ mục) trên Google Search Console.

**Cách sử dụng:**
```bash
/optimize content/blog/3-finalized/Final-tin-phieu-la-gi.md
/optimize content/blog/2-user-review/Draft-roce-la-gi.md
```
*Nếu chạy lệnh không có tham số đường dẫn tệp → Agent sẽ yêu cầu người dùng cung cấp.*

---

## Các bước thực hiện chi tiết cho Agent

### 1. Phân tích hiện trạng & Nghiên cứu SERP (Phase 1)
- Đọc nội dung file mục tiêu, xác định từ khóa chính ở trường `Target_Keyword` trong YAML header.
- **BẢO TOÀN HÌNH ẢNH (Image Audit):** Kiểm tra và lập danh sách toàn bộ các hình ảnh (`![alt](url)` hoặc `[![alt](img_url)](url)`) hiện có trong bài viết gốc/file thô.
  - ⚠️ **CẤM XÓA ẢNH:** Agent tuyệt đối KHÔNG ĐƯỢC xóa bỏ ảnh từ bài gốc trong quá trình viết lại. Phải giữ nguyên ảnh và phân bổ lại vào đúng section phù hợp sau khi tái cấu trúc.
- **BẮT BUỘC Phân tích SERP:** Sử dụng `search_web` hoặc gọi `SEO Collector` để tìm kiếm thông tin Top 10 đối thủ đang hiển thị trên SERP cho từ khóa đó.
- Phân tích: Trích xuất các ý chính, cấu trúc heading, và những lỗ hổng nội dung (Content Gaps) của đối thủ.
- Đọc các tài liệu quy chuẩn nội bộ: `.antigravity/rules/anti-ai-digest.md`, `writing-guidelines.md`, `glossary.md` và `financial-logic.md`.
- Đối soát bài viết hiện tại để tìm lỗi AI-vibe và xác định nguyên nhân bài viết chưa được index (thiếu chiều sâu vĩ mô/thực tế, thiếu liên kết nội bộ, hoặc trùng lặp ý tưởng đối thủ).

### 2. Thu hoạch và Bổ sung "Information Gain" (Phase 2)
- Dựa trên lỗ hổng nội dung của đối thủ đã tìm ra ở Phase 1, thiết kế **Section Độc quyền (Unique Value Block)**:
  - Bổ sung ít nhất 1 Case Study thực tế tại thị trường Việt Nam (sử dụng mã cổ phiếu thực: VCB, HPG, VNM, SSI... hoặc sự kiện vĩ mô có thật như chu kỳ lãi suất, hút tiền qua tín phiếu năm 2024).
  - Bổ sung ít nhất 1 kịch bản giao dịch/nhận định thực chiến (Nếu [Biến số A] -> [Kịch bản 1]. Nếu [Biến số B] -> [Kịch bản 2]).
  - Bổ sung ít nhất 1 bảng so sánh hoặc đối chiếu số liệu thực tế (Markdown Table) để tăng trải nghiệm trực quan.

### 3. Thiết lập Liên kết nội bộ chuẩn Sitemap (Phase 3)
- Sử dụng `.antigravity/skills/internal-linking/SKILL.md` và `fetch_sitemap.py`:
  - **Single Source of Truth:** Quét trực tiếp `https://taichinhso.hvsvn.com/sitemap.xml` hoặc chạy:
    ```powershell
    python .antigravity/scripts/fetch_sitemap.py --suggest "[từ khóa/chủ đề]"
    ```
  - **CẤM TỰ BỊA URL:** Tuyệt đối không tự suy diễn đường dẫn category (như `/kinh-te-vi-mo/` hay `/dau-tu/`), không dùng link tương đối hoặc `file:///`.
  - **CHỈ LINK BÀI ĐÃ PUBLISHED:** Chỉ chèn markdown link đến các URL thật sự tồn tại trong `sitemap.xml`. Bài chưa có trong sitemap thì viết text thông thường và ghi chú lại cho backfill.
  - **Outbound Link:** Đề xuất 2-4 link từ bài viết này trỏ tới các bài Pillar và bài viết cùng cluster đã published bằng anchor text tự nhiên (partial match).
  - **Inbound Link (Backfill):** Quét các bài viết khác trong cùng cluster có trong sitemap, đề xuất cụ thể ít nhất 2 bài viết cũ để chèn link trỏ ngược về bài này.
  - **Validation:** BẮT BUỘC chạy script kiểm tra link trước khi hoàn tất:
    ```powershell
    python .antigravity/scripts/fetch_sitemap.py --validate [đường_dẫn_file]
    ```

### 4. Tinh chỉnh văn phong, Bố trí ảnh & QA/QC (Phase 4)
- **Bố trí & Tối ưu Ảnh:**
  - Chèn lại đầy đủ các ảnh gốc vào vị trí ngữ cảnh tương ứng.
  - Tối ưu Alt-text và Caption mô tả ảnh chuẩn xác, tự nhiên, chứa thực thể liên quan (không dùng alt-text rỗng hoặc chung chung).
  - Nếu bài gốc hoàn toàn không có ảnh, áp dụng skill `image-generation` để bổ sung ảnh tối thiểu (bìa/quy trình/so sánh).
- **Anti-AI Polish:** Viết lại các câu từ bị gắn mác "AI-vibe", chuyển câu bị động thành chủ động, loại bỏ hoàn toàn các từ cấm Tier 1 và Tier 2 trong `anti-ai-digest.md`.
- **Formatting Diversity:** Chia nhỏ các đoạn văn dài (đảm bảo mỗi đoạn ≤ 4 câu và ≤ 80 từ), không để quá 2 đoạn văn thường đứng cạnh nhau mà không có list/table ngắt dòng.
- **Product Hierarchy:** Lồng ghép sản phẩm HVS theo đúng phân tầng (HVS Tài chính số / HVS Thực tập số làm trọng tâm, HVS Demo và HVS Forum bổ trợ).
- Chạy thử nghiệm đếm số từ từng section và toàn bài bằng Word Count Script (nếu có thể) để đảm bảo đạt Target Word Count.

### 5. Cập nhật YAML Metadata & Revision Log (Phase 5)
- Đảm bảo YAML Header ở đầu file chứa đầy đủ thông tin:
  ```yaml
  ---
  Author: Claude Code
  Status: Draft | Finalized
  Mode: Optimized
  Persona: [Tên Persona]
  Target_Keyword: [Từ khóa chính]
  Search_Intent: [Informational | Commercial | Transactional]
  Word_Count_Target: [Số từ mục tiêu]
  Meta_Description: [Mô tả SEO ≤ 160 ký tự, ngắn gọn, chứa keyword]
  ---
  ```
- Tạo hoặc cập nhật phần `## Revision Log` ở cuối file theo cấu trúc:
  ```markdown
  ## Revision Log
  - **[Ngày/Tháng/Năm] (v1.x - Optimized):**
    - Nghiên cứu SERP và khắc phục lỗi crawled but not indexed: Bổ sung Case Study thực tế về [Tên Case Study] và kịch bản [Tên kịch bản] dựa trên lỗ hổng nội dung đối thủ.
    - Bảo toàn và tối ưu hình ảnh: Giữ trọn vẹn [N] ảnh gốc, nâng cấp alt-text chuẩn SEO.
    - Tối ưu liên kết nội bộ: Cấu hình outbound link chuẩn sitemap tới [Mục tiêu 1], đề xuất backfill từ [Bài viết 2].
    - Loại bỏ AI-vibe: Xóa các từ cấm "hành trình", "mở khóa", sửa câu bị động.
  ```

### 6. Trình bày kết quả cho User
- Trình bày bài viết đã tối ưu dưới dạng Markdown hoàn chỉnh (hoặc file diff nếu chỉnh sửa nhỏ).
- Hiển thị **Bảng Kiểm định Chất lượng Index (Indexation Audit Table)**:

| Tiêu chuẩn Index | Hiện trạng trước tối ưu | Cải tiến sau tối ưu | Trạng thái |
| :--- | :--- | :--- | :--- |
| **SERP & Information Gain** | [Nêu điểm yếu/Lỗ hổng so với đối thủ] | [Mô tả chi tiết Case Study/Dữ liệu mới thêm vào dựa trên lỗ hổng SERP] | `PASSED` |
| **Image Retention & UX** | [Số lượng ảnh gốc] | Bảo toàn 100% ảnh gốc, tối ưu Alt-text & Caption chuẩn SEO | `PASSED` |
| **Internal Linking (Sitemap)** | [Nêu thực trạng link cũ] | Outbound: [X] link (100% khớp Sitemap); Inbound (Backfill): [Y] link | `PASSED` |
| **Anti-AI Scan** | [Ví dụ lỗi AI cũ] | Sạch 100% từ cấm, cấu trúc câu tự nhiên | `PASSED` |
| **UX & Formatting** | [Ví dụ đoạn văn dài/thiếu bảng] | Đoạn ngắn ≤4 câu, thêm bảng so sánh dữ liệu | `PASSED` |

- Chờ người dùng duyệt `/approve` để tiến hành lưu hoặc cập nhật file.
