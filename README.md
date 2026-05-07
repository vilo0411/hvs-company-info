# HVS SEO Content Agent System

Hệ thống Agent AI được thiết lập riêng cho **HVS Securities**, tối ưu hóa quy trình sản xuất nội dung SEO chất lượng cao, thực chiến và loại bỏ hoàn toàn "AI-vibe".

---

## Kiến trúc Hệ thống

Hệ thống hoạt động theo 3 lớp: **Knowledge Base** → **Keyword Strategy** → **Content Pipeline**, đảm bảo mọi bài viết đều có nền tảng dữ liệu vững chắc trước khi được sản xuất.

### Sub-Agents

| Sub-Agent | Nhiệm vụ |
| :--- | :--- |
| **SEO Collector** | SERP research + tạo Content Brief |
| **Brand Guardian** | Brand audit cho `/optimize` |
| **Quality Guardian** | QA/QC độc lập |
| **Research Agent** | Build Knowledge Base cho `/setup` |

> Nguyên tắc: Chỉ Main Agent viết bài. Sub-agents chỉ thu thập context.

---

## Slash Commands

### Layer 1 — Knowledge Base

| Lệnh | Mô tả |
| :--- | :--- |
| `/setup [all\|company\|market\|audience\|icp]` | Build Knowledge Base — chạy 1 lần khi khởi tạo project |

### Layer 2 — Keyword Strategy

| Lệnh | Mô tả |
| :--- | :--- |
| `/cluster [csv\|raw file]` | Tạo Topic Cluster map từ file keyword |
| `/keyword-plan [N] [persona]` | Chọn N bài nên viết tiếp từ cluster map |

### Layer 3 — Content Pipeline

**Single keyword:**

| Lệnh | Mô tả |
| :--- | :--- |
| `/write [keyword]` | **Express** — duyệt Outline, AI tự hoàn thiện Draft → Final |
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
| `/approve` | Duyệt giai đoạn hiện tại (Outline → Draft/Final tùy mode) |
| `/optimize [path]` | Tối ưu bài cũ — Brand audit + rewrite + QA |
| `/link` | Gắn internal links cho bài đang làm |
| `/raw [path]` | Xử lý nội dung thô HTML/text → Markdown chuẩn |

*Alias: `/detailed [kw]` = `/write [kw] --step` | `/fast [kw]` = `/write [kw] --no-serp`*

---

## Vòng đời Bài viết

```
content/blog/
├── 0-raw/          Raw-[slug].md       nguyên liệu thô chưa xử lý
├── 1-outlines/     Outline-[slug].md   content brief chờ duyệt
├── 2-user-review/  Draft-[slug].md     bản nháp đã qua QA, chờ duyệt
└── 3-finalized/    Final-[slug].md     bài hoàn chỉnh, sẵn sàng đăng
```

**Sprint Status** (theo dõi tại `seo-strategy/content-plan/sprint-backlog.md`):

| Status | Ý nghĩa |
| :--- | :--- |
| `Planned` | Chờ generate outline |
| `Outline-Pending` | Outline đã tạo, chờ review trong `1-outlines/` |
| `Outline-Approved` | Đã duyệt, sẵn sàng cho `--flush` |
| `Writing` | Đang trong `--flush` pipeline |

---

## Nguyên tắc Anti-AI

Điểm khác biệt cốt lõi là bộ lọc **Anti-AI Rules** (`seo-strategy/resources/content-strategy/anti-ai-rules.md`):

- **Cấm sáo rỗng:** Loại bỏ các cụm từ "Trong thế giới...", "Hành trình...", "Mở khóa tiềm năng...".
- **Thực chiến:** Luôn lấy ví dụ từ thị trường Việt Nam (HOSE, HNX, mã chứng khoán cụ thể).
- **Persona-driven:** Dẫn dắt sản phẩm HVS dựa trên nhu cầu thực tế của từng đối tượng (F0, Sinh viên, Pro).

---

## Tài nguyên chính

| Resource | Path |
| :--- | :--- |
| Pipeline rules | `.antigravity/rules/write-track.md` |
| Anti-AI Rules | `seo-strategy/resources/content-strategy/anti-ai-rules.md` |
| Glossary | `seo-strategy/resources/content-strategy/glossary.md` |
| Topic Clusters | `seo-strategy/content-plan/topic-clusters.md` |
| Sprint Backlog | `seo-strategy/content-plan/sprint-backlog.md` |
| Progress Log | `seo-strategy/content-plan/progress-log.md` |
| Keywords CSV | `seo-strategy/keywords/keyword-hvs.csv` |
| Company Profile | `resources/company/` |
| Personas | `resources/audience/` |

---

**Author:** Antigravity AI Agent
**Project:** HVS Securities Content SEO Framework
