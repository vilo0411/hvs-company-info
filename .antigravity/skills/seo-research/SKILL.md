---
name: SEO SERP Research & Analysis
description: Cào dữ liệu đối thủ tại Phase 1. Kích hoạt bởi lệnh `/detailed` hoặc `/optimize`.
---
# Skill: SEO SERP Research & Analysis

Kỹ năng này cho phép Agent thực hiện nghiên cứu chuyên sâu về đối thủ cạnh tranh trên công cụ tìm kiếm và trả về dữ liệu cấu trúc sạch.

---

## 🛠️ Công cụ sử dụng
- `search_web`: Tìm kiếm URL.
- `read_url_content`: Đọc nội dung thô (Ưu tiên).
- `read_browser_page`: Dùng khi gặp trang web chặn bot hoặc yêu cầu Render JS.

---

## 📝 Định dạng Output (Standardized Context Snippet)

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
    {
      "url": "link đối thủ",
      "headings": ["H1", "H2", "H3..."]
    }
  ],
  "gaps": ["Các điểm đối thủ chưa nói tới hoặc nói sơ sài"]
}
```

---

## 🛡️ Chiến lược xử lý lỗi (Exception Handling)

1.  **Chặn Scraping:** Nếu gặp 403/429, tự động thử lại bằng `read_browser_page`.
2.  **Trang web quá dài:** Chỉ lấy nội dung chính trong thẻ `<article>` hoặc `main`, bỏ qua Header/Footer để tiết kiệm token.
3.  **Không có kết quả:** Nếu không tìm thấy đối thủ phù hợp, báo cáo lại cho Main Agent để sử dụng kiến thức nội tại nhưng kèm cảnh báo "No SERP Data".

---

## 🚀 Cách kích hoạt
Skill này thường được gọi bởi **SEO Collector** trong giai đoạn nghiên cứu ban đầu của lệnh `/detailed` hoặc `/optimize`.
