---
trigger: always_on
---

# Writing Guidelines — HVS Content

## Nguyên tắc bất biến
Mọi bài viết phải PASS toàn bộ checklist này trước khi trình bày cho user.

## Anti-AI Checklist (tự kiểm tra trước khi output)

### Từ & cụm từ bị cấm tuyệt đối
Không dùng: "Trong thế giới không ngừng phát triển", "Mở khóa tiềm năng", "Hành trình", "Hơn cả một", "Nâng tầm", "Giải pháp toàn diện", "Đáng chú ý là", "Tóm lại,", "Đại dương", "Sóng dữ"
→ Full list: `seo-strategy/resources/content-strategy/anti-ai-rules.md`

### Translation-vibe detector
- ❌ Câu bị động dồn dập: "được thực hiện", "được xem là", "được cho là"
- ❌ Danh từ hóa kiểu Anh: "việc thực hiện" → dùng "thực hiện"; "sự phát triển" → "phát triển"
- ❌ Câu quá 30 từ với mệnh đề lồng nhau

### Specificity check — mỗi claim phải có bằng chứng cụ thể
- ✅ Mã cổ phiếu thực: VCB, VNM, HPG (không dùng "một doanh nghiệp lớn")
- ✅ Con số thực: phí 0.15%, biên độ ±7% (không dùng "một khoản phí nhỏ")
- ✅ Tên sàn cụ thể: HOSE, HNX (không dùng "sàn chứng khoán")

### Sentence rhythm
- ❌ Hơn 3 câu liên tiếp cùng cấu trúc Subject + Verb + Object

## Persona & Xưng hô
- Gọi người đọc: **"bạn"** (không dùng "quý nhà đầu tư", "bạn đọc")
- Gọi bản thân HVS: **"HVS"** hoặc **"chúng tôi"**
- Icon & Formatting: **Không dùng icon ở H1, H2, H3**. **CẤM DÙNG LATEX** cho công thức toán (dùng Unicode thuần: `×`, `÷`, `-`, `+`, `=`).
- **Tiêu đề H1:** Cô đọng, đánh đúng Intent, không dùng đuôi giật tít AI-vibe ("từ A-Z", "tất tần tật", "chi tiết nhất"...).
- **Cấu trúc phần Kết luận (H2):** ❌ Cấm mặc định rập khuôn mẫu "Checklist 4 bước..." cho mọi bài viết. ✅ Bắt buộc luân phiên đa dạng hóa các hình thức như: *3 Nguyên tắc vàng tư duy cốt lõi*, *Đối chiếu cạm bẫy F0 vs Tư duy chuyên nghiệp*, *Tóm lược góc nhìn dòng tiền & Lộ trình thực chiến*.
- Nguồn pháp lý: chỉ `vanban.chinhphu.vn` hoặc `vbpl.vn`

## Anchor Text & Internal Linking Rules
- ❌ **Cấm gượng ép anchor exact match "là gì" trong câu prose:** Không dùng `...khi giá vượt qua [hỗ trợ kháng cự là gì]...` hay `...thực hiện [cắt lỗ là gì]...`.
- ✅ **Bắt buộc dùng Anchor Text ngữ nghĩa tự nhiên (Partial Match / Semantic):** Sử dụng các cụm từ khớp ngữ cảnh tự nhiên như `...khi giá vượt qua [vùng hỗ trợ và kháng cự]...`, `...thực hiện [nguyên tắc cắt lỗ]...`, `...kết hợp [đường trung bình động MA]...`, `...xem [chỉ báo RSI]...`.

## QA/QC trước khi output
Đọc `.antigravity/skills/qa-qc/SKILL.md` và tự chạy checklist. Chỉ trình bày bản đã PASS.

