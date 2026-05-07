---
name: Raw Content Processing
description: Chuẩn hóa dữ liệu thô (HTML/Text) sang Markdown hoặc Outline. Kích hoạt bằng lệnh `/raw [path]` trước khi đưa vào pipeline tối ưu hoặc chi tiết.
---

# Workflow: Raw Content Processing (/raw)

Clean up HTML snippets, plain text, or poorly named files to prepare them for the optimization pipeline.

## Detailed Steps
1. **Source Detection:** Identify the input content (HTML, plain text, or poorly named file) in `0-raw/`.
2. **Conversion:** 
   - Strip HTML tags while preserving structure.
   - Normalize formatting to standard Markdown.
3. **Metadata Inference:** Infer Target_Keyword and Persona, then create YAML frontmatter.
4. **Renaming & Routing:** 
   - If content is **Unstructured/Full article**: Save as `Raw-[slug].md` in `content/blog/0-raw/`.
   - If content is a **Structured Outline**: Save as `Outline-[slug].md` in `content/blog/1-outlines/`.
5. **Reporting:** 
   - For `Raw-` files: Update status to **Processed** in `Content Inventory`.
   - For `Outline-` files: Create a new entry in the **Active Pipeline** section of `progress-log.md`.
