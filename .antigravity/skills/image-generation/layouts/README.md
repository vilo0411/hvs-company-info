# Layout System — HVS Image Templates

## Cấu trúc thư mục

```
layouts/
├── layout-1-split/          ← 60% dark panel | 40% company photo
├── layout-2-fullbleed/      ← Photo phủ toàn canvas, text overlay
├── layout-3-editorial/      ← Photo strip trên, data bar dưới
└── layout-4-brutalist/      ← Dark grid trái, raw photo phải + glass cards
```

## Mô tả từng layout

### Layout 1 — Split Panel
- **Cấu trúc:** Left 60% dark | Right 40% company photo
- **Đặc điểm:** Classic, dễ đọc nhất, cân bằng text/visual
- **Phù hợp:** Stock profile, Definition, Comparison

### Layout 2 — Full Bleed Magazine
- **Cấu trúc:** Photo phủ toàn 1000×562, gradient overlay đậm bên trái
- **Đặc điểm:** Dramatic nhất, giống magazine/editorial cover
- **Phù hợp:** Featured article cover, Stock profile nổi bật

### Layout 3 — Editorial Top Strip
- **Cấu trúc:** Photo top 58%, Dark data bar bottom 42%
- **Đặc điểm:** Sạch nhất, phong cách Bloomberg/Reuters news card
- **Phù hợp:** Market data, Stock news, Timeline

### Layout 4 — Brutalist Dark + Photo
- **Cấu trúc:** Left 45% dark với subtle grid | Right 55% raw photo + glass cards
- **Đặc điểm:** Modern nhất, ảnh lộ nhiều nhất, premium feeling
- **Phù hợp:** Stock profile, Psychology, Ranking

---

## Template types (sẽ bổ sung theo layout)

Mỗi layout folder sẽ chứa các file template tương ứng:

| File | Mô tả | Status |
|---|---|---|
| `stock-profile.html` | Hồ sơ cổ phiếu (mã, ngành, thông số) | ✅ Done |
| `definition.html` | Định nghĩa thuật ngữ tài chính | 🔜 Planned |
| `comparison.html` | So sánh 2-3 cổ phiếu hoặc sản phẩm | 🔜 Planned |

---

## Convention — CỔNG CHỜ

Tất cả template dùng comment `<!-- CỔNG CHỜ: ... -->` để đánh dấu các điểm agent cần điều chỉnh khi generate ảnh cụ thể.

**Ảnh công ty:** `assets/company-photos/[MÃ].png`
- Ví dụ: `POW.png`, `VCB.png`, `FPT.png`
- Nếu chưa có: generate bằng `generate_image` tool rồi lưu vào folder này

**Industry accent color:**
```
Ngân hàng/TC  → #2196F3
Điện/NL       → #FFD600
BĐS           → #FF7043
Thép/VL       → #78909C
Công nghệ     → #7C4DFF
Tiêu dùng     → #66BB6A
Dầu khí       → #FFA726
Dược phẩm     → #26C6DA
```
