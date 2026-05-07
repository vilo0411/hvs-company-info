---
description: "Tạo Topic Cluster map từ CSV đã grouped, hoặc gom nhóm raw keywords từ Ahrefs/Semrush/GKP"
allowed-tools: Read, Write, Bash
---

Tạo **Topic Cluster Map** — content management system cho toàn bộ bài viết dự kiến.

**Cách dùng:**
```
/cluster                          → Mode 1: CSV chuẩn (default path)
/cluster [csv-path]               → Mode 1: CSV tùy chỉnh
/cluster raw [file]               → Mode 2: raw export từ Ahrefs/Semrush/GKP
```

`$ARGUMENTS` — nếu trống: Mode 1 với default CSV. Nếu bắt đầu bằng "raw": Mode 2.

---

## Prerequisite — CSV encoding

File gốc `Nghiên cứu từ khóa - HVS Tư vấn số.csv` có thể bị lỗi encoding (Vietnamese chars thành `?`).

**Giải pháp tốt nhất:** Re-export từ Google Sheets → File → Download → CSV UTF-8 → lưu tại `seo-strategy/keywords/keywords.csv`.

Nếu chưa có `keywords.csv`, đọc file gốc bằng Python:
```python
import csv, io
with open(filepath, 'rb') as f:
    raw = f.read()
text = raw.decode('cp1258')
reader = csv.reader(io.StringIO(text))
rows = list(reader)
```

---

## Mode 1: CSV Import

**Khi nào dùng:** CSV từ Google Sheets đã có cấu trúc 4-cấp (user đã gom nhóm thủ công).

**Columns được nhận biết** (dùng header name, không dùng vị trí cố định):

| Column | Vai trò | Nếu thiếu |
|--------|---------|-----------|
| `Subtopic 3` hoặc tên tương đương | Cluster name | ❌ Không chạy được — báo user |
| `Subtopic 4 / Individual Page` hoặc `Keyword` | Article title | ❌ Không chạy được — báo user |
| `Status` | Published / In Editing / Researching | ⚠️ Mọi bài đều mark ⭕ Planned |
| `Ưu tiên` / `Priority` | Thứ tự ưu tiên | ⚠️ Không phân biệt Priority 1/2, gộp chung |
| `Subtopic 2` | Cluster group | ⚠️ Gộp hết vào 1 group "Uncategorized" |
| `Search Volume` / `Volume` | Volume data | ⚠️ Không hiển thị volume |

**Steps:**

1. Đọc CSV bằng Python (ưu tiên `keywords.csv`, fallback file gốc với `cp1258`)
2. Detect headers → kiểm tra columns bắt buộc, ghi nhận columns thiếu
3. **Báo cáo ngay** những columns thiếu và ảnh hưởng (trước khi chạy tiếp)
4. Group bằng các columns có sẵn
5. Xác định Pillar mỗi cluster = article có keyword/title ngắn nhất (broad/head term)
6. Liệt kê `content/blog/3-finalized/` — cross-reference ✅ Published (nếu không có Status column)
7. Đọc `progress-log.md` Active Pipeline — mark 🔄 In Progress
8. Ghi `seo-strategy/content-plan/topic-clusters.md`
9. Báo cáo cuối: tổng clusters, coverage %, top 5 clusters thiếu Pillar

---

## Mode 2: Raw Keyword Grouping

**Khi nào dùng:** Raw keywords mới từ Ahrefs/Semrush/GKP chưa được grouped.

**Detect tool bằng column headers:**

| Tool | Key columns | Logic |
|------|------------|-------|
| Semrush | `Keyword`, `Intent`, `Volume` | Group by Intent → topic noun |
| Ahrefs | `Keyword`, `Parent Topic`, `Volume`, `KD` | Group by Parent Topic (built-in cluster) |
| GKP | `Keyword`, `Avg. monthly searches` | Group by topic noun, flag ALL for SERP check |

**Output Mode 2:** Draft file `seo-strategy/keywords/draft-clusters-[YYYY-MM-DD].md`
Không ghi `topic-clusters.md` — đây chỉ là draft để user review/adjust.

---

## Output format `topic-clusters.md`

```markdown
# Topic Clusters — HVS SEO Content Map
> Cập nhật: [date] | Nguồn: keywords.csv ([N] articles)
> ✅ Published: X | 🔄 In Progress: Y | ⭕ Planned: Z

---

## Group: [Subtopic 2] ([N] articles)

### Cluster: [Subtopic 3] ([N] | ✅ X | 🔄 Y | ⭕ Z)

**Pillar:** ✅/⭕ [keyword] *(Published — Final-xxx.md / Priority 1)*

**Priority 1:**
- ✅ [keyword] *(Final-xxx.md)*
- 🔄 [keyword] *(Draft-xxx.md)*
- ⭕ [keyword]*

**Priority 2:** [N bài — dùng /keyword-plan để xem]
```

Priority 2 gộp thành summary count để file readable với ~600 articles.
