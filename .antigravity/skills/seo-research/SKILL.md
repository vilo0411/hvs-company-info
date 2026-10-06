---
name: SEO SERP Research & Analysis
description: Cào dữ liệu đối thủ và phân tích chiến lược nội dung. Kích hoạt bởi SEO & Strategy Collector trong luồng /write.
---
# Skill: SEO SERP Research & Analysis

Kỹ năng này cho phép Agent thực hiện nghiên cứu chuyên sâu về đối thủ cạnh tranh trên công cụ tìm kiếm, phân tích mạch logic (Narrative Flow) và đề xuất cấu trúc bài viết linh hoạt.

---

## Công cụ sử dụng (theo thứ tự)

1. **`python .antigravity/skills/seo-research/scripts/serp_research.py "<keyword>" --top 10 --extract 5`** — DataForSEO (Google VN, tiếng Việt): top 10, PAA (+ nguồn Google đang lấy), Featured Snippet, Related Searches, extract 5 đối thủ (parser local, Jina fallback). **Có phí ~$0.002/kw**, cache 30 ngày `seo-strategy/raw/serp/`. Không `--no-cache`. Keyword ngoài topic-clusters/backlog → script từ chối (cần `--force`, hỏi user). `--paa-depth N` tốn thêm, chỉ cho pillar.
2. **Fallback** (thiếu key / lỗi): `WebSearch` keyword → top 5 URL → `WebFetch` (lấy `<article>`/`<main>`). Cùng format output.
3. `python .antigravity/skills/seo-research/scripts/scrape.py <url…>` — Firecrawl cho trang chặn bot (cần key).
4. `python scripts/serp_opportunities.py` — gom PAA/Related từ cache (0 API call) → `seo-strategy/content-plan/serp-opportunities.md` cho `/keyword-plan`.

Key: `.antigravity/config/api-keys.md` (copy từ `api-keys.example.md`) hoặc `.env`.

---

## Định dạng Output (Standardized Context Snippet)

Mọi kết quả trả về phải tuân thủ cấu trúc sau để Main Agent có thể đọc và viết bài tự động:

```json
{
  "keyword": "từ khóa mục tiêu",
  "word_count_target": 2000,
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
  "entities_gap_analysis": ["Thực thể đối thủ bỏ sót — đưa vào Outline YAML Entities_Gap_Analysis"],
  "paa_questions": [
    {"q": "Câu hỏi PAA", "placement": "body | faq", "google_source": "domain đang được Google lấy đáp án", "priority_gap": true}
  ],
  "related_searches": {"same_intent": ["…"], "spin_off": ["…"]},
  "featured_snippet": {"type": "Paragraph | List | Table | None", "current_owner": "domain"},
  "word_count_benchmark": {"min": 900, "median": 1400, "max": 2100},
  "recommended_unique_structure": [
    {
      "heading": "H2: [Tên heading gợi ý]",
      "focus": "Trọng tâm cần viết (Ví dụ: Giải thích trực diện khái niệm, dùng ví dụ VCB)",
      "is_hvs_bridge": false
    },
    {
      "heading": "H2: [Tên heading lồng ghép HVS]",
      "focus": "Nỗi đau → lộ trình HVS Thực tập số (Demo/Forum hỗ trợ)",
      "is_hvs_bridge": true
    }
  ]
}
```

*`word_count_target`:* lấy từ `word_count_benchmark` (median đối thủ, làm tròn lên) đối chiếu bảng độ dài theo loại bài ở `.antigravity/rules/seo-formatting.md §3`. Không dùng 1 con số mặc định.

---

## Xử lý lỗi

1. **403/429:** Thử lại với approach khác trước khi bỏ qua URL.
2. **Trang quá dài:** Chỉ lấy nội dung trong `<article>` hoặc `<main>`, bỏ Header/Footer để tiết kiệm token.
3. **Không tìm được đối thủ:** Báo cáo "No SERP Data" cho Main Agent — không bịa thông tin.

## Kích hoạt

Skill này được gọi bởi **SEO & Strategy Collector** tại Phase 1 của `/write` (khi có SERP research).
