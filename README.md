# HVS Tài Chính Số — SEO Content System

Workspace sản xuất bài SEO tiếng Việt cho `taichinhso.hvsvn.com`, chạy bằng Claude Code hoặc Antigravity.
**Tài liệu vận hành duy nhất: [`CLAUDE.md`](CLAUDE.md).** File này chỉ là lối vào cho người mới.

## Bắt đầu nhanh

```
/keyword-plan 5              # chọn 5 bài tiếp theo vào sprint
/write "sàn otc là gì"       # Outline → (bạn /approve) → Draft → Final
/approve                     # duyệt giai đoạn hiện tại
/revise san-otc-la-gi "…"    # sửa 1 đoạn, có lint
/learn                       # đưa feedback vào rule/instinct
/audit                       # kiểm tra sức khỏe pipeline
```

## Kiến trúc

- `.antigravity/workflows/<cmd>.md` — SOP duy nhất cho mỗi lệnh. `.claude/commands/` và `.agents/workflows/` chỉ là wrapper.
- `.antigravity/rules/` — 4 rule cốt lõi: `workflow-integrity`, `seo-formatting`, `learning-loop`, `write-track`.
- `scripts/` — `qa_lint.py` (lint tất định, gate trước Quality Guardian), `topic_status.py`, `sprint_status.py`, `find_links.py`, `finalize.py`, `pipeline_audit.py`, `optimize_instincts.py`, `migrate_legacy.py`.
- `seo-strategy/resources/content-strategy/anti-ai-rules.md §0` — nguồn rule anti-AI mà lint đọc; sửa `.md`, không sửa code.
- `content/blog/` — `0-raw → 1-outlines → 2-user-review → 3-finalized`.

## Yêu cầu

Python 3.10+, `pip install pillow` (ảnh). SERP research cần DataForSEO key trong `.antigravity/config/api-keys.md` (xem `api-keys.example.md`); không có key thì SEO Collector dùng WebSearch.
