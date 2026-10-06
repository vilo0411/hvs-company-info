# Learning Loop — Hệ thống tự học

> Kích hoạt sau mỗi `/approve` (Draft/Optimize) và khi user gõ `/learn`. SOP chi tiết: `.antigravity/skills/content-feedback-loop/SKILL.md`.

## Routing feedback → đúng nơi lưu

| Loại feedback | Ghi vào | Ví dụ |
|---|---|---|
| Regex bắt được (từ, cụm từ, ký tự, format) | `anti-ai-rules.md §0` (`FORBIDDEN_STRINGS` / `RESTRICTED_STRINGS` / `HEDGE_WORDS`) hoặc thêm check vào `scripts/qa_lint.py` | "bỏ từ Giải mã", "không dùng —" |
| Pattern lặp ở ≥2 bài, cần suy luận | `anti-ai-rules.md §0 FORBIDDEN_PATTERNS` + log §4 | "mô tả sai HVS Tài chính số là công cụ" |
| Judgment call, gu của user, ngoại lệ theo topic | `.antigravity/memory/instincts-archive.md` (append-only) → chạy `python scripts/optimize_instincts.py` | "bài vĩ mô: thêm góc nhìn dòng tiền" |
| Sự kiện thô (bài nào, sửa gì, khi nào) | `seo-strategy/content-plan/revision-log.md` | mọi lần sửa |
| Cập nhật kiến thức brand/sản phẩm | Brand Guardian Mode C đề xuất → user xác nhận → `glossary.md` / `hvs-profile.md` / `financial-logic.md` | đổi học phí |

## Quy tắc

1. **Máy bắt được → không thành instinct.** Nếu lỗi có thể bắt bằng regex, thêm vào §0 / lint. `optimize_instincts.py` tự chuyển instinct đã được lint bao phủ vào bảng "Đã tự động hoá".
2. **Archive là append-only**, đủ metadata (`Nguồn`, `Phản hồi từ User` nguyên văn, `Phạm vi`). `instincts.md` là bản sinh tự động ≤8.000 ký tự — không sửa tay.
3. **Ghi log trước khi sửa**: 1 dòng vào `revision-log.md` ngay khi nhận feedback, rồi mới sửa bài.
4. `/approve` Draft phải hỏi: *"Ngoài chat, bạn có tự sửa gì trong file không?"* — câu trả lời là input cho vòng học.
5. Mỗi entry §4 anti-ai-rules ghi ngày + nguồn (slug) để truy vết.

## Format instinct (archive)

```
### <Tiêu đề ngắn>
- **Trạng thái:** Active
- **Nguồn:** <slug> · <YYYY-MM-DD>
- **Phản hồi từ User:** "<nguyên văn>"
- **Bản năng:** <rule hành động, 1–2 câu>
- **Phạm vi:** Global | Chỉ topic: <topic>
```
