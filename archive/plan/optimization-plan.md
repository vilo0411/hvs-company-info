# Kế hoạch Tối ưu HVS SEO Content Agent

> Mục tiêu: Mở rộng pipeline từ keyword-level lên chiến lược hoàn chỉnh (Research → Cluster → Content), đồng thời fix 3 bottleneck: SERP research, AI-vibe, internal linking.

---

## Tổng quan kiến trúc mới

```
Layer 1 — Knowledge Base (setup 1 lần)
  /setup → Research Agent → resources/

Layer 2 — Keyword Strategy
  /keyword-plan → khám phá keyword mới
  /cluster     → tạo Topic Cluster map (Pillar + Cluster)

Layer 3 — Content Pipeline (cải thiện)
  /detailed → /fast → /optimize → /approve → /link
```

---

## LAYER 1: Knowledge Base Setup

### Task 1.1 — Tạo command `/setup` ✅
- **File:** `.claude/commands/setup.md`
- **Chức năng:** Kích hoạt Research Agent để build knowledge base 3 module
- **Sub-tasks:**
  - [x] Định nghĩa `/setup company` — đọc `resources/products/`, tạo `resources/company/hvs-profile.md`
  - [x] Định nghĩa `/setup market` — WebSearch đối thủ, tạo `resources/market/market-landscape.md`
  - [x] Định nghĩa `/setup audience` — mở rộng CSV thành `resources/audience/personas-deep.md`
  - [x] Định nghĩa `/setup all` — chạy cả 3 song song

---

### Task 1.2 — Tạo Research Agent ✅
- **File:** `.antigravity/agents/research-agent.md`
- **Chức năng:** Sub-agent chuyên Layer 1, không viết content
- **Sub-tasks:**
  - [x] Module 1: Company Research (đọc internal resources)
  - [x] Module 2: Market Research (WebSearch đối thủ VN)
  - [x] Module 3: Audience Research (persona chi tiết với pain points, vocabulary)
  - [x] Output format chuẩn cho từng module

---

### Task 1.3 — Tạo thư mục Knowledge Base ✅
- **Files:** `resources/company/`, `resources/market/`
- Đã tạo cả 2 thư mục

---

## LAYER 2: Keyword Strategy

### Task 2.1 — Tạo command `/keyword-plan` ✅
- **File:** `.claude/commands/keyword-plan.md`
- **Chức năng:** Khám phá keyword mới từ Knowledge Base + WebSearch
- **Sub-tasks:**
  - [x] Đọc knowledge base (company + audience + market)
  - [x] Đọc CSV hiện có, tránh duplicate
  - [x] WebSearch 4 query chuẩn theo persona
  - [x] Output: danh sách keyword mới có Intent + Priority + Persona

---

### Task 2.2 — Tạo command `/cluster` ✅
- **File:** `.claude/commands/cluster.md`
- **Chức năng:** Gom nhóm keywords thành Topic Cluster map
- **Sub-tasks:**
  - [x] Đọc CSV + progress-log để map coverage
  - [x] Semantic grouping theo chủ đề
  - [x] Xác định Pillar/Cluster cho từng nhóm
  - [x] Đánh dấu status (Published / In Progress / Planned / Suggested)
  - [x] Output: `seo-strategy/content-plan/topic-clusters.md`

---

### Task 2.3 — Tạo Keyword Clustering Skill ✅
- **File:** `.antigravity/skills/keyword-clustering/SKILL.md`
- **Chức năng:** Logic phân nhóm chuẩn — tiêu chí Pillar vs Cluster
- **Sub-tasks:**
  - [x] Tiêu chí Pillar: volume cao + intent informational + 2000+ words
  - [x] Tiêu chí Cluster: long-tail + how-to/commercial + link ngược về Pillar
  - [x] Output format chuẩn cho `topic-clusters.md`

---

## LAYER 3: Cải thiện Content Pipeline

### Task 3.1 — Cải thiện SERP Research (Bottleneck #1) ✅
- **File:** `.antigravity/agents/seo-collector.md`
- **Vấn đề:** Research hiện tại chỉ lấy headings, thiếu PAA và featured snippet
- **Sub-tasks:**
  - [x] Thêm People Also Ask (PAA) — top 5 câu hỏi từ SERP
  - [x] Thêm Featured Snippet detection — có không? format gì?
  - [x] Thêm Content length benchmark — ước tính word count top 3
  - [x] Thêm Keyword variations — LSI keywords trong headings đối thủ
  - [x] Thêm SERP Intelligence summary block trước Content Brief

---

### Task 3.2 — Cải thiện Anti-AI QA (Bottleneck #2) ✅
- **File:** `.antigravity/skills/qa-qc/SKILL.md`
- **Vấn đề:** Checklist hiện tại thiếu detection cho translation-vibe và câu chung chung
- **Sub-tasks:**
  - [x] Thêm Translation-vibe detector (câu bị động, danh từ hóa kiểu Anh)
  - [x] Thêm Specificity check (mỗi claim phải có mã CK / con số / tên sàn cụ thể)
  - [x] Thêm Sentence rhythm check (>3 câu cùng cấu trúc)
  - [x] Thêm Terminology check — tích hợp `glossary.md`

---

### Task 3.3 — Cải thiện Internal Linking (Bottleneck #3) ✅
- **File:** `.claude/commands/link.md`
- **Vấn đề:** 10/11 bài Finalized không có link nội bộ
- **Sub-tasks:**
  - [x] Đọc `topic-clusters.md` trước để xác định cluster
  - [x] Ưu tiên Pillar link (bắt buộc với Cluster articles)
  - [x] Phân loại đề xuất: Pillar / Cluster / Cross-cluster
  - [x] Báo cáo trước khi chèn link

---

### Task 3.4 — Tích hợp Topic Cluster vào `/detailed` ✅
- **File:** `.claude/commands/detailed.md`
- **Sub-tasks:**
  - [x] Thêm Bước 0: check `topic-clusters.md` trước khi research
  - [x] Xác định Pillar/Cluster, linking obligations
  - [x] Outline phải có linking plan tương ứng

---

## Fixes & Debt

### Task 4.1 — Tạo Glossary ✅
- **File:** `seo-strategy/resources/content-strategy/glossary.md`
- **Vấn đề:** Được reference bởi 2 skills nhưng chưa tồn tại
- **Sub-tasks:**
  - [x] HVS product terms (HVS Demo, Forum, Tài chính số, Thực tập số)
  - [x] Thuật ngữ chứng khoán VN chuẩn (cổ phiếu, trái phiếu, HOSE, HNX...)
  - [x] Tone & xưng hô chuẩn HVS (bạn / chúng tôi / CTA)

---

### Task 4.2 — Fix naming convention violation
- **File:** `content/blog/3-finalized/phan-tich-nganh-la-gi.md`
- **Sub-tasks:**
  - [ ] Rename → `Final-phan-tich-nganh-la-gi.md`
  - [ ] Cập nhật `seo-strategy/content-plan/progress-log.md`

---

### Task 4.3 — Fix inventory count mismatch
- **File:** `seo-strategy/content-plan/progress-log.md`
- **Vấn đề:** Dashboard ghi "8 files" nhưng `0-raw/` thực tế có 10 files
- **Sub-tasks:**
  - [ ] Audit `0-raw/` — liệt kê đầy đủ 10 files
  - [ ] Cập nhật Dashboard count
  - [ ] Add missing entries vào Inventory table

---

### Task 4.4 — Cập nhật CLAUDE.md
- **File:** `CLAUDE.md`
- **Sub-tasks:**
  - [ ] Thêm `/setup` vào bảng Commands
  - [ ] Thêm `/keyword-plan` vào bảng Commands
  - [ ] Thêm `/cluster` vào bảng Commands

---

## Thứ tự thực hiện

| Priority | Task | Impact | Effort | Status |
| :---: | :--- | :--- | :--- | :--- |
| 1 | 4.1 Glossary | High | Low | ✅ Done |
| 2 | 1.2 Research Agent | High | Medium | ✅ Done |
| 3 | 1.1 `/setup` command | High | Medium | ✅ Done |
| 4 | 2.3 Clustering Skill | High | Medium | ✅ Done |
| 5 | 2.1 `/keyword-plan` | High | Medium | ✅ Done |
| 6 | 2.2 `/cluster` | High | Medium | ✅ Done |
| 7 | 3.1 SERP Research++ | High | Low | ✅ Done |
| 8 | 3.2 Anti-AI QA++ | High | Low | ✅ Done |
| 9 | 3.3 Internal Linking++ | Medium | Low | ✅ Done |
| 10 | 3.4 `/detailed` cluster check | Medium | Low | ✅ Done |
| 11 | 4.4 Update CLAUDE.md | Low | Low | ⭕ TODO |
| 12 | 4.2 Fix filename | Low | Low | ⭕ TODO |
| 13 | 4.3 Fix inventory count | Low | Low | ⭕ TODO |

---

## Files thay đổi (tổng hợp)

### Tạo mới ✅
| File | Mô tả |
| :--- | :--- |
| `.claude/commands/setup.md` | Command `/setup` |
| `.claude/commands/keyword-plan.md` | Command `/keyword-plan` |
| `.claude/commands/cluster.md` | Command `/cluster` |
| `.antigravity/agents/research-agent.md` | Research Agent |
| `.antigravity/skills/keyword-clustering/SKILL.md` | Keyword clustering logic |
| `seo-strategy/resources/content-strategy/glossary.md` | Thuật ngữ chuẩn |
| `resources/company/` | Thư mục KB company |
| `resources/market/` | Thư mục KB market |

### Chỉnh sửa ✅
| File | Thay đổi |
| :--- | :--- |
| `.antigravity/agents/seo-collector.md` | Thêm PAA, featured snippet, benchmark |
| `.antigravity/skills/qa-qc/SKILL.md` | Thêm translation-vibe, specificity, terminology check |
| `.claude/commands/link.md` | Tích hợp topic-clusters |
| `.claude/commands/detailed.md` | Thêm Bước 0 cluster check |

### TODO ⭕
| File | Action |
| :--- | :--- |
| `CLAUDE.md` | Thêm 3 commands mới |
| `content/blog/3-finalized/phan-tich-nganh-la-gi.md` | Rename với prefix `Final-` |
| `seo-strategy/content-plan/progress-log.md` | Fix inventory count (8 → 10) |

---

## Verification Checklist

Sau khi hoàn tất 3 TODO còn lại, test theo flow:

- [ ] `/setup all` → 3 file knowledge base được tạo đúng format
- [ ] `/keyword-plan` → đọc được CSV + đề xuất keyword hợp lệ
- [ ] `/cluster` → tạo được `topic-clusters.md` với cấu trúc Pillar/Cluster
- [ ] `/detailed [keyword]` → Outline có SERP Intelligence block + cluster context
- [ ] `/approve` → Draft qua QA không còn translation-vibe, có ví dụ cụ thể
- [ ] `/link` → suggestions phân loại Pillar/Cluster/Cross-cluster
