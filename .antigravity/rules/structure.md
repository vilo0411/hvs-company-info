# 🗺️ Workspace Architecture (structure.md)

Cấu trúc thư mục chuẩn Antigravity dành cho dự án HVS Securities SEO Content.

---

## 📂 1. Thư mục Hệ thống (.antigravity/)

| Thư mục/Tệp | Vai trò (Role) |
| :--- | :--- |
| **`agent.md`** | **Tri thức trung tâm.** Tệp đầu tiên AI phải đọc để nắm bắt dự án. |
| **`agents/`** | **Chuyên gia AI.** Chứa chỉ dẫn cho SEO Collector, Brand Guardian, Quality Guardian. |
| **`rules/`** | **Quy trình & Quy tắc.** Chứa Detailed Track, Content Optimization và bản đồ này. |
| **`skills/`** | **Kỹ năng cục bộ.** Chứa các bộ công cụ thực thi (Internal Link, Audit). |
| **`artifacts/`** | **Sản phẩm AI.** Lưu trữ sơ đồ, hình ảnh minh họa cho bài viết. |
| **`memory/`** | **Kinh nghiệm.** Lưu trữ tệp `DECISIONS.md` về các thỏa thuận chiến lược. |

---

## 📂 2. Thư mục Nội dung (Content)
- `content/blog/1-outlines/`: `Outline-[slug].md`.
- `content/blog/2-user-review/`: `Draft-[slug].md`.
- `content/blog/3-finalized/`: `Final-[slug].md`.

---

## 📂 3. Thư mục Chiến lược (Strategy)
- `seo-strategy/resources/content-strategy/`: `anti-ai-rules.md`, `persona.md`.
- `seo-strategy/content-plan/progress-log.md`: Bảng tiến độ.
