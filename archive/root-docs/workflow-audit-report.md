# Workflow Audit Report — HVS SEO Content Pipeline

**Ngày kiểm tra:** 2026-05-07  
**Test case:** `/write cổ phiếu là gì --no-serp --auto`  
**File output:** `content/blog/3-finalized/Final-co-phieu-la-gi.md`  
**Người kiểm tra:** Claude Code (Main Agent)

---

## Tóm tắt kết quả

| Phase | Tên | Kết quả | Ghi chú |
|-------|-----|---------|---------|
| 0 | Pre-flight | ✅ PASS | Duplicate check + cluster role OK |
| 1 | Context Collection | ✅ PASS | --no-serp, fallback chain hoạt động |
| 2 | Outline | ✅ PASS | YAML đủ fields, brief đúng template |
| 3 | Draft | ✅ PASS | ~1350 từ, anti-AI clean |
| 4 | QA/QC | ✅ PASS (vòng 2) | 2 items fail → fix targeted → PASS |
| 5 | Internal Linking | ✅ PASS | 4 links, tất cả slug tồn tại |
| 6 | Finalize | ⚠️ PASS* | 3/4 files synced; sprint-backlog.md thiếu |

**Overall: PASS với 8 issues cần xử lý (3 quan trọng, 5 nhỏ)**

---

## Chi tiết từng Phase

### Phase 0 — Pre-flight ✅

- **Duplicate check:** Đọc `progress-log.md` đúng → xác nhận keyword chưa tồn tại ✅
- **Cluster check:** Đọc `topic-clusters.md` đúng → xác định Cluster: Cổ phiếu, Cluster_Role: Cluster, Pillar "Cổ tức là gì" chưa Published → không có mandatory Pillar link ✅
- **Published cluster articles** được ghi nhận đúng để embed vào Linking Plan ✅

### Phase 1 — Context Collection (--no-serp) ✅

- `resources/company/hvs-profile.md` được đọc ✅ (Priority 1 — tồn tại)
- `resources/audience/personas-deep.md` — **KHÔNG TỒN TẠI** → fallback về Priority 3: `hvs-target-audience.csv` + `persona-mapping.md` ✅ fallback hoạt động
- Persona mapping: keyword "cổ phiếu là gì" → F0/NV VP chưa đầu tư ✅
- Product files: `hvs-demo.md` + `hvs-forum.md` ✅ (đúng theo Persona→Product map)
- `anti-ai-rules.md` được đọc ✅

### Phase 2 — Tạo Outline ✅

- Outline lưu tại `content/blog/1-outlines/Outline-co-phieu-la-gi.md` ✅
- YAML đủ tất cả fields bắt buộc (Pipeline_Mode, SERP_Research, Persona, Tone, Writing_Method, HVS_Products, Anti_AI_Flags, Cluster, Cluster_Role, Internal_Links, Featured_Snippet, Word_Count_Target) ✅
- Brief template (`brief-template.md`) được theo đúng 4 phần: YAML / SERP Intelligence / Content Brief / Linking Plan ✅
- Definition Block trong H2 đầu tiên được spec rõ trong Outline ✅

### Phase 3 — Viết Draft ✅

- Đọc **chỉ Outline** — không đọc lại brand files (đã embed trong YAML) ✅ đúng quy trình
- H2 đầu có Definition Block ≤50 từ ✅
- Mỗi H2 có ví dụ cụ thể (VCB, HPG, VNM, con số giá thực) ✅
- HVS section theo PAS format ✅
- Kết bài dùng H2 thay "Tóm lại/Kết luận" ✅
- Không dùng forbidden phrases ✅

### Phase 4 — QA/QC ✅ (sau 1 vòng fix)

**Vòng 1 — 2 items Fail:**

| Item Fail | Vấn đề | Fix |
|-----------|--------|-----|
| H2 "Cổ phiếu khác trái phiếu" | Không có ví dụ cụ thể với con số | Thêm: "trái phiếu 9%/năm vs VNM" |
| CTA format | "Mở tài khoản HVS Demo" ≠ chuẩn glossary | Đổi thành "Thử ngay HVS Demo" |

**Vòng 2:** All items ✅ PASS — đúng mục tiêu ≤2 vòng

### Phase 5 — Internal Linking ✅

| Link | Anchor | Vị trí | Slug verify |
|------|--------|---------|-------------|
| Cross-cluster | "chứng khoán" | H2 "Cổ phiếu là gì" | ✅ tồn tại |
| Same-cluster | "cổ phiếu penny" | H2 "Các loại cổ phiếu" | ✅ tồn tại |
| Cross-cluster | "trái phiếu" | H2 "Khác trái phiếu" | ✅ tồn tại |
| Same-cluster | "nên đầu tư cổ phiếu nào" | Kết bài | ✅ tồn tại |

Không có URL xuất hiện 2 lần ✅. Anchor text tự nhiên trong câu ✅.

### Phase 6 — Finalize ⚠️

- `Final-co-phieu-la-gi.md` moved → `3-finalized/` ✅
- YAML `Status: Finalized` ✅
- Draft xóa tại `2-user-review/` ✅
- `progress-log.md`: +1 vào Publication Log, Dashboard count 12→13 ✅
- `topic-clusters.md`: ⭕ → ✅, cluster count 2→3 ✅
- `sprint-backlog.md`: **FILE KHÔNG TỒN TẠI** — bỏ qua ⚠️
- **Content Feedback Loop:** Fresh article không có Revision Log → skip (đúng) ✅

---

## Issues Tìm Thấy

### 🔴 Quan trọng (cần fix để tránh lỗi workflow)

**Issue 1: Path sai trong `seo-collector.md` và `AGENTS.md`**

Cả hai file dùng path `.agent/` thay vì `.antigravity/`:

| File | Path sai | Path đúng |
|------|----------|-----------|
| `seo-collector.md` line 13 | `.agent/skills/seo-research/SKILL.md` | `.antigravity/skills/seo-research/SKILL.md` |
| `AGENTS.md` line 9 | `.agent/agents/seo-collector.md` | `.antigravity/agents/seo-collector.md` |
| `AGENTS.md` line 14 | `.agent/agents/brand-guardian.md` | `.antigravity/agents/brand-guardian.md` |
| `AGENTS.md` line 19 | `.agent/agents/quality-guardian.md` | `.antigravity/agents/quality-guardian.md` |
| `AGENTS.md` line 25 | `.agent/docs/structure.md` | `.antigravity/rules/structure.md` |

**Tác động:** SEO Collector sub-agent sẽ fail khi cố đọc seo-research/SKILL.md theo path cũ. Bất kỳ agent nào đọc AGENTS.md để tìm đường đến sub-agents cũng sẽ bị sai.

---

**Issue 2: `resources/audience/personas-deep.md` không tồn tại**

`write-track.md` định nghĩa priority chain cho Personas:
1. `resources/audience/personas-deep.md` ← `/setup audience` — **FILE NÀY KHÔNG TỒN TẠI**
2. `resources/audience/icp.md` ← bổ sung — **FILE NÀY KHÔNG TỒN TẠI**
3. `resources/audience/hvs-target-audience.csv` ← fallback

Hệ thống đang chạy **100% trên fallback** (Priority 3) vì Priority 1 và 2 chưa được `/setup audience` tạo ra. Persona data trong csv khá sơ sài so với `personas-deep.md` sẽ có sau khi chạy `/setup`. Đây không phải lỗi crash nhưng ảnh hưởng đáng kể đến chất lượng persona targeting.

**Khuyến nghị:** Chạy `/setup audience` để tạo `personas-deep.md`.

---

**Issue 3: `seo-strategy/content-plan/sprint-backlog.md` không tồn tại**

`write-track.md` Phase 6 bước 4 yêu cầu:
> `sprint-backlog.md`: xóa bài vừa finalize (nếu có)

CLAUDE.md cũng list đây là resource quan trọng. File chưa được tạo. Phase 6 skip bước này silently (do "(nếu có)" trong write-track). Về lâu dài, nếu workflow `/keyword-plan` được dùng để tạo sprint backlog thì Phase 6 sẽ không clean up đúng cách.

---

### 🟡 Nhỏ (stale references, không ảnh hưởng ngay)

**Issue 4: `content-feedback-loop/SKILL.md` reference lệnh cũ**

Dòng cuối SKILL.md: 
> "Every time `/fast`, `/detailed`, or `/optimize` is triggered, the agent **MUST** read `anti-ai-rules.md`"

`/fast` và `/detailed` đã deprecated (giờ là `/write --no-serp` và `/write --step`). Cần update thành `/write`.

---

**Issue 5: `seo-collector.md` description outdated**

Frontmatter:
```yaml
description: Phân tích SERP & Intent tại Phase 1 của @detailed-track.md. Kích hoạt khi User dùng lệnh `/detailed`.
```

`/detailed` đã deprecated. `detailed-track.md` đã được replace bởi `write-track.md`. Description nên update.

---

**Issue 6: `AGENTS.md` thiếu Research Agent**

`AGENTS.md` list 3 agents (SEO Collector, Brand Guardian, Quality Guardian) nhưng `agent.md` (Project Knowledge Hub) và `CLAUDE.md` đều mention **Research Agent** là agent thứ 4. File `research-agent.md` tồn tại trong `.antigravity/agents/` nhưng không được list trong AGENTS.md.

---

**Issue 7: `resources/market/` không tồn tại**

`write-track.md` và `seo-collector.md` đều reference `resources/market/market-landscape.md`. Thư mục `resources/market/` chưa được tạo. Cả hai file đều có điều kiện "nếu tồn tại" nên không crash. Nhưng nếu `/setup market` được chạy, cần biết đây là path target.

---

**Issue 8: Không có clear trigger cho Content Feedback Loop với fresh articles**

`content-feedback-loop/SKILL.md` step 1 nói "đọc Revision Log cuối file". Fresh articles không có Revision Log. write-track.md Phase 6 nói "đọc Revision Log cuối file (nếu có)". Cần document rõ hơn trong SKILL.md: fresh article → skip feedback loop.

---

## Files Được Gọi Đúng vs Bị Bỏ Qua

| File | Được gọi? | Ghi chú |
|------|-----------|---------|
| `.antigravity/rules/write-track.md` | ✅ | Core pipeline, đọc đầu tiên |
| `.antigravity/skills/seo-research/examples/brief-template.md` | ✅ | Tạo Outline |
| `resources/company/hvs-profile.md` | ✅ | Company context |
| `resources/audience/hvs-target-audience.csv` | ✅ | Persona fallback |
| `.antigravity/skills/keyword-management/resources/persona-mapping.md` | ✅ | Persona fallback |
| `resources/products/hvs-demo.md` | ✅ | Product context |
| `resources/products/hvs-forum.md` | ✅ | Product context |
| `seo-strategy/resources/content-strategy/anti-ai-rules.md` | ✅ | Phase 1 + QA |
| `seo-strategy/content-plan/topic-clusters.md` | ✅ | Phase 0 + Phase 5 |
| `seo-strategy/content-plan/progress-log.md` | ✅ | Phase 0 + Phase 6 |
| `.antigravity/skills/qa-qc/SKILL.md` | ✅ | Phase 4 |
| `.antigravity/skills/internal-linking/SKILL.md` | ✅ | Phase 5 |
| `seo-strategy/resources/content-strategy/glossary.md` | ✅ | Phase 4 |
| `resources/audience/personas-deep.md` | ❌ | Không tồn tại → fallback OK |
| `resources/audience/icp.md` | ❌ | Không tồn tại → fallback OK |
| `resources/market/market-landscape.md` | ❌ | Không tồn tại → skip (--no-serp anyway) |
| `seo-strategy/content-plan/sprint-backlog.md` | ❌ | Không tồn tại → skip phase 6 bước 4 |
| `.antigravity/skills/content-feedback-loop/SKILL.md` | ⚠️ | Đọc nhưng skip vì no Revision Log |
| `resources/company/identity.md` + `usps.md` | ❌ | Không cần — hvs-profile.md tồn tại |
| `.antigravity/agents/seo-collector.md` | ❌ | Không cần — flag --no-serp |

---

## Edge Cases Phát Hiện

### Edge Case 1: Fallback Chain không có intermediate level
Khi `personas-deep.md` thiếu, system nhảy thẳng từ Priority 1 xuống Priority 3 (không có Priority 2 `icp.md`). Vẫn hoạt động, nhưng nếu chỉ có Priority 2 tồn tại thì có thể bị miss.

### Edge Case 2: Auto mode + Pillar chưa Published
Bài "cổ phiếu là gì" là Cluster article nhưng Pillar ("Cổ tức là gì") chưa Published. write-track.md không có rule rõ cho case này (chỉ có rule cho Cluster article với Pillar đã Published). Xử lý hiện tại: ghi nhận trong YAML, không chèn mandatory Pillar link. Đây là behavior hợp lý nhưng chưa được document.

### Edge Case 3: Content Feedback Loop không trigger với fresh article
Fresh article không có Revision Log → feedback loop skip hoàn toàn. Đây là expected behavior nhưng SKILL.md không document điều này — developer mới có thể hiểu nhầm rằng feedback loop luôn chạy.

### Edge Case 4: sprint-backlog.md thiếu trong Phase 6
Phase 6 yêu cầu sync 3 files nhưng có 4 files được nhắc đến (progress-log, topic-clusters, sprint-backlog, và implicit là content-feedback-loop). sprint-backlog vắng mặt không crash workflow nhờ "(nếu có)", nhưng cần tạo file này để workflow đầy đủ.

---

## Đánh Giá Chất Lượng Bài Viết Output

| Tiêu chí | Đánh giá | Chi tiết |
|----------|----------|---------|
| Word count | ~1,380 từ | Gần đạt target 1,400 ✅ |
| Anti-AI | Sạch | Không có forbidden phrases |
| Specificity | Cao | VCB, HPG, VNM, giá thực tế, % cụ thể |
| Internal links | 4 links | Tự nhiên trong câu ✅ |
| HVS integration | Đúng PAS | Benefit-first, không quảng cáo trực tiếp |
| Persona fit | F0 | Tone Conversational + Authoritative ✅ |
| Featured Snippet | Có | Definition Block H2 đầu ≤50 từ ✅ |

---

## Khuyến Nghị Ưu Tiên

### Làm ngay (blocker cho /write --serp):
1. **Fix paths trong `seo-collector.md` và `AGENTS.md`** — `.agent/` → `.antigravity/`

### Làm sớm (cải thiện chất lượng output):
2. **Chạy `/setup audience`** — tạo `personas-deep.md` để thay thế fallback csv
3. **Tạo `sprint-backlog.md`** — để Phase 6 sync đầy đủ

### Làm khi có thời gian (housekeeping):
4. Update description trong `seo-collector.md` frontmatter (thay /detailed → /write --step)
5. Update `content-feedback-loop/SKILL.md` (thay /fast, /detailed → /write)
6. Thêm Research Agent vào `AGENTS.md`
7. Document edge case "Cluster article khi Pillar chưa Published" trong write-track.md
8. Chạy `/setup market` để tạo `resources/market/market-landscape.md` (cải thiện SERP collection)

---

## Files Changed trong Test Run

| File | Thay đổi |
|------|---------|
| `content/blog/1-outlines/Outline-co-phieu-la-gi.md` | Tạo mới |
| `content/blog/3-finalized/Final-co-phieu-la-gi.md` | Tạo mới |
| `seo-strategy/content-plan/progress-log.md` | Dashboard +1, thêm dòng Publication Log |
| `seo-strategy/content-plan/topic-clusters.md` | Cluster count update, ⭕ → ✅ |
