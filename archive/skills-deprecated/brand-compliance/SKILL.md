---
name: Brand & Style Compliance
description: Trích xuất quy tắc HVS tại Phase 1. Kích hoạt bởi Brand Guardian Mode A.
---

# Skill: Brand & Style Compliance

Đối chiếu nội dung với bộ quy tắc thương hiệu HVS, Persona người dùng, và bài học từ feedback cũ.

## Công cụ sử dụng
- `Read`: Đọc các file quy tắc (`anti-ai-digest.md`, `glossary.md`)
- `Grep`: Tìm pattern feedback cũ trong `2-user-review/`

## Quy trình trích xuất Context

1. **Persona Filter:** Dựa trên Search Intent (Informational/Commercial...) → lọc sản phẩm HVS phù hợp (F0 → HVS Demo, Sinh viên → HVS Thực tập số)
2. **Anti-AI Filter:** Đọc `.antigravity/rules/anti-ai-digest.md` → trích xuất FORBIDDEN_STRINGS, FORBIDDEN_PATTERNS, REQUIRED items liên quan đến topic bài viết
3. **Terminology Sync:** Đọc `glossary.md` → lấy đúng thuật ngữ chuẩn (ví dụ: "HVS Demo" thay vì "app chơi thử")

## Kích hoạt

Skill được gọi bởi **Brand Guardian Mode A** sau khi nhận keyword và Search Intent từ Main Agent.
