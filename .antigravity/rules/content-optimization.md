---
name: Content Optimization
description: Nâng cấp bài cũ/bài thô sang chuẩn HVS. Kích hoạt bằng lệnh `/optimize [path]` khi cần sửa văn phong Anti-AI và cấu trúc SEO.
---

# Workflow: Content Optimization (/optimize)

Quy trình này bỏ qua bước nghiên cứu SERP (Phase 1) và tập trung vào việc tinh chỉnh văn phong, kiểm soát chất lượng.

## Các bước thực hiện

### 1. Phân tích Hiện trạng (Phase 2)
- **Kích hoạt:** [Brand Guardian Mode B](.antigravity/agents/brand-guardian.md).
- **Hành động:** AI đọc nội dung hiện tại và đối soát với `.antigravity/rules/anti-ai-digest.md` để liệt kê vi phạm cụ thể.

### 2. Thực thi Nâng cấp (Phase 3)
- **Hành động:** Main Agent viết lại các đoạn văn "vibe AI", lồng ghép USPs của HVS (HVS Demo, Forum) và điều chỉnh tone màu Persona.

### 3. Kiểm định Chất lượng (Phase 4)
- **Kích hoạt:** [Quality Guardian](.antigravity/agents/quality-guardian.md).
- **Hành động:** Chạy vòng lặp soát lỗi tự động. Đảm bảo bản thảo mới không còn lỗi logic hoặc AI-vibe.

### 4. Gắn Link & Hoàn tất (Phase 5)
- **Hành động:** Chèn Link nội bộ qua kỹ năng [internal-linking](.antigravity/skills/internal-linking/SKILL.md) và lưu vào thư mục `2-user-review/`.

---
*Lệnh kích hoạt: `/optimize [đường dẫn tệp]`*
