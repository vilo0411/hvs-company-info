---
description: "Duyệt giai đoạn hiện tại: Outline→Draft/Final (tùy Pipeline_Mode) hoặc Draft→Final"
---

User đã duyệt. Tự xác định trạng thái file đang làm việc và thực hiện.

**Cách dùng:**
```
/approve
```

---

## Nếu file hiện tại là Outline (`1-outlines/Outline-*.md`)

1. Đọc toàn bộ Outline + YAML metadata
2. Đọc `Pipeline_Mode` từ YAML:
   - `Express` → viết Draft → QA → Link → Auto-finalize (không dừng)
   - `Guided` → viết Draft → QA → Link → Dừng, trình bày Draft

**Viết Draft:**
3. Viết từng section theo Key Points trong Brief (không đọc lại brand files — đã trong YAML)
4. Sao chép phần `## Revision Log` (hoặc `## Nhật ký chỉnh sửa (Revision Log)`) từ Outline sang cuối file Draft.
5. Lưu `content/blog/2-user-review/Draft-[slug].md`

**QA/QC:**
6. Chạy `.antigravity/skills/qa-qc/SKILL.md` → verify checklist → fix targeted

**Internal Linking:**
7. Chạy `.antigravity/skills/internal-linking/SKILL.md`

**Nếu Guided:** Trình bày Draft → **DỪNG — chờ /approve lần nữa.**

**Nếu Express:** Tiếp tục Finalize ngay.

---

## Nếu file hiện tại là Draft (`2-user-review/Draft-*.md`)

→ **Finalize:**

1. Di chuyển → `content/blog/3-finalized/Final-[slug].md` (Bảo toàn phần `## Revision Log` nguyên vẹn ở cuối file)
2. Cập nhật YAML: `Status: Finalized`
3. Xóa Draft cũ tại `2-user-review/` VÀ Outline cũ tại `1-outlines/` (Chỉ thực hiện sau khi đã di chuyển và bảo toàn Revision Log)
4. Cập nhật `seo-strategy/content-plan/progress-log.md`:
   - Xóa khỏi Active Pipeline
   - Thêm lên đầu Publication Log
   - Cập nhật Published count
5. Cập nhật `seo-strategy/content-plan/topic-clusters.md` (nếu tồn tại):
   - Đổi ⭕/🔄 → ✅, thêm tên file
   - Cập nhật count ✅ trong cluster header và summary header
6. Cập nhật `seo-strategy/content-plan/sprint-backlog.md` (nếu tồn tại):
   - Xóa bài vừa finalize khỏi backlog
7. **Learning** — nếu file Finalized có Revision Log (chứa lịch sử chỉnh sửa từ cả giai đoạn Outline và Draft):
   - **Content Feedback Loop**: chạy `.antigravity/skills/content-feedback-loop/SKILL.md` → cập nhật `anti-ai-rules.md` + `anti-ai-digest.md` nếu phát hiện pattern mới
   - **Brand Guardian Mode C**: chạy `.antigravity/agents/brand-guardian.md` Mode C → đề xuất cập nhật `glossary.md` / `hvs-profile.md` / `financial-logic.md` → chờ xác nhận trước khi ghi
8. Báo cáo: keyword, word count, file path, các file đã cập nhật
