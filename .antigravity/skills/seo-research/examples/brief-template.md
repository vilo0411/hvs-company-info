---
name: Content Brief Template — HVS SEO (Expert & Holistic Metadata)
description: Template dàn ý SEO chi tiết tích hợp hệ thống Koray Gübür (Holistic SEO Writing) và tiêu chuẩn chuyên gia tài chính HVS.
---

# SEO Content Outline: [Tên bài viết]

## 1. Thông số kỹ thuật (Metadata)

```yaml
---
Author: Antigravity
aliases: ["[Từ khóa chính]"]
Status: Outline
Pipeline_Mode: Express | Guided | Auto
SERP_Research: true

# SEO Technical & Holistic (Koray Gübür Standard)
Target_Keyword: [Từ khóa chính]
Secondary_Keywords: [Từ khóa phụ 1, phụ 2...]
LSI_Keywords: [Từ khóa LSI]
Niche_Context: [Ví dụ: Securities Trading | Personal Finance]
Entities: [List thực thể quan trọng từ SERP & KB]
Entities_Gap_Analysis: [Các thực thể đối thủ bỏ sót - Rule 14]
Search_Intent: [Informational | Transactional | Commercial]
Search_Intent_Deep: [Nỗi đau thực sự của user]
Word_Count_Target: [Số từ đề xuất]

# Strategic Guardrails (Professionalism & Memory)
Persona: [HVS Senior Mentor - tham chiếu @tone-and-voice.md]
Tone_Style: [Direct, Data-driven, Objective]
Lexicon_Focus: [Professional terms từ @glossary.md]
Financial_Logic: [Scenario-based, Risk-Reward - tham chiếu @financial-logic.md]
Avoid_Mistakes: [Danh sách lỗi cần tránh trích xuất từ Past Revision Logs]

# Mandatory Compliance (BẮT BUỘC ĐỌC TRƯỚC KHI VIẾT)
Mandatory_Rules:
  - "@.antigravity/rules/writing-guidelines.md"
  - "@seo-strategy/resources/content-strategy/anti-ai-rules.md"
  - "@seo-strategy/resources/content-strategy/financial-logic.md"
  - "@seo-strategy/resources/content-strategy/tone-and-voice.md"
  - "@seo-strategy/resources/content-strategy/glossary.md"

# Response Mapping (Rule 9 & 12)
Direct_Answer_Targets:
  - heading: "H2: [Tên heading]"
    type: "Definition / Direct Answer"
    bold_target: "[Cụm từ then chốt sẽ bôi đậm]"

# Audience & Brand
Writing_Method: [PAS | AIDA | 4Cs]
HVS_Products: ["HVS Tài chính số", "HVS Thực tập số"]

# Cluster info
Cluster: [Tên Cluster]
Internal_Links: []
---
```

- **Title:** [Tối đa 59 ký tự, chứa từ khóa chính]
- **Sapo:** [Chứa từ khóa chính, ưu tiên thực thể ở đầu câu]
- **Meta description:** [~155 ký tự, chứa keyword]

---

## 2. Cấu trúc Heading Đề xuất (Dynamic Structure)

*(Cấu trúc này được sinh tự động dựa trên Recommended Unique Structure từ SERP & Strategy Collector, đảm bảo lấp đầy Entity Gap và chèn HVS Bridge tự nhiên)*

### H1: [Tiêu đề chính - Chứa keyword]

[DYNAMIC_HEADINGS]
*(Agent tự động render danh sách các H2, H3 theo định dạng sau cho mỗi mục:)*

#### H2: [Tiêu đề Section]
- **Nhiệm vụ/Trọng tâm:** [Giải quyết intent gì? Giải thích khái niệm hay so sánh?]
- **HVS Bridge:** [Có lồng ghép sản phẩm HVS không? Nếu có, lồng ghép thế nào?]
- **Entities & Keywords:** [List cụ thể các entity cần xuất hiện trong section này]
- **Direct Answer (nếu có):** [Nháp 1 câu trả lời trực diện ≤40 từ]
- **Word_Count:** [Số từ dự kiến]

[END_DYNAMIC_HEADINGS]

---

## 3. Chiến lược liên kết & Tối ưu hóa
- **Internal Links:** [Anchor text khớp Title bài đích]
- **Yếu tố cạnh tranh:** [Bảng biểu / Box chuyên gia]

---

## 4. Nhật ký chỉnh sửa (Revision Log)
- **v1.3 (2026-05-20):** Cập nhật Cấu trúc Động (Dynamic Structure) dựa trên Search Intent sâu sắc.

---

## 5. 🛡️ Quy định tuân thủ (Mandatory Compliance)

Để bài viết đạt chuẩn HVS, người viết (Agent) **BẮT BUỘC** phải tuân thủ các tài liệu tham chiếu sau:

1.  **Văn phong & Persona:** Phải đúng chất "Senior Mentor" theo [tone-and-voice.md](file:///e:/project/hvs-company-info/seo-strategy/resources/content-strategy/tone-and-voice.md).
2.  **Thuật ngữ:** Chỉ dùng từ Professional, tuyệt đối không dùng từ Amateur trong [glossary.md](file:///e:/project/hvs-company-info/seo-strategy/resources/content-strategy/glossary.md).
3.  **Tư duy tài chính:** Mọi nhận định phải theo kịch bản và có cảnh báo rủi ro theo [financial-logic.md](file:///e:/project/hvs-company-info/seo-strategy/resources/content-strategy/financial-logic.md).
4.  **Anti-AI:** Kiểm tra lại danh sách từ cấm tại [anti-ai-rules.md](file:///e:/project/hvs-company-info/seo-strategy/resources/content-strategy/anti-ai-rules.md).

---

## 6. ⛔ Anti-AI — Enforcement

> Đọc **Section 0 — QUICK SCAN** trong `seo-strategy/resources/content-strategy/anti-ai-rules.md` (ngắn, luôn cập nhật).  
> Loop qua từng `FORBIDDEN_STRINGS`, `FORBIDDEN_PATTERNS`, và `REQUIRED` trước khi viết bất kỳ section nào.

### Word Count — BẮT BUỘC đạt số từ trong outline
- Viết đủ Word_Count ghi trong Brief, KHÔNG cắt ngắn.
- Nếu thiếu từ: bổ sung ví dụ cụ thể, kịch bản thực tế, hoặc bảng so sánh.
- Không được dừng lại khi chưa đạt Word_Count của từng section.
