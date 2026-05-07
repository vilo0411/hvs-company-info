---
name: qa-qc
description: Quality Assurance with an iterative fixing loop. AI must correct issues found during the check.
---

# Skill: QA/QC for HVS Content

## Workflow (Agent Internal)
1. **Check:** Agent evaluates the current content against the checklist.
2. **Report:** Agent generates an internal summary of Pass/Fail items.
3. **Action (Auto-Fix Loop):**
   - If **FAIL**: Agent identifies the exact sections causing the failure.
   - Agent **automatically modifies** the content to fix the issues.
   - Agent re-runs the checklist.
   - Repeat until **PASS**.
4. **Final Result:** Agent only presents the finalized, passing version to the user. No intermediate files or folders are created for the QA process.

## Checklist Items
- Persona Alignment
- SEO (H1, Sapo, Keywords, Meta)
- **Anti-AI Check:** Cross-reference content with `seo-strategy/resources/content-strategy/anti-ai-rules.md`.
- Brand Ecosystem (HVS Demo/Forum/Tài chính số)
- Technical (Typos, Markdown, YAML Metadata completeness, CTA)

