---
description: "Xử lý nội dung thô (HTML/text) → chuẩn Markdown. Args: [đường dẫn file]"
allowed-tools: Read, Write, Bash
---

Xử lý nội dung thô tại: **$ARGUMENTS**

**Cách dùng:**
```
/raw content/blog/0-raw/bai-viet-thu.md
/raw content/blog/0-raw/2.md
```

Nếu `$ARGUMENTS` trống → liệt kê các file đang có trong `content/blog/0-raw/` và hỏi user chọn file nào.

---

Đọc `.antigravity/rules/raw-processing.md` để nắm đầy đủ quy trình.

1. **Đọc file** tại `$ARGUMENTS`

2. **Phân loại:**
   - HTML → strip tags, giữ cấu trúc heading
   - Plain text → normalize Markdown
   - Outline có cấu trúc (H2/H3 rõ ràng) → route sang `1-outlines/`

3. **Inference metadata** từ nội dung:
   - `Target_Keyword` từ H1 / tiêu đề chính
   - `Persona` dựa trên `resources/audience/`

4. **Lưu:**
   - Bài đầy đủ → `content/blog/0-raw/Raw-[slug].md` (Status: Processed)
   - Outline có cấu trúc → `content/blog/1-outlines/Outline-[slug].md`

5. **Cập nhật** `seo-strategy/content-plan/progress-log.md` — thêm vào Active Pipeline

6. **Cập nhật** `seo-strategy/content-plan/topic-clusters.md` (nếu tồn tại):
   - Tìm dòng khớp keyword → đổi ⭕ → 🔄 In Progress, ghi tên file

7. **Báo cáo:** file lưu ở đâu, bước tiếp theo nên dùng `/optimize` hay `/approve`
