---
description: "Build Knowledge Base cho project. Args: all | company | market | audience | icp"
allowed-tools: WebSearch, WebFetch, Read, Write, Bash
---

Khởi chạy **Research Agent** để xây dựng Knowledge Base.

**Cách dùng:**
```
/setup all        → Chạy toàn bộ (company + market + audience + icp)
/setup company    → Profile công ty, sản phẩm, USPs, tone
/setup market     → Đối thủ, content gaps, xu hướng thị trường
/setup audience   → Persona chi tiết (pain points, câu hỏi, trigger)
/setup icp        → Ideal Customer Profile — nhóm convert tốt nhất
```

Nếu `$ARGUMENTS` trống → chạy `/setup all` theo mặc định.

---

Đọc `.antigravity/agents/research-agent.md` để nắm đầy đủ quy trình và output format.

## Bước 0: Hỏi user trước khi bắt đầu

Hỏi 2 câu này trước (không bỏ qua):

```
Để research chính xác hơn, cho tôi biết:

1. Website chính thức của công ty là gì? (nếu có)
   → Để tôi đọc trực tiếp thay vì chỉ dựa vào WebSearch

2. Bạn có tài liệu nội bộ nào trong resources/ chưa?
   (brief, deck, mô tả sản phẩm, v.v.)
   → Nếu chưa có, tôi sẽ tự research hoàn toàn
```

Nếu user cung cấp URL → dùng WebFetch cho Module 1 và 2.
Nếu không → dùng WebSearch thuần.

---

## Bước 1: Auto Research

Chạy từng module dưới dạng sub-agent (Agent tool). Mỗi sub-agent gắn nhãn:
- `[verified ✅]` — từ internal docs / website chính thức
- `[assumed ⚠️]` — suy luận từ WebSearch
- `[TBD ❓]` — không tìm được, cần hỏi user

Module → file output:
- `company` → `resources/company/hvs-profile.md`
- `market` → `resources/market/market-landscape.md`
- `audience` → `resources/audience/personas-deep.md`
- `icp` → `resources/audience/icp.md` *(cần company + audience xong trước)*

---

## Bước 2: Gap Form

Sau khi auto research xong, tổng hợp tất cả `[TBD ❓]` và `[assumed ⚠️]` quan trọng thành **1 form duy nhất**:

```
📋 CẦN XÁC NHẬN — Trả lời để hoàn thiện Knowledge Base:

[Company]
Q1. ...

[Audience / ICP]
Q2. ...
```

Chỉ hỏi những câu thực sự ảnh hưởng đến chất lượng content.

---

## Bước 3: 2 Outputs

**① Cập nhật Knowledge Base** — điền câu trả lời vào files, đổi nhãn `[TBD]` → `[verified ✅]`

**② Tạo Confirmation Template** → `resources/confirm-with-leadership.md`
```markdown
# Xác nhận thông tin — HVS Securities
_Dùng để confirm với leader/client trước khi triển khai_

| # | Hạng mục | Thông tin hiện tại (assumed) | Xác nhận |
|---|----------|------------------------------|----------|
```

Báo cáo cuối: files đã tạo, số `[verified/assumed/TBD]`, đề xuất bước tiếp `/keyword-plan`.
