# Continuous Learning: Instincts (Bản năng rút gọn)

> **Bắt buộc:** Mọi agent/skill đọc file này trước khi viết. Bản đầy đủ (nguồn, feedback gốc) ở `.antigravity/memory/instincts-archive.md`.
> **Sinh tự động** bởi `scripts/optimize_instincts.py` — không sửa tay. Sau `/learn`, ghi vào archive rồi chạy lại script.

> **Bản năng theo topic:** `instincts-by-scope/he-thong.md` — chỉ load khi bài thuộc topic đó.

## Văn phong & Ngôn từ (Style & Tone)

### quy tắc hạn chế ngoặc kép và cá nhân hóa sản phẩm theo Persona.
- Thêm quy tắc hạn chế ngoặc kép và cá nhân hóa sản phẩm theo Persona.

### dùng câu chủ động cho định nghĩa, yêu cầu tính mạch lạc giữa các Heading và cấu trúc Vấn đ
- Ép dùng câu chủ động cho định nghĩa, yêu cầu tính mạch lạc giữa các Heading và cấu trúc Vấn đề - Giải pháp khi lồng ghép sản phẩm HVS.

### từ "Đọc vị" (AI filler), yêu cầu tách nhỏ các bước "Cách thực hiện" thành H3, và siết chặt
- Cấm từ "Đọc vị" (AI filler), yêu cầu tách nhỏ các bước "Cách thực hiện" thành H3, và siết chặt cấu trúc Vấn đề - Giải pháp (phải nêu nỗi đau bẫy tâm lý/phá vỡ giả trước khi dẫn về HVS).

### triệt để các danh từ hóa ("sự bùng nổ", "việc ký kết") và chuẩn hóa Tuyên bố miễn trừ trác
- Loại bỏ triệt để các danh từ hóa ("sự bùng nổ", "việc ký kết") và chuẩn hóa Tuyên bố miễn trừ trách nhiệm dưới dạng blockquote không heading H2 riêng ở cuối bài.

### triệt để các từ cấm "nên"/"cần" và tối ưu hóa mật độ phân bố danh sách/bảng so sánh để trá
- Triệt tiêu triệt để các từ cấm "nên"/"cần" và tối ưu hóa mật độ phân bố danh sách/bảng so sánh để tránh sự liền kề của các đoạn văn bản.

### H4 (####) cho các tiêu đề con bổ trợ để tránh làm gián đoạn việc phân tách khối H2/H3 của
- Sử dụng H4 (####) cho các tiêu đề con bổ trợ để tránh làm gián đoạn việc phân tách khối H2/H3 của công cụ đếm từ wordcount.

### tiêu đề Kết luận thành "## Kết luận" đơn giản và trực diện, loại bỏ việc cố kéo dài tiêu đ
- Chuẩn hóa tiêu đề Kết luận thành "## Kết luận" đơn giản và trực diện, loại bỏ việc cố kéo dài tiêu đề kết luận theo từ khóa.

### Đồng bộ cấu trúc H3 cho các phần phân loại công cụ và hướng dẫn vẽ thực chiến để đảm bảo c
- Đồng bộ cấu trúc H3 cho các phần phân loại công cụ và hướng dẫn vẽ thực chiến để đảm bảo công cụ wordcount phân tách chính xác từ mục tiêu; cập nhật Word_Count_Target trong YAML khớp với dung lượng bài viết thực tế để pass toàn bộ QA/QC.

### Luôn gắn link nội bộ theo ngữ nghĩa thay vì gắn link đại trà vào các từ khóa chung như "F0
- Luôn gắn link nội bộ theo ngữ nghĩa thay vì gắn link đại trà vào các từ khóa chung như "F0".

### Viết Sapo cuốn hút có hook kêu gọi người đọc, lồng anchor text internal link tự nhiên theo ngữ nghĩa.
- Sapo phải viết cuốn hút, lồng ghép câu kêu gọi người đọc (hook) và nêu đúng nỗi đau F0; anchor text internal link bắt buộc lồng tự nhiên theo ngữ nghĩa (partial match), tuyệt đối không chèn nguyên câu từ khóa hỏi đáp thô ráp gây gượng ép.

## Cấu trúc & Định dạng (Structure & Formatting)

### phạm vi đào tạo của HVS Tài chính số (tập trung vào FA LV1 và TA LV1), cấm viết sai lệch r
- Đính chính phạm vi đào tạo của HVS Tài chính số (tập trung vào FA LV1 và TA LV1), cấm viết sai lệch rằng HVS Tài chính số trực tiếp hướng dẫn tính thuế phí hay quản trị danh mục cho F0.

### cơ chế lồng ghép sản phẩm HVS Tài chính số (với chương trình HVS Thực tập số) gắn liền với
- Làm rõ cơ chế lồng ghép sản phẩm HVS Tài chính số (với chương trình HVS Thực tập số) gắn liền với nỗi đau F0 trong phân tích báo cáo tài chính ngân hàng; gỡ bỏ heading H2 riêng biệt cho Tuyên bố miễn trừ trách nhiệm và tích hợp dạng blockquote in đậm ở cuối bài.

### định dạng danh sách (bullet list) cho các mục phân tích rủi ro song song để tránh tối đa v
- Sử dụng định dạng danh sách (bullet list) cho các mục phân tích rủi ro song song để tránh tối đa việc dồn các đoạn văn bản thông thường liền kề nhau.

## Tư duy tài chính (Financial Logic)

### quy trình 3 bước Force Sell theo SERP ACBS/VFS, áp dụng cơ chế khớp lệnh thực tế sàn HOSE/
- Chuẩn hóa quy trình 3 bước Force Sell theo SERP ACBS/VFS, áp dụng cơ chế khớp lệnh thực tế sàn HOSE/HNX (lệnh MP, MTL, ATO/ATC), hiển thị công thức tính tiền nạp thêm/bán cổ phiếu bằng blockquote in đậm và đồng bộ HVS product hierarchy.

### quy tắc logic tài chính — bắt buộc phân tích bẫy giá trị (Value Trap) hoặc ngoại lệ thực t
- Thêm quy tắc logic tài chính — bắt buộc phân tích bẫy giá trị (Value Trap) hoặc ngoại lệ thực tế đi kèm các tiêu chí định lượng (P/E < 9, P/B < 1.2) để đảm bảo chiều sâu thực chiến.

## Sản phẩm & Thương hiệu (Products & Brand Context)

### quy tắc về nguồn trích dẫn Chính phủ, cấm ẩn dụ hoa mỹ (đại dương, sóng dữ). *(gộp: quy tắc về nguồn trích dẫn Chính phủ, cấm ẩn dụ hoa mỹ (đại dương, sóng dữ).)*
- Bổ sung quy tắc về nguồn trích dẫn Chính phủ, cấm ẩn dụ hoa mỹ (đại dương, sóng dữ).

### rule hvs_product_hierarchy_sai — HVS Thực tập số là chương trình NẰM TRONG HVS Tài chính s
- Thêm rule hvs_product_hierarchy_sai — HVS Thực tập số là chương trình NẰM TRONG HVS Tài chính số, không phải sản phẩm độc lập; HVS Demo và HVS Forum là công cụ bổ trợ. User đã sửa lại nhiều lần vì AI thường trình bày 4 sản phẩm như ngang hàng nhau.

### HVS Tài chính số tập trung đào tạo kiến thức đầu tư (FA/TA) giúp nâng cao năng lực phân tí
- Đính chính HVS Tài chính số tập trung đào tạo kiến thức đầu tư (FA/TA) giúp nâng cao năng lực phân tích tự đọc hiểu pháp lý chứ không hướng dẫn đọc hiểu biểu mẫu hành chính cụ thể; HVS Forum gỡ rối vướng mắc pháp lý cụ thể của các công ty chứng khoán.

## ✅ Đã tự động hoá bởi `scripts/qa_lint.py` (vẫn phải tuân thủ khi viết)

| Bản năng | Check |
|---|---|
| "Hiểu một cách đơn giản" (filler), hạn chế "Nhịp đập thị trường" (cliché). | `CL2-hard` |
| "Chúng tôi thấu hiểu rằng" (AI empathy filler), thêm quy tắc Pacing khi giới thiệu sản phẩ | `CL2-hard` |
| tuyệt đối dấu ngoặc kép nhấn mạnh (Quy tắc 3.4), yêu cầu chia nhỏ phương pháp tính toán th | `FMT-quotes` |
| tiêu đề H1 loại bỏ từ cấm "đọc vị" | `CL2-hard` |
| Cập nhật từ "Dòng tiền trong chứng khoán" feedback (v1.1): Cấm cụm từ "dấu chân dòng tiền | `CL2-hard` |
