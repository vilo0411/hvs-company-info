---
trigger: always_on
---

# Workspace Structure & Naming Convention

## Pipeline thư mục (theo thứ tự)
```
content/blog/
├── 0-raw/          Raw-[slug].md        (nội dung thô chưa xử lý)
├── 1-outlines/     Outline-[slug].md    (brief + outline chờ duyệt)
├── 2-user-review/  Draft-[slug].md      (bản nháp chờ user approve)
└── 3-finalized/    Final-[slug].md      (bài hoàn chỉnh)
```

## Naming Convention — BẮT BUỘC
- Tiền tố theo giai đoạn: `Outline-`, `Draft-`, `Final-`
- Slug dạng kebab-case tiếng Việt không dấu: `co-phieu-penny-la-gi`
- Không được bỏ tiền tố, không đặt tên tự do

## YAML Metadata — BẮT BUỘC cho mọi file content
```yaml
---
Author: Claude Code
Status: Outline | Draft | Finalized
Mode: Detailed | Fast | Optimized
Persona: [Tên persona]
Target_Keyword: [Từ khóa chính]
Search_Intent: [Informational | Commercial | Transactional]
Word_Count_Target: [Số chữ]
Meta_Description: [Mô tả SEO ≤160 ký tự]
---
```

## Approval Flow (2 lớp bắt buộc)
```
Outline → [user /approve] → Draft → [user /approve] → Final
```
Agent không được tự chuyển giai đoạn nếu chưa có `/approve` từ user.

## Knowledge Base (Layer 1 — setup 1 lần)
```
resources/
├── company/hvs-profile.md          [verified ✅ / assumed ⚠️ / TBD ❓]
├── market/market-landscape.md
├── audience/personas-deep.md
├── audience/icp.md
└── confirm-with-leadership.md      (template xác nhận với leader)
```
