---
description: "Viết bài SEO — Express / Guided (--step) / Auto (--auto) / Batch (--sprint [--flush])"
---

Khởi chạy pipeline viết bài SEO.

**Single keyword modes:**
```
/write ETF là gì                 → Express: duyệt Outline → AI tự hoàn thiện
/write ETF là gì --step          → Guided: duyệt Outline + duyệt Draft
/write ETF là gì --auto          → Auto: không duyệt, chạy thẳng đến Final
/write ETF là gì --no-serp       → Express, bỏ SERP research
```

**Batch sprint modes:**
```
/write --sprint                  → Generate outlines cho tất cả Planned items (--no-serp mặc định)
/write --sprint --with-serp      → Như trên nhưng có SERP research (chậm hơn)
/write --sprint --flush          → Viết tất cả Outline-Approved items → Final
```

Nếu không có args → hỏi user keyword cần viết.

Parse args: Keyword = text trước flags. Flags: `--step` / `--auto` / `--no-serp` / `--sprint` / `--flush` / `--with-serp`.

Đọc `.antigravity/rules/write-track.md` để nắm toàn bộ quy trình.

---

## Sprint Mode — `--sprint`

**Mục đích:** Generate outlines hàng loạt cho tất cả `Planned` items. Chạy unattended.

1. Đọc `seo-strategy/content-plan/sprint-backlog.md`
2. Filter: lấy tất cả item có `Status: Planned`
3. Nếu rỗng → "Không có item Planned. Chạy `/keyword-plan N` để thêm." → DỪNG
4. SERP: mặc định `false` trừ khi có `--with-serp`
5. Với mỗi keyword (tuần tự):
   - Phase 0 + Phase 1 + Phase 2
   - Lưu `content/blog/1-outlines/Outline-[slug].md`
   - Update sprint-backlog: `Planned` → `Outline-Pending`
   - Log: "✅ [N/Total] Outline-[slug].md"
6. Summary + hướng dẫn review

---

## Sprint Flush Mode — `--sprint --flush`

**Mục đích:** Viết tất cả bài đã approve outline. Chạy unattended.

1. Đọc `seo-strategy/content-plan/sprint-backlog.md`
2. Filter: lấy tất cả item có `Status: Outline-Approved`
3. Nếu rỗng → "Không có Outline-Approved. Review `1-outlines/` → đổi Status." → DỪNG
4. Update các item được chọn: → `Status: Writing`
5. Với mỗi keyword (tuần tự):
   - Đọc `content/blog/1-outlines/Outline-[slug].md`
   - Phase 3 → Phase 4 → Phase 5 → Phase 6
   - Phase 6 xóa item khỏi sprint-backlog
   - Log: "✅ [N/Total] Final-[slug].md (X từ)"
6. Summary: N bài hoàn thành, danh sách file paths

---

## Phase 0: Pre-flight

1. Đọc `seo-strategy/content-plan/progress-log.md` → duplicate check
2. Đọc `seo-strategy/content-plan/topic-clusters.md` (nếu có) → Pillar/Cluster role + linking obligations

## Phase 1: Context Collection

**Nếu --no-serp:** Main Agent đọc brand + persona files trực tiếp (priority: personas-deep.md → fallback CSV). Xác định Persona → đọc 1-2 product files phù hợp.

**Nếu SERP:** Chạy song song:
- **SEO Collector Agent**: market-landscape.md (nếu có) → WebSearch + WebFetch top 5 → SERP Intelligence
- **Main Agent**: đọc company + persona + product files + anti-ai-rules.md

## Phase 2: Tạo Outline

Kết hợp context → Content Brief theo template `.antigravity/skills/seo-research/examples/brief-template.md`.
YAML đủ fields: Pipeline_Mode, Persona, Tone, Writing_Method, HVS_Products (benefit-first), Anti_AI_Flags, Cluster info, Featured_Snippet, Word_Count_Target.

Lưu: `content/blog/1-outlines/Outline-[slug].md`
Trình bày Outline.

**→ Express / Guided: DỪNG — chờ /approve**
**→ Auto: tiếp tục Phase 3–6**
