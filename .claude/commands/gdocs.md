---
description: "Xuất bài Finalized lên Google Docs. Args: [đường dẫn file] — vd: content/blog/3-finalized/Final-chung-khoan-la-gi.md"
allowed-tools: Read, Bash, mcp__claude_ai_Google_Drive__authenticate, mcp__claude_ai_Google_Drive__complete_authentication
---

Xuất bài lên Google Docs: **$ARGUMENTS**

**Cách dùng:**
```
/gdocs content/blog/3-finalized/Final-chung-khoan-la-gi.md
/gdocs                    ← tự detect bài mới nhất
```

---

Đọc `.antigravity/skills/export/SKILL.md` để nắm toàn bộ quy trình, sau đó thực hiện:

1. **Xác định file:** Nếu `$ARGUMENTS` có path → dùng path đó. Nếu trống → tìm file mới nhất trong `content/blog/3-finalized/` bằng `ls -t content/blog/3-finalized/ | head -1`. Confirm với user trước khi tiếp tục.

2. **Kiểm tra xác thực:** Thử gọi một Google Drive MCP tool. Nếu chưa xác thực → chạy `mcp__claude_ai_Google_Drive__authenticate`, hướng dẫn user mở URL → nhận callback URL → gọi `mcp__claude_ai_Google_Drive__complete_authentication`.

3. **Đọc và xử lý file:** Đọc file markdown, strip toàn bộ YAML frontmatter (phần `---`...`---` đầu file), giữ lại content thuần. Trích `Target_Keyword` từ YAML làm tên Google Doc.

4. **Upload lên Google Drive:** Dùng Drive MCP tools (xuất hiện sau xác thực) để tạo Google Doc mới tên `[Target_Keyword] — HVS Securities` trong folder "HVS Blog".

5. **Báo cáo kết quả:** In URL Google Doc vừa tạo.
