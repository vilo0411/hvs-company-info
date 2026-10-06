---
name: cluster
description: Tạo/cập nhật Topic Cluster map từ keyword-hvs.csv, hoặc gom raw keywords Ahrefs/Semrush/GKP. Args: [csv-path] | raw <file>
---

# /cluster

Skill: `.antigravity/skills/keyword-clustering/SKILL.md`. Output: `seo-strategy/content-plan/topic-clusters.md` (format bullet — `topic_status.py` phụ thuộc, **không đổi format**).

## Mode 1 — CSV chuẩn (mặc định `seo-strategy/keywords/keyword-hvs.csv`)

Cột: `Main Topic 1`, `Subtopic 2`, `Subtopic 3`, `Subtopic 4 / Individual Page`, `Keyword`, `Search Volume`, `Tiêu đề`, `Đối tượng`. Không có `Status` — trạng thái lấy từ file Final.

1. Đọc CSV bằng Python (UTF-8; fallback `cp1258`). Báo cột thiếu trước khi chạy.
2. Group: `Subtopic 2` → Group, `Subtopic 3` → Cluster, mỗi `Keyword` → 1 dòng. Pillar = keyword ngắn nhất/volume cao nhất trong cluster.
3. Trạng thái: `Final-<slug>.md` tồn tại → ✅; Draft/Outline tồn tại → 🔄; còn lại ⭕.
4. **Merge, không ghi đè**: dòng đã có trong `topic-clusters.md` giữ nguyên trạng thái; chỉ thêm dòng mới vào đúng cluster (`python scripts/topic_status.py --add "<kw>" --cluster "<tên>"` cho từng dòng mới, hoặc ghi batch rồi `--recount`).
5. `python scripts/topic_status.py --recount`.
6. Báo: tổng cluster, coverage %, top 5 cluster thiếu Pillar.

## Mode 2 — `raw <file>` (Ahrefs / Semrush / GKP)

Detect theo header (`Parent Topic` = Ahrefs, `Intent` = Semrush, `Avg. monthly searches` = GKP) → gom theo topic noun → ghi **draft** `seo-strategy/keywords/draft-clusters-<YYYY-MM-DD>.md`. Không đụng `topic-clusters.md` — user review rồi chạy Mode 1.

## Format dòng (bắt buộc giữ)

```
### Cluster: <tên> (N articles | ✅ a | 🔄 b | ⭕ c)
**Pillar:** ✅ <kw> *(Published — Final-<slug>.md)*
**Priority 1:**
- ⭕ <kw> *(Planned)*
```
