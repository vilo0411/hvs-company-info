---
name: content-feedback-loop
description: Biến feedback của user thành rule máy bắt được (lint/§0), pattern (§0 FORBIDDEN_PATTERNS) hoặc instinct (archive). Kích hoạt sau /approve và bởi /learn.
---

# Skill: Content Feedback Loop

Rule routing: `.antigravity/rules/learning-loop.md`. Nguyên tắc: **máy bắt được → không thành instinct**.

## Giai đoạn 0 — Ghi nhận (ngay khi có feedback, trước khi sửa bài)

Append `seo-strategy/content-plan/revision-log.md`:
```
### [YYYY-MM-DD] - <slug>
- Phản hồi: "<nguyên văn user>"
- Lỗi đã sửa: …
- Pattern: <1 dòng, nếu thấy lặp>
- Rule học được: <đề xuất, chưa ghi vào rule>
```
Trong Draft/Optimize: thêm bullet vào `## Revision Log` cuối file (finalize giữ nguyên section này).

## Giai đoạn 1 — Phân tích (sau `/approve` hoặc `/learn`)

Input: entry chưa có tag `[learned]` trong `revision-log.md` (+ `## Revision Log` của Final). Với mỗi feedback, hỏi 3 câu theo thứ tự:

1. **Regex bắt được không?** (từ/cụm/ký tự/format) → **Đích A**: `anti-ai-rules.md §0` — thêm vào `FORBIDDEN_STRINGS` / `RESTRICTED_STRINGS` / `HEDGE_WORDS`; nếu là format (ví dụ "không dùng ###### H6") → thêm check trong `scripts/qa_lint.py` + hàng trong `seo-formatting.md §1`.
2. **Là pattern cần suy luận, đã gặp ≥2 bài?** → **Đích B**: `anti-ai-rules.md §0 FORBIDDEN_PATTERNS` (1 dòng `tên_pattern: 'mô tả' → cách sửa`) + dòng log §4 `- [YYYY-MM-DD]: Cập nhật từ "<slug>": …`.
3. **Còn lại (gu, judgment, ngoại lệ theo topic)** → **Đích C**: append `.antigravity/memory/instincts-archive.md`:
```
### <Tiêu đề ngắn>
- **Trạng thái:** Active
- **Nguồn:** <slug> · <YYYY-MM-DD>
- **Phản hồi từ User:** "<nguyên văn>"
- **Bản năng:** <rule hành động 1–2 câu>
- **Phạm vi:** Global | Chỉ topic: <topic>
```
Kiến thức brand/sản phẩm → Brand Guardian Mode C (đề xuất, chờ user).

## Giai đoạn 2 — Trình bày & ghi

1. Bảng đề xuất `| # | Feedback | Đích | Nội dung |` → chờ user xác nhận.
2. Ghi (append-only). Tag entry revision-log `[learned YYYY-MM-DD]`.
3. ```
   python scripts/optimize_instincts.py      # sinh lại instincts.md, chuyển instinct lint đã bao phủ vào bảng "Đã tự động hoá"
   python scripts/qa_lint.py --dump-rules   # xác nhận §0 đã load rule mới
   ```
4. Báo: số rule §0 / lint / instinct mới; kích thước `instincts.md` (≤8.000 ký tự).

## Không làm

- Không sửa entry cũ trong archive; không sửa `instincts.md` tay.
- Không ghi cùng 1 feedback vào 2 đích.
- Không tạo instinct cho thứ regex bắt được.
