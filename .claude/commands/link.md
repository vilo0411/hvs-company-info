---
description: "Gắn internal links cho bài đang viết, ưu tiên theo Topic Cluster"
allowed-tools: Read, Write, Bash
---

Chạy quy trình **Internal Linking** cho bài đang làm.

**Cách dùng:**
```
/link             → Gắn link cho bài đang mở/làm việc
```

---

Đọc `.antigravity/skills/internal-linking/SKILL.md` để biết đầy đủ quy tắc.

1. **Kiểm tra Topic Cluster** (nếu `topic-clusters.md` tồn tại):
   - Xác định bài này thuộc cluster nào
   - Báo cáo: "Bài này thuộc Cluster: [X] — Pillar: [Y]"
   - Nếu là Cluster article → link về Pillar là **bắt buộc**
   - Nếu là Pillar → link xuống ít nhất 2 Cluster articles đã Published

2. **Quét kho bài:** đọc `content/blog/3-finalized/`, lấy Target_Keyword từ YAML

3. **Đề xuất links** (phân loại rõ):
   ```
   🏛️ PILLAR LINK (bắt buộc nếu là Cluster article):
   "[anchor text]" → Final-xxx.md

   🛰️ CLUSTER LINKS (khuyến nghị):
   "[anchor text]" → Final-xxx.md  (lý do: liên quan về X)

   🔗 CROSS-CLUSTER (nếu phù hợp ngữ nghĩa):
   "[anchor text]" → Final-xxx.md
   ```

4. **Trình bày danh sách → chờ user xác nhận** trước khi chèn

5. **Chèn link:**
   - Ngữ nghĩa: `[anchor](đường dẫn)` lồng vào câu văn
   - Link Wheel: `>> Xem thêm: [Tên bài](đường dẫn)` cuối H2

**Ràng buộc:** Mỗi URL đích chỉ xuất hiện **đúng 1 lần** trong toàn bài.
