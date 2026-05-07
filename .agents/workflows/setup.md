---
description: "Build Knowledge Base cho project. Args: all | company | market | audience | icp"
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

Nếu không có args → chạy `all` theo mặc định.

Đọc `.antigravity/agents/research-agent.md` để nắm đầy đủ quy trình và output format.

## Bước 0: Hỏi user trước khi bắt đầu

Hỏi 2 câu này trước (không bỏ qua):

```
1. Website chính thức của công ty là gì? (nếu có)
2. Bạn có tài liệu nội bộ nào trong resources/ chưa?
```

Nếu có URL → dùng WebFetch. Nếu không → WebSearch thuần.

## Bước 1: Auto Research

Chạy từng module dưới dạng sub-agent. Gắn nhãn độ tin cậy:
- `[verified ✅]` — từ internal docs / website chính thức
- `[assumed ⚠️]` — suy luận từ WebSearch
- `[TBD ❓]` — không tìm được

Module → file output:
- `company` → `resources/company/hvs-profile.md`
- `market` → `resources/market/market-landscape.md`
- `audience` → `resources/audience/personas-deep.md`
- `icp` → `resources/audience/icp.md`

## Bước 2: Gap Form

Tổng hợp tất cả `[TBD ❓]` và `[assumed ⚠️]` quan trọng thành **1 form duy nhất** để hỏi user.

## Bước 3: 2 Outputs

**① Cập nhật Knowledge Base** — điền câu trả lời, đổi nhãn `[TBD]` → `[verified ✅]`

**② Tạo Confirmation Template** → `resources/confirm-with-leadership.md`

Báo cáo cuối: files đã tạo, số verified/assumed/TBD, đề xuất chạy `/keyword-plan`.
