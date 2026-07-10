---
Author: Antigravity
aliases: ["Mô hình CAPM là gì"]
Status: Finalized
Pipeline_Mode: Express
SERP_Research: true
Target_Keyword: Mô hình CAPM là gì
Secondary_Keywords: mô hình capm, công thức capm, mô hình định giá tài sản vốn, cách tính capm
LSI_Keywords: lợi nhuận kỳ vọng, lãi suất phi rủi ro, hệ số Beta, phần bù rủi ro, rủi ro hệ thống, định giá cổ phiếu, đa dạng hóa danh mục, danh mục thị trường
Niche_Context: Corporate Finance | Valuation Models
Entities: HVS Tài chính số, HVS Thực tập số, HVS Demo, HVS Forum, VCB, VNM, trái phiếu chính phủ
Entities_Gap_Analysis: Phân tích sâu sự khác biệt giữa rủi ro hệ thống (systematic risk - đo bằng Beta, không thể đa dạng hóa) và rủi ro phi hệ thống (unsystematic risk - có thể triệt tiêu bằng cách đa dạng hóa danh mục), giúp người đọc hiểu bản chất định giá rủi ro của CAPM.
Search_Intent: Informational
Search_Intent_Deep: Lan Newbie muốn hiểu bản chất mô hình CAPM là gì, công thức tính chi tiết từng thành phần từ số liệu thực tế tại Việt Nam (lấy lãi suất trái phiếu chính phủ làm Rf, tính Beta của cổ phiếu VCB/VNM) và ý nghĩa thực tế khi định giá cổ phiếu.
Word_Count_Target: 1200
Persona: HVS Senior Mentor
Tone_Style: Direct, Data-driven, Objective
Lexicon_Focus: lợi nhuận kỳ vọng, lãi suất phi rủi ro, hệ số Beta, phần bù rủi ro, HVS Thực tập số, Lan Newbie
Financial_Logic: Scenario-based (Kịch bản tính lợi nhuận kỳ vọng của cổ phiếu có Beta > 1 và cổ phiếu có Beta < 1 khi thị trường chung biến động), Risk-Reward (Mối liên hệ tỷ lệ thuận giữa rủi ro hệ thống và lợi nhuận kỳ vọng), non-recommendation.
Avoid_Mistakes: Tránh dùng từ cấm (hành trình, giải pháp toàn diện, mở khóa tiềm năng, đóng vai trò là, tóm lại, kết luận là). Tránh ngoặc kép nhấn mạnh. Tránh công thức LaTeX.
---

# Mô hình CAPM là gì? Công thức tính lợi nhuận kỳ vọng

Trong quản lý danh mục đầu tư và thẩm định doanh nghiệp, mô hình CAPM là công cụ kinh điển được các nhà phân tích chuyên nghiệp sử dụng để đo lường mối quan hệ giữa rủi ro và lợi nhuận. Đối với nhà đầu tư F0, làm chủ mô hình này giúp xác định mức sinh lời kỳ vọng hợp lý trước khi giải ngân vốn. Bài viết dưới đây của HVS sẽ giải thích chi tiết mô hình CAPM là gì, công thức tính và cách ứng dụng thực chiến tại thị trường Việt Nam.

## Mô hình CAPM là gì?

Mô hình CAPM là mô hình định giá tài sản vốn thiết lập mối quan hệ tuyến tính giữa rủi ro hệ thống của một tài sản và mức lợi nhuận kỳ vọng mà nhà đầu tư yêu cầu để nắm giữ tài sản đó. William Sharpe phát triển công cụ này vào những năm 1960. Để định giá cổ phiếu một cách khoa học, bạn cần phân biệt rõ rủi ro hệ thống và rủi ro phi hệ thống của doanh nghiệp.

Bảng dưới đây so sánh hai loại rủi ro:

| Rủi ro | Đặc điểm tác động | Cách thức xử lý |
| :--- | :--- | :--- |
| **Hệ thống** | Tác động toàn thị trường (như lạm phát, lãi suất) | Không thể đa dạng hóa |
| **Phi hệ thống** | Tác động một doanh nghiệp (như sự cố kỹ thuật, kiện tụng) | Triệt tiêu bằng đa dạng hóa |

Hiểu rõ hai loại rủi ro này giúp bạn đánh giá vị thế đầu tư một cách khách quan nhất. Hãy đọc thêm bài viết [phân tích cơ bản là gì](https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/phan-tich-co-ban-la-gi) để ứng dụng linh hoạt các bộ lọc này vào thực tế.

## Chi tiết công thức tính lợi nhuận kỳ vọng theo mô hình CAPM

Công thức CAPM tính toán lợi nhuận kỳ vọng của cổ phiếu dựa trên lãi suất phi rủi ro, hệ số Beta và tỷ suất sinh lời thị trường để định lượng mối tương quan này.

Công thức tính toán được thiết lập như sau:

> **E(Ri) = Rf + Beta * [E(Rm) - Rf]**

Trong công thức trên, các thành phần được giải thích chi tiết như sau:
- **E(Ri):** Tỷ suất sinh lời kỳ vọng của cổ phiếu i mà nhà đầu tư yêu cầu.
- **Rf:** Lãi suất phi rủi ro, lấy từ [lợi suất trái phiếu chính phủ](https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/bond-yield-la-gi) Việt Nam kỳ hạn 10 năm làm thước đo.
- **Beta (β):** Hệ số đo lường độ biến động giá cổ phiếu so với [chỉ số VN-Index](https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/chi-so-vn-index-la-gi).
- **E(Rm):** Tỷ suất sinh lời thị trường, tính từ hiệu suất trung bình 5 năm của VN-Index.
- **[E(Rm) - Rf]:** Phần bù rủi ro thị trường (Market Risk Premium), thể hiện lợi nhuận yêu cầu khi đầu tư cổ phiếu thay vì trái phiếu chính phủ.

Hãy xem xét ví dụ thực tế định giá cổ phiếu VCB giả lập trên sàn HOSE với các thông số cụ thể:
- Giả định lãi suất trái phiếu chính phủ Việt Nam kỳ hạn 10 năm hiện tại là 3% (Rf = 3%).
- Hiệu suất sinh lời trung bình lịch sử của VN-Index là 10% (E(Rm) = 10%).
- Hệ số Beta của cổ phiếu VCB được tính toán từ dữ liệu biến động giá lịch sử là 1.2 (Beta = 1.2).

Áp dụng số liệu vào công thức CAPM:

> **E(Ri) = 3% + 1.2 * [10% - 3%] = 11.4%**

Nhà đầu tư yêu cầu tỷ suất sinh lời kỳ vọng tối thiểu đối với cổ phiếu VCB là 11.4%/năm. Nếu hiệu suất thực tế dự phóng trong tương lai thấp hơn mức sinh lời này, bạn nên cân nhắc gửi tiền tiết kiệm hoặc tìm kiếm cơ hội đầu tư khác hiệu quả hơn.

## Ý nghĩa thực tế và các hạn chế của mô hình CAPM

Ý nghĩa thực tế lớn nhất của mô hình CAPM là xác định chi phí vốn chủ sở hữu (Ke) làm tỷ lệ chiết khấu. Khi định giá dòng tiền chiết khấu (DCF) tìm [giá trị nội tại của cổ phiếu](https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/gia-tri-noi-tai-cua-co-phieu), Ke chính là tham số đầu vào quan trọng nhất.

Mô hình CAPM cũng giúp bạn xây dựng kịch bản quản trị danh mục đầu tư dựa trên biến động của hệ số Beta:
- **Kịch bản 1:** Hệ số Beta > 1 (như cổ phiếu chứng khoán). Nếu VN-Index tăng hoặc giảm 10%, cổ phiếu có Beta 1.5 sẽ bứt phá tăng hoặc thoái lui giảm 15%.
- **Kịch bản 2:** Hệ số Beta < 1 (như cổ phiếu điện lực). Nếu VN-Index giảm 10%, cổ phiếu có Beta 0.7 chỉ điều chỉnh giảm 7%, giúp phòng thủ danh mục.

Tuy nhiên, mô hình CAPM cũng bộc lộ một số hạn chế kỹ thuật đáng lưu ý khi áp dụng tại Việt Nam:
- **Giả định thị trường hoàn hảo:** Mô hình giả định chi phí giao dịch bằng không và không có thuế. Thực tế trên sàn HOSE, bạn chịu phí giao dịch 0.1% đến 0.2% cùng thuế bán cổ phiếu 0.1%.
- **Beta biến động:** Hệ số Beta tính theo lịch sử giá nên không phản ánh rủi ro tương lai khi doanh nghiệp thay đổi cơ cấu.

## Ứng dụng mô hình định giá chuyên nghiệp cùng HVS Tài chính số

Bạn có thể chủ động giải quyết khó khăn thu thập dữ liệu và tính toán hệ số Beta thực tế bằng cách tham gia lộ trình đào tạo bài bản của HVS. Lan Newbie thường gặp rào cản lớn khi thu thập dữ liệu lợi suất trái phiếu làm Rf và giá đóng cửa lịch sử để tính Beta trên Excel. Tính toán sai lệch các biến số này sẽ dẫn đến kết quả định giá cổ phiếu sai số lớn, ảnh hưởng tiêu cực đến hiệu quả giải ngân vốn.

Để khắc phục triệt để khó khăn này, nền tảng đào tạo trực tuyến **HVS Tài chính số** mang đến lộ trình đào tạo **HVS Thực tập số** (giai đoạn Chuyên hóa với môn học Thẩm định doanh nghiệp và mô hình định giá - FA Level 2). Chương trình đào tạo này hướng dẫn bạn từng bước thực hành phân tích và định giá chuyên nghiệp:
- Thu thập lãi suất phi rủi ro Việt Nam từ các nguồn chính thức.
- Tải dữ liệu giá đóng cửa lịch sử cổ phiếu từ HOSE.
- Sử dụng công cụ hồi quy tuyến tính trong Excel để tính toán chính xác hệ số Beta thực tế của doanh nghiệp.

Song song với việc học lý thuyết, bạn có thể ứng dụng ngay các mô hình định giá vừa xây dựng để thực hành giao dịch giả lập không rủi ro trên hệ thống mô phỏng trực quan **HVS Demo**. Đồng thời, bạn dễ dàng gửi bài tập Excel định giá lên cộng đồng **HVS Forum** để nhận phản hồi, sửa lỗi tính toán trực tiếp từ các Mentor CFA giàu kinh nghiệm thực chiến.

## Kết luận

Mô hình CAPM giúp liên kết rủi ro hệ thống với tỷ suất sinh lời yêu cầu để hỗ trợ định giá doanh nghiệp. Thấu hiểu mô hình này giúp bạn xây dựng tư duy đầu tư thực chiến bài bản cùng các Mentor chuyên nghiệp tại HVS.

> **Tuyên bố miễn trừ trách nhiệm:** Mọi phân tích và nhận định chỉ mang tính chất tham khảo học tập tại HVS, không cấu thành lời khuyên đầu tư hay khuyến nghị mua bán bất kỳ mã cổ phiếu nào. Bạn tự chịu trách nhiệm trước các quyết định đầu tư của bản thân.

## Nhật ký chỉnh sửa (Revision Log)
- **v1.0 (2026-06-25):** Khởi tạo outline cho từ khóa "Mô hình CAPM là gì" thuộc Cluster Phân tích cơ bản theo yêu cầu viết bài mới.
