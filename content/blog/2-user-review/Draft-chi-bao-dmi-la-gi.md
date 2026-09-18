---
Author: Claude Code
Status: Draft
Pipeline_Mode: Express
SERP_Research: true
Persona: Lan Newbie / Nhà đầu tư F0
Tone: Chuyên nghiệp, thực chiến, hỗ trợ chu đáo
Writing_Method: PAS / How-to steps
Target_Keyword: chỉ báo dmi
Cluster: Phân tích kỹ thuật
Cluster_Role: Cluster
Search_Intent: Informational
Content_Type: Guide
Featured_Snippet: Paragraph
Word_Count_Target: 1750
Meta_Description: Chỉ báo DMI (Directional Movement Index) là gì? Hướng dẫn cấu tạo bộ 3 đường +DI, -DI, ADX, công thức tính và 3 chiến lược giao dịch thực chiến hiệu quả nhất.
HVS_Products:
  - product: HVS Demo
    benefit: Luyện tập theo dõi đường +DI, -DI và ADX không rủi ro
  - product: HVS Forum
    benefit: Trao đổi tín hiệu DMI thực chiến cùng cộng đồng F0, F1
  - product: HVS Thực tập số
    benefit: Rèn luyện kỹ năng phân tích kỹ thuật và quản trị danh mục chuyên nghiệp
Anti_AI_Flags:
  - Không dùng "Trong thế giới không ngừng phát triển", "Mở khóa tiềm năng", "Tóm lại,", "Hành trình"
  - Không dùng "giải pháp toàn diện", "nâng tầm", "đáng chú ý là", "sóng dữ"
Internal_Links:
  - role: Related Cluster
    file: Final-chi-bao-adx.md
    anchor_suggestion: chỉ báo ADX
  - role: Related Cluster
    file: Final-rsi-la-gi.md
    anchor_suggestion: chỉ báo RSI
  - role: Related Cluster
    file: Final-ho-tro-khang-cu-la-gi.md
    anchor_suggestion: vùng hỗ trợ và kháng cự
  - role: Related Cluster
    file: Final-cat-lo-la-gi.md
    anchor_suggestion: nguyên tắc cắt lỗ
  - role: Related Cluster
    file: Final-phan-tich-ky-thuat-la-gi.md
    anchor_suggestion: phương pháp phân tích kỹ thuật
---

# Chỉ báo DMI là gì? Cấu tạo, công thức & 3 chiến lược giao dịch thực chiến

Trong đầu tư chứng khoán, việc chọn đúng cổ phiếu có đà tăng là một chuyện, nhưng mua đúng thời điểm khi xu hướng vừa bùng nổ lại là bài toán khó với nhà đầu tư F0. Nhiều người thường rơi vào bẫy mua đúng cổ phiếu đang đi ngang kiệt thanh khoản hoặc mở vị thế khi xu hướng tăng đã vào giai đoạn suy yếu.

Chỉ báo DMI (Directional Movement Index) ra đời như một hệ thống phân tích kỹ thuật đa năng giải quyết trọn vẹn hai câu hỏi cốt lõi của thị trường: Giá đang đi theo hướng nào và sức mạnh của xu hướng đó ra sao? 

Bài viết này từ HVS sẽ hướng dẫn bạn chi tiết chỉ báo DMI là gì, cấu tạo bộ 3 đường +DI, -DI, ADX, công thức tính toán và 3 chiến lược giao dịch thực chiến giúp nâng cao hiệu quả đầu tư trên sàn HOSE và HNX.

## 1. Chỉ báo DMI là gì? Nguồn gốc và vai trò trong phân tích kỹ thuật

Chỉ báo DMI (Directional Movement Index - Chỉ số Chuyển động Định hướng) là công cụ phân tích kỹ thuật giúp nhà đầu tư xác định hướng di chuyển của giá cổ phiếu (tăng hay giảm) đồng thời đánh giá cường độ (độ mạnh yếu) của xu hướng đó.

Công cụ này do nhà phân tích kỹ thuật lừng danh J. Welles Wilder Jr. phát triển và công bố vào năm 1978 trong cuốn sách kinh điển "New Concepts in Technical Trading Systems". Ông cũng chính là cha đẻ của các chỉ báo nổi tiếng khác như RSI hay Parabolic SAR.

Trong [phương pháp phân tích kỹ thuật](file:///e:/project/hvs-company-info/content/blog/3-finalized/Final-phan-tich-ky-thuat-la-gi.md), DMI giữ vai trò như một bộ lọc tín hiệu hai chiều. Nếu các chỉ báo động lượng thông thường chỉ đo lường tốc độ thay đổi giá, DMI tách biệt rõ ràng giữa lực mua (áp lực đẩy giá lên) và lực bán (áp lực đè giá xuống), sau đó hợp nhất với chỉ số sức mạnh chung để đưa ra góc nhìn toàn diện.

### Cảnh báo phân biệt quan trọng cho người mới
Khi cài đặt công cụ trên các nền tảng đồ thị như TradingView hay Amibroker, bạn cần phân biệt hai chỉ báo có cùng tên viết tắt DMI:
- **Directional Movement Index (Wilder's DMI):** Bộ chỉ báo chuyển động định hướng gồm 3 đường (+DI, -DI, ADX) mà bài viết này đang đề cập.
- **Dynamic Momentum Index:** Chỉ báo dao động động lượng biến đổi do Tushar Chande và Stanley Kroll phát triển (một biến thể điều chỉnh chu kỳ của RSI).

Nhà đầu tư nên kiểm tra kỹ tên đầy đủ trên phần mềm biểu đồ để đảm bảo chọn đúng hệ thống DMI của J. Welles Wilder.

## 2. Cấu tạo bộ 3 đường chính trong chỉ báo DMI

Hệ thống chỉ báo DMI tiêu chuẩn bao gồm 3 đường cấu thành, hoạt động nhịp nhàng cùng nhau trên biểu đồ giá:

```
Hệ thống chỉ báo DMI
├── Đường +DI (Positive Directional Indicator - Xanh)  --> Đo lực tăng giá
├── Đường -DI (Negative Directional Indicator - Đỏ)   --> Đo lực giảm giá
└── Đường ADX (Average Directional Index - Vàng/Xám) --> Đo sức mạnh xu hướng chung
```

### Đường +DI (Positive Directional Indicator)
Đường +DI đo lường sức mạnh của các chuyển động tăng giá trong chu kỳ quan sát (mặc định là 14 phiên). Khi đường +DI hướng lên và nằm ở mức cao, phe mua đang chiếm ưu thế trên thị trường.

### Đường -DI (Negative Directional Indicator)
Đường -DI đo lường sức mạnh của các chuyển động giảm giá trong chu kỳ 14 phiên. Khi đường -DI hướng lên và duy trì ở mức cao, phe bán đang áp đảo và đè nặng lên giá cổ phiếu.

### Đường ADX (Average Directional Index)
Đường ADX đo lường độ mạnh yếu tổng thể của xu hướng hiện tại trên thang điểm từ 0 đến 100. ADX được tính bằng cách làm mượt giá trị chênh lệch giữa +DI và -DI.

Điểm cốt lõi cần nhớ: Đường ADX là chỉ báo phi hướng (non-directional). ADX dốc lên chỉ thể hiện thị trường đang có xu hướng rất mạnh, bất kể đó là xu hướng tăng hay xu hướng giảm. Muốn biết thị trường tăng hay giảm, bạn bắt buộc phải quan sát vị trí tương quan giữa đường +DI và -DI.

## 3. Công thức tính chỉ báo DMI chi tiết

Để hiểu bản chất của DMI thay vì chỉ áp dụng máy móc, nhà đầu tư cần nắm rõ 4 bước tính toán cốt lõi sau đây.

### Bước 1: Tính Chuyển động Định hướng (+DM và -DM)
Chuyển động định hướng được xác định bằng cách so sánh đỉnh và đáy của phiên hiện tại với phiên trước đó:
- **+DM (Positive Directional Movement):** Giá cao nhất hôm nay - Giá cao nhất hôm qua. Điều kiện: Giá trị này phải lớn hơn 0 và lớn hơn khoảng chênh lệch đáy (-DM). Nếu không thỏa mãn, +DM = 0.
- **-DM (Negative Directional Movement):** Giá thấp nhất hôm qua - Giá thấp nhất hôm nay. Điều kiện: Giá trị này phải lớn hơn 0 và lớn hơn khoảng chênh lệch đỉnh (+DM). Nếu không thỏa mãn, -DM = 0.

Nếu cả hai giá trị đều nhỏ hơn 0 hoặc bằng nhau, cả +DM và -DM đều bằng 0.

### Bước 2: Tính Biên độ biến động thực tế True Range (TR)
TR đo lường độ biến động thực sự của giá cổ phiếu trong phiên, tính bằng giá trị lớn nhất trong 3 khoảng sau:
- Khoảng cách từ Giá cao nhất đến Giá thấp nhất phiên hôm nay.
- Giá trị tuyệt đối của (Giá cao nhất hôm nay - Giá đóng cửa hôm qua).
- Giá trị tuyệt đối của (Giá thấp nhất hôm nay - Giá đóng cửa hôm qua).

### Bước 3: Tính đường +DI14 và -DI14
Các giá trị +DM, -DM và TR được làm mượt qua chu kỳ 14 phiên (theo phương pháp làm mượt Wilder):
- +DI14 = (Smoothed +DM14 ÷ Smoothed TR14) × 100
- -DI14 = (Smoothed -DM14 ÷ Smoothed TR14) × 100

### Bước 4: Tính đường DX và ADX
- Chỉ số định hướng DX = (|+DI14 - -DI14| ÷ (+DI14 + -DI14)) × 100
- ADX14 = Đường trung bình động làm mượt 14 phiên của DX.

### Ví dụ tính toán minh họa thực tế
Giả sử trên cổ phiếu HPG, sau khi làm mượt dữ liệu 14 phiên giao dịch, ta có các số liệu:
- Smoothed +DM14 = 18.5
- Smoothed -DM14 = 6.2
- Smoothed TR14 = 42.0

Khi đó:
- +DI14 = (18.5 ÷ 42.0) × 100 = 44.05
- -DI14 = (6.2 ÷ 42.0) × 100 = 14.76
- DX = (|+44.05 - 14.76| ÷ (44.05 + 14.76)) × 100 = (29.29 ÷ 58.81) × 100 = 49.80

Giá trị +DI14 (44.05) vượt xa -DI14 (14.76) cho thấy phe mua đang kiểm soát hoàn toàn HPG, đồng thời DX đạt 49.80 báo hiệu một xu hướng bứt phá có động lượng rất mạnh.

## 4. 3 Cách đọc tín hiệu & Chiến lược giao dịch thực chiến với DMI

Nắm vững cách vận hành của bộ 3 đường DMI sẽ giúp nhà đầu tư thiết lập các điểm mua bán chuẩn xác và hạn chế tối đa các nhịp rũ bỏ của thị trường.

### Chiến lược 1: Tín hiệu giao cắt +DI và -DI (Xác định điểm vào lệnh sớm)
Giao cắt giữa hai đường định hướng là tín hiệu phát hiện sự thay đổi quyền kiểm soát giữa phe mua và phe bán:
- **Tín hiệu Mua (Bullish Cross):** Xảy ra khi đường +DI cắt vượt lên trên đường -DI từ dưới lên. Tín hiệu này cho biết phe mua bắt đầu áp đảo phe bán, mở ra cơ hội mua cổ phiếu.
- **Tín hiệu Bán (Bearish Cross):** Xảy ra khi đường -DI cắt vượt lên trên đường +DI từ dưới lên. Tín hiệu này xác nhận phe bán bắt đầu làm chủ thế trận, nhà đầu tư nên chủ động bán hạ tỷ trọng hoặc đóng vị thế.

### Chiến lược 2: Bộ lọc sức mạnh xu hướng bằng đường ADX
Để tránh rơi vào các bẫy giao cắt giả, nhà đầu tư cần kết hợp [chỉ báo ADX](file:///e:/project/hvs-company-info/content/blog/3-finalized/Final-chi-bao-adx.md) làm bộ lọc điều kiện:
- **ADX < 20 (Thị trường Sideway):** Các đường +DI và -DI thường xoắn lấy nhau. Tín hiệu giao cắt lúc này có độ nhiễu cao, nhà đầu tư kiên nhẫn đứng ngoài quan sát.
- **ADX vượt mốc 25 (Xu hướng hình thành):** Khi ADX cắt lên trên mức 25 và dốc lên, xu hướng tăng hoặc giảm đã được xác nhận. Tín hiệu mua (+DI > -DI) xuất hiện khi ADX > 25 có tỷ lệ thành công cao nhất.
- **ADX > 40 - 50 (Xu hướng quá đà):** Thị trường đang trong giai đoạn tăng tốc mạnh. Tuy nhiên nếu ADX đạt trên 50 và có dấu hiệu quay đầu dốc xuống, đó là cảnh báo đà tăng bắt đầu mệt mỏi, cần chuẩn bị chiến lược chốt lời.

### Chiến lược 3: Tín hiệu phân kỳ giữa DMI/ADX và đường giá
Phân kỳ xuất hiện khi hướng di chuyển của đường giá và đường chỉ báo DMI không đồng nhất:
- **Phân kỳ giảm giá (Bearish Divergence):** Giá cổ phiếu SSI liên tục vượt đỉnh mới, nhưng đường +DI hoặc đường ADX lại tạo đỉnh sau thấp hơn đỉnh trước. Hiện tượng này thể hiện lực mua đang đuối dần dù giá vẫn tăng do đà tâm lý. Đây là cảnh báo đảo chiều giảm giá sớm mà nhà đầu tư không nên bỏ qua.

### Bảng tổng hợp trạng thái DMI và hành động khuyến nghị

| Trạng thái DMI | Tương quan +DI / -DI | Mức giá trị ADX | Ý nghĩa thị trường | Hành động khuyến nghị |
| :--- | :--- | :--- | :--- | :--- |
| **Uptrend mạnh** | +DI nằm trên -DI | ADX > 25 và dốc lên | Xu hướng tăng có động lượng mua áp đảo | Mở mua mới, nắm giữ cổ phiếu, gia tăng vị thế |
| **Downtrend mạnh** | -DI nằm trên +DI | ADX > 25 và dốc lên | Phe bán đè giá quyết liệt | Bán hạ tỷ trọng, quản trị rủi ro, đứng ngoài |
| **Sideway tích lũy** | +DI và -DI xoắn vào nhau | ADX < 20 | Biến động hẹp, chưa có sóng rõ ràng | Hạn chế giao dịch, chờ tín hiệu breakout |
| **Cảnh báo suy yếu** | +DI nằm trên -DI | ADX > 40 dốc xuống | Động lượng tăng bắt đầu hụt hơi | Chốt lời từng phần, siết chặt dừng lỗ |

## 5. Lưu ý quản trị rủi ro & Bẫy tín hiệu nhiễu F0 cần tránh

Dù DMI là bộ công cụ phân tích xu hướng mạnh mẽ, nhà đầu tư F0 vẫn cần lưu ý các điểm yếu cố hữu sau:

### 1. Bản chất độ trễ (Lagging Indicator)
Do sử dụng dữ liệu trung bình làm mượt trong 14 phiên, các điểm giao cắt +DI/-DI hoặc đà tăng của ADX luôn xuất hiện sau khi giá đã có một nhịp biến động nhất định. Việc đua lệnh mua đuổi khi ADX đã lên quá cao (>45) dễ khiến bạn dính nhịp chỉnh ngắn hạn.

### 2. Bẫy giao cắt giả trong vùng sideway
Trong giai đoạn thị trường đi ngang tích lũy, đường +DI và -DI liên tục cắt nhau qua lại. Nếu giao dịch mua bán theo từng điểm cắt khi ADX < 20, tài khoản của bạn sẽ nhanh chóng bị bào mòn bởi phí giao dịch và các khoản lỗ nhỏ nối tiếp nhau.

### 3. Nguyên tắc kết hợp công cụ đa lớp
Không nên sử dụng DMI một cách độc lập. Chiến lược thực chiến tối ưu nhất là kết hợp DMI với:
- [Chỉ báo RSI](file:///e:/project/hvs-company-info/content/blog/3-finalized/Final-rsi-la-gi.md) để đánh giá vùng quá mua/quá bán.
- [Vùng hỗ trợ và kháng cự](file:///e:/project/hvs-company-info/content/blog/3-finalized/Final-ho-tro-khang-cu-la-gi.md) trên đồ thị kỹ thuật để tìm điểm vào lệnh có tỷ lệ Risk/Reward đẹp.
- Luôn đặt kỷ luật tuân thủ [nguyên tắc cắt lỗ](file:///e:/project/hvs-company-info/content/blog/3-finalized/Final-cat-lo-la-gi.md) từ 5% đến 7% để bảo vệ nguồn vốn trước mọi biến động bất ngờ.

## 6. Thực hành phân tích chỉ báo DMI cùng hệ sinh thái HVS

Để biến kiến thức lý thuyết thành kỹ năng thực chiến sinh lời, bạn có thể từng bước rèn luyện thông qua hệ sinh thái hỗ trợ đầu tư từ HVS:

### Kịch bản phân tích thực chiến trên cổ phiếu SSI
- **Bước 1:** Quan sát biểu đồ SSI khi giá tích lũy quanh đường trung bình động.
- **Bước 2:** Theo dõi đường +DI cắt vượt lên -DI, đồng thời ADX từ mốc 18 bắt đầu quay đầu dốc lên bứt phá mốc 25.
- **Bước 3:** Khối lượng giao dịch gia tăng đột biến xác nhận dòng tiền lớn gia nhập. Đây là thời điểm mở vị thế mua tối ưu với xác suất thắng cao.

### Đồng hành cùng các công cụ hỗ trợ từ HVS
- **Luyện tập không rủi ro trên HVS Demo:** Trước khi xuống tiền thật, bạn nên trải nghiệm giao dịch và theo dõi tín hiệu DMI trên nền tảng **HVS Demo** để làm quen với nhịp vận hành của chỉ báo.
- **Trao đổi cùng cộng đồng tại HVS Forum:** Tham gia thảo luận, chia sẻ góc nhìn đồ thị DMI thực tế với các nhà đầu tư F0, F1 khác trên **HVS Forum** để nhận phản hồi từ những người có kinh nghiệm.
- **Nâng tầm kỹ năng với HVS Thực tập số:** Đăng ký chương trình **HVS Thực tập số** (thuộc phễu **HVS Tài chính số**) để được rèn luyện tư duy phân tích kỹ thuật thực chiến, xây dựng bộ quy tắc giao dịch cá nhân và làm chủ kỹ năng quản trị danh mục chuyên nghiệp.

---

## Revision Log

- **Init:** Lên dàn ý bài viết "Chỉ báo DMI là gì".
- **Draft:** Triển khai nội dung chi tiết theo cấu trúc brief, bổ sung công thức tính toán thực tế và ví dụ cổ phiếu SSI/HPG.
- **Finalized:** Chuyển sang giai đoạn Finalized.

