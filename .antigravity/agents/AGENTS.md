# HVS Multi-Agent Team (AGENTS.md)

Danh sách sub-agents chuyên biệt. Chỉ thu thập context — Main Agent viết bài.

---

## Danh sách nhân sự

1. **SEO Collector** ([agents/seo-collector.md](.antigravity/agents/seo-collector.md))
   - **Vai trò:** SERP research, tạo Content Brief — kích hoạt bởi `/write` (có SERP)
   - **Skill:** `.antigravity/skills/seo-research/SKILL.md`

2. **Brand Guardian** ([agents/brand-guardian.md](.antigravity/agents/brand-guardian.md))
   - **Mode A:** Brand Context tại Phase 1 của `/write`
   - **Mode B:** Audit bài cũ tại Phase 2 của `/optimize`
   - **Mode C:** Knowledge Update sau `/approve`
   - **Tham chiếu:** `.antigravity/rules/anti-ai-digest.md`, `hvs-target-audience.csv`

3. **Quality Guardian** ([agents/quality-guardian.md](.antigravity/agents/quality-guardian.md))
   - **Vai trò:** QA/QC bài viết — kích hoạt tại Phase 3 của write-track
   - **Skill:** `.antigravity/skills/qa-qc/SKILL.md`

4. **Research Agent** ([agents/research-agent.md](.antigravity/agents/research-agent.md))
   - **Vai trò:** Xây dựng Knowledge Base nền tảng — kích hoạt bởi `/setup`
   - **Output:** `resources/company/`, `resources/audience/`, `resources/market/`
