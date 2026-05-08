---
name: Export to Google Docs (Antigravity)
description: Xuất bài viết Finalized lên Google Docs.
---

# Skill: `/gdocs` — Export to Google Docs

Skill này cho phép Antigravity xuất nội dung từ `content/blog/3-finalized/` lên Google Docs thông qua Google Drive MCP.

## Hướng dẫn sử dụng

Gõ `/gdocs [slug]` hoặc chỉ cần `/gdocs` để lấy bài mới nhất.

## Luồng xử lý

1. **Kiểm tra MCP**: Đảm bảo tools `mcp__google_drive__...` đã xuất hiện. Nếu chưa, yêu cầu user restart Antigravity sau khi đã config `mcp_config.json`.
2. **Đọc file**: Lấy file `Final-[slug].md`.
3. **Xử lý nội dung**:
   - Loại bỏ YAML frontmatter (phần giữa `---`).
   - Lấy `Target_Keyword` từ YAML làm tiêu đề Doc.
4. **Export**:
   - Sử dụng tool `mcp__google_drive__create_file` hoặc tương đương để tạo Google Doc.
   - Nội dung là Markdown thuần.
5. **Phản hồi**: Trả về link Google Doc cho user.

## Cấu hình (Đã thực hiện)
File cấu hình tại: `C:\Users\loc.nv\.gemini\antigravity\mcp_config.json`
```json
{
  "mcpServers": {
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-drive"]
    }
  }
}
```
