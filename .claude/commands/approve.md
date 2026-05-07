---
description: "Duyệt giai đoạn hiện tại: Outline→Draft/Final (tùy mode) hoặc Draft→Final"
allowed-tools: Read, Write, Bash
---

User đã duyệt. Tự xác định file đang làm việc và Pipeline_Mode, thực hiện tự động.

**Cách dùng:**
```
/approve          → Tự phát hiện file đang ở giai đoạn nào
```

---

## Nếu file hiện tại là Outline (`content/blog/1-outlines/Outline-*.md`)

1. Đọc toàn bộ Outline (YAML metadata + Content Brief)
2. Đọc `Pipeline_Mode` từ YAML:
   - `Express` → viết Draft → QA → Link → **Auto-finalize** (không dừng)
   - `Guided` → viết Draft → QA → Link → **Dừng, trình bày Draft**
   - `Auto` → (thường không gọi /approve, nhưng nếu có) → finalize ngay

**Viết Draft:**
3. Viết từng section theo đúng Key Points trong Brief — không đọc lại brand files (đã embedded trong YAML)
4. Lưu `content/blog/2-user-review/Draft-[slug].md` (Status: Draft)

**QA/QC:**
5. Chạy `.antigravity/skills/qa-qc/SKILL.md` → verify checklist → fix targeted nếu có item fail

**Internal Linking:**
6. Chạy `.antigravity/skills/internal-linking/SKILL.md`

**Nếu `Guided`:** Trình bày Draft → **DỪNG — chờ `/approve` lần nữa để finalize.**

**Nếu `Express`:** Tiếp tục Finalize ngay (bước bên dưới).

---

## Nếu file hiện tại là Draft (`content/blog/2-user-review/Draft-*.md`)

→ **Finalize** (mọi mode đều finalize khi /approve từ Draft):

1. Di chuyển → `content/blog/3-finalized/Final-[slug].md`
2. Cập nhật YAML: `Status: Finalized`
3. Xóa file Draft cũ tại `2-user-review/`
4. Cập nhật `seo-strategy/content-plan/progress-log.md`:
   - Xóa bài khỏi Active Pipeline
   - Thêm dòng mới nhất lên đầu Publication Log (Date, Keyword, Persona, Mode, File)
   - Cập nhật Published count trong Dashboard
5. Cập nhật `seo-strategy/content-plan/topic-clusters.md` (nếu tồn tại):
   - Tìm dòng khớp keyword/title
   - Đổi ⭕/🔄 → ✅, thêm `Final-[slug].md`
   - Cập nhật count ✅ trong cluster header và summary header
6. Cập nhật `seo-strategy/content-plan/sprint-backlog.md` (nếu tồn tại):
   - Xóa bài vừa finalize nếu có trong backlog
7. **Content Feedback Loop**: nếu file có Revision Log → chạy `.antigravity/skills/content-feedback-loop/SKILL.md` → đề xuất cập nhật `anti-ai-rules.md` nếu phát hiện pattern mới
8. Báo cáo: keyword | word count | file path | các file đã cập nhật
