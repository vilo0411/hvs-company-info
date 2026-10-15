# HVS Tài Chính Số — SEO Content System

Hệ thống sản xuất bài SEO tiếng Việt cho `taichinhso.hvsvn.com` (chứng khoán, đầu tư cho F0). 381+ bài Final. Output tiếng Việt, code comment tiếng Anh.

---

## ⚖️ Project Rules (đọc theo thứ tự khi bắt đầu session)

1. `.antigravity/rules/workflow-integrity.md` — gate, mode, context bắt buộc, Content Edit Rule, bảng "dùng script thay vì đọc file"
2. `.antigravity/rules/seo-formatting.md` — rule hình thức ↔ lint ID, độ dài theo loại bài, YAML schema
3. `.antigravity/rules/learning-loop.md` — feedback đi đâu (lint / §0 / instincts / revision-log)
4. `.antigravity/rules/write-track.md` — pipeline `/write` Phase 0–5
5. `.antigravity/rules/content-optimization.md` — `/optimize`

---

## 🔄 Mandatory Context Protocol (load 1 lần / session)

1. `resources/company/hvs-profile.md`
2. `seo-strategy/resources/content-strategy/anti-ai-rules.md` — **chỉ §0 Quick Scan**
3. `seo-strategy/resources/content-strategy/glossary.md`
4. `seo-strategy/resources/content-strategy/tone-and-voice.md`
5. `.antigravity/memory/instincts.md` (+ `instincts-by-scope/<topic>.md` chỉ khi bài thuộc topic đó; `instincts-archive.md` không load khi viết)
6. Đúng **1 section persona** trong `resources/audience/personas-deep.md` + 1–2 file `resources/products/`

Các bước sau (QA, sửa, approve) **không đọc lại**. Tra cứu bằng script:

| Việc | KHÔNG làm | Làm |
|---|---|---|
| Trạng thái bài | đọc `topic-clusters.md` (600 dòng) | `python scripts/topic_status.py <slug> [--set S]` · `--find "kw"` · `--add "kw" --cluster C` |
| Sprint | đọc `sprint-backlog.md` / `progress-log.md` | `python scripts/sprint_status.py "<kw>" [--set S \| --remove]` · `--sync` |
| Internal link | đọc `anchor-index.md` (450 dòng) | `python scripts/find_links.py "<kw>" --exclude <slug>` |
| Bài cũ nên link tới bài mới | đọc các Final | `python scripts/find_links.py --backfill <slug>` |
| SEO / anti-AI / format / word count | rà checklist bằng mắt | `python scripts/qa_lint.py <file> [--outline] [--original] [--fix]` |
| Nhịp câu / bằng chứng / trùng khung (AI slop) | đọc lại đoán "nghe như AI" | `python scripts/slop_check.py <file> [-v]` · `--baseline` |
| Số liệu thị trường để viết / kiểm chứng số trong bài | tự nhớ giá, chỉ số | `python scripts/market_facts.py --brief` · `--verify <file>` |
| Tin tức, sự kiện mới quanh keyword | WebSearch | `python scripts/news_feed.py --topic "<kw>" --days 14` |
| URL có live không | đoán slug | `python scripts/fetch_sitemap.py --slug <slug>` / `--search "kw"` / `--refresh` |
| Lỗi cũ của bài | đọc cả `revision-log.md` | `grep -n "<slug>" seo-strategy/content-plan/revision-log.md` |
| Finalize | 9 bước tay | `python scripts/finalize.py <slug> [--optimize] [--dry-run]` |
| Sức khỏe pipeline | so file bằng mắt | `python scripts/pipeline_audit.py [--fix] [--wrappers]` |

## ✍️ Content Edit Rule (mọi yêu cầu sửa nội dung, kể cả chat tự do)

Sửa bất kỳ file nào trong `content/blog/` → (1) đã load context trên; (2) sửa đúng phạm vi; (3) `python scripts/qa_lint.py <file>` + `python scripts/slop_check.py <file>` + `python scripts/market_facts.py --verify <file>` rồi self-audit ngữ nghĩa; (4) trình bày `❌ BẢN CŨ / ✅ BẢN SỬA`; (5) 1 dòng vào `revision-log.md`. Entry point: `/revise`.
**QA loop tối đa 2 vòng** → vẫn FAIL thì dừng, trình bày `⚠️ Remaining issues`.
Học bản năng mới → `/learn`: regex bắt được → `anti-ai-rules.md §0` / `qa_lint.py`; judgment → `instincts-archive.md` + `python scripts/optimize_instincts.py`.

## 🛡️ HVS Hard Constraints

- **HVS Thực tập số** = phễu chuyển đổi chính cho MỌI persona (chương trình nằm trong nền tảng **HVS Tài chính số**). **HVS Demo / Forum** = công cụ hỗ trợ, không phải đích CTA. Học phí: "từ 1.500.000 VNĐ".
- **Không** nêu % phí giao dịch của HVS; **không** nhắc lịch sử đình chỉ/xử phạt (`resources/confirm-with-leadership.md`; lint `BRAND-fee`, `BRAND-regulatory`).
- Persona: Sơn Sinh Viên · Lan Newbie / Nhà đầu tư F0 · Anh Minh F1. Xưng "bạn" / "HVS". Voice: HVS Senior Mentor (`tone-and-voice.md`).
- Link nội bộ = URL sitemap tuyệt đối; cấm `file:///`, `Final-*.md`. Conversion link: `https://taichinhso.hvsvn.com/thuc-tap-so`.
- Nguồn pháp lý: `vanban.chinhphu.vn` / `vbpl.vn`. Không LaTeX. H2 cuối `## Kết luận`.

## 🤖 Sub-Agents

| Agent | File | Vai trò |
|---|---|---|
| SEO Collector | `.antigravity/agents/seo-collector.md` | SERP (`serp_research.py` / WebSearch fallback), PAA, gap, cấu trúc đề xuất |
| Quality Guardian | `.antigravity/agents/quality-guardian.md` | QA ngữ nghĩa CL1–CL10 **sau khi** lint PASS |
| Brand Guardian | `.antigravity/agents/brand-guardian.md` | Mode B audit `/optimize`; Mode C đề xuất cập nhật kiến thức |
| Research Agent | `.antigravity/agents/research-agent.md` | `/setup` Knowledge Base |
| Visual Architect | `.antigravity/agents/visual-architect.md` | `/image` |

## ⌨️ Slash Commands

SOP duy nhất: `.antigravity/workflows/<cmd>.md`. Wrapper: `.claude/commands/<cmd>.md` (Claude Code) và `.agents/workflows/<cmd>.md` (Antigravity) — chỉ trỏ, không chứa logic.

| Lệnh | Việc |
|---|---|
| `/write "<kw>" [--step\|--auto\|--no-serp]` · `--sprint [N] [--with-serp]` · `--sprint --flush` | Pipeline Outline → Draft → Final (Express mặc định: 1 gate) |
| `/approve` | Duyệt Outline / Draft / Optimize — gọi `finalize.py` |
| `/revise <slug> "yêu cầu"` | Sửa có phạm vi + lint bắt buộc |
| `/optimize <path>` | Tối ưu bài cũ (SERP gap, anti-AI, link 2 chiều, giữ ảnh) |
| `/link <slug> [--backfill] [--audit]` | Internal link / backfill / dashboard |
| `/learn [slug]` | Feedback → §0 / lint / instincts |
| `/image <slug> [--plan]` | Ảnh template → WebP → chèn |
| `/audit [--fix] [--wrappers]` | Sức khỏe pipeline |
| `/cluster [csv] \| raw <file>` | Topic cluster map (`keyword-hvs.csv`) |
| `/keyword-plan [N] [persona]` | Sprint planner |
| `/raw [path] \| --all` | Chuẩn hóa nội dung thô |
| `/gdocs [path]` | Export Google Docs |
| `/setup [module]` | Knowledge Base |

## 🛠️ Helper Scripts (`scripts/`)

| Script | Dùng để |
|---|---|
| `qa_lint.py <file> [--outline] [--original] [--fix] [--json] [--log] [--no-sitemap] [--dump-rules]` | ~40 check tất định, Score 0–100, exit 1 = FAIL. Rule đọc từ `anti-ai-rules.md §0`, `glossary.md`, `confirm-with-leadership.md`, sitemap cache; word count qua `wordcount.py` |
| `slop_check.py <file> [-v] [--json]` · `--baseline [--csv f] [--top N]` · `--thresholds` | Tầng B: 13 rule `SLOP-*` thống kê (burstiness, rhythm_gap, evidence/100w, vague, template_sim…). Ngưỡng relative theo corpus — xem `seo-strategy/content-plan/slop-audit-2026-10-15.md`. Gate: score < 80 = FAIL |
| `market_facts.py --brief [--tickers …]` · `--ticker VCB` · `--index VNINDEX --years 2022,2026` · `--verify <file>` | **Script duy nhất có network trong pipeline viết.** Lấy OHLCV thật (VNDirect dchart) + danh sách mã niêm yết (SSI iboard), cache 24h `market-cache.json`. `--verify` bắt `FACT-index-wrong` / `FACT-ticker` / `FACT-stale`. Exit 3 = nguồn chết, KHÔNG chặn pipeline |
| `news_feed.py --topic "<kw>" [--days N]` · `--latest` · `--feeds` | RSS 6 báo (CafeF, VnExpress, Vietstock, Tuổi Trẻ, Dân Trí), cache 6h. Dùng để tìm góc bài + mốc sự kiện có ngày, KHÔNG dùng để viết lại tin |
| `topic_status.py` | Đọc/ghi trạng thái trong `topic-clusters.md` (giữ format bullet) |
| `sprint_status.py` | Ghi duy nhất cho `sprint-backlog.md` + Dashboard/Active Pipeline của `progress-log.md` |
| `find_links.py` | Tra anchor-index + sitemap; backfill; `--add-row` |
| `finalize.py <slug> [--optimize] [--dry-run] [--force]` | Toàn bộ bước finalize, từ chối khi còn CRITICAL (qa_lint) hoặc slop score < 80 (`slop_check`) |
| `pipeline_audit.py [--fix] [--wrappers]` | Outline/draft/backlog stale, dashboard, path hỏng, wrapper drift |
| `optimize_instincts.py [--dry-run]` | Sinh `instincts.md` + `instincts-by-scope/` từ archive |
| `normalize_raw.py [--apply]` | `0-raw/<Tiêu đề>.md` → `Raw-<slug>.md` |
| `migrate_legacy.py [--apply] [--only …]` | Sửa hàng loạt Final cũ (YAML `Mode:`, `file:///`, link `.md`, LaTeX) — dry-run mặc định |
| `fetch_sitemap.py [--refresh\|--slug\|--search\|--validate]` | Cache sitemap 24h |
| `link_audit.py` | Dashboard link in/out |
| `serp_opportunities.py` | PAA/related từ cache SERP → `serp-opportunities.md` (0 API call) |
| `.antigravity/skills/seo-research/scripts/serp_research.py "<kw>" [--top 10] [--extract 5]` | SERP Google VN (DataForSEO, **có phí**, cache 30 ngày `seo-strategy/raw/serp/`). Key: `.antigravity/config/api-keys.md` hoặc `.env` |
| `.antigravity/skills/qa-qc/scripts/wordcount.py <draft> [--outline]` | Word count từng H2 ±10% (qa_lint import) |

## 📂 Workspace

```
.antigravity/        # ENGINE: agents/ rules/ workflows/ (SOP) skills/ memory/ config/
.claude/commands/    # wrapper Claude Code  ·  .agents/workflows/ + .agents/rules/ = wrapper/pointer Antigravity
scripts/             # helper scripts + sitemap-cache.json
content/blog/        # 0-raw → 1-outlines → 2-user-review → 3-finalized · assets/images/<slug>/
seo-strategy/        # content-plan/ (topic-clusters, sprint-backlog, progress-log, anchor-index, revision-log)
                     # resources/content-strategy/ (anti-ai-rules, glossary, tone-and-voice, financial-logic, holistic-seo-rules)
                     # keywords/keyword-hvs.csv · raw/serp/ (cache)
resources/           # company/ audience/ products/ market/ confirm-with-leadership.md
archive/             # tài liệu & script cũ (không load)
```

## 🏷️ YAML schema

Xem `.antigravity/rules/seo-formatting.md §4`. Bắt buộc: `Author, Status, Pipeline_Mode (Express|Guided|Auto|Optimized), SERP_Research, Persona, Target_Keyword, Search_Intent, Word_Count_Target, Meta_Description, HVS_Products` (list chuỗi phẳng). Outline thêm `PAA_Questions`, `Internal_Links`, `Word_Count` từng H2. Final có thể có `Section_Targets` (finalize sinh).
