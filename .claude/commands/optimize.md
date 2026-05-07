---
description: "Tối ưu bài viết cũ (anti-AI + SEO + linking). Args: [đường dẫn file] — vd: content/blog/3-finalized/Final-chung-khoan-la-gi.md"
allowed-tools: Read, Write, Bash, Agent
---

Tối ưu bài viết tại: **$ARGUMENTS**

**Cách dùng:**
```
/optimize content/blog/3-finalized/Final-chung-khoan-la-gi.md
/optimize content/blog/2-user-review/Draft-co-phieu-penny-la-gi.md
```

Nếu `$ARGUMENTS` trống → hỏi user đường dẫn file cần tối ưu.

---

Đọc `.antigravity/rules/content-optimization.md` để nắm toàn bộ quy trình.

1. **Phân tích hiện trạng:** Đọc nội dung tại `$ARGUMENTS` + đọc `seo-strategy/resources/content-strategy/anti-ai-rules.md`

2. **Brand Guardian (Sub-Agent):** Spawn sub-agent theo `.antigravity/agents/brand-guardian.md` → trả về:
   - Danh sách câu/đoạn "AI-vibe" cần sửa (kèm số dòng)
   - Điểm thiếu HVS USPs
   - Đề xuất Persona / tone phù hợp hơn

3. **Rewrite:** Sửa bài theo Brand Guardian report — viết lại AI-vibe, lồng ghép HVS products tự nhiên, điều chỉnh tone

4. **QA/QC:** Chạy `.antigravity/skills/qa-qc/SKILL.md` → loop đến khi PASS

5. **Internal Linking:** Chạy `.antigravity/skills/internal-linking/SKILL.md`

6. **Lưu:** `content/blog/2-user-review/Draft-[slug].md` (Status: Draft)

7. **Trình bày** bản đã tối ưu, highlight thay đổi chính. Chờ `/approve` để finalize.
