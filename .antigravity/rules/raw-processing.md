---
name: Raw Content Processing
description: Chuẩn hóa dữ liệu thô (HTML/text/Google Docs export) sang Markdown hoặc Outline. Kích hoạt bởi /raw.
---

# Rule: Raw Content Processing

1. **Tên file:** mọi file trong `content/blog/0-raw/` phải là `Raw-<slug>.md` — `python scripts/normalize_raw.py --apply` làm việc này, giữ tiêu đề gốc trong YAML `Source_Title`.
2. **Chuyển đổi:** strip HTML giữ heading; Markdown chuẩn; loại `---`, LaTeX, `file:///`, ngoặc kép nhấn mạnh (chạy `qa_lint.py --fix` cho phần cơ học).
3. **YAML:** `Author`, `Status: Raw | Processed`, `Source_Title`, `Imported`, `Target_Keyword`, `Persona`, `Search_Intent`.
4. **Routing:** bài đầy đủ → ở lại `0-raw/`; outline có cấu trúc → `1-outlines/Outline-<slug>.md` (thêm `Word_Count` từng H2).
5. **Trạng thái:** `topic_status.py --find` → `--set "In Progress"` hoặc `--add`. Không sửa `progress-log.md` tay (`sprint_status.py --sync` tự đếm).
6. Bước tiếp: `/optimize` (bài đầy đủ) hoặc `/approve` (outline).
