---
description: "Gắn internal links cho bài đang viết với nhiều chế độ: Cluster, Silo, Power, Conversion"
---

Chạy quy trình **Internal Linking** để tối ưu hóa sức mạnh SEO và trải nghiệm người dùng.

**Cách dùng:**
```
/link [mode]
```

**Các chế độ (Modes):**
- `--cluster` (Mặc định): Liên kết Pillar <-> Cluster trong cùng một nhóm chủ đề.
- `--silo`: Liên kết dọc và ngang trong cùng một Category lớn (Group).
- `--power`: Tập trung đẩy link về các trang "Super Pillar" có authority cao.
- `--conversion`: Ưu tiên link về sản phẩm/dịch vụ của HVS (Demo, Forum, Tài chính số).

Đọc `.antigravity/skills/internal-linking/SKILL.md` để biết chi tiết logic từng mode.

### Quy trình thực hiện:

1. **Xác định Mode:** Nếu không chỉ định, mặc định dùng `--cluster`.
2. **Kiểm tra Topic Cluster** (`seo-strategy/content-plan/topic-clusters.md`):
   - Xác định vị trí của bài viết hiện tại trong cấu trúc tổng thể.
3. **Tra cứu & Gợi ý URL từ Sitemap (`https://taichinhso.hvsvn.com/sitemap.xml`):**
   - Chạy `python .antigravity/scripts/fetch_sitemap.py --suggest "[từ khóa]"` hoặc `--search "[chủ đề]"` để tìm đúng URL bài viết đang live trên sitemap.
   - BẮT BUỘC dùng URL tuyệt đối `https://taichinhso.hvsvn.com/...` (KHÔNG DÙNG `Final-xxx.md`, `file://` hay đường dẫn tương đối).
4. **Đề xuất links theo Mode (100% Khớp Sitemap):**
   ```
   🚀 MODE: [Tên mode]
   🏛️ PRIMARY LINKS (Pillar): "[anchor]" → https://taichinhso.hvsvn.com/...
   🛰️ SECONDARY LINKS (Spoke): "[anchor]" → https://taichinhso.hvsvn.com/...
   🎁 CONVERSION LINKS (nếu có): "[anchor]" → https://taichinhso.hvsvn.com/thuc-tap-so (hoặc trang sản phẩm tương ứng)
   ```
5. **Trình bày → chờ user xác nhận** trước khi chèn.
6. **Chèn link & Xác thực:**
   - Tự động chèn inline với anchor text tự nhiên (ưu tiên Partial Match theo `anchor-index.md`).
   - Chạy `python .antigravity/scripts/fetch_sitemap.py --validate [đường_dẫn_file]` để xác nhận 0 lỗi 404/broken.

**Ràng buộc Bất biến:** 
- Mỗi URL đích chỉ xuất hiện **đúng 1 lần** trong toàn bài.
- 100% URL phải tồn tại trong `https://taichinhso.hvsvn.com/sitemap.xml`.
- Anchor text phải tự nhiên, không dùng các từ "AI-vibe" (xem `anti-ai-rules.md`).
