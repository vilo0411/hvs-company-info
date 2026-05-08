---
name: Internal Linking
description: Gắn internal links đa chế độ (Cluster, Silo, Power, Conversion). Sử dụng bộ Anchor Index đã duyệt.
---

# Skill: Internal Linking

## Nguyên tắc Anchor Text (HVS Standard)

Chúng ta chỉ sử dụng 2 loại Anchor chính để đảm bảo sức mạnh SEO và tính tự nhiên:

1.  **Exact Match (Chính xác):** Trùng 100% từ khóa chính của bài đích. Sử dụng tối đa 15% tổng số link trỏ về bài đó.
2.  **Partial Match (Bổ trợ/Semantic):** Sử dụng các cụm từ biến thể được phê duyệt trong `anchor-index.md`. Đây là loại ưu tiên hàng đầu (65%+).

**Cấm:** Sử dụng các từ Generic vô nghĩa như "tại đây", "xem thêm" (trừ khi dùng Title Link ở cuối đoạn).

---

## Nguồn dữ liệu (theo thứ tự ưu tiên)
1. **`seo-strategy/content-plan/anchor-index.md`** — Nguồn tra cứu bộ từ khóa Exact/Partial cho từng bài.
2. **`seo-strategy/content-plan/topic-clusters.md`** — Xác định cấu trúc nhóm và vai trò bài viết.
3. **`seo-strategy/content-plan/internal-link-dashboard.md`** — Kiểm tra mật độ link hiện tại để quyết định loại Anchor cần dùng (tránh Over-opt).

---

## Quy trình thực hiện

1. **Xác định Mode & Đối tượng:**
   - Nếu chạy bình thường: Gắn link cho bài hiện tại.
   - Nếu chạy `--backfill [slug]`: Quét toàn bộ kho bài cũ để tìm chỗ trỏ link về bài `[slug]`.

2. **Tra cứu Anchor Index:** Đọc `anchor-index.md` để lấy danh sách từ khóa được phép dùng cho bài đích.

3. **Tối ưu ngữ cảnh (Contextual Optimization):**
   - Không chỉ tìm từ có sẵn. Agent chủ động đề xuất **sửa lại hoặc thêm câu mới** vào bài viết để lồng ghép Anchor Partial Match một cách tự nhiên nhất.
   - Ví dụ: Thay vì tìm từ "chứng khoán nợ", Agent có thể đề xuất sửa câu *"Trái phiếu là một công cụ tài chính"* thành *"Trái phiếu là một loại [chứng khoán nợ](...) quan trọng"*.

4. **Kiểm tra Ratio & Xung đột (Anchor Pruning):**
   - Tra cứu Dashboard. Nếu bài đích đang bị `⚠️ Over-opt`, Agent tuyệt đối không dùng Exact Match, chỉ dùng Partial Match hoặc Title Link.
   - **Quy tắc Cắt tỉa (Pruning):** Khi một bài mới được thêm vào Index, nếu Keyword chính của nó trùng với Partial Match của bài khác, Agent phải đề xuất xóa bỏ Partial Match đó ở bài cũ.

5. **Trình bày danh sách đề xuất:**
   ```
   🚀 CHẾ ĐỘ: [Normal / Backfill]
   📍 BÀI ĐÍCH: [Tên bài]
   
   📝 ĐỀ XUẤT SỬA NỘI DUNG & CHÈN LINK:
   - Đoạn gốc: "..."
   - Đoạn sửa: "... [Anchor Text](URL) ..."
   - Loại Anchor: [Exact / Partial / Title]
   ```

---

## Ràng buộc
- Mỗi bài viết đích chỉ xuất hiện **đúng 1 lần** trong toàn bài.
- Đường dẫn link luôn sử dụng dạng tương đối: `content/blog/3-finalized/Final-[slug].md`.
- Tuyệt đối không chiếm dụng các cụm từ là từ khóa của các bài viết khác (tra cứu Planned trong `topic-clusters.md`).
