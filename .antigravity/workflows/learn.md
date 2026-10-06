---
name: learn
description: Tổng hợp feedback → cập nhật anti-ai-rules §0 / lint / instincts. Args: [slug] (trống = mọi entry chưa xử lý)
---

# /learn

Rule routing: `.antigravity/rules/learning-loop.md`. SOP: `.antigravity/skills/content-feedback-loop/SKILL.md`.

## Bước 0 — Input

- `grep -n "<slug>" seo-strategy/content-plan/revision-log.md` (hoặc phần chưa có tag `[learned]`).
- `## Revision Log` cuối `Final-<slug>.md` nếu có.
- `.antigravity/memory/instincts-archive.md` — chỉ grep title để tránh trùng.

## Bước 1 — Phân loại từng feedback

| Loại | Đích |
|---|---|
| Từ/cụm/ký tự/format regex bắt được | `anti-ai-rules.md §0` (`FORBIDDEN_STRINGS` / `RESTRICTED_STRINGS` / `HEDGE_WORDS`) hoặc check mới trong `scripts/qa_lint.py` + hàng trong `seo-formatting.md §1` |
| Pattern ≥2 bài cần suy luận | `anti-ai-rules.md §0 FORBIDDEN_PATTERNS` + dòng log `§4` (ngày, nguồn) |
| Judgment / gu / theo topic | append `.antigravity/memory/instincts-archive.md` (format trong learning-loop.md) |
| Kiến thức brand/sản phẩm | Brand Guardian Mode C → đề xuất, chờ user |

## Bước 2 — Trình bày đề xuất (chờ xác nhận)

```
| # | Feedback | Loại | Ghi vào | Nội dung rule |
```

## Bước 3 — Ghi (sau xác nhận)

- Append (không sửa entry cũ). Đánh tag `[learned YYYY-MM-DD]` vào entry revision-log đã xử lý.
- ```
  python scripts/optimize_instincts.py
  python scripts/qa_lint.py --dump-rules      # xác nhận rule mới đã load
  ```
- Báo: số rule vào §0, số instinct mới, kích thước `instincts.md`.
