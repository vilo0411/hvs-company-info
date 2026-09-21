# Plan: Layer 2 — Keyword Strategy

> **Trạng thái:** Draft v2 — đã update sau clarification
> **Cập nhật:** 2026-05-07

---

## Tình trạng thực tế (sau khi audit CSV)

| Chỉ số | Giá trị |
| :--- | :--- |
| Tổng keywords trong CSV | 592 |
| Đã Published | 27 |
| Đang In Editing | 65 |
| Chưa bắt đầu (Researching) | 500 |
| Main Topic 1 | 1 ("Đầu tư") |
| Subtopic 2 (cluster groups) | 4 |
| Subtopic 3 (clusters thực sự) | ~20 |
| **Search Volume có data** | **1/592 (0.2%)** |

---

## Vấn đề thiết kế hiện tại

### `/keyword-plan` — sai về concept

**Thiết kế cũ:** WebSearch để "khám phá" keyword mới → tự bịa volume + difficulty.

**Vấn đề:**
- Volume không có data thật → agent đang hallucinate số liệu
- 500 keywords đang "Researching" trong CSV chưa được viết → không cần khám phá thêm trước
- Thực tế cần: **chọn cái gì viết tiếp** từ 500 keywords đã có, không phải tìm thêm

**Thiết kế đúng:** Sprint Planner + Gap Analyzer (dựa trên CSV có sẵn).

---

### `/cluster` — đang làm việc không cần thiết

**Thiết kế cũ:** Gom nhóm keywords từ CSV → tạo Topic Cluster map.

**Vấn đề:**
- CSV **đã có** cấu trúc 4 cấp sẵn: Main Topic → Subtopic 2 → Subtopic 3 → Individual Page
- Đây chính là Topic Cluster map — chỉ cần **parse và format**, không cần "tạo mới"

**Thiết kế đúng:** CSV Parser → `topic-clusters.md` formatter.

---

## Context sau clarification

**Từ user:** CSV là file đã gom nhóm thủ công (Google Sheets), chỉ cần viết thôi. Quy trình gom nhóm của user là check SERP xem keyword nào cùng intent → nhóm vào. Nếu agent làm thay = rất nhiều web search.

**Kết luận:**
- CSV hiện tại = đã grouped, chỉ cần render sang Markdown
- Raw keywords (chưa grouped) = agent có thể làm **semantic grouping** (không cần SERP), output draft để user review
- `/cluster` xử lý cả 2 path, detect input type

---

## Thiết kế lại Layer 2

### Luồng chính (CSV đã grouped)

```
Google Sheets export → CSV
    ↓
/cluster [csv-path] → parse → topic-clusters.md
    ↓
/keyword-plan → sprint backlog (5 bài tiếp theo)
    ↓
/detailed [keyword]
```

### Luồng phụ (raw keywords chưa grouped)

```
Raw keyword list (paste hoặc file .txt)
    ↓
/cluster raw [file] → semantic grouping (không SERP)
                    → draft clusters → user review/adjust
                    → user confirm → /cluster [csv]
```

---

## Task 2.1 — Redesign `/cluster` (2 modes)

**Mục tiêu:** Smart command, detect input type, xử lý 2 scenario

### Mode 1: CSV Import (path to CSV)

```
/cluster seo-strategy/keywords/keywords.csv
```

**Logic:**
```
Subtopic 3 = tên cluster (ví dụ: "Phân tích cơ bản")
Individual Page = article trong cluster đó
Pillar = bài có keyword ngắn nhất + broad trong group
Cluster articles = long-tail variants
```

**Steps:**
1. Detect input là CSV path → chạy Mode 1
2. Đọc CSV bằng Python (`encoding='utf-8-sig', errors='replace'`) — không dùng bash
3. Group by: Subtopic 2 → Subtopic 3 → Individual Page
4. Xác định Pillar: keyword ngắn nhất trong group (proxy cho "broad/head term")
5. Cross-reference với `content/blog/3-finalized/` để update Published status
6. Output `topic-clusters.md`

### Mode 2: Raw Keyword Grouping (từ tool export)

```
/cluster raw ahrefs-export.csv
/cluster raw semrush-export.csv
/cluster raw gkp-export.csv
```

**Agent detect tool source bằng column headers, áp dụng logic tương ứng:**

#### Semrush export

Columns cần thiết: `Keyword`, `Intent`, `Volume`

| Bước | Logic |
|------|-------|
| 1 | Group by `Intent` (Informational / Commercial / Transactional) |
| 2 | Trong mỗi intent group, extract topic noun → sub-group |
| 3 | Pillar = Informational keyword có volume cao nhất trong topic group |
| 4 | Cluster articles = remaining keywords trong cùng topic group |

→ **Chính xác nhất** vì Semrush đã có intent data thật.

#### Ahrefs export

Columns cần thiết: `Keyword`, `Parent Topic`, `Volume`, `KD`

| Bước | Logic |
|------|-------|
| 1 | Group by `Parent Topic` — đây chính là cluster signal, Ahrefs đã làm sẵn |
| 2 | Keyword khớp với Parent Topic = Pillar candidate |
| 3 | Remaining keywords trong group = Cluster articles |
| 4 | Sort by Volume → Pillar = volume cao nhất khớp Parent Topic |

→ **Chính xác cao** vì Parent Topic là built-in cluster grouping của Ahrefs.

#### Google Keyword Planner (GKP)

Columns cần thiết: `Keyword`, `Avg. monthly searches`

| Bước | Logic |
|------|-------|
| 1 | Extract topic noun từ keyword (entity extraction đơn giản) |
| 2 | Group by shared topic noun |
| 3 | **Flag tất cả groups** — user phải SERP check intent thủ công |

→ **Giới hạn nhất** — không có intent data. Output là pre-sort để giảm số SERP check cần thiết (500 keywords → ~50 buckets → user SERP check theo bucket).

#### Output draft cho user review

```markdown
## Draft Clusters — từ Ahrefs export (chưa finalized)
> ⚠️ Review và adjust trước khi `/cluster [csv]`

### Cluster đề xuất: Phân tích cơ bản
Parent Topic: "phân tích cơ bản"
Pillar candidate: phân tích cơ bản là gì (Vol: 2,400)
  - cách phân tích cơ bản cổ phiếu (Vol: 880)
  - phân tích cơ bản vs kỹ thuật (Vol: 590)
  - công cụ phân tích cơ bản (Vol: 320)

### ⚠️ Ambiguous — cần SERP check:
  - "cổ phiếu tốt là gì" (Parent Topic: cổ phiếu — quá rộng)
  - "đầu tư an toàn" (Parent Topic: đầu tư — không đủ specific)
```

**Sau khi user review:** Adjust groupings → agent format lại thành CSV chuẩn → `/cluster [csv]`.

### Output format (cả 2 modes)

```markdown
## Cluster: Phân tích cơ bản
**Group:** Cho người mới
**Tổng:** 115 | ✅ Published: 3 | 🔄 In Editing: 5 | ⭕ Planned: 107

### Pillar
- ⭕ phân tích cơ bản là gì *(Researching, Priority 1)*

### Cluster Articles
- ✅ EPS là gì *(Published — Final-eps-la-gi.md)*
- 🔄 P/E là gì *(In Editing)*
- ⭕ ROE là gì *(Researching, Priority 1)*
- ⭕ P/B là gì *(Researching, Priority 2)*
```

### Output format

```markdown
## Cluster: Phân tích cơ bản
**Subtopic group:** Cho người mới
**Tổng articles:** 115 | Published: 3 | In Progress: 5 | Planned: 107

### Pillar
- [ ] phân tích cơ bản là gì *(Researching)*

### Cluster Articles
- ✅ EPS là gì *(Published — Final-eps-la-gi.md)*
- 🔄 P/E là gì *(In Editing)*
- ⭕ ROE là gì *(Researching, Priority 1)*
- ⭕ P/B là gì *(Researching, Priority 2)*
```

---

## Task 2.2 — Redesign `/keyword-plan` thành Sprint Planner

**Mục tiêu:** Trả lời "Nên viết 5 bài gì tiếp theo?" dựa trên data thực

### Inputs

- `seo-strategy/content-plan/topic-clusters.md` (phải chạy `/cluster` trước)
- `seo-strategy/content-plan/progress-log.md`
- Args: persona focus (tùy chọn) — ví dụ `/keyword-plan F0`

### Scoring logic (không cần volume)

| Tiêu chí | Điểm | Lý do |
| :--- | :--- | :--- |
| Priority = 1 trong CSV | +2 | User đã đánh dấu |
| Cluster chưa có Pillar | +2 | SEO impact cao nhất |
| Cluster có Pillar rồi, thiếu Cluster article | +1 | Build cluster |
| Persona match với args | +1 | Tập trung |
| Status = In Editing | +0 (skip) | Đang làm rồi |

### Output format

```markdown
## Sprint Backlog — [date]

**Persona focus:** F0 — Cho người mới
**Logic:** Ưu tiên Pillar missing + Priority 1

| # | Keyword | Cluster | Loại | Lý do chọn |
|---|---------|---------|------|------------|
| 1 | phân tích cơ bản là gì | Phân tích cơ bản | Pillar | Cluster 115 bài, chưa có Pillar |
| 2 | cách đọc báo cáo tài chính | Phân tích cơ bản | Cluster | Priority 1, liên kết Pillar trên |
| 3 | ... | | | |

**Cluster coverage hiện tại:**
- Phân tích cơ bản: 3/115 published (2.6%)
- Phân tích kỹ thuật: 5/113 published (4.4%)
- ...
```

### Về keyword discovery mới (ngoài CSV)

Khi user có keywords mới từ Ahrefs/Semrush:
- **Đã grouped (CSV chuẩn):** `/cluster [csv]` → render trực tiếp
- **Raw export từ tool:** `/cluster raw [file]` → agent đọc Intent/Parent Topic → draft clusters → user review → `/cluster [csv]`
- **GKP (không có intent):** `/cluster raw [file]` → topic noun pre-sort → user SERP check theo bucket → confirm groupings

Agent không discover volume mới. Volume data là trách nhiệm của user với tool research.

---

## Task 2.3 — Fix CSV encoding (prerequisite)

**Vấn đề:** Khi agent đọc CSV bằng bash, Vietnamese characters bị garbled. Ảnh hưởng toàn bộ Layer 2.

**Giải pháp:** Convert file sang UTF-8 thuần 1 lần.

```bash
python3 -c "
import csv, io
with open('seo-strategy/keywords/Nghiên cứu từ khóa - HVS Tư vấn số.csv', encoding='utf-8-sig', errors='replace') as f:
    content = f.read()
with open('seo-strategy/keywords/keywords.csv', 'w', encoding='utf-8') as f:
    f.write(content)
"
```

→ Tạo file `seo-strategy/keywords/keywords.csv` (UTF-8 chuẩn) làm source of truth.
→ Giữ nguyên file gốc, agent chỉ đọc `keywords.csv`.

**Ai làm:** User chạy script này 1 lần, hoặc agent tự chạy ở đầu `/cluster`.

---

## Task 2.4 — Cập nhật workflow files

Sau khi redesign logic, cần update:

| File | Thay đổi |
|------|----------|
| `.agents/workflows/cluster.md` | Viết lại theo logic CSV Parser ở trên |
| `.agents/workflows/keyword-plan.md` | Viết lại thành Sprint Planner |
| `.claude/commands/cluster.md` | Mirror từ workflow |
| `.claude/commands/keyword-plan.md` | Mirror từ workflow |

---

## Thứ tự thực hiện

| # | Task | Ghi chú |
|---|------|---------|
| 1 | **2.3** Fix CSV encoding | Prerequisite — làm trước hết |
| 2 | **2.1** Redesign `/cluster` | Logic rõ, implement được ngay |
| 3 | **2.2** Redesign `/keyword-plan` | Phụ thuộc cluster map |
| 4 | **2.4** Update workflow files | Cuối cùng |

---

## Câu hỏi cần confirm trước khi implement

1. **Pillar identification:** Không có volume data, dùng rule "keyword ngắn nhất trong group = Pillar" — có OK không, hay muốn tự mark trong CSV?

2. **CSV encoding:** Tạo `keywords.csv` (UTF-8 sạch) để agent đọc, giữ nguyên file gốc — đồng ý không?

3. **Sprint size:** `/keyword-plan` suggest mặc định bao nhiêu bài? (đề xuất: 5)

4. **Raw clustering feedback loop:** Sau khi agent draft semantic clusters, user muốn review thế nào? (edit file text hay agent hỏi từng cluster?)
