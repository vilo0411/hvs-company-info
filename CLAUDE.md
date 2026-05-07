# HVS Securities SEO Content System

Hệ thống sản xuất nội dung SEO cho HVS Securities. Triết lý cốt lõi: **loại bỏ hoàn toàn "AI-vibe"**, nội dung 100% thực chiến từ dữ liệu thật.

---

## Kiến trúc Sub-Agent

| Sub-Agent | File hướng dẫn | Nhiệm vụ |
| :--- | :--- | :--- |
| **SEO Collector** | `.antigravity/agents/seo-collector.md` | SERP research + tạo Content Brief |
| **Brand Guardian** | `.antigravity/agents/brand-guardian.md` | Brand audit cho `/optimize` |
| **Quality Guardian** | `.antigravity/agents/quality-guardian.md` | QA/QC độc lập |
| **Research Agent** | `.antigravity/agents/research-agent.md` | Build Knowledge Base cho `/setup` |

**Nguyên tắc:** Chỉ Main Agent viết bài. Sub-agents chỉ thu thập context.

---

## Slash Commands

### Layer 1 — Knowledge Base
| Lệnh | Mô tả |
| :--- | :--- |
| `/setup [all\|company\|market\|audience\|icp]` | Build Knowledge Base — chạy 1 lần |

### Layer 2 — Keyword Strategy
| Lệnh | Mô tả |
| :--- | :--- |
| `/cluster [csv\|raw file]` | Tạo Topic Cluster map |
| `/keyword-plan [N] [persona]` | Fill sprint lên đủ N active items (default 5) |

### Layer 3 — Content Pipeline

**Single keyword:**
| Lệnh | Mô tả |
| :--- | :--- |
| `/write [keyword]` | **Express** — duyệt Outline, AI tự hoàn thiện Draft→Final |
| `/write [keyword] --step` | **Guided** — duyệt Outline + duyệt Draft |
| `/write [keyword] --auto` | **Auto** — không duyệt, chạy thẳng đến Final |
| `/write [keyword] --no-serp` | Bỏ SERP research (kết hợp được với mọi mode) |

**Batch sprint:**
| Lệnh | Mô tả |
| :--- | :--- |
| `/write --sprint` | Generate outlines cho tất cả `Planned` items (unattended, no-serp) |
| `/write --sprint --with-serp` | Như trên, có SERP research |
| `/write --sprint --flush` | Viết tất cả `Outline-Approved` items → Final (unattended) |

**Utilities:**
| Lệnh | Mô tả |
| :--- | :--- |
| `/approve` | Duyệt giai đoạn hiện tại (mode-aware) |
| `/optimize [path]` | Tối ưu bài cũ — Brand audit + rewrite + QA |
| `/link` | Gắn internal links cho bài đang làm |
| `/raw [path]` | Xử lý nội dung thô từ `content/blog/0-raw/` |

*Alias: `/detailed [kw]` = `/write [kw] --step` | `/fast [kw]` = `/write [kw] --no-serp`*

### Sprint Status Values (sprint-backlog.md)
| Status | Ý nghĩa |
| :--- | :--- |
| `Planned` | Chờ generate outline |
| `Outline-Pending` | Outline đã tạo, chờ review trong `1-outlines/` |
| `Outline-Approved` | Đã duyệt, sẵn sàng cho `--flush` |
| `Writing` | Đang trong `--flush` pipeline |

---

## Workspace Structure

```
content/blog/
├── 0-raw/          Raw-[slug].md       (nội dung thô chưa xử lý)
├── 1-outlines/     Outline-[slug].md   (content brief đã duyệt)
├── 2-user-review/  Draft-[slug].md     (bản nháp chờ duyệt)
└── 3-finalized/    Final-[slug].md     (bài hoàn chỉnh)
```

---

## Key Resources

| Resource | Path |
| :--- | :--- |
| **Pipeline rules** | `.antigravity/rules/write-track.md` |
| **Brief template** | `.antigravity/skills/seo-research/examples/brief-template.md` |
| **Anti-AI Rules** | `seo-strategy/resources/content-strategy/anti-ai-rules.md` |
| **Glossary** | `seo-strategy/resources/content-strategy/glossary.md` |
| **Topic Clusters** | `seo-strategy/content-plan/topic-clusters.md` |
| **Progress Log** | `seo-strategy/content-plan/progress-log.md` |
| **Sprint Backlog** | `seo-strategy/content-plan/sprint-backlog.md` |
| **Keywords CSV** | `seo-strategy/keywords/keywords.csv` |
| **Company** | `resources/company/hvs-profile.md` (hoặc `identity.md` + `usps.md`) |
| **Personas** | `resources/audience/personas-deep.md` (hoặc `hvs-target-audience.csv`) |
| **Products** | `resources/products/` |

---

## Metadata YAML (Bắt buộc cho mọi file content)

```yaml
---
Author: Claude Code
Status: Outline | Draft | Finalized
Pipeline_Mode: Express | Guided | Auto
SERP_Research: true | false
Persona: [Tên persona]
Tone: [Tone]
Writing_Method: PAS | AIDA | 4Cs | How-to steps
Target_Keyword: [Từ khóa chính]
Cluster: [Tên cluster]
Cluster_Role: Pillar | Cluster
Search_Intent: Informational | Commercial | Transactional
Content_Type: [Loại bài]
Featured_Snippet: Paragraph | List | Table | None
Word_Count_Target: [Số chữ]
HVS_Products:
  - product: [Tên]
    benefit: "[Benefit-first description]"
Anti_AI_Flags: [phrases nguy cơ cao cho topic này]
Internal_Links:
  - role: Pillar
    file: Final-[slug].md
    anchor_suggestion: "[anchor text]"
---
```
