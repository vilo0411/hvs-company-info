---
trigger: always_on
---

# HVS Securities — SEO Content System

## Mục tiêu dự án
Sản xuất nội dung SEO thực chiến cho HVS Securities. Triết lý cốt lõi: **loại bỏ hoàn toàn "AI-vibe"**, mọi bài viết phải có dữ liệu thật, ví dụ cụ thể, giọng văn con người.

## Kiến trúc 3 lớp
- **Layer 1 — Knowledge Base** (`/setup`): Research công ty, thị trường, audience, ICP — chạy 1 lần
- **Layer 2 — Keyword Strategy** (`/cluster`, `/keyword-plan`): Topic Cluster map Pillar + Cluster
- **Layer 3 — Content Pipeline** (`/detailed`, `/fast`, `/optimize`, `/approve`, `/link`)

## Sub-Agents (không viết bài, chỉ thu thập context)
- **SEO Collector** (`.antigravity/agents/seo-collector.md`): SERP, PAA, Featured Snippet, Intent
- **Brand Guardian** (`.antigravity/agents/brand-guardian.md`): Anti-AI rules, HVS USPs, Persona
- **Quality Guardian** (`.antigravity/agents/quality-guardian.md`): QA/QC audit loop
- **Research Agent** (`.antigravity/agents/research-agent.md`): Knowledge Base builder (Layer 1)

## Sản phẩm HVS cần lồng ghép đúng persona
- **HVS Demo** → F0, Sinh viên (luyện tập không rủi ro)
- **HVS Forum** → F0, F1 (học từ cộng đồng)
- **HVS Tài chính số** → F1+ (quản lý danh mục)
- **HVS Thực tập số** → Sinh viên (kinh nghiệm thực tế)

## Key Resources
- Anti-AI Rules: `seo-strategy/resources/content-strategy/anti-ai-rules.md`
- Glossary: `seo-strategy/resources/content-strategy/glossary.md`
- Keywords: `seo-strategy/keywords/Nghiên cứu từ khóa - HVS Tư vấn số.csv`
- Progress Log: `seo-strategy/content-plan/progress-log.md`
- Topic Clusters: `seo-strategy/content-plan/topic-clusters.md`
