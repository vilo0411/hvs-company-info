---
name: gdocs
description: Xuất bài Finalized lên Google Docs (folder "HVS Blog"). Args: [path|slug] — trống = bài mới nhất
---

# /gdocs [path|slug]

Skill: `.antigravity/skills/export/SKILL.md`.

1. Xác định file `content/blog/3-finalized/Final-<slug>.md` (trống → mới nhất theo mtime; confirm với user).
2. `python scripts/qa_lint.py <file> --no-sitemap` → có CRITICAL → hỏi user có export không.
3. Strip YAML + `## Revision Log`. Tiêu đề Doc = H1.
4. Claude Code: `mcp__claude_ai_Google_Drive__create_file` vào folder "HVS Blog" (chưa xác thực → chạy `mcp__claude_ai_Google_Drive__authenticate` → `complete_authentication`). Antigravity: tool `google-drive` tương đương.
5. Trả link Doc.
