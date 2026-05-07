---
description: "Viết bài SEO. Args: [keyword] [--step] [--auto] [--no-serp] | --sprint [--flush] [--with-serp]"
allowed-tools: WebSearch, WebFetch, Read, Write, Bash, Agent
---

Khởi chạy pipeline viết bài SEO cho: **$ARGUMENTS**

**Single keyword modes:**
```
/write ETF là gì                     → Express: duyệt Outline → AI tự hoàn thiện
/write ETF là gì --step              → Guided: duyệt Outline + duyệt Draft
/write ETF là gì --auto              → Auto: không duyệt, chạy thẳng đến Final
/write ETF là gì --no-serp           → Express, bỏ SERP research
/write ETF là gì --step --no-serp    → Guided, bỏ SERP research
```

**Batch sprint modes:**
```
/write --sprint                      → Generate outlines cho tất cả Planned items (--no-serp mặc định)
/write --sprint --with-serp          → Như trên nhưng có SERP research (chậm hơn)
/write --sprint --flush              → Viết tất cả Outline-Approved items → Final
```

Nếu `$ARGUMENTS` trống → hỏi user keyword cần viết.

Parse `$ARGUMENTS`:
- Nếu có `--sprint` → chạy **Sprint Mode** (xem bên dưới)
- Nếu không có `--sprint`:
  - Keyword = phần text trước flags
  - `--step` → `Pipeline_Mode: Guided`
  - `--auto` → `Pipeline_Mode: Auto`
  - `--no-serp` → `SERP_Research: false`
  - Mặc định → `Pipeline_Mode: Express`, `SERP_Research: true`

Đọc `.antigravity/rules/write-track.md` để nắm toàn bộ pipeline.

---

## Sprint Mode — `/write --sprint`

**Mục đích:** Generate outlines hàng loạt cho tất cả `Planned` items trong sprint backlog. Chạy unattended — user review sau trong `1-outlines/`.

### Steps:

1. Đọc `seo-strategy/content-plan/sprint-backlog.md`
2. Filter: lấy tất cả item có `Status: Planned`
3. Nếu không có item nào → thông báo "Không có item Planned. Chạy `/keyword-plan N` để thêm." → DỪNG
4. SERP flag: mặc định `--no-serp` trừ khi có `--with-serp`
5. **Với mỗi keyword** (chạy tuần tự):
   a. Phase 0: duplicate check + cluster check
   b. Phase 1: context collection (theo SERP flag)
   c. Phase 2: tạo Outline → lưu `content/blog/1-outlines/Outline-[slug].md`
   d. Cập nhật sprint-backlog: Status `Planned` → `Outline-Pending`
   e. Log tiến độ: "✅ [N/Total] Outline-[slug].md"
6. Summary: "Đã tạo N outlines. Review tại `1-outlines/` → đổi Status thành `Outline-Approved` → chạy `/write --sprint --flush`"

**Không dừng để chờ approve** — toàn bộ outline được generate liên tiếp.

---

## Sprint Flush Mode — `/write --sprint --flush`

**Mục đích:** Viết tất cả bài đã được approve outline. Chạy unattended.

### Steps:

1. Đọc `seo-strategy/content-plan/sprint-backlog.md`
2. Filter: lấy tất cả item có `Status: Outline-Approved`
3. Nếu không có item nào → thông báo "Không có item Outline-Approved. Review outlines trong `1-outlines/` → đổi Status." → DỪNG
4. Cập nhật sprint-backlog: các item được chọn → `Status: Writing`
5. **Với mỗi keyword** (chạy tuần tự):
   a. Đọc `content/blog/1-outlines/Outline-[slug].md`
   b. Phase 3: viết Draft (dựa hoàn toàn vào Outline YAML — không cần đọc lại brand files)
   c. Phase 4: QA/QC
   d. Phase 5: Internal Linking
   e. Phase 6: Finalize → xóa item khỏi sprint-backlog
   f. Log tiến độ: "✅ [N/Total] Final-[slug].md ([word count] từ)"
6. Summary: N bài hoàn thành, danh sách file paths

---

## Phase 0: Pre-flight (Single keyword)

1. **Duplicate check** — đọc `seo-strategy/content-plan/progress-log.md`:
   - Keyword đã Published hoặc In Progress → DỪNG, thông báo file path

2. **Cluster check** — đọc `seo-strategy/content-plan/topic-clusters.md` (nếu tồn tại):
   - Xác định: Pillar hay Cluster article?
   - Nếu Cluster: ghi nhận Pillar file để embed vào Linking Plan
   - Nếu Pillar: ghi nhận Published cluster articles để link xuống

---

## Phase 1: Context Collection

**Nếu `--no-serp`:** Main Agent đọc trực tiếp brand + persona files (xem priority trong write-track.md), xác định Persona → đọc 1-2 product files phù hợp.

**Nếu có SERP:** Chạy song song:

**Agent: SEO Collector** (`.antigravity/agents/seo-collector.md`):
- Nếu `resources/market/market-landscape.md` tồn tại → đọc Competitor section trước
- WebSearch + WebFetch top 5 → SERP Intelligence report

**Main Agent** (đồng thời với Agent trên):
- Đọc company file: `resources/company/hvs-profile.md` nếu có, else `identity.md` + `usps.md`
- Đọc persona file: `resources/audience/personas-deep.md` nếu có, else `hvs-target-audience.csv` + `persona-mapping.md`
- Xác định Persona phù hợp keyword → đọc 1-2 product files trong `resources/products/`
- Đọc `seo-strategy/resources/content-strategy/anti-ai-rules.md`

---

## Phase 2: Tạo Outline

Kết hợp SERP Intelligence + Brand/Persona context + Cluster info → tạo Content Brief theo `.antigravity/skills/seo-research/examples/brief-template.md`.

YAML phải có đủ: `Pipeline_Mode`, `SERP_Research`, `Persona`, `Tone`, `Writing_Method`, `HVS_Products` (benefit-first), `Anti_AI_Flags`, `Cluster`, `Cluster_Role`, `Internal_Links`, `Featured_Snippet`, `Word_Count_Target`.

Lưu: `content/blog/1-outlines/Outline-[slug].md`
Trình bày Outline.

**→ Express / Guided: DỪNG — chờ `/approve`**
**→ Auto: tiếp tục Phase 3–6 tự động**
