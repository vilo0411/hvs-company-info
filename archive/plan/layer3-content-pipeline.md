# Plan: Layer 3 — Content Pipeline Redesign

## Audit hiện trạng

### A. Token/Context — vấn đề hiệu năng

**1. Brand Guardian spawn thừa khi viết bài mới**

Hiện tại Phase 1 spawn 2 sub-agents song song: SEO Collector (hợp lý) và Brand Guardian. Brand Guardian đọc 5-6 file:
```
brand-guardian.md → anti-ai-rules.md → identity.md → usps.md → glossary.md → product files
```
Output là một Brand Context Snippet, sau đó `/approve` (Phase 3) lại đọc lại `anti-ai-rules.md` + HVS resources một lần nữa. **`anti-ai-rules.md` bị đọc 3 lần trong 1 pipeline.**

→ Fix: Bỏ Brand Guardian khỏi pipeline viết bài mới. Main Agent đọc brand files trực tiếp trong Phase 2 (Outline), nhúng toàn bộ brand context vào YAML của Outline. Phase 3 (Draft) chỉ cần đọc Outline — không đọc lại brand files.

Brand Guardian vẫn giữ cho `/optimize` (cần audit độc lập trên bài cũ).

**2. 4 file CSV generic không có giá trị**

| File | Nội dung | Vấn đề |
|------|---------|--------|
| `article-styles.csv` | 12 tone options | All in English, LLM đã biết |
| `search-intent.csv` | 4 dòng định nghĩa intent | Trivial |
| `content-type.csv` | 15 content types | Generic, LLM đã biết |
| `writing-methods.csv` | AIDA, PAS, BAB... | LLM đã biết |

Không file nào được reference trong pipeline thực tế. Xóa bỏ.

**3. `hvs-target-audience.csv` định dạng tệ cho LLM**

CSV lộn xộn, merge cells, khó parse. Agent phải "reason qua" format thay vì đọc trực tiếp. 4 personas với pain points + products mapping nên là Markdown.

**4. 3 skill files QA/QC chồng chéo**

| File | Trạng thái |
|------|-----------|
| `skills/qa-qc/SKILL.md` | Tốt — checklist đầy đủ, có auto-fix loop |
| `skills/internal-audit/SKILL.md` | Overlap — SEO + Brand checklist |
| `skills/brand-compliance/SKILL.md` | Overlap — trích xuất rules |

→ Giữ `qa-qc/SKILL.md`, deprecate 2 cái còn lại.

**5. `agent.md` và rules lỗi thời**

`agent.md` vẫn reference `/detailed`, phase numbering cũ. `detailed-track.md` chỉ có Phase 1-2, thiếu Phase 3-5. `fast-track.md` viết tiếng Anh.

---

### B. Chất lượng bài viết — vấn đề kết quả SEO

**1. Outline chưa embed đủ context cho Draft writer**

Outline hiện tại lưu: Keyword, Persona, Intent, Content Type, Word Count, heading structure.

Chưa lưu: tone chọn, writing method (AIDA/PAS...), specific anti-AI flags cho topic này, HVS products cần nhắc, anchor cho internal links.

→ Khi `/approve` chạy Draft writer, nó phải "suy nghĩ lại" từ đầu thay vì follow instructions rõ ràng.

**2. Writing Method (AIDA, PAS...) chưa được assign**

`writing-methods.csv` tồn tại nhưng không được sử dụng. Pipeline không quyết định "bài này dùng PAS hay AIDA". Kết quả: AI tự chọn, inconsistent.

**3. Persona → Product mapping không explicit**

Brand Guardian phải đọc audience CSV + products folder để suy ra "F0 → HVS Demo". Cần 1 lookup table explicit.

**4. Internal linking dựa trên scan file thô**

Hiện tại scan `3-finalized/` và đọc YAML từng file. Với 11 bài: OK. Với 100 bài: chậm và tốn token.

→ Fix: Dùng `topic-clusters.md` (đã có cluster info + published articles) làm primary source cho linking suggestions. Scan file chỉ để verify slug.

---

## Thiết kế mới

### Command scheme

| Lệnh | Mode | SERP | Human Gates |
|------|------|------|-------------|
| `/write [keyword]` | Express (default) | ✅ | Outline only |
| `/write [keyword] --step` | Guided | ✅ | Outline + Draft |
| `/write [keyword] --auto` | Auto | ✅ | Không |
| `/write [keyword] --no-serp` | Express | ❌ | Outline only |
| `/write [keyword] --step --no-serp` | Guided | ❌ | Outline + Draft |
| `/detailed [keyword]` | → alias → `/write --step` | | |
| `/fast [keyword]` | → alias → `/write --no-serp` | | |

**Mode được lưu vào YAML của Outline/Draft:**
```yaml
Pipeline_Mode: Express   # Express | Guided | Auto
SERP_Research: true      # true | false
```
`/approve` đọc `Pipeline_Mode` để quyết định dừng hay chạy tiếp.

---

### Pipeline tối ưu

```
Phase 0: Pre-flight
  ├─ Duplicate check: progress-log.md (keyword đã tồn tại?)
  └─ Cluster check: topic-clusters.md → Pillar/Cluster role + linking obligations

Phase 1: Context Collection [song song]
  ├─ [IF SERP] SEO Collector Agent:
  │    WebSearch top 5 → WebFetch → extract H1/H2/H3, PAA, Featured Snippet, gaps
  │    Output: SERP Intelligence report
  └─ Main Agent đọc brand files trực tiếp (KHÔNG spawn Brand Guardian):
       resources/brand/brand-brief.md (file MỚI — xem phần Resources bên dưới)
       seo-strategy/resources/content-strategy/anti-ai-rules.md

Phase 2: Tạo Outline
  Kết hợp SERP + Brand Context + Cluster info → Content Brief
  YAML phải chứa đủ:
  ┌─────────────────────────────────────────────────────┐
  │ Target_Keyword, Cluster, Role (Pillar/Cluster)      │
  │ Persona, Tone, Writing_Method                       │
  │ HVS_Products: [sản phẩm cụ thể match persona]      │
  │ Anti_AI_Flags: [từ cấm relevant cho topic này]     │
  │ Word_Count_Target                                   │
  │ Featured_Snippet: Paragraph/List/None               │
  │ Internal_Links: [Pillar slug nếu là Cluster article]│
  │ Pipeline_Mode: Express/Guided/Auto                  │
  │ SERP_Research: true/false                           │
  └─────────────────────────────────────────────────────┘
  Lưu: 1-outlines/Outline-[slug].md
  Hiển thị Outline

[Express/Guided: DỪNG → chờ /approve]
[Auto: tiếp tục Phase 3]

Phase 3: Viết Draft
  Đọc: Outline ONLY (brand context đã embedded trong YAML)
  Viết từng heading theo Content Brief
  Lưu: 2-user-review/Draft-[slug].md

Phase 4: QA/QC Loop
  Đọc: qa-qc/SKILL.md
  Đọc: anti-ai-rules.md (final check)
  Đọc: glossary.md
  Auto-fix → lặp đến PASS
  (KHÔNG đọc lại identity.md, usps.md — đã xử lý trong Phase 2)

Phase 5: Internal Linking
  Input primary: topic-clusters.md (đã trong context từ Phase 0)
  Verify: scan 3-finalized/ để confirm file tồn tại + lấy đúng slug
  Ưu tiên: Pillar link (bắt buộc nếu Cluster article) → Same-cluster → Cross-cluster
  Chèn link (auto hoặc confirm tùy mode)

[Guided: DỪNG → chờ /approve]
[Express/Auto: tiếp tục Phase 6]

Phase 6: Finalize
  Move: 2-user-review/Draft-[slug].md → 3-finalized/Final-[slug].md
  Update YAML: Status: Finalized
  Xóa Draft cũ
  Sync 3 files:
    progress-log.md (Active Pipeline + Publication Log + count)
    topic-clusters.md (⭕/🔄 → ✅ + filename + cluster count)
    sprint-backlog.md (xóa bài vừa xong)
  Báo cáo: keyword | word count | file path | files updated
```

---

### Tối ưu Resources

#### Xóa (không giá trị)
- `seo-strategy/resources/content-strategy/article-styles.csv`
- `seo-strategy/resources/content-strategy/search-intent.csv`
- `seo-strategy/resources/content-strategy/content-type.csv`
- `seo-strategy/resources/content-strategy/writing-methods.csv`

#### Tạo mới: `resources/brand/brand-brief.md`
1 file tổng hợp thay cho việc đọc `identity.md` + `usps.md` + `audience CSV` riêng lẻ. Nội dung:
```
## HVS Brand Summary
[Positioning, voice, giá trị cốt lõi — 5 dòng]

## Persona → Product Map
| Persona | Mô tả ngắn | HVS Products | Tone |
|---------|-----------|-------------|------|
| Sinh viên tài chính | ... | HVS Thực tập số, HVS Demo | Thực chiến, cơ hội nghề nghiệp |
| Sinh viên không tài chính | ... | HVS Thực tập số | Kỹ năng, chứng chỉ |
| F0 - Nhân viên VP mới đầu tư | ... | HVS Demo, HVS Forum | Đơn giản hóa, không mất tiền thật |
| F1 - Đã đầu tư | ... | HVS Tài chính số, Tư vấn số | Hiệu quả, phân tích sâu |

## Writing Method by Intent
| Intent | Method | Lý do |
|--------|--------|-------|
| Informational | 4Cs + PAA structure | Cần clear + credible |
| Commercial | PAS | Dẫn pain → HVS solution |
| How-to | Numbered steps + FAB | Actionable |
| Comparison | BAB hoặc Feature table | Show before/after |
```

#### Convert: `resources/audience/hvs-target-audience.csv` → `resources/audience/personas.md`
Cùng nội dung, format Markdown, dễ đọc hơn.

#### Deprecate (merge vào qa-qc/SKILL.md nếu thiếu)
- `.antigravity/skills/internal-audit/SKILL.md`
- `.antigravity/skills/brand-compliance/SKILL.md`

---

## Files cần tạo / sửa

### Tạo mới
| File | Mô tả |
|------|-------|
| `.claude/commands/write.md` | Main command — 3 modes + 2 flags |
| `.agents/workflows/write.md` | Mirror Antigravity |
| `.antigravity/rules/write-track.md` | Rule mới thay thế detailed-track + fast-track |
| `resources/brand/brand-brief.md` | Tổng hợp brand + persona→product map |
| `resources/audience/personas.md` | Convert từ CSV sang Markdown |

### Chỉnh sửa
| File | Thay đổi |
|------|---------|
| `.claude/commands/detailed.md` | Redirect → `/write --step` |
| `.claude/commands/fast.md` | Redirect → `/write --no-serp` |
| `.agents/workflows/detailed.md` | Redirect tương tự |
| `.agents/workflows/fast.md` | Redirect tương tự |
| `.claude/commands/approve.md` | Mode-aware: đọc `Pipeline_Mode` từ YAML |
| `.agents/workflows/approve.md` | Mirror |
| `.claude/commands/raw.md` | Thêm: cập nhật topic-clusters.md |
| `.agents/workflows/raw.md` | Mirror |
| `.antigravity/agent.md` | Cập nhật commands + phase list |
| `.antigravity/rules/detailed-track.md` | Deprecate → point sang write-track.md |
| `.antigravity/rules/fast-track.md` | Deprecate → point sang write-track.md |
| `.antigravity/skills/internal-linking/SKILL.md` | Ưu tiên topic-clusters.md over raw scan |
| `CLAUDE.md` | Cập nhật Layer 3 commands |

### Xóa
| File | Lý do |
|------|-------|
| `seo-strategy/resources/content-strategy/article-styles.csv` | Generic, không dùng |
| `seo-strategy/resources/content-strategy/search-intent.csv` | Trivial |
| `seo-strategy/resources/content-strategy/content-type.csv` | Generic |
| `seo-strategy/resources/content-strategy/writing-methods.csv` | Generic |

---

## YAML metadata chuẩn mới

### Outline
```yaml
---
Author: Claude Code
Status: Outline
Pipeline_Mode: Express        # Express | Guided | Auto
SERP_Research: true
Persona: F0 - Nhà đầu tư mới
Tone: Conversational + Authoritative
Writing_Method: PAS
Target_Keyword: ETF là gì
Cluster: Phân tích cơ bản
Cluster_Role: Cluster          # Pillar | Cluster
Search_Intent: Informational
Content_Type: Comprehensive Guide
HVS_Products:
  - HVS Demo
  - HVS Forum
Anti_AI_Flags:
  - "Hành trình"
  - "Trong thế giới"
Word_Count_Target: 1800
Featured_Snippet: Paragraph
Internal_Links:
  - Pillar: Final-phan-tich-co-ban-la-gi.md
---
```

### Draft / Final
```yaml
---
Status: Draft | Finalized
Pipeline_Mode: Express
Word_Count_Actual: 1750
---
```

---

## Thứ tự implement

| # | Việc | Phụ thuộc | Effort |
|---|------|-----------|--------|
| 1 | Tạo `resources/brand/brand-brief.md` | Không | Low |
| 2 | Convert `hvs-target-audience.csv` → `personas.md` | Không | Low |
| 3 | Tạo `.antigravity/rules/write-track.md` | #1, #2 | Medium |
| 4 | Tạo `.claude/commands/write.md` + `.agents/workflows/write.md` | #3 | Medium |
| 5 | Update `approve.md` cả 2 hệ thống (mode-aware) | #4 | Low |
| 6 | Update `internal-linking/SKILL.md` (dùng topic-clusters trước) | Không | Low |
| 7 | Update `raw.md` cả 2 hệ thống (topic-clusters sync) | Không | Low |
| 8 | Redirect `detailed.md`, `fast.md` cả 2 hệ thống | #4 | Low |
| 9 | Deprecate `detailed-track.md`, `fast-track.md`, 2 skills | #3 | Low |
| 10 | Xóa 4 CSV generic | Không | Low |
| 11 | Update `agent.md`, `CLAUDE.md` | Tất cả | Low |

---

## Token savings estimate

| Thay đổi | Tiết kiệm mỗi lần chạy `/write` |
|----------|--------------------------------|
| Bỏ Brand Guardian spawn | ~1 Agent overhead + đọc 6 files |
| Outline YAML embed context | `/approve` không cần đọc lại identity + usps + audience |
| Xóa 4 CSV generic | Không bao giờ bị đọc nhầm |
| topic-clusters làm link source | Không phải scan hết 3-finalized/ YAML |
| Consolidate brand-brief.md | 3 reads (identity + usps + audience) → 1 read |

---

## Verify sau implement

```
/write ETF là gì
→ SERP chạy, Outline YAML có đủ fields, dừng chờ /approve

/approve (từ Outline)
→ Đọc Pipeline_Mode=Express → viết Draft → QA → Link → Auto-finalize → sync 3 files

/write cổ phiếu penny là gì --step
→ Outline → dừng → /approve → Draft → dừng → /approve → Final

/write lãi suất vs chứng khoán --auto
→ Chạy thẳng toàn bộ, báo cáo cuối
```
