---
name: Detailed Track (Pillar Content)
description: Quy trình sản xuất bài viết chuyên sâu 5 giai đoạn. Kích hoạt bằng lệnh `/detailed [keyword]` khi cần tạo nội dung Pillar chất lượng cao.
---

# Workflow: Detailed Track (Human-in-the-loop)

## Các bước thực hiện chi tiết

### 1. Nghiên cứu & Brief (Phase 1)
- **Kích hoạt:** [SEO Collector](file:///e:/project/hvs-company-info/.antigravity/agents/seo-collector.md).
- **Mục tiêu:** Tạo **Standard Content Brief**.
- **Lưu trữ:** `content/blog/1-outlines/Outline-[slug].md`.

### 2. Phê duyệt Lớp 1 (Outline Approval)
- **Hành động:** User kiểm tra Outline.
- **Lệnh duyệt:** Gõ `/approve` tại file Outline.
- **Tự động hóa sau duyệt:** AI Viết nháp -> Tự soát lỗi -> Gắn Link.

### 3. Sản xuất & Kiểm soát (Phase 2)
- **Lưu trữ nháp:** `content/blog/2-user-review/Draft-[slug].md`.
- **Nhiệm vụ:** Main Agent viết dựa trên Brief. Triệu hồi [Quality Guardian](file:///e:/project/hvs-company-info/.antigravity/agents/quality-guardian.md) để tự soát lỗi.

### 4. Phê duyệt Lớp 2 (Draft Approval)
- **Hành động:** User review nội dung bản Draft.
- **Lệnh duyệt:** Gõ `/approve` tại file Draft.

### 5. Hoàn tất & Lưu trữ (Phase 3)
- **Hành động:** Sau khi User duyệt Draft, **di chuyển (MOVE)** file sang `content/blog/3-finalized/Final-[slug].md` và xóa tệp cũ tại `2-user-review/`.
- **Naming Rule:** `Outline-`, `Draft-`, `Final-`.
