---
description: "Xử lý nội dung thô (HTML/text) → chuẩn Markdown. Args: [đường dẫn file]"
---

Xử lý nội dung thô.

**Cách dùng:**
```
/raw content/blog/0-raw/bai-viet-thu.md
/raw content/blog/0-raw/2.md
```

Nếu không có args → liệt kê files trong `content/blog/0-raw/` và hỏi chọn file nào.

Đọc `.antigravity/rules/raw-processing.md` để nắm toàn bộ quy trình.

1. **Đọc file** nguồn
2. **Phân loại:** HTML / plain text / outline có cấu trúc
3. **Strip + normalize** → chuẩn Markdown
4. **Inference YAML:** Target_Keyword, Persona
5. **Lưu:**
   - Bài đầy đủ → `content/blog/0-raw/Raw-[slug].md`
   - Outline → `content/blog/1-outlines/Outline-[slug].md`
6. **Cập nhật** `progress-log.md` — thêm vào Active Pipeline
7. **Cập nhật** `topic-clusters.md` (nếu có) — ⭕ → 🔄, ghi tên file
8. **Báo cáo:** file lưu ở đâu, bước tiếp nên dùng `/optimize` hay `/approve`
