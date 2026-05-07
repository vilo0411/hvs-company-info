---
name: Internal Linking
description: Gắn internal links theo Topic Cluster. Primary source: topic-clusters.md. Kích hoạt trong Phase 5 của write-track.
---

# Skill: Internal Linking

## Nguồn dữ liệu (theo thứ tự ưu tiên)

1. **`seo-strategy/content-plan/topic-clusters.md`** — primary source: biết bài nào đã Published trong cluster, Pillar là file nào
2. **Linking Plan trong Outline YAML** — đã có `Internal_Links` với file và anchor suggestion
3. **Scan `content/blog/3-finalized/`** — chỉ để verify slug tồn tại, lấy đường dẫn chính xác

Không cần đọc YAML từng file finalized — topic-clusters.md đã có metadata cần thiết.

---

## Quy trình

1. **Đọc Linking Plan** từ YAML Outline (hoặc Draft nếu đã qua Phase 3):
   - `Cluster_Role` → Pillar hay Cluster article?
   - `Internal_Links` → danh sách link obligations

2. **Priority links:**
   - 🏛️ **Pillar link** (BẮT BUỘC nếu là Cluster article): link về Pillar của cluster
   - 🛰️ **Same-cluster links** (khuyến nghị): các bài Published cùng cluster
   - 🔗 **Cross-cluster** (nếu phù hợp ngữ nghĩa): bài từ cluster khác

3. **Tra cứu trong topic-clusters.md**: tìm Published articles trong cùng cluster → lấy slug file

4. **Verify slug**: dùng Bash `ls content/blog/3-finalized/` để confirm file tồn tại

5. **Trình bày danh sách links** trước khi chèn:
   ```
   🏛️ PILLAR LINK (bắt buộc):
   "[anchor text gợi ý]" → Final-[slug].md

   🛰️ CLUSTER LINKS (khuyến nghị):
   "[anchor]" → Final-[slug].md  (lý do: liên quan về X)

   🔗 CROSS-CLUSTER (nếu có):
   "[anchor]" → Final-[slug].md
   ```

6. **Chèn link** vào bài:
   - Link ngữ nghĩa: `[anchor text](content/blog/3-finalized/Final-[slug].md)` lồng vào câu văn
   - Link wheel: `>> Xem thêm: [Tên bài](...)` cuối H2 nếu phù hợp

---

## Ràng buộc

- Mỗi URL đích xuất hiện **đúng 1 lần** trong toàn bài
- Không link ra ngoài trừ khi có yêu cầu
- Anchor text phải tự nhiên trong câu, không ép buộc
