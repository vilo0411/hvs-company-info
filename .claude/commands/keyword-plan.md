---
description: "Sprint Planner — chọn N bài nên viết tiếp từ topic cluster map (không dùng WebSearch)"
allowed-tools: Read, Write, Bash
---

Khởi chạy **Sprint Planner** — trả lời "Tôi cần thêm bao nhiêu bài nữa để đủ N active?"

**Cách dùng:**
```
/keyword-plan               → Fill sprint lên đủ 5 active items
/keyword-plan 10            → Fill sprint lên đủ 10 active items
/keyword-plan F0            → Fill sprint lên đủ 5, ưu tiên persona F0
/keyword-plan 10 F0         → Fill sprint lên đủ 10, ưu tiên persona F0
```

`$ARGUMENTS` — số lượng target (default 5) và/hoặc persona filter.

**Prerequisite:** Phải có `seo-strategy/content-plan/topic-clusters.md`. Nếu chưa → nhắc chạy `/cluster` trước.

---

## Steps

1. Parse `$ARGUMENTS`:
   - Nếu có số → `TARGET = số đó`, else `TARGET = 5`
   - Nếu có persona string (F0, sinh-vien, nha-dau-tu...) → lưu làm filter

2. Đọc `seo-strategy/content-plan/sprint-backlog.md`:
   - Đếm `ACTIVE = số item có Status ∈ {Planned, Outline-Pending, Outline-Approved}`
   - Nếu `ACTIVE >= TARGET` → thông báo "Sprint đã đủ N active items, không cần thêm" → DỪNG

3. `NEED = TARGET - ACTIVE`

4. Đọc `seo-strategy/content-plan/topic-clusters.md` và `seo-strategy/content-plan/progress-log.md`:
   - Loại bỏ: ✅ Published, 🔄 In Progress, keywords đã có trong sprint-backlog

5. Score các bài còn lại:

   | Tiêu chí | Điểm |
   |----------|------|
   | Priority 1 trong cluster | +2 |
   | Pillar — cluster chưa có Pillar | +3 |
   | Pillar — cluster đã có Pillar | +1 |
   | Cluster article — cluster đã có Pillar | +1 |
   | Cluster article — cluster chưa có Pillar | 0 |
   | Persona match với filter | +1 |

6. Lấy top `NEED` bài có điểm cao nhất

7. **Append** vào `seo-strategy/content-plan/sprint-backlog.md` — **không ghi đè**, chỉ thêm dòng mới với `Status: Planned`
   - `#` = tiếp nối số thứ tự cuối cùng trong backlog

8. Hiển thị kết quả

---

## Output format

```
## Sprint Update — [date]

Active hiện tại: X / TARGET
Thêm mới: NEED bài

| # | Keyword | Cluster | Loại | Lý do chọn | Status |
|---|---------|---------|------|------------|--------|
| N+1 | ... | ... | Pillar | Cluster 115 bài, chưa có Pillar | Planned |
| N+2 | ... | ... | Cluster | Priority 1, Pillar ở #N+1 | Planned |

Cluster coverage tổng thể:
| Cluster | Total | Published | % |
|---------|-------|-----------|---|
| ... | ... | ... | ... |

Bước tiếp: /write --sprint   (generate tất cả outlines batch)
```

---

## Giới hạn

Không dùng WebSearch để tìm keyword mới — không có volume data thật.
Khi cần thêm keywords: export Ahrefs/Semrush → `/cluster raw [file]`.
