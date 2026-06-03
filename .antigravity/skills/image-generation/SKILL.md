---
name: image-generation
description: Quy chuẩn và quy trình tự động hóa tạo ảnh minh họa bài viết trực tiếp trên Antigravity, áp dụng Hệ thống Bản vẽ Thị giác (Visual Typologies), tự động nén WebP và chèn logo HVS Tài Chính Số.
---

# 🎨 Skill: HVS Image Prompting & Drawing System

Tài liệu này định nghĩa quy chuẩn và luồng thực thi tự động để thiết kế, vẽ ảnh trực tiếp trên Antigravity, tối ưu hóa WebP SEO-ready, và tự động chèn logo thương hiệu **HVS Tài Chính Số**.

---

## 📂 1. Cấu trúc Skill Quy chuẩn (Self-Contained Structure)

Skill này được thiết kế khép kín và độc lập theo đúng cấu trúc tiêu chuẩn:

```text
.antigravity/skills/image-generation/
├── SKILL.md                          # Tài liệu hướng dẫn chính (file này)
│
├── assets/                           # Nơi chứa tài nguyên tĩnh và ảnh mẫu tham chiếu
│   ├── hvs-tai-chinh-so-logo.jpg     # Logo HVS Tài Chính Số gốc (màu chủ đạo #f0e0f8)
│   ├── ref-conceptual.png            # [Ảnh mẫu] Phong cách bìa khái niệm (Kiểu A)
│   ├── ref-process.png               # [Ảnh mẫu] Sơ đồ quy trình (Kiểu B)
│   ├── ref-comparison.png            # [Ảnh mẫu] So sánh đối chiếu (Kiểu C)
│   └── ref-mockup.png                # [Ảnh mẫu] Mockup ứng dụng (Kiểu D)
│
├── scripts/                          # Script tự động xử lý ảnh
│   └── image_processor.py            # Chèn đè logo đính kèm và xuất nén ảnh WebP
│
├── templates/                        # Cấu hình hệ thống ảnh
│   └── palette-config.yaml           # Định nghĩa biến màu sắc động
│
└── references/                       # Tài liệu thiết kế bổ sung (cover-template.html, process-template.html, comparison-template.html, mockup-template.html, definition-template.html)
```

---

## 🎨 2. Hệ thống Bản vẽ Thị giác (4 Visual Typologies)

Dựa trên cấu trúc bài viết và Search Intent, Agent sẽ tự động chọn một trong bốn kiểu bố cục dưới đây để vẽ ảnh:

### 📸 Kiểu A: Conceptual Featured Image (Ảnh Bìa Khái niệm)
*   **Ứng dụng:** Ảnh bìa H1 của bài viết (đặc biệt là bài định nghĩa khái niệm tài chính).
*   **Bố cục:** Bố cục tập trung (Centered Focus), 3D isometric sang trọng. Thể hiện ẩn dụ trực quan của từ khóa.
*   **Bảng màu:** 65% Nền tối (`BG_DARK`) | 20% Tím chủ đạo (`PRIMARY_COLOR`) | 10% Tím nhạt (`LOGO_BACKGROUND`) | 5% Neon Cyan (`ACCENT_COLOR`).
*   **Đường dẫn ảnh mẫu:** [ref-conceptual.png](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/assets/ref-conceptual.png)
*   **Trực quan mẫu:**
    ![Conceptual Style Reference](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/assets/ref-conceptual.png)

### 🔄 Kiểu B: How-to & Process Flow (Ảnh Quy trình/Hướng dẫn)
*   **Ứng dụng:** Minh họa cho các phần hướng dẫn từng bước của bài viết (H2/H3).
*   **Bố cục:** Dạng chuỗi nằm ngang (Horizontal Flow/Cards), có mũi tên mờ mềm mại kết nối. Sử dụng icon thay cho chữ phức tạp để tránh AI vẽ lỗi.
*   **Bảng màu:** 65% Nền kem sáng ấm (`BG_LIGHT`) | 20% Tím nhạt (`LOGO_BACKGROUND`) | 10% Tím đậm (`PRIMARY_COLOR`) | 5% Xanh ngọc (`ACCENT_COLOR`).
*   **Đường dẫn ảnh mẫu:** [ref-process.png](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/assets/ref-process.png)
*   **Trực quan mẫu:**
    ![Process Style Reference](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/assets/ref-process.png)

### ⚖️ Kiểu C: Split Comparison (Ảnh So sánh/Đối chiếu)
*   **Ứng dụng:** Section so sánh hai khái niệm khác nhau (A vs B).
*   **Bố cục:** Chia đôi màn hình 50/50. Sử dụng hai tông màu tương tương phản nhẹ từ palette màu để làm nổi bật hai mặt đối lập.
*   **Bảng màu:** 65% Nền tối (`BG_DARK`) | 20% Tím (`PRIMARY_COLOR`) | 10% Xanh ngọc (`ACCENT_COLOR`) | 5% Pastel Lavender (`LOGO_BACKGROUND`).
*   **Đường dẫn ảnh mẫu:** [ref-comparison.png](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/assets/ref-comparison.png)
*   **Trực quan mẫu:**
    ![Comparison Style Reference](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/assets/ref-comparison.png)

### 📊 Kiểu D: UI Mockup (Ảnh Giao diện/Dữ liệu HVS)
*   **Ứng dụng:** Giới thiệu tính năng, chỉ số tài chính, hoặc tính thực chiến của app **HVS Tài chính số**.
*   **Bố cục:** Giao diện Mockup điện thoại hoặc web mờ (glassmorphism) bo góc mềm mại, hiển thị biểu đồ nến phát sáng neon.
*   **Bảng màu:** 60% Nền tối (`BG_DARK`) | 20% Lavender nhạt (`LOGO_BACKGROUND`) | 15% Tím chủ đạo (`PRIMARY_COLOR`) | 5% Neon Cyan (`ACCENT_COLOR`).
*   **Đường dẫn ảnh mẫu:** [ref-mockup.png](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/assets/ref-mockup.png)
*   **Trực quan mẫu:**
    ![UI Mockup Style Reference](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/assets/ref-mockup.png)

---

### 📈 Kiểu E: Stock Profile Card (Thẻ Nhận diện Cổ phiếu)
*   **Ứng dụng:** Ảnh featured hoặc section ảnh cho **~35 bài dạng `cach-mua-co-phieu-[MÃ]`** (POW, VCB, FPT, HPG, CTG...).
*   **Bố cục:** Hai cột 60/40 — Trái: mã cổ phiếu khổng lồ + sparkline xu hướng + tên công ty + ngành. Phải: 4 data card (Vốn hóa / Sàn / Biên độ / Ngành) + CTA banner.
*   **Biến động theo ngành (`--industry-accent`):** Ngân hàng → `#2196F3` | Điện → `#FFD600` | BĐS → `#FF7043` | Thép → `#78909C` | Công nghệ → `#7C4DFF` | Tiêu dùng → `#66BB6A` | Dầu khí → `#FFA726`.
*   **Template:** [stock-profile-template.html](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/references/stock-profile-template.html)
*   **Cổng chờ chính:** Mã ticker (2-4 ký tự), tên công ty, ngành, sàn, 4 data card values, sparkline direction.

### 🏆 Kiểu F: Ranking / Listicle Scoreboard (Bảng Xếp hạng)
*   **Ứng dụng:** Bài **so sánh nhiều hơn 2 lựa chọn** — Top X, "nên chọn cái nào", danh sách tốt nhất (VD: ETF nào tốt, cổ phiếu blue chip tiêu biểu, chỉ số thế giới quan trọng).
*   **Bố cục:** Vertical stack — tiêu đề top + 3-5 rank row, mỗi row có số thứ tự lớn + accent bar trái + tên + mô tả ngắn + tag bên phải. Hạng 1 nổi bật với glow cyan.
*   **Bảng màu:** Nền tối `#0D0D16` + Rank 1 Cyan | Rank 2 Lavender | Rank 3 Mint | Rank 4-5 mờ dần.
*   **Template:** [ranking-template.html](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/references/ranking-template.html)
*   **Cổng chờ chính:** Tiêu đề section, 3-5 item name + mô tả + tag, badge loại nội dung.

### ⚠️ Kiểu G: Psychology / Warning Card (Thẻ Tâm lý / Cảnh báo)
*   **Ứng dụng:** Bài về **tâm lý đầu tư, quản trị rủi ro, cổ phiếu đầu cơ, call margin** — nội dung cần gợi cảm giác kiểm soát và cân bằng.
*   **Bố cục:** Hai cột 55/45 — Trái: danh sách trap (warn icon) + nguyên tắc (safe icon). Phải: cân thăng bằng trừu tượng "Cảm xúc vs Kỷ luật" + floating keywords.
*   **Màu sắc:** Cam `#FF6B35` (cảnh báo/cảm xúc) + Cyan `#00E5FF` (kỷ luật/an toàn) trên nền tối.
*   **Template:** [psychology-template.html](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/references/psychology-template.html)
*   **Cổng chờ chính:** Topic badge, tiêu đề (warn/accent class), 2-4 trap-item (warn-icon/safe-icon), 2-3 floating keyword.

### 🌐 Kiểu H: Market Data Dashboard (Bảng Điện Thị trường)
*   **Ứng dụng:** Bài về **chỉ số thị trường** — VN-Index, S&P 500, chỉ số thế giới, chỉ số châu Á, HNX, VN30.
*   **Bố cục:** Grid 2×3 (hoặc 2×2) thẻ chỉ số — mỗi thẻ có tên + giá trị + % thay đổi + mini sparkline. Hiệu ứng scanline nhẹ gợi màn hình bảng điện. VN-Index card được featured (cyan glow).
*   **Quan trọng:** Tất cả số liệu là **GIẢ LẬP** (fictional) — chỉ phục vụ visual, không phải dữ liệu thực.
*   **Template:** [market-data-template.html](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/references/market-data-template.html)
*   **Cổng chờ chính:** Tiêu đề, subtitle, 4-6 index card (tên + giá trị giả lập + % + up/down class).

### ⏱️ Kiểu I: Timeline / Scenario Flow (Lộ trình Thời gian)
*   **Ứng dụng:** Bài có **tính thời gian hoặc chu kỳ** — quy trình tái cơ cấu ETF, lộ trình đầu tư, chiến lược tích sản, giờ giao dịch theo phiên.
*   **Bố cục (Linear):** Node ngang nối bằng connector gradient, mỗi node có circle (done/active/pending) + period + tên bước + mô tả. Tối đa 5 node.
*   **Bố cục (Circular):** Đổi sang variant circular (có sẵn trong comment của template) cho chu kỳ lặp lại vô hạn.
*   **Template:** [timeline-template.html](file:///e:/project/hvs-company-info/.antigravity/skills/image-generation/references/timeline-template.html)
*   **Cổng chờ chính:** Header badge, tiêu đề, 3-5 node (period + tên + mô tả + state class), chọn variant Linear/Circular.

---

## 📊 3. Quy tắc Số lượng Ảnh mỗi Bài

Số lượng ảnh được tính dựa trên **3 yếu tố kết hợp**: loại bài (Pillar / Cluster), word count mục tiêu, và số H2 section cần minh họa.

### Bảng giới hạn số lượng ảnh

| Loại bài | Word Count | Số ảnh tối thiểu | Số ảnh tối đa |
|---|---|---|---|
| **Cluster** (Informational / How-to) | < 2.000w | 2 | 3 |
| **Cluster** (Informational / How-to) | 2.000 – 3.000w | 3 | 4 |
| **Pillar** | > 3.000w | 4 | 6 |

> *Nguyên tắc chung:* Không quá **1 ảnh mỗi H2 chính**. Không chèn ảnh vào H3 trừ khi có chỉ định rõ trong outline.

### Ảnh Bắt buộc (Mandatory)

| Điều kiện | Ảnh bắt buộc | Template |
|---|---|---|
| **Mọi bài** | Ảnh bìa (cover) | `cover-template.html` |
| Bài có từ khóa dạng **"X là gì?"** | Ảnh định nghĩa (definition) | `definition-template.html` |
| Bài có H2 hướng dẫn **"Cách làm / Các bước"** | Ảnh quy trình (process) | `process-template.html` |

> Ảnh bắt buộc được tính vào giới hạn tối thiểu. Nếu bài đủ điều kiện cả definition lẫn process thì cả hai đều bắt buộc.

### Ảnh Tùy chọn (Optional — chọn theo Outline)

Sau khi xác nhận ảnh bắt buộc, Agent điền thêm ảnh tùy chọn đến khi đạt số lượng tối thiểu. Ưu tiên theo mức độ phù hợp với H2 section trong outline:

| Ưu tiên | Loại ảnh | Chọn khi |
|---|---|---|
| 1 | Mockup HVS (`mockup-template.html`) | Bài có section giới thiệu tính năng / sản phẩm HVS |
| 2 | Comparison (`comparison-template.html`) | Bài có H2 so sánh 2 khái niệm đối lập |
| 3 | Ranking (`ranking-template.html`) | Bài có H2 danh sách / Top X |
| 4 | Psychology (`psychology-template.html`) | Bài có H2 về rủi ro / tâm lý đầu tư |
| 5 | Market Data (`market-data-template.html`) | Bài có H2 về chỉ số thị trường |
| 6 | Stock Profile (`stock-profile-template.html`) | Bài `cach-mua-co-phieu-[MÃ]` |
| 7 | Timeline (`timeline-template.html`) | Bài có H2 lộ trình / chu kỳ thời gian |

### Quy trình Quyết định của Agent (Checklist)

```
1. Xác định Pillar/Cluster + Word Count Target → tra bảng giới hạn → ghi min/max
2. Liệt kê ảnh bắt buộc theo điều kiện bài viết
3. Đếm H2 trong outline → chọn ảnh tùy chọn phù hợp đến khi đạt số tối thiểu
4. Không vượt quá số ảnh tối đa — cắt ảnh ít quan trọng nhất nếu cần
5. Khai báo danh sách ảnh sẽ tạo (loại + template) trước khi bắt đầu Bước 1 workflow
```

---

## 🚫 4. Brand Safety Rules — Ảnh bị cấm tuyệt đối

> **Mục đích:** HVS Securities là công ty chứng khoán được cấp phép. Mọi ảnh tạo ra phải phản ánh sự chuyên nghiệp, minh bạch và uy tín tài chính. Bất kỳ hình ảnh nào gợi lên cờ bạc, rủi ro phi pháp hoặc đầu cơ vô trách nhiệm đều **BỊ CẤM TUYỆT ĐỐI**.

### ❌ Chủ đề & Đối tượng bị cấm

| Nhóm | Ví dụ cụ thể bị cấm |
|---|---|
| **Cờ bạc / Cá cược** | Bài poker, xúc xắc, bàn casino, roulette, slot machine, chip casino |
| **Đầu cơ rủi ro cao** | Hình ảnh "đặt cược toàn bộ", người đang "chơi lớn", ván cược cuối cùng |
| **Tiền mặt thô** | Núi tiền mặt, tờ tiền rải trên mặt bàn (gợi rửa tiền / tiền bẩn) |
| **Cảm xúc cực đoan** | Người vỡ nợ gục đầu, đập bàn vì thua lỗ, ăn mừng thái quá kiểu "trúng số" |
| **Biểu tượng may mắn / Mê tín** | Lá bùa, tứ linh, vận may phi lý trí, hình ảnh hên xui |
| **Thao túng thị trường** | Nhiều màn hình lệnh chồng chéo ám chỉ pump-dump, robot giao dịch "thần kỳ" |
| **Hình ảnh người nổi tiếng** | Bất kỳ khuôn mặt có thể nhận dạng (rủi ro pháp lý) |
| **Nội dung chính trị / Tôn giáo** | Cờ quốc gia, biểu tượng đảng phái, ký hiệu tôn giáo |

### ✅ Đối tượng thị giác được khuyến khích

- **Biểu đồ tài chính:** Candlestick chart, đường giá, volume bar, indicator kỹ thuật (RSI, MACD)
- **Màn hình app/web:** Giao diện HVS Tài chính số, bảng điện tử chứng khoán (mã VCB, VNM, HPG...)
- **Ký hiệu tài chính trừu tượng:** Đồ thị tăng trưởng, mũi tên xu hướng, biểu tượng cổ phiếu
- **Không gian làm việc chuyên nghiệp:** Màn hình phân tích, bàn làm việc hiện đại, dữ liệu số
- **Biểu tượng concept trừu tượng:** Mạng lưới kết nối, luồng dữ liệu, hình học 3D isometric

### 🔍 Self-Check bắt buộc trước khi gọi `generate_image`

Trước khi viết prompt cho `generate_image`, Agent **phải tự hỏi**:

1. **"Prompt này có thể bị AI hiểu nhầm thành ảnh cờ bạc không?"**
   - Từ nguy hiểm: *luck, bet, gamble, risk, jackpot, chips, cards, dice, wager, odds*
   - → Thay bằng: *investment, portfolio, market, growth, analysis, chart, data*

2. **"Hình ảnh này có phù hợp xuất hiện trên website của công ty chứng khoán được cấp phép không?"**
   - Test: Nếu đặt ảnh này lên website ngân hàng hay công ty tài chính, có gây phản cảm không?

3. **"Prompt có đề cập con người cụ thể, khuôn mặt, hoặc nhân vật có thể nhận dạng không?"**
   - → Thay bằng hình ảnh trừu tượng, icon, hoặc mockup giao diện

### 📝 Cấu trúc Prompt an toàn — Template bắt buộc

Mọi prompt gọi `generate_image` phải bao gồm các yếu tố sau theo thứ tự:

```
[Mô tả visual chính — phải là đối tượng tài chính/kỹ thuật]
[Phong cách: 3D isometric / glassmorphism / flat design]
[Màu sắc: deep purple #2D1F4E background, neon cyan accent, no white background]
[Loại trừ rõ ràng: no cards, no dice, no casino chips, no gambling elements, no people faces, no poker]
[Định dạng: 16:9 aspect ratio, professional financial website aesthetic]
```

**Ví dụ prompt ĐÚNG:**
```
A 3D isometric candlestick chart with glowing neon cyan bars rising upward,
floating data nodes connected by light trails, abstract financial growth concept,
deep purple #2D1F4E background, glassmorphism style,
NO gambling elements, NO cards, NO dice, NO casino, NO people,
16:9 professional financial website aesthetic
```

**Ví dụ prompt SAI** (dễ sinh ảnh casino):
```
❌ "high stakes investment visualization with chips and cards"
❌ "lucky trader winning big"
❌ "financial gamble paying off"
```

---

## ⚙️ 5. Quy trình Tạo ảnh Tự động trên Antigravity (HTML-to-Image Workflow)

Khi nhận lệnh vẽ `/draw [slug-bai-viet]`, Agent thực thi chính xác 6 bước quy chuẩn sau:

### Bước 1: Phân tích Bài viết & Ánh xạ Template
Agent quét nội dung Outline/Draft của bài viết để tự động xác định các ảnh cần vẽ và ánh xạ sang bản mẫu HTML phù hợp trong thư mục `references/`. Bảng quyết định đầy đủ:

| Loại ảnh cần tạo | Template | Điều kiện áp dụng |
|---|---|---|
| Ảnh Featured chính (H1) | `cover-template.html` | Mọi bài — ảnh bìa mặc định |
| Ảnh quy trình / hướng dẫn 3-5 bước đơn giản | `process-template.html` | Bài how-to ngắn |
| Ảnh so sánh 2 khái niệm đối lập | `comparison-template.html` | A vs B (2 lựa chọn) |
| Ảnh định nghĩa khái niệm tài chính | `definition-template.html` | Bài "X là gì?" |
| Ảnh giới thiệu app / dashboard HVS | `mockup-template.html` | Section HVS sản phẩm |
| **Ảnh nhận diện cổ phiếu cụ thể** | **`stock-profile-template.html`** | **Bài `cach-mua-co-phieu-[MÃ]`** |
| **Ảnh xếp hạng / listicle nhiều lựa chọn** | **`ranking-template.html`** | **Bài Top X, so sánh 3+ phương án** |
| **Ảnh tâm lý / cảnh báo rủi ro** | **`psychology-template.html`** | **Bài tâm lý, FOMO, stop-loss, margin** |
| **Ảnh bảng điện chỉ số thị trường** | **`market-data-template.html`** | **Bài VN-Index, S&P 500, chỉ số TG** |
| **Ảnh lộ trình thời gian / chu kỳ** | **`timeline-template.html`** | **Bài quy trình ETF, chiến lược tích sản** |

### Bước 2: Nạp Cấu hình Màu sắc động & Vẽ nền AI ngầm (AI Backdrop Fusion)
*   Agent đọc file cấu hình tại `templates/palette-config.yaml` để nhúng các mã màu đồng bộ.
*   Đối với ảnh bìa, Agent gọi công cụ `generate_image` vẽ một ảnh minh họa trừu tượng bám sát khái niệm bài viết để nạp động làm hình nền (`background-image`) bên phải trong mã HTML tạm.

### Bước 3: Biên dịch DOM linh hoạt & Ghi đè Dữ liệu (Dynamic DOM Compilation)
Agent tạo ra một file HTML tạm thời từ bản mẫu. Tại đây, Agent có thể:
*   **Đối với Quy trình:** Nhân bản thẻ `.step-card` động trong `.steps-container`. CSS Flexbox Auto-scaling sẽ tự động điều chỉnh bề ngang hoàn hảo (2, 3, 4 hoặc 5 bước).
*   **Đối với Định nghĩa:** Điều khiển ẩn/hiện (`display: none/flex`) các Widget bên phải: `#widgetBasket` (ETF/Chỉ số), `#widgetSingleStock` (Cổ phiếu cụ thể), hoặc `#widgetConceptIcon` (Khái niệm trừu tượng nhúng ảnh trong suốt từ AI).
*   Tìm và thay thế các từ khóa cổng chờ khác (tiêu đề, sapo, thông số) bằng dữ liệu thực chiến tiếng Việt của bài viết.

### Bước 4: Gọi Edge Headless chụp ảnh pixel-perfect

Kích thước output quy chuẩn:
| Loại ảnh | Kích thước | Template |
|---|---|---|
| **Ảnh bìa (cover)** | **1000 × 600 px** | `cover-template.html` |
| **Tất cả ảnh section khác** | **800 × 500 px** | Mọi template còn lại |

```powershell
# Ảnh bìa (cover-template.html)
Start-Process -FilePath "msedge" -ArgumentList "--headless", "--disable-gpu", "--virtual-time-budget=2000", "--screenshot=`"content/blog/assets/raw-images/[slug]/[ten-anh].png`"", "--window-size=1000,600", "`"file:///[duong-dan-html-tam]`"" -Wait

# Ảnh section (tất cả template khác)
Start-Process -FilePath "msedge" -ArgumentList "--headless", "--disable-gpu", "--virtual-time-budget=2000", "--screenshot=`"content/blog/assets/raw-images/[slug]/[ten-anh].png`"", "--window-size=800,500", "`"file:///[duong-dan-html-tam]`"" -Wait
```
*Lưu ý: Tham số `--virtual-time-budget=2000` là bắt buộc để trình duyệt đợi 2 giây tải xong Google Fonts tiếng Việt và ảnh nền trước khi bấm máy chụp.*

### Quy tắc đặt tên file ảnh (Bắt buộc)

Tên file ảnh phải phản ánh nội dung và ưu tiên chứa từ khóa SEO:

**Pattern:** `[keyword-chinh]-[mo-ta-ngan].[ext]`

| Loại ảnh | Ví dụ tên file |
|---|---|
| Ảnh bìa | `co-phieu-blue-chip-la-gi-cover.webp` |
| Ảnh định nghĩa | `co-phieu-blue-chip-dinh-nghia.webp` |
| Ảnh quy trình | `cach-mua-co-phieu-blue-chip-quy-trinh.webp` |
| Ảnh so sánh | `co-phieu-blue-chip-vs-penny-stock.webp` |
| Ảnh stock profile | `co-phieu-vcb-vietcombank-profile.webp` |
| Ảnh ranking | `top-co-phieu-blue-chip-viet-nam.webp` |
| Ảnh market data | `vn-index-chi-so-thi-truong.webp` |
| Ảnh psychology | `tam-ly-dau-tu-fomo-canh-bao.webp` |
| Ảnh timeline | `lo-trinh-dau-tu-chung-khoan.webp` |

**Quy tắc cụ thể:**
- Dùng slug tiếng Việt không dấu, nối bằng `-`
- Bắt đầu bằng từ khóa chính của section/bài viết
- Kết thúc bằng loại ảnh (`-cover`, `-quy-trinh`, `-so-sanh`, `-profile`...)
- Tối đa 60 ký tự (không tính extension)
- Không dùng: số thứ tự tùy ý (`img-1`, `photo-2`), tên mô tả chung chung (`featured-image`)

### Bước 5: Nén tối ưu WebP & Cập nhật Manifest
*   Chạy ngầm script Python `image_processor.py` để nén tệp PNG vừa chụp thành định dạng `.webp` chất lượng 85% siêu nhẹ cho SEO tại thư mục `content/blog/assets/images/[slug]/`.
*   Ghi nhận thông tin ảnh vừa xử lý (đường dẫn, alt text, title, kích thước thực tế) vào file manifest:
`content/blog/assets/manifests/[slug].image-manifest.json`

### Bước 6: Tự động chèn thẻ ảnh vào Bài viết
Agent tiến hành chèn thẻ ảnh trực tiếp vào bài viết Markdown tại đúng vị trí H2/H3 tương ứng:
```markdown
![[Alt Text chuẩn SEO]](file:///e:/project/hvs-company-info/content/blog/assets/images/[slug]/[keyword-chinh]-[mo-ta-ngan].webp)
*Hình 1: [Caption mô tả ảnh chuẩn xác, không AI-vibe]*
```
