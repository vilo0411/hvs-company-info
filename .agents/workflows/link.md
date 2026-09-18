---
description: "Gắn internal links cho bài đang viết với nhiều chế độ: Cluster, Silo, Power, Conversion"
---

Chạy quy trình **Internal Linking** để tối ưu SEO và trải nghiệm người dùng.

**Cách dùng:**
```
/link [mode]
```

**Các chế độ (Modes):**
- `--cluster` (Mặc định): Liên kết Pillar ↔ Cluster trong cùng một nhóm chủ đề.
- `--silo`: Liên kết dọc và ngang trong cùng một Category lớn (Group).
- `--power`: Tập trung đẩy link về các trang "Super Pillar" có authority cao.
- `--conversion`: Ưu tiên link về sản phẩm/dịch vụ của HVS (Thực tập số, khóa học).

### Quy trình thực hiện:

**Bước 1 — Xác định Mode**
Nếu không chỉ định, mặc định dùng `--cluster`.

**Bước 2 — Xác định vị trí bài viết trong Topic Cluster**
Đọc `seo-strategy/content-plan/topic-clusters.md` để biết bài hiện tại thuộc Cluster nào.

**Bước 3 — Tra cứu URL từ Anchor Index (nguồn chính)**
Đọc `seo-strategy/content-plan/anchor-index.md`:
- Tìm Cluster của bài hiện tại
- **Chỉ dùng URL có dấu ✅** — TUYỆT ĐỐI không dùng URL có dấu ⚠️ (chưa live)
- BẮT BUỘC dùng URL tuyệt đối `https://taichinhso.hvsvn.com/...`
- KHÔNG dùng `Final-xxx.md`, `file://` hay đường dẫn tương đối

> **Lưu ý cấu trúc URL:** Site có 2 loại path khác nhau:
> - Bài đầu tư / chứng khoán: `/dau-tu/danh-cho-nguoi-moi-bat-dau/[slug]`
> - Bài kinh tế vĩ mô: `/kinh-te-vi-mo/[category]/[slug]`
> Chọn đúng URL theo anchor-index, không tự suy diễn slug.

Nếu bài cần link chưa có trong anchor-index, chạy lệnh tra cứu:
```
python .antigravity/scripts/fetch_sitemap.py --suggest "[từ khóa]"
```

**Bước 4 — Đề xuất links theo Mode**

Trình bày theo format sau (chờ user xác nhận trước khi chèn):

```
🚀 MODE: [Tên mode]

🏛️ PRIMARY LINKS (Cùng Cluster):
  - "[anchor text]" → https://taichinhso.hvsvn.com/...
  - "[anchor text]" → https://taichinhso.hvsvn.com/...

🛰️ SECONDARY LINKS (Cross-Cluster):
  - "[anchor text]" → https://taichinhso.hvsvn.com/...

🎁 CONVERSION LINK:
  - "[anchor text]" → https://taichinhso.hvsvn.com/thuc-tap-so/NHA-PHAN-TICH (hoặc NHA-TU-VAN / EXCEL-* / thuc-tap-so tùy ngữ cảnh bài)

📊 Tổng: [N] links | Tất cả đã xác nhận ✅ trong anchor-index
```

**Bước 5 — Chờ user xác nhận → Chèn link**
- Chèn inline với anchor text ngữ nghĩa tự nhiên (BẮT BUỘC dùng Partial Match / Semantic từ `anchor-index.md`; TUYỆT ĐỐI KHÔNG dùng gượng ép đuôi "là gì" trong câu văn prose).
- Không dùng anchor text "AI-vibe" (xem `anti-ai-rules.md`).

**Bước 6 — Validate sau khi chèn**
```
python .antigravity/scripts/fetch_sitemap.py --validate [đường_dẫn_file]
```
Xác nhận output: `0 broken links | 0 URL not in sitemap`.

---

### Khi Sitemap có bài mới (Append vào Anchor Index)

Khi đăng bài mới lên site và cần cập nhật anchor-index:

1. Crawl sitemap để lấy URL mới:
   ```
   python .antigravity/scripts/fetch_sitemap.py --suggest "[slug bài mới]"
   ```
2. Xác nhận URL thực trả về, map với file `Final-xxx.md` tương ứng
3. Trong `anchor-index.md`, tìm dòng `⚠️ Final-xxx.md` và thay bằng `✅ https://taichinhso.hvsvn.com/...`
4. Nếu bài hoàn toàn mới (chưa có trong index), append vào đúng Cluster

---

### Ràng buộc Bất biến

- Mỗi URL đích chỉ xuất hiện **đúng 1 lần** trong toàn bài
- 100% URL phải có dấu ✅ trong `anchor-index.md` hoặc tồn tại trong sitemap.xml
- Anchor text phải tự nhiên, không dùng các từ "AI-vibe" (xem `anti-ai-rules.md`)
- Mỗi bài: **3–6 internal links** (1 conversion + 2–3 cùng cluster + 1–2 cross-cluster)
