---
name: image
description: Tạo ảnh cho bài (HTML template → Edge headless → WebP → chèn). Args: <slug> [--cover-only] [--plan]
---

# /image <slug>

Agent: `.antigravity/agents/visual-architect.md`. Skill đầy đủ (typology A–I, template, prompt, brand safety): `.antigravity/skills/image-generation/SKILL.md`.

1. Đọc `Final-<slug>.md` (hoặc Draft) → đề xuất số ảnh theo loại bài (bảng trong SKILL) → `--plan` thì DỪNG tại đây chờ user chọn.
2. Với mỗi ảnh: chọn template trong `.antigravity/skills/image-generation/references/*.html`, điền nội dung, màu theo `templates/palette-config.yaml` (`#7B57E0` / `#20C997`).
3. Render: Edge headless `--window-size=1000,600` (cover) hoặc `800,500` (inline) → `content/blog/assets/raw-images/<slug>/<name>.png`.
4. `python .antigravity/skills/image-generation/scripts/image_processor.py --input <png> --output content/blog/assets/images/<slug>/<name>.webp`.
5. Chèn `![<alt mô tả thực thể>](content/blog/assets/images/<slug>/<name>.webp)` + caption `*Hình N: …*` đúng section. **Không** dùng `file:///`.
6. `python scripts/qa_lint.py <file> --no-sitemap` → `LINK-file` = 0. Cập nhật manifest `content/blog/assets/manifests/<slug>.json`.
