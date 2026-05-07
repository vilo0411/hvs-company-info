---
name: Fast Track (Quick Post)
description: Viết nhanh bài SEO chuẩn Brand. Kích hoạt bằng lệnh `/fast [keyword]` cho các chủ đề tin tức hoặc bài viết không cần nghiên cứu SERP sâu.
---

# Workflow: Fast Track SEO Content Creation

This workflow is optimized for speed and efficiency. Use it for standard blog topics that don't require complex strategy sessions.

## Detailed Steps
1. **Duplicate Check:** Verify the keyword isn't already covered in `progress-log.md`.
2. **Strategy Selection:** Automatically pick the best Persona and Search Intent based on the keyword and project resources.
3. **Drafting:** Write the full article directly to `content/blog/2-user-review/Draft-[slug].md`.
4. **Internal QA (The Loop):** 
   - Agent performs an internal QA/QC check using the `qa-qc` skill.
   - Automatically fix any issues identified (Anti-AI, SEO, Brand).
   - Only present the "Passed" version to the user.
5. **Review:** 
   - Present the draft to the user for review.
   - If revisions are requested, **APPEND** new entries to the **Revision Log** at the bottom.
6. **Finalize:** 
   - Once approved (`pass` or `/approve`), **move** the file to `content/blog/3-finalized/Final-[keyword-slug].md` (deleting the draft from `2-user-review/`).
   - **Naming Rule:** Use a concise [keyword-slug] (e.g., Final-co-phieu-penny.md).
   - Update `progress-log.md` with status `Finalized`.

## Metadata Requirements
```yaml
Author: Antigravity
Status: User_Review
Mode: Fast
Persona: [Name]
Target_Keyword: [Keyword]
```
