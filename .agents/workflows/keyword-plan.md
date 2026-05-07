---
description: "Sprint Planner — fill sprint lên đủ N active items từ topic cluster map"
---

Khởi chạy **Sprint Planner** — trả lời "Tôi cần thêm bao nhiêu bài nữa để đủ N active?"

**Cách dùng:**
```
/keyword-plan               → Fill sprint lên đủ 5 active items
/keyword-plan 10            → Fill sprint lên đủ 10 active items
/keyword-plan F0            → Fill sprint lên đủ 5, ưu tiên persona F0
/keyword-plan 10 F0         → Fill sprint lên đủ 10, ưu tiên persona F0
```

**Prerequisite:** Phải chạy `/cluster` trước để có `seo-strategy/content-plan/topic-clusters.md`.
Nếu chưa có → nhắc user chạy `/cluster` trước.

---

## Steps

1. Parse args:
   - Nếu có số → `TARGET = số đó`, else `TARGET = 5`
   - Nếu có persona string → lưu làm filter

2. Đọc `seo-strategy/content-plan/sprint-backlog.md`:
   - Đếm `ACTIVE = số item có Status ∈ {Planned, Outline-Pending, Outline-Approved}`
   - Nếu `ACTIVE >= TARGET` → thông báo "Sprint đã đủ N active items, không cần thêm" → DỪNG

3. `NEED = TARGET - ACTIVE`

4. Đọc `seo-strategy/content-plan/topic-clusters.md` và `seo-strategy/content-plan/progress-log.md`:
   - Loại bỏ: ✅ Published, 🔄 In Progress, keywords đã có trong sprint-backlog

5. Score các bài còn lại:

   | Tiêu chí | Điểm | Lý do |
   |----------|------|-------|
   | Priority 1 trong cluster | +2 | User đã đánh dấu |
   | Là Pillar của cluster chưa có Pillar | +3 | SEO impact cao nhất |
   | Là Pillar nhưng cluster đã có Pillar | +1 | |
   | Cluster article — cluster đã có Pillar | +1 | Build cluster strength |
   | Cluster article — cluster chưa có Pillar | 0 | Delay until Pillar written |
   | Persona match với filter | +1 | Tập trung |

6. Lấy top `NEED` bài có điểm cao nhất

7. **Append** vào `seo-strategy/content-plan/sprint-backlog.md` — **không ghi đè**, thêm dòng mới với `Status: Planned`
   - `#` = tiếp nối số thứ tự cuối trong backlog

8. Hiển thị kết quả

---

## Output format

```markdown
## Sprint Update — [date]

Active hiện tại: X / TARGET
Thêm mới: NEED bài

| # | Keyword | Cluster | Loại | Lý do chọn | Status |
|---|---------|---------|------|------------|--------|
| N+1 | phân tích cơ bản là gì | Phân tích cơ bản | Pillar | Cluster 115 bài, chưa có Pillar | Planned |
| N+2 | ROE là gì | Phân tích cơ bản | Cluster | Priority 1, Pillar ở trên | Planned |

Cluster coverage tổng thể:
| Cluster | Total | Published | % |
|---------|-------|-----------|---|
| Phân tích cơ bản | 115 | 1 | 0.9% |

Bước tiếp: /write --sprint   (generate tất cả outlines batch)
```

---

## Về keyword discovery mới

**Không dùng WebSearch để tìm keyword** — agent không có volume data thật.

Khi cần thêm keywords mới:
- Export từ Ahrefs/Semrush → `/cluster raw [file]` → review → `/cluster [csv]`
- Export từ GKP → `/cluster raw [file]` → SERP check theo bucket → `/cluster [csv]`
