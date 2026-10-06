# HVS Multi-Agent Team

Sub-agent chỉ thu thập / kiểm định — **Main Agent viết bài**. Mọi agent có block "Context Loading": trong pipeline không đọc lại file đã load ở Bước 0.

| Agent | File | Kích hoạt | Skill / Script |
|---|---|---|---|
| **SEO Collector** | `.antigravity/agents/seo-collector.md` | `/write` Phase 1, `/optimize` Bước 2 | `seo-research/SKILL.md`, `serp_research.py` |
| **Quality Guardian** | `.antigravity/agents/quality-guardian.md` | `/write` Phase 3, `/optimize` Bước 5, `/revise` | `qa-qc/SKILL.md`, `scripts/qa_lint.py` |
| **Brand Guardian** | `.antigravity/agents/brand-guardian.md` | Mode B `/optimize`; Mode C sau `/approve` | `glossary.md`, `confirm-with-leadership.md` |
| **Research Agent** | `.antigravity/agents/research-agent.md` | `/setup` | → `resources/` |
| **Visual Architect** | `.antigravity/agents/visual-architect.md` | `/image` | `image-generation/SKILL.md`, `image_processor.py` |
