---
description: "Tạo Topic Cluster map từ CSV đã grouped, hoặc gom nhóm raw keywords từ tool export"
---

Tạo **Topic Cluster Map** — content management system cho toàn bộ bài viết dự kiến.

**Cách dùng:**
```
/cluster                          → Mode 1: CSV chuẩn (default path)
/cluster [csv-path]               → Mode 1: CSV tùy chỉnh
/cluster raw [file]               → Mode 2: raw export từ Ahrefs/Semrush/GKP
```

---

## Prerequisite — CSV encoding

File gốc `Nghiên cứu từ khóa - HVS Tư vấn số.csv` có thể bị lỗi encoding (Vietnamese chars thành `?`).

**Giải pháp tốt nhất:** Re-export từ Google Sheets → File → Download → CSV UTF-8.
Sau khi có file UTF-8, lưu tại `seo-strategy/keywords/keywords.csv`.

Nếu chưa có `keywords.csv`, đọc file gốc bằng Python với `encoding='cp1258'`:
```python
with open(filepath, 'rb') as f:
    raw = f.read()
text = raw.decode('cp1258')
```

---

## Mode 1: CSV Import (CSV đã grouped)

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

1. **Đọc CSV** bằng Python (xem encoding note trên), parse header row thành dict

2. **Detect columns** — kiểm tra từng column bắt buộc vs tùy chọn. **Báo cáo ngay:**
   ```
   ✅ Columns tìm thấy: Subtopic 3, Individual Page, Status, Ưu tiên
   ⚠️ Columns thiếu: Search Volume → sẽ không hiển thị volume
   ```
   Nếu thiếu column bắt buộc → dừng lại, hướng dẫn user kiểm tra CSV

3. **Group** bằng các columns có sẵn (Subtopic 2 nếu có, fallback "Uncategorized")

4. **Xác định Pillar** cho mỗi cluster = article có keyword/title ngắn nhất (broad/head term)

5. **Cross-reference** với `content/blog/3-finalized/` để update Published status

6. **Cross-reference** với `seo-strategy/content-plan/progress-log.md` (Active Pipeline) → mark 🔄 In Progress

7. **Output** `seo-strategy/content-plan/topic-clusters.md`

8. **Báo cáo:** tổng clusters, coverage %, top 5 clusters thiếu Pillar

---

## Mode 2: Raw Keyword Grouping (tool export)

**Khi nào dùng:** User có raw keywords mới từ Ahrefs/Semrush/GKP chưa grouped.

**Agent detect tool bằng column headers:**

### Semrush export
Headers chứa: `Keyword`, `Intent`, `Volume`

```
1. Group by Intent (Informational / Commercial / Transactional)
2. Trong mỗi intent group → extract topic noun → sub-group
3. Pillar = Informational keyword volume cao nhất trong topic group
4. Cluster articles = remaining keywords cùng topic group
```

### Ahrefs export
Headers chứa: `Keyword`, `Parent Topic`, `Volume`, `KD`

```
1. Group by Parent Topic (Ahrefs đã pre-cluster)
2. Keyword khớp Parent Topic = Pillar candidate
3. Remaining = Cluster articles
4. Sort by Volume → Pillar = volume cao nhất khớp Parent Topic
```

### GKP export
Headers chứa: `Keyword`, `Avg. monthly searches`, `Competition`

```
1. Extract topic noun từ keyword (shared root word)
2. Group by topic noun
3. Flag ALL groups: user phải SERP check intent
4. Output: pre-sort để giảm số SERP checks cần thiết
```

**Output Mode 2:** Draft file `seo-strategy/keywords/draft-clusters-[date].md` — KHÔNG phải `topic-clusters.md`.
User review, adjust groupings, rồi format thành CSV chuẩn → chạy `/cluster [csv]`.

---

## Output format `topic-clusters.md`

```markdown
# Topic Clusters — HVS SEO Content Map
> Cập nhật: [date] | Nguồn: keywords.csv (592 articles)
> ✅ Published: 12 | 🔄 In Progress: 2 | ⭕ Planned: 578

---

## Group: [Subtopic 2] ([N] articles)

### Cluster: [Subtopic 3] ([N] articles | ✅ X | 🔄 Y | ⭕ Z)

**Pillar:** ✅/⭕ [keyword] *(Published — Final-xxx.md / Researching, Priority 1)*

**Priority 1:**
- ✅ [keyword] *(Published — Final-xxx.md)*
- 🔄 [keyword] *(In Editing — Draft-xxx.md)*
- ⭕ [keyword] *(Researching)*

**Priority 2:** [N bài — chạy /keyword-plan để xem full list]
```

**Lưu ý:** Chỉ liệt kê đầy đủ Priority 1. Priority 2 gộp thành summary count. Giữ file readable với 600 articles.
