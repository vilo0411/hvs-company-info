---
description: "Viết bài SEO — Express / Guided (--step) / Auto (--auto) / Batch (--sprint [--flush])"
---

Khởi chạy pipeline viết bài SEO.

**Single keyword modes:**
```
/write ETF là gì                 → Express (CÓ SERP research) → Duyệt Outline → Auto-finalize
/write ETF là gì --step          → Guided (CÓ SERP research) → Duyệt Outline → Duyệt Draft
/write ETF là gì --auto          → Auto (CÓ SERP research) → Không dừng, chạy thẳng Final
/write ETF là gì --no-serp       → Bỏ qua SERP research (chỉ dùng khi keyword quá đơn giản)
```

**Batch sprint modes:**
```
/write --sprint                  → Generate outlines cho tất cả Planned items (--no-serp mặc định)
/write --sprint --with-serp      → Như trên nhưng có SERP research
/write --sprint --flush          → Viết tất cả Outline-Approved items → Final
```

Nếu không có args → hỏi user keyword cần viết.

Parse args: Keyword = text trước flags. Flags: `--step` / `--auto` / `--no-serp` / `--sprint` / `--flush` / `--with-serp`.

**Toàn bộ quy trình xử lý chi tiết → đọc `.antigravity/rules/write-track.md`.**

---

## Sprint Mode — `--sprint`

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

1. Đọc `seo-strategy/content-plan/sprint-backlog.md`
2. Filter: lấy tất cả item có `Status: Outline-Approved`
3. Nếu rỗng → "Không có Outline-Approved. Review `1-outlines/` → đổi Status." → DỪNG
4. Update các item được chọn: → `Status: Writing`
5. Với mỗi keyword (tuần tự):
   - Đọc `content/blog/1-outlines/Outline-[slug].md`
   - Phase 3 → Phase 4 → Phase 5
   - Xóa item khỏi sprint-backlog sau Phase 5
   - Log: "✅ [N/Total] Final-[slug].md (X từ)"
6. Summary: N bài hoàn thành, danh sách file paths
