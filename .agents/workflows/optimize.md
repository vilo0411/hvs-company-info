---
description: "Tối ưu bài viết cũ (anti-AI + SEO + linking). Args: [đường dẫn file]"
---

Tối ưu bài viết.

**Cách dùng:**
```
/optimize content/blog/3-finalized/Final-chung-khoan-la-gi.md
/optimize content/blog/2-user-review/Draft-co-phieu-penny-la-gi.md
```

Nếu không có args → hỏi user đường dẫn file cần tối ưu.

Đọc `.antigravity/rules/content-optimization.md` để nắm toàn bộ quy trình.

1. **Phân tích hiện trạng:** Đọc nội dung file + `anti-ai-rules.md`

2. **Brand Guardian (Sub-Agent)** (`.antigravity/agents/brand-guardian.md`):
   - Liệt kê câu/đoạn "AI-vibe" cần sửa (kèm số dòng)
   - Điểm thiếu HVS USPs
   - Đề xuất Persona / tone phù hợp hơn

3. **Rewrite:** Sửa AI-vibe, lồng ghép HVS products tự nhiên, điều chỉnh tone

4. **QA/QC** → loop đến PASS

5. **Internal Linking**

6. **Lưu** `content/blog/2-user-review/Draft-[slug].md` → trình bày → chờ `/approve`
