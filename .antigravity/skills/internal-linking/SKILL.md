---
name: Internal Linking
description: Gắn internal links theo cấu trúc Link Wheel — bài mới link đến bài cùng cluster + pillar. Sử dụng bộ Anchor Index đã duyệt.
---

# Skill: Internal Linking

## Triết lý: Link Wheel

Mỗi bài viết mới khi publish phải tạo thành một "bánh xe":
- **Spoke → Hub:** Bài cluster link lên Pillar của cluster đó.
- **Spoke → Spoke:** Bài cluster link đến 2-3 bài Published cùng cluster (bài cũ hơn hoặc liên quan nhất).
- **KHÔNG link ngẫu nhiên** sang các cluster khác trừ khi có liên kết chủ đề tự nhiên.

---

## Nguyên tắc Anchor Text (HVS Standard)

1. **Exact Match (Chính xác):** Trùng 100% từ khóa chính của bài đích. Tối đa 15% tổng số link trỏ về bài đó.
2. **Partial Match (Bổ trợ/Semantic):** Dùng các cụm từ biến thể trong `anchor-index.md`. Ưu tiên hàng đầu (65%+).

**Cấm:** 
- Dùng anchor generic như "tại đây", "xem thêm", "đọc thêm".
- Ép các từ khóa có đuôi câu hỏi như "là gì" vào ngữ cảnh chạy của câu làm mất tự nhiên (ví dụ: "lạm dụng [margin là gì]"). 
- **Giải pháp:** Nếu liên kết chèn inline vào câu, bắt buộc phải dùng Partial Match tự nhiên (ví dụ: "lạm dụng [đòn bẩy margin]") hoặc viết lại câu rõ ràng (ví dụ: "tham khảo bài viết [margin là gì] để...").

---

## Nguồn dữ liệu (theo thứ tự ưu tiên)

1. **Sitemap Live (`https://taichinhso.hvsvn.com/sitemap.xml`) / Sitemap Cache (`.antigravity/scripts/sitemap-cache.json`)** — **Nguồn chân lý duy nhất (Single Source of Truth)** cho toàn bộ URL đích. Đảm bảo mọi URL được gắn đều đang live 100% trên website.
2. **`seo-strategy/content-plan/topic-clusters.md`** — Xác định cluster, pillar, và toàn bộ bài Published trong cùng nhóm.
3. **`seo-strategy/content-plan/anchor-index.md`** — Tra Exact/Partial anchor text được duyệt cho từng bài đích.
4. **`seo-strategy/content-plan/internal-link-dashboard.md`** — Kiểm tra mật độ link hiện tại (tránh Over-opt).

> ⚠️ **TUYỆT ĐỐI KHÔNG TỰ ĐOÁN URL.** Site có nhiều path khác nhau (`/kinh-te-vi-mo/chinh-sach-tai-khoa/`, `/dau-tu/danh-cho-nguoi-moi-bat-dau/`, `/kinh-te-vi-mo/chinh-sach-tien-te/`, v.v.). Bắt buộc phải tra sitemap hoặc dùng công cụ tìm kiếm link để lấy URL chuẩn xác.

---

## Quy trình thực hiện

### Bước 1 — Xác định Cluster của bài đang viết

Đọc `topic-clusters.md`. Tìm bài hiện tại theo keyword hoặc slug. Xác định:
- **Cluster name** bài thuộc về
- **Pillar** của cluster đó (và file Final tương ứng)
- **Danh sách bài Published (✅)** trong cùng cluster (loại bỏ bài hiện tại)

### Bước 2 — Chọn target links & Gợi ý từ Sitemap

| Loại link | Số lượng | Ưu tiên chọn |
| :--- | :--- | :--- |
| **Spoke → Hub (Pillar)** | 1 bắt buộc | Luôn link lên Pillar, dù đã có nhiều link |
| **Spoke → Spoke (Cluster siblings)** | 2-4 bài | Ưu tiên bài có nội dung liên quan trực tiếp với section đang viết |
| **Cross-cluster** | 0-1 bài | Chỉ khi có liên kết chủ đề thực sự (không cố ép) |

**Nếu cluster có ít hơn 3 bài Published:** Link hết tất cả Published, không bắt buộc đủ số.

### Bước 3 — Tra cứu Anchor text

Với mỗi bài đích đã chọn, tra `anchor-index.md`:
- Lấy Partial Match phù hợp ngữ cảnh nhất → dùng trước
- Dùng Exact Match nếu không tìm được Partial Match tự nhiên
- Kiểm tra Dashboard: bài đích đang `⚠️ Over-opt` → chỉ dùng Partial Match

### Bước 4 — Tra cứu & Gợi ý URL từ Sitemap (`fetch_sitemap.py`)

**BẮT BUỘC** tra cứu URL chính xác từ sitemap trước khi gắn link. Dùng các lệnh sau:

```powershell
# 1. Gợi ý link theo từ khóa hoặc chủ đề:
python .antigravity/scripts/fetch_sitemap.py --suggest "dxy"
python .antigravity/scripts/fetch_sitemap.py --search "chứng khoán phái sinh"

# 2. Tra cứu URL chính xác theo 1 slug cụ thể:
python .antigravity/scripts/fetch_sitemap.py --slug chung-khoan-phai-sinh-la-gi

# 3. Refresh cache sitemap từ live site (tự động tải https://taichinhso.hvsvn.com/sitemap.xml):
python .antigravity/scripts/fetch_sitemap.py --refresh
```

Ví dụ tra cứu:
```
# Input:
python .antigravity/scripts/fetch_sitemap.py --slug chi-so-dxy-la-gi

# Output:
Slug: chi-so-dxy-la-gi
URL:  https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/chi-so-dxy-la-gi
```

Sau khi có URL, mới thực hiện gắn link contextual. Nếu slug hoặc từ khóa **KHÔNG TÌM THẤY** trong sitemap → bài chưa publish → **tuyệt đối không được gắn link markdown**, chỉ giữ dạng text thuần và ghi chú lại cho backfill sau khi publish.

### Bước 5 — Kiểm tra Ratio & Xung đột

- Nếu bài đích đang `⚠️ Over-opt`: không dùng Exact Match.
- **Pruning rule:** Nếu keyword của bài MỚI trùng với Partial Match đang dùng ở bài cũ → đề xuất xóa Partial Match đó ở bài cũ (để tránh keyword cannibalization).

### Bước 6 — Kiểm tra Hợp lệ Tự động (Validation)

Chạy script validate để đảm bảo 100% internal links trong bài viết đều tồn tại trên sitemap:

```powershell
python .antigravity/scripts/fetch_sitemap.py --validate content/blog/2-user-review/Draft-[slug].md
```

### Bước 7 — Trình bày kết quả

```
🔗 LINK WHEEL — BÀI: [Tên bài]
📍 CLUSTER: [Tên cluster] | PILLAR: [Tên pillar]

📝 ĐỀ XUẤT LINK (ĐÃ XÁC THỰC SITEMAP):

1. [Pillar] → [Bài đích] ([Loại: Exact/Partial])
   - Đoạn gốc: "..."
   - Đoạn sửa:  "... [Anchor Text](https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/[slug]) ..."

2. [Spoke] → [Bài đích] ([Loại: Exact/Partial])
   - Đoạn gốc: "..."
   - Đoạn sửa:  "... [Anchor Text](https://taichinhso.hvsvn.com/dau-tu/danh-cho-nguoi-moi-bat-dau/[slug]) ..."
```

---

## Chế độ --backfill [slug]

Khi chạy `--backfill [slug]`:
1. Tìm cluster của bài `[slug]` vừa publish.
2. Quét toàn bộ bài Published cùng cluster → tìm đoạn có thể chèn link ngược về `[slug]`.
3. Đề xuất sửa từng bài cũ để chúng link về bài mới — hoàn tất vòng tròn link wheel.

---

## Ràng buộc Bất biến

- Mỗi bài đích chỉ xuất hiện **đúng 1 lần** trong toàn bài.
- Đường dẫn link dùng **URL tuyệt đối** lấy từ sitemap — **không tự đoán path**.
- **Tuyệt đối cấm** sử dụng link dạng `file://`, đường dẫn tương đối, hoặc `Final-*.md`.
- Chỉ link đến URL **có trong sitemap** (bài đã publish). Bài chưa có trong sitemap → bỏ qua, ghi chú backfill.
- Không chiếm anchor text là keyword của bài Planned trong `topic-clusters.md`.
- Tổng số internal link trong 1 bài: **3-6 link** (dưới 3 là thiếu, trên 6 là spam).
- **Refresh cache** mỗi khi publish bài mới: `python .antigravity/scripts/fetch_sitemap.py --refresh`
