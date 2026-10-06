---
name: raw
description: Chuẩn hóa nội dung thô (HTML/text/Google Docs export) → Raw-<slug>.md hoặc Outline-<slug>.md. Args: [path] | --all
---

# /raw [path | --all]

Rule: `.antigravity/rules/raw-processing.md`. Trống → liệt kê `content/blog/0-raw/` chưa có prefix `Raw-` và hỏi.

## Bước 1 — Chuẩn hóa tên & YAML (script)

```
python scripts/normalize_raw.py                 # dry-run: liệt kê file sẽ đổi tên
python scripts/normalize_raw.py --apply         # <Tiêu đề>.md → Raw-<slug>.md + YAML Source_Title / Imported
```

## Bước 2 — Chuyển đổi nội dung (từng file)

- HTML → strip tag, giữ heading; text → Markdown chuẩn; bỏ `---`, LaTeX, `file:///`.
- Suy luận `Target_Keyword` (từ H1/tiêu đề), `Persona` (theo `persona-mapping.md`), `Search_Intent`.
- Có cấu trúc H2/H3 rõ + chưa có nội dung → route sang `content/blog/1-outlines/Outline-<slug>.md` (thêm `Word_Count` từng H2).
- Bài đầy đủ → giữ `Raw-<slug>.md`, `Status: Processed`.

## Bước 3 — Trạng thái

```
python scripts/topic_status.py --find "<keyword>"           # có → --set "In Progress"; không → --add
```

## Bước 4 — Báo cáo

File lưu ở đâu · bước tiếp: `/optimize content/blog/0-raw/Raw-<slug>.md` (bài đầy đủ) hoặc `/approve` (outline).
