---
description: "Gắn internal links cho bài đang viết với nhiều chế độ: Cluster, Silo, Power, Conversion"
allowed-tools: Read, Write, Bash
---

Chạy quy trình **Internal Linking** để tối ưu hóa sức mạnh SEO và trải nghiệm người dùng.

**Cách dùng:**
```
/link [mode]       → Gắn link cho bài đang mở theo chế độ đã chọn
```

**Các chế độ (Modes):**
- `--cluster` (Mặc định): Liên kết Pillar <-> Cluster trong cùng một nhóm chủ đề.
- `--silo`: Liên kết dọc và ngang trong cùng một Category lớn (Group).
- `--power`: Tập trung đẩy link về các trang "Super Pillar" có authority cao.
- `--conversion`: Ưu tiên link về sản phẩm/dịch vụ của HVS (Demo, Forum, Tài chính số).

---

Đọc `.antigravity/skills/internal-linking/SKILL.md` để biết đầy đủ quy tắc.

1. **Xác định Mode:** Nếu không chỉ định, mặc định dùng `--cluster`.
2. **Kiểm tra Topic Cluster** (`seo-strategy/content-plan/topic-clusters.md`):
   - Xác định vị trí của bài viết hiện tại trong cấu trúc tổng thể.
3. **Quét kho bài:** Đọc `content/blog/3-finalized/` để verify các bài đã xuất bản.
4. **Đề xuất links theo Mode:**
   ```
   🚀 MODE ĐANG CHẠY: [Tên mode]
   
   🏛️ PRIMARY LINKS: "[anchor]" → Final-xxx.md
   🛰️ SECONDARY LINKS: "[anchor]" → Final-xxx.md
   🎁 CONVERSION LINKS (nếu có): "[anchor]" → [URL/File]
   ```
5. **Trình bày → chờ user xác nhận** trước khi chèn.
6. **Chèn link:** 
   - Inline: Lồng vào câu văn một cách tự nhiên.
   - Link Wheel: `>> Xem thêm: [Tên bài](...)` cuối H2 hoặc cuối bài.

**Ràng buộc:** 
- Mỗi URL đích chỉ xuất hiện **đúng 1 lần** trong toàn bài.
- Anchor text phải tự nhiên, không dùng các từ "AI-vibe" (xem `anti-ai-rules.md`).
