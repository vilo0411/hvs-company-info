# Strategic Decisions & Lessons Learned (DECISIONS.md)

Tệp này lưu trữ các quyết định quan trọng đã được thống nhất giữa User và Agent để đảm bảo tính nhất quán lâu dài. Entry mới ghi trên cùng mỗi mục; entry bị thay thế đánh dấu `~~SUPERSEDED~~`.

---

## 🏛️ Quyết định Kiến trúc

- **[2026-09-21] Refactor theo mẫu seo-writer-agent:** SOP command duy nhất tại `.antigravity/workflows/<cmd>.md`; `.claude/commands/` và `.agents/workflows/` là wrapper ≤12 dòng. Script ở `scripts/` (qa_lint, topic_status, sprint_status, find_links, finalize, pipeline_audit, optimize_instincts, migrate_legacy). Rule gộp về 4 file: `workflow-integrity.md`, `seo-formatting.md`, `learning-loop.md`, `write-track.md` (+ `content-optimization.md`, `raw-processing.md`).
- **[2026-09-21] QA 2 tầng:** `python scripts/qa_lint.py` (tất định, exit 0 bắt buộc) chạy **trước** Quality Guardian (ngữ nghĩa). Rule lint đọc từ `anti-ai-rules.md §0`, `glossary.md`, `confirm-with-leadership.md` — sửa .md, không sửa code. QA loop tối đa 2 vòng.
- **[2026-09-21] Memory 2 tầng:** `.antigravity/memory/instincts-archive.md` (append-only) → `optimize_instincts.py` → `instincts.md` (≤8k, auto). Lỗi regex bắt được → lint, không thành instinct.
- **[2026-09-21] Pipeline_Mode:** Express (1 gate sau Outline) là mặc định; Guided `--step` 2 gate; Auto `--auto` 0 gate chỉ khi user gõ rõ. Thay thế quyết định 2026-05-07 bên dưới.
- **[2026-09-21] Phase numbering:** 0 Pre-flight · 1 Context · 2 Outline · 3 Draft+Lint+QG+Link · 4 User review · 5 Finalize+Learn (theo `write-track.md`; bỏ bản 0–6 cũ).
- **[2026-09-21] SERP:** mặc định bật cho `/write` đơn lẻ (`serp_research.py` DataForSEO, fallback WebSearch). `--no-serp` chỉ khi user gõ rõ hoặc `--sprint`; YAML `SERP_Research: false`.
- **[2026-09-21] Brand Guardian:** bỏ Mode A khỏi `/write` (Main Agent đọc brand file trực tiếp ở Bước 0). Giữ Mode B (`/optimize` audit) và Mode C (đề xuất cập nhật kiến thức sau `/approve`).
- **[2026-09-21] Outline xóa khi finalize** (`finalize.py` snapshot `Word_Count` từng H2 vào YAML `Section_Targets` trước khi xóa).
- **[2026-05-07]:** Chuyển từ Single-Agent sang **Multi-Agent (Sub-agent) Framework**.
- **[2026-05-07]:** Áp dụng cấu trúc thư mục GSD (Agents, Docs, Scripts).
- ~~**[2026-05-07]:** Quy trình phê duyệt 2 lớp (Outline & Draft) là bắt buộc.~~ SUPERSEDED 2026-09-21 (Pipeline_Mode).

## ✍️ Quyết định Nội dung

- **[2026-09-21] Phân tầng sản phẩm:** **HVS Thực tập số** là phễu chính cho MỌI persona; Demo/Forum là công cụ hỗ trợ. Học phí "từ 1.500.000 VNĐ". Không nêu % phí giao dịch, không nhắc lịch sử xử phạt (`confirm-with-leadership.md`). Thay thế quyết định 2026-05-07 bên dưới.
- **[2026-09-21] YAML:** `Pipeline_Mode` (không `Mode:`); `HVS_Products` là list chuỗi phẳng; `Section_Targets` do finalize sinh.
- **[2026-09-21] Link:** cấm `file:///` và link `.md` ở mọi nơi kể cả ảnh; ảnh dùng path repo-relative `content/blog/assets/images/<slug>/…`; link bài = URL sitemap tuyệt đối.
- **[2026-09-21] Từ Tier 2** ("Đột phá", "Hệ sinh thái", "Cốt lõi"…): tối đa 1 lần/bài, không nâng lên Tier 1.
- **[2026-09-21] Kết luận:** H2 cuối là `## Kết luận` (được thêm `: <góc nhìn>`), chứa "HVS", 150–200 từ, không rập khuôn "Checklist 4 bước".
- **[2026-09-21] Màu brand cho ảnh:** theo `resources/company/visual-brand-guidelines.md` (`#7B57E0` primary, `#20C997` accent); canvas 1000×600 hero / 800×500 inline.
- ~~**[2026-05-07]:** Tất cả bài viết F0 bắt buộc phải dẫn dắt đến sản phẩm **HVS Demo** và **HVS Forum**.~~ SUPERSEDED 2026-09-21 (phân tầng sản phẩm).
- **[2026-05-07]:** Naming convention bắt buộc dùng tiền tố `Outline-`, `Draft-`, `Final-`.
- **[2026-05-07]:** Hoàn tất thiết lập bộ nhận diện thương hiệu tại `resources/company/` (Identity, USPs).
- **[2026-05-07]:** Content Brief theo `.antigravity/skills/seo-research/examples/brief-template.md` (H1, Sapo, Heading Details + Word_Count, Conclusion).
- **[2026-05-25]:** Đoạn phân tích kỹ thuật hoặc liệt kê nguyên nhân/rủi ro dài → chuyển thành bullet/numbered list kèm bôi đậm từ khóa tiêu điểm.

## 💡 Bài học kinh nghiệm (Retrospective)

- Rule không có script enforce sẽ không được tuân thủ: sau 4 tháng, 66 bài Final có `file:///`, 35 bài LaTeX, 215 bài YAML cũ dù rule đã cấm. → mọi rule cơ học phải có lint ID.
- Hai bản copy của cùng một SOP sẽ lệch nhau trong vài tuần (`.claude/commands` vs `.agents/workflows`). → 1 SOP, wrapper mỏng.
- Tránh sử dụng lệnh `dir /s /b` trong terminal trên Windows, thay bằng đường dẫn tuyệt đối.
- Luôn gắn link nội bộ theo ngữ nghĩa thay vì gắn link đại trà vào các từ khóa chung như "F0".
