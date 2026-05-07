---
description: "Gắn internal links cho bài đang viết, ưu tiên theo Topic Cluster"
---

Chạy quy trình **Internal Linking**.

**Cách dùng:**
```
/link
```

Đọc `.antigravity/skills/internal-linking/SKILL.md` để biết đầy đủ quy tắc.

1. **Kiểm tra Topic Cluster** (`seo-strategy/content-plan/topic-clusters.md`):
   - Bài này thuộc cluster nào? Pillar là gì?
   - Nếu là Cluster article → link về Pillar **bắt buộc**
   - Nếu là Pillar → link xuống ít nhất 2 Cluster articles đã Published

2. **Quét kho bài:** đọc `content/blog/3-finalized/`, lấy Target_Keyword từ YAML

3. **Đề xuất links** (phân loại rõ):
   ```
   🏛️ PILLAR LINK (bắt buộc): "[anchor]" → Final-xxx.md
   🛰️ CLUSTER LINKS: "[anchor]" → Final-xxx.md
   🔗 CROSS-CLUSTER: "[anchor]" → Final-xxx.md
   ```

4. **Trình bày → chờ user xác nhận** trước khi chèn

5. **Chèn link:** ngữ nghĩa inline hoặc Link Wheel cuối H2

**Ràng buộc:** Mỗi URL đích chỉ xuất hiện **đúng 1 lần** trong toàn bài.
