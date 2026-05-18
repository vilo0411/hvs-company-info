---
name: SEO SERP Research & Analysis
description: Cào dữ liệu đối thủ tại Phase 1. Kích hoạt bởi SEO Collector Agent trong luồng /write (có SERP).
---
# Skill: SEO SERP Research & Analysis

Kỹ năng này cho phép Agent thực hiện nghiên cứu chuyên sâu về đối thủ cạnh tranh trên công cụ tìm kiếm và trả về dữ liệu cấu trúc sạch.

---

## Công cụ sử dụng
- `WebSearch`: Tìm kiếm URL.
- `WebFetch`: Đọc nội dung trang (Ưu tiên).
- Fallback: thử lại với approach khác khi gặp trang chặn bot.

---

## Định dạng Output (Standardized Context Snippet)

Mọi kết quả trả về phải tuân thủ cấu trúc sau để Main Agent có thể đọc tự động:

```json
{
  "keyword": "từ khóa mục tiêu",
  "intent": {
    "primary": "Informational/Commercial/...",
    "secondary": ["intent 1", "intent 2"]
  },
  "archetype": "Loại bài viết (Guide, News, ...)",
  "style": "Văn phong (Chuyên nghiệp, Gần gũi, ...)",
  "competitor_outline": [
    { "url": "link đối thủ", "headings": ["H1", "H2", "H3..."] }
  ],
  "paa": ["Câu hỏi People Also Ask"],
  "entities": ["Thực thể quan trọng trong ngành"],
  "lexicon": ["Thuật ngữ chuyên môn từ nguồn uy tín"],
  "gaps": ["Các điểm đối thủ chưa nói tới hoặc nói sơ sài"]
}
```

---

## Xử lý lỗi

1. **403/429:** Thử lại với approach khác trước khi bỏ qua URL.
2. **Trang quá dài:** Chỉ lấy nội dung trong `<article>` hoặc `<main>`, bỏ Header/Footer để tiết kiệm token.
3. **Không tìm được đối thủ:** Báo cáo "No SERP Data" cho Main Agent — không bịa thông tin.

## Kích hoạt

Skill này được gọi bởi **SEO Collector Agent** tại Phase 1 của `/write` (khi có SERP research).
