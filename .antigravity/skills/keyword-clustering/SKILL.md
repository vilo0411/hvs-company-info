---
name: Keyword Clustering
description: Gom nhóm keywords thành Topic Cluster map (Pillar + Cluster articles). Kích hoạt bởi lệnh `/cluster`.
---

# Skill: Keyword Clustering — Topic Cluster Map

Kỹ năng này phân nhóm danh sách keywords thành cấu trúc Pillar-Cluster, giúp xây dựng content strategy có chiều sâu và liên kết nội bộ mạnh.

---

## 📐 Tiêu chí phân loại

### Pillar Article (Bài Trụ cột)
Keyword đủ tiêu chuẩn Pillar khi thỏa **cả 3**:
- **Volume:** Cao (> 1000 lượt/tháng, hoặc top volume trong nhóm)
- **Intent:** Informational — người dùng muốn hiểu tổng quan
- **Depth:** Có thể viết 2000+ từ bao phủ toàn bộ chủ đề

### Cluster Article (Bài Vệ tinh)
Keyword là Cluster khi:
- **Long-tail:** Cụ thể hơn, thường có 4+ từ
- **Intent:** How-to, Commercial, Comparison, hoặc sub-topic của Pillar
- **Link:** Có thể link ngược về Pillar một cách tự nhiên

---

## ⚙️ Quy trình thực hiện

### Bước 1: Đọc dữ liệu đầu vào
- Đọc `seo-strategy/keywords/Nghiên cứu từ khóa - HVS Tư vấn số.csv`
- Đọc `seo-strategy/content-plan/progress-log.md` để biết keyword nào đã có bài

### Bước 2: Nhóm theo chủ đề (Semantic Grouping)
Gom các keywords có cùng chủ đề lõi. Ví dụ:
- Nhóm "Cổ phiếu": cổ phiếu là gì, cách mua cổ phiếu, cổ phiếu penny, cổ phiếu blue-chip...
- Nhóm "Chỉ số": VN-Index là gì, chỉ số chứng khoán châu Á, cách đọc chỉ số...
- Nhóm "Phân tích": phân tích kỹ thuật, phân tích cơ bản, phân tích ngành...

### Bước 3: Xác định Pillar của mỗi nhóm
Trong mỗi nhóm, chọn keyword có Intent rộng nhất và Volume cao nhất làm Pillar.

### Bước 4: Map Coverage
Với mỗi keyword, đánh dấu:
- `✅ Published` — đã có bài Finalized
- `🔄 In Progress` — đang trong pipeline (Outline/Draft)
- `⭕ Planned` — chưa viết, ưu tiên cao
- `💡 Suggested` — keyword mới đề xuất

### Bước 5: Output chuẩn

```markdown
## Cluster: [Tên nhóm chủ đề]

### 🏛️ Pillar: [Keyword Pillar]
- Intent: [Informational]
- Status: [✅/🔄/⭕]
- File: [đường dẫn nếu đã có]
- Target word count: 2000+

### 🛰️ Cluster Articles:
| Keyword | Intent | Status | File | Priority |
| :--- | :--- | :--- | :--- | :--- |
| [keyword 1] | How-to | ✅ | Final-... | — |
| [keyword 2] | Commercial | ⭕ | — | High |
| [keyword 3] | Comparison | 💡 | — | Medium |

### 🔗 Linking Plan:
- Cluster articles phải link về Pillar qua anchor: "[keyword Pillar]"
- Pillar phải có section hoặc mention đến các Cluster articles chính
```

---

## 📊 Output File: `seo-strategy/content-plan/topic-clusters.md`

File này là **nguồn sự thật duy nhất** cho content strategy. Được đọc bởi:
- `/detailed` — để biết bài mới thuộc cluster nào, cần link gì
- `/link` — để gợi ý internal links theo cluster
- `/keyword-plan` — để tránh duplicate và xác định gaps

**Cập nhật:** Mỗi khi có bài mới Finalized, cập nhật status trong file này.
