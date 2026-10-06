---
trigger: always_on
---

# Workspace & Naming (pointer)

> Nguồn chính: `.antigravity/rules/workflow-integrity.md` §7 (vị trí file, naming) và `.antigravity/rules/seo-formatting.md` §4 (YAML schema).

- `content/blog/0-raw/Raw-<slug>.md` → `1-outlines/Outline-<slug>.md` → `2-user-review/Draft-<slug>.md` → `3-finalized/Final-<slug>.md`
- YAML dùng `Pipeline_Mode: Express | Guided | Auto | Optimized` (không dùng `Mode:` cũ)
- Gate theo mode: xem `workflow-integrity.md` §1. Express = 1 gate sau Outline.
- Script: `scripts/` (qa_lint, topic_status, sprint_status, find_links, finalize, fetch_sitemap, link_audit, pipeline_audit)
