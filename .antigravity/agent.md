# 🧠 Project Knowledge Hub (agent.md)

Chào mừng bạn đến với hệ sinh thái tri thức của HVS Securities SEO Content. Tệp này cung cấp cái nhìn tổng quan về dự án và cách phối hợp giữa con người và AI.

---

## 🎯 Mục tiêu dự án
Xây dựng hệ thống sản xuất nội dung SEO chuyên sâu, thực chiến và loại bỏ hoàn toàn "vibe AI" cho thương hiệu HVS Securities.

## 👥 Hệ thống Sub-Agents
- **SEO Collector:** Nghiên cứu đối thủ & SERP.
- **Brand Guardian:** Kiểm soát bản sắc thương hiệu & Anti-AI.
- **Quality Guardian:** Biên tập viên soát lỗi nội bộ.

## 🔄 Quy trình làm việc theo giai đoạn (Phases)
Quy trình [/detailed](file:///e:/project/hvs-company-info/.antigravity/rules/detailed-track.md) được chia làm 5 giai đoạn bắt buộc:

1.  **Phase 1 (Research):** Thu thập dữ liệu SERP & Intent. Kích hoạt bởi [SEO Collector](file:///e:/project/hvs-company-info/.antigravity/agents/seo-collector.md).
2.  **Phase 2 (Strategy):** Định hướng Brand & Persona. Kích hoạt bởi [Brand Guardian](file:///e:/project/hvs-company-info/.antigravity/agents/brand-guardian.md).
3.  **Phase 3 (Drafting):** Viết bản thảo. Thực hiện bởi Main Agent sau khi User gõ `/approve` Outline.
4.  **Phase 4 (Audit):** Soát lỗi & Tối ưu. Kích hoạt bởi [Quality Guardian](file:///e:/project/hvs-company-info/.antigravity/agents/quality-guardian.md).
5.  **Phase 5 (Finalize):** Đóng gói & Gắn link. Kích hoạt sau khi User gõ `/approve` bản Draft.

## 🏷️ Quy chuẩn Đặt tên (Naming Convention)
Tất cả các tệp nội dung phải có tiền tố trạng thái:
- `Outline-[slug].md` (Tại `content/blog/1-outlines/`)
- `Draft-[slug].md` (Tại `content/blog/2-user-review/`)
- `Final-[slug].md` (Tại `content/blog/3-finalized/`)

## 🛠️ Quy trình vận hành cốt lõi (Commands)
- `/detailed [keyword]`: Khởi chạy Phase 1 & 2.
- `/optimize [path]`: Tối ưu bài viết cũ (Phase 2 & 4).
- `/approve`: Duyệt để chuyển giai đoạn. Khi duyệt bản Draft, hệ thống tự động di chuyển sang `3-finalized/` và **xóa bản nháp cũ**.
- `/link`: Chạy độc lập Phase 5 cho bài bất kỳ.

## 📚 Tài liệu quan trọng
- **Quy tắc viết:** [anti-ai-rules.md](file:///e:/project/hvs-company-info/seo-strategy/resources/content-strategy/anti-ai-rules.md)
- **Quy trình chi tiết:** [rules/detailed-track.md](file:///e:/project/hvs-company-info/.antigravity/rules/detailed-track.md)
- **Bản đồ Workspace:** [rules/structure.md](file:///e:/project/hvs-company-info/.antigravity/rules/structure.md)

---
*Ghi chú: Luôn bắt đầu phiên làm việc bằng cách đọc tệp này.*
