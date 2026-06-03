# AGENT-GUIDE — Image Generation Templates

> Đây là tài liệu quyết định duy nhất cho agent chọn template và layout.
> Đọc file này TRƯỚC khi chọn bất kỳ template nào.

---

## 1. Bảng quyết định nhanh

Tất cả file template nằm trong thư mục này (`references/`). Không còn thư mục `layouts/` riêng.

### 1a. Template mặc định (không cần chọn layout)

| Loại bài / Section | File |
|---|---|
| So sánh 2 sản phẩm / khái niệm | `comparison-template.html` |
| Dashboard dữ liệu thị trường / chỉ số | `market-data-template.html` |
| Bài tâm lý / bẫy đầu tư | `psychology-template.html` |
| Top N / Xếp hạng / Danh sách chọn lọc | `ranking-template.html` |
| Lộ trình / Timeline / Chu kỳ | `timeline-template.html` |
| Hướng dẫn từng bước (how-to) | `process-template.html` |
| Ảnh bìa / Featured image bài viết | `cover-template.html` |
| Demo UI app / Mockup sản phẩm | `mockup-template.html` |

### 1b. Stock Profile — chọn theo phong cách

| Phong cách | File | Khi nào dùng |
|---|---|---|
| Split (classic) — **mặc định** | `stock-profile-template.html` | Hầu hết các bài |
| Fullbleed (dramatic) | `stock-profile-fullbleed.html` | Bài hero / mã CP lớn (VCB, VNM, FPT) |
| Editorial (Bloomberg) | `stock-profile-editorial.html` | Bài phong cách news card |
| Brutalist (premium) | `stock-profile-brutalist.html` | Bài muốn ảnh lộ nhiều nhất |

### 1c. Definition — chọn theo tone và visual

| Tone / Visual | File | Khi nào dùng |
|---|---|---|
| Dark split — **mặc định** | `definition-template.html` | Hầu hết thuật ngữ |
| Dark fullbleed | `definition-fullbleed.html` | Khi có ảnh concept mạnh |
| Dark editorial | `definition-editorial.html` | Khi ảnh quan trọng hơn text |
| Dark brutalist | `definition-brutalist.html` | Visual đối lập text/ảnh tối giản |
| Light fullbleed | `definition-light.html` | Bài nhập môn / đối tượng mới bắt đầu |

---

## 2. Quy tắc chọn Visual Mode

Mỗi template hỗ trợ **photo-mode** hoặc **icon-mode**. Chọn theo bảng:

| Template | Mặc định | Có thể dùng photo? | Điều kiện |
|---|---|---|---|
| `stock-profile` | **photo-required** | ✅ Bắt buộc | File ảnh tại `assets/company-photos/[MÃ].png` |
| `cover` | **photo-required** | ✅ Bắt buộc | Ảnh nền AI-generated hoặc Unsplash |
| `definition` | **icon-mode** | ✅ Tùy chọn | Dùng `.widget-concept-icon` khi có ảnh concept |
| `psychology` | **icon-mode** | ❌ Không dùng | Visual trừu tượng phù hợp hơn cho chủ đề cảm xúc |
| `comparison` | **icon-mode** | ❌ Không dùng | Color-split đủ visual weight |
| `market-data` | **data-only** | ❌ Không cần | Data grid tự là visual |
| `ranking` | **data-only** | ❌ Không cần | List structure tự là visual |
| `timeline` | **icon-mode** | ❌ Không cần | SVG timeline đủ visual |
| `process` | **icon-mode** | ❌ Không cần | Step icons đủ visual |
| `mockup` | **screenshot** | ✅ Tùy chọn | Screenshot UI thực tế nếu có |

---

## 3. Quy tắc CỔNG CHỜ

Tất cả điểm agent cần thay nội dung đều được đánh dấu bằng comment:

```html
<!-- CỔNG CHỜ: [mô tả ngắn] -->
```

**Quy trình làm việc với template:**
1. Mở file template → Ctrl+F tìm `CỔNG CHỜ`
2. Thay nội dung tại từng điểm theo chỉ dẫn trong comment
3. Không xóa CSS class hay thay đổi cấu trúc HTML
4. Chỉ chỉnh `src`, text content, và màu inline style khi cần

---

## 4. Industry Accent Colors

Dùng cho `stock-profile-template.html` → biến `--industry-accent`:

```
Ngân hàng / Tài chính  → #2196F3  (xanh dương)
Điện / Năng lượng       → #FFD600  (vàng)
Bất động sản            → #FF7043  (cam đỏ)
Thép / Vật liệu         → #78909C  (xám xanh)
Công nghệ               → #7C4DFF  (tím)
Tiêu dùng               → #66BB6A  (xanh lá)
Dầu khí                 → #FFA726  (cam vàng)
Dược phẩm               → #26C6DA  (xanh ngọc)
```

---

## 5. Kích thước và định dạng output

- **Canvas:** 1000 × 562 px (tỷ lệ 16:9)
- **Font:** Plus Jakarta Sans (load qua Google Fonts)
- **Export:** Screenshot toàn bộ `.template-container`, không bao gồm `<body>`
- **Tên file output:** `[slug-bài-viết]-[loại].png`
  - Ví dụ: `etf-la-gi-definition.png`, `pow-stock-profile.png`

---

## 6. Quy trình tạo ảnh (tóm tắt)

```
1. Đọc H2/H3 section cần ảnh → xác định loại nội dung
2. Tra bảng quyết định (mục 1) → chọn template + layout
3. Mở template → thay tất cả CỔNG CHỜ
4. Screenshot → lưu vào content/blog/[slug]/images/
5. Gắn vào bài viết tại đúng vị trí section
```
