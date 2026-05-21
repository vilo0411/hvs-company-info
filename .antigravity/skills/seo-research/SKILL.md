---
name: SEO SERP Research & Analysis
description: Cào dữ liệu đối thủ và phân tích chiến lược nội dung. Kích hoạt bởi SEO & Strategy Collector trong luồng /write.
---
# Skill: SEO SERP Research & Analysis

Kỹ năng này cho phép Agent thực hiện nghiên cứu chuyên sâu về đối thủ cạnh tranh trên công cụ tìm kiếm, phân tích mạch logic (Narrative Flow) và đề xuất cấu trúc bài viết linh hoạt.

---

## Công cụ sử dụng
- `WebSearch`: Tìm kiếm URL.
- `WebFetch`: Đọc nội dung trang (Ưu tiên).
- Fallback: thử lại với approach khác khi gặp trang chặn bot.

---

## Định dạng Output (Standardized Context Snippet)

Mọi kết quả trả về phải tuân thủ cấu trúc sau để Main Agent có thể đọc và viết bài tự động:

```json
{
  "keyword": "từ khóa mục tiêu",
  "intent": {
    "primary": "Informational/Commercial/...",
    "secondary": ["intent 1", "intent 2"],
    "deep_pain_point": "Nỗi đau thực sự user muốn giải quyết là gì?"
  },
  "competitor_analysis": [
    {
      "url": "link đối thủ top 1",
      "narrative_flow": "Mạch logic của bài viết này là gì? (Ví dụ: Định nghĩa -> Phân loại -> So sánh -> Ví dụ -> CTA)",
      "gaps": "Phần nào họ nói hời hợt hoặc bỏ sót?"
    }
  ],
  "entities": ["Thực thể quan trọng trong ngành", "LSI Keywords"],
  "recommended_unique_structure": [
    {
      "heading": "H2: [Tên heading gợi ý]",
      "focus": "Trọng tâm cần viết (Ví dụ: Giải thích trực diện khái niệm, dùng ví dụ VCB)",
      "is_hvs_bridge": false
    },
    {
      "heading": "H2: [Tên heading lồng ghép HVS]",
      "focus": "Điểm chạm để giới thiệu HVS Demo hoặc giải pháp",
      "is_hvs_bridge": true
    }
  ]
}
```

---

## Xử lý lỗi

1. **403/429:** Thử lại với approach khác trước khi bỏ qua URL.
2. **Trang quá dài:** Chỉ lấy nội dung trong `<article>` hoặc `<main>`, bỏ Header/Footer để tiết kiệm token.
3. **Không tìm được đối thủ:** Báo cáo "No SERP Data" cho Main Agent — không bịa thông tin.

## Kích hoạt

Skill này được gọi bởi **SEO & Strategy Collector** tại Phase 1 của `/write` (khi có SERP research).
