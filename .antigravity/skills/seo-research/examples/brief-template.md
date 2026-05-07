---
name: Content Brief Template — HVS SEO
description: Template chuẩn cho Content Brief (Outline). Dùng bởi SEO Collector khi tạo Outline.
---

# Content Brief Template — HVS SEO

Template này là output chuẩn mà SEO Collector phải tạo ra. Mỗi section có đủ hướng dẫn để Main Agent viết bài mà không cần đọc thêm file nào khác.

---

## Phần 1: YAML Metadata

```yaml
---
Author: Claude Code
Status: Outline
Pipeline_Mode: Express          # Express | Guided | Auto
SERP_Research: true             # true | false

# SEO
Target_Keyword: [keyword chính xác user nhập]
Search_Intent: Informational    # Informational | Commercial | Transactional
Content_Type: Comprehensive Guide  # Guide / How-to / Listicle / Comparison / Informational
Featured_Snippet: Paragraph     # Paragraph | List | Table | None
Word_Count_Target: 1500         # dựa trên benchmark SERP top 3

# Audience & Brand
Persona: F0                     # F0 | Sinh viên tài chính | Sinh viên không tài chính | F1+
Tone: Conversational + Authoritative
Writing_Method: PAS             # PAS | AIDA | 4Cs | How-to steps
HVS_Products:
  - product: HVS Demo
    benefit: "luyện phân tích kỹ thuật trên dữ liệu realtime, không rủi ro tiền thật"
  - product: HVS Forum
    benefit: "hỏi chuyên gia và cộng đồng nhà đầu tư khi có thắc mắc thực tế"

# Anti-AI — chỉ list phrases nguy cơ cao cho topic này
Anti_AI_Flags:
  - "Hành trình đầu tư"
  - "Trong bối cảnh thị trường không ngừng phát triển"

# Cluster
Cluster: [Tên cluster]
Cluster_Role: Pillar            # Pillar | Cluster
Internal_Links:
  - role: Pillar                # nếu là Cluster article — link bắt buộc
    file: Final-[pillar-slug].md
    anchor_suggestion: "[cụm từ tự nhiên trong bài để đặt link]"
---
```

---

## Phần 2: SERP Intelligence

> Section này do SEO Collector điền. Main Agent đọc để hiểu bối cảnh — không cần viết lại.

```
📊 SERP Intelligence: "[keyword]"
- Featured Snippet: [Có/Không] — Format: [Paragraph/List/Table]
- Content length benchmark: Top 1 (~X từ) | Top 3 avg (~Y từ)
- People Also Ask:
  1. [Câu hỏi 1]
  2. [Câu hỏi 2]
  3. [Câu hỏi 3]
  4. [Câu hỏi 4]
  5. [Câu hỏi 5]
- Keyword variations phổ biến trong headings đối thủ: [var1], [var2], [var3]
- Content gap (đối thủ chưa có): [gap 1], [gap 2]
```

---

## Phần 3: Content Brief

### H1

- **Format:** [Keyword chính] + [Hook ngắn] — tổng ≤65 ký tự
- **Ví dụ pattern:** "ETF là gì? Hướng dẫn đầu tư từ A-Z cho người mới"
- **Keyword cần có:** [keyword chính]
- **Hook hướng tới:** [nỗi đau / benefit / số liệu cụ thể]

---

### Sapo

- **Mục tiêu:** Câu đầu chạm pain point, câu 2-3 có keyword, câu cuối dẫn vào bài
- **Key points:**
  - [Pain point của persona — cụ thể, không chung chung]
  - [Keyword xuất hiện tự nhiên]
  - [Preview ngắn về giá trị bài sẽ mang lại]
- **Entities/Keywords:** [keyword chính], [keyword variation 1]
- **Target:** ≤150 từ

---

### H2: [Tiêu đề — nên bắt đầu bằng keyword variation hoặc PAA question]

> *(Nếu là H2 đầu tiên của bài Informational — phải có Definition Block)*

- **Definition Block (nếu cần):** Viết đoạn đầu dạng: "[Term] là [định nghĩa ≤50 từ]. Cụ thể, [expand 1 câu]." → capture Featured Snippet
- **Key points:**
  - [Point 1 — cụ thể, có số liệu / ví dụ thực tế nếu có thể]
  - [Point 2]
  - [Point 3]
- **Ví dụ bắt buộc:** [mã cổ phiếu / tên sàn / con số cụ thể liên quan]
- **Keywords & entities:** [keyword], [entity 1], [entity 2]
- **HVS integration:** [nếu section này liên quan đến product → gợi ý đặt benefit-first ở đâu]
- **Target:** ≤300 từ

---

### H3: [Tiêu đề cụ thể hơn H2 cha]

- **Key points:**
  - [Point 1]
  - [Point 2]
- **Keywords & entities:** [keyword variation], [entity]
- **Target:** ≤200 từ

---

### H2: [PAA question — biến thành H2]

*(Lặp lại pattern trên cho mỗi H2/H3)*

---

### H2: HVS Có Thể Giúp Gì? *(Section HVS — đặt gần cuối bài)*

- **Mục tiêu:** Dẫn dắt tự nhiên từ topic → pain point persona → HVS giải quyết
- **Format:** Không quảng cáo trực tiếp. Dùng Writing Method đã chọn (PAS/BAB)
- **Key points:**
  - [Pain point cụ thể liên quan đến topic vừa học]
  - [HVS Product: benefit — không phải feature]
  - [CTA: tự nhiên, phù hợp persona]
- **Products cần nhắc:**
  - [Product 1]: "[benefit như trong YAML]"
  - [Product 2 nếu có]: "[benefit]"
- **Target:** ≤150 từ

---

### Kết bài

- **Mục tiêu:** Tóm tắt insight → CTA cuối
- **Không dùng:** "Tóm lại," / "Kết luận," / "Như vậy chúng ta đã thấy"
- **Thay bằng:** Tiêu đề H2 như "Bắt đầu từ đâu?" hoặc "Điều quan trọng cần nhớ"
- **CTA phù hợp persona:**
  - F0: "Thử ngay HVS Demo — miễn phí, không cần nạp tiền thật"
  - Sinh viên: "Khám phá HVS Thực tập số để có kinh nghiệm thực chiến"
  - F1+: "Tham gia HVS Forum để trao đổi với chuyên gia"
- **Target:** ≤100 từ

---

## Phần 4: Linking Plan

```
Bài này là: [Pillar / Cluster article]
Cluster: [Tên cluster]

Nếu là Cluster article:
  → Link bắt buộc về Pillar:
    File: Final-[slug].md
    Anchor: "[cụm từ tự nhiên]"
    Đặt tại: [H2 nào, hoặc đoạn nào trong bài]

Cluster articles đã Published (để link tới nếu là Pillar):
  - Final-[slug-1].md — "[keyword]"
  - Final-[slug-2].md — "[keyword]"

Cross-cluster gợi ý (nếu phù hợp ngữ nghĩa):
  - Final-[slug].md — "[keyword]" — lý do: [...]
```
