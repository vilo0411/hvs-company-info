---
name: Export to Google Docs
description: Xuất bài Finalized lên Google Docs qua Google Drive connector. Kích hoạt bởi /gdocs.
---

# Skill: `/gdocs [slug]` — Export to Google Docs

## Tool
- Claude Code: `mcp__claude_ai_Google_Drive__create_file` (connector claude.ai — không cần mcp_config).
- Antigravity: MCP server `google-drive` chạy qua `node scripts/mcp-launcher.js` (đọc `GOOGLE_DRIVE_CREDENTIALS_FILE` trong `.env`); tool tương đương `create_file`.

## Luồng

1. Xác định file: `content/blog/3-finalized/Final-<slug>.md` (không có slug → file mới nhất theo mtime).
2. `python scripts/qa_lint.py <file> --no-sitemap` → nếu có CRITICAL, báo user trước khi export.
3. Xử lý nội dung:
   - Bỏ YAML frontmatter.
   - Bỏ section `## Revision Log` / `## Nhật ký chỉnh sửa` (nội bộ, không xuất).
   - Ảnh: giữ dòng `![alt](content/blog/assets/images/…)` nguyên (người đăng upload tay) — hoặc bỏ nếu user yêu cầu.
   - Tiêu đề Doc = H1 của bài.
4. Tạo Doc trong folder **"HVS Blog"** (tạo folder nếu chưa có); nội dung Markdown thuần.
5. Trả link Doc + nhắc: cập nhật cột `Google Doc` trong `keyword-hvs.csv` nếu cần.
