---
name: keyword-plan
description: Sprint Planner — chọn N bài nên viết tiếp từ cluster map (+ tín hiệu SERP nếu có cache). Args: [N] [persona]
---

# /keyword-plan [N=5] [persona]

Không dùng WebSearch tìm keyword mới (không có volume thật). Cần keyword mới → `/cluster raw <file>`.

## Bước 1 — Hiện trạng

```
python scripts/sprint_status.py --list           # ACTIVE = Planned + Outline-Pending + Outline-Approved + Writing
python scripts/sprint_status.py --sync           # loại row stale
```
`ACTIVE ≥ N` → "Sprint đã đủ" → DỪNG. `NEED = N − ACTIVE`.

## Bước 2 — Ứng viên

```
python scripts/topic_status.py --list Planned --json
python scripts/serp_opportunities.py             # nếu có cache SERP → serp-opportunities.md (PAA chưa có bài)
```
Loại bỏ: đã ✅/🔄, đã trong backlog.

## Bước 3 — Chấm điểm

| Tiêu chí | Điểm |
|---|---|
| Pillar của cluster chưa có Pillar | +3 |
| Priority 1 | +2 |
| Cluster đã có Pillar (bài vệ tinh dễ link) | +1 |
| Persona khớp filter | +1 |
| Có trong `serp-opportunities.md` §1 (PAA chưa ai giữ) | +1 |

## Bước 4 — Ghi

Với mỗi bài chọn: `python scripts/sprint_status.py --add "<kw>" --cluster "<tên>" --persona "<P>" [--type "Priority 1"]`.

## Output

```
## Sprint Update — <date>
Active: X / N · Thêm: NEED
| # | Keyword | Cluster | Loại | Lý do | Status |
Coverage: | Cluster | Total | Published | % |
Bước tiếp: /write --sprint
```
