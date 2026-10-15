# Revision Log — HVS Content

> Append-only. `/approve`, `/learn`, `/revise` ghi feedback; `qa_lint.py --log` ghi điểm.

## QA Score Log (auto — qa_lint.py)

| Ngày | Slug | Score | C/M/m | Theo nhóm |
|---|---|---|---|---|
| 2026-09-21 | bieu-do-ky-thuat | 95 | 0/0/8 | anti_=100 seo=97 reada=79 link=100 brand=100 |

## Human Feedback & Revision History

### 2026-10-15 - chung-khoan-la-gi [demo rule data_anchor]
- Lỗi đã sửa: bài định nghĩa thuần, slop 77 (evidence 0.2/100 từ, anchor 80%). Thêm mỏ neo theo đúng ý định từng H2: H2 định nghĩa dùng mỏ neo pháp lý + cấu trúc (Luật Chứng khoán, lô 100 cp, phiên 9h00-14h45, biên độ 7%); H2 phân loại dùng kỳ hạn trái phiếu 1-10 năm; H2 "tại sao nên" dùng số so sánh thật (VN-Index 770 điểm 24/08/2017 → 1.698 điểm 15/10/2026, +120,6% / 9,1 năm, CAGR 9,0%, chỉ số giá chưa gồm cổ tức); H2 rủi ro dùng biên độ thiệt hại (5 phiên sàn liên tiếp ≈ -30%; VN-Index -40% từ 1.529 điểm 06/01/2022 về 912 điểm 15/11/2022).
- Pattern: bài định nghĩa KHÔNG cần dữ liệu giá sống. Mỏ neo đúng cho nó là pháp lý + cấu trúc thị trường (không hết hạn). Dữ liệu sống chỉ dùng ở H2 so sánh định lượng và H2 bối cảnh hiện tại.
- Rule học được: sửa luôn 2 phát biểu sai/không kiểm chứng được — "bán chứng khoán lấy lại tiền chỉ sau vài thao tác" (thực tế tiền về theo T+2) và "lợi nhuận cao hơn đáng kể so với gửi tiết kiệm" (giờ có số: 9,0%/năm). Slop 77 → 97, FACT clean.
- ⚠️ Còn tồn đọng (có sẵn trước khi sửa, không thuộc phạm vi slop): CL1-meta 170 ký tự, thiếu "HVS" trong sapo, H2 cuối không phải `## Kết luận`, thiếu conversion link, từ cấm "Giải mã", WC-total -57% so với target 2500.

### 2026-10-15 - batch slop-audit 12 bài (layer B)
- Lỗi đã sửa: 12 bài có slop score < 80 theo `scripts/slop_check.py` (tầng B mới). Toàn bộ đều là bài khái niệm không có đối tượng cụ thể: 6 khái niệm TA/thị trường, 3 FA/BCTC, 2 price pattern, 1 nến.
- Pattern: nhịp câu phẳng (không có câu ≤7 từ trong 60–80 câu liên tiếp) + mật độ bằng chứng dưới 0.6 token/100 từ. Cách sửa: chèn câu 3–7 từ để phá nhịp, thay câu khẳng định trơn bằng mỏ neo kiểm chứng được (biên độ sàn HOSE 7%/HNX 10%/UPCoM 15%, T+2, phiên ATC 14h30–14h45, mốc VN-Index 1.500 điểm tháng 1/2022 và 900 điểm tháng 11/2022, ngưỡng RSI 70/30, khối lượng so bình quân 20 phiên, ngưỡng D/E và Cash Ratio).
- Rule học được: bài khái niệm trừu tượng (mô hình giá, mô hình nến, chỉ số BCTC) phải gắn tối thiểu 1 ví dụ có đối tượng thật (mã CP hoặc mốc thời gian hoặc ngưỡng số); không có đối tượng thì văn trôi thành lý thuyết đều đều và lint từ vựng không bắt được.
- Chi tiết từng bài (slop trước → sau):
  - `kenh-gia-la-gi`: 44 → 94 — nhịp phẳng (stdev 4.4), 0 câu ngắn, evidence 0.53/100w, mốc thời gian sai “tháng 9/2026”
  - `mo-hinh-cai-nem-la-gi`: 61 → 94 — rhythm_gap 81, anchor 79%, mọi đoạn cùng hình dạng
  - `nen-hanging-man`: 67 → 100 — stdev 5.1, uniform_run 10, evidence 0.5/100w
  - `vung-dinh-va-day-la-gi`: 68 → 94 — evidence 0.6/100w, anchor 76%
  - `chien-luoc-thi-truong-la-gi`: 70 → 94 — evidence 0.3/100w, anchor 82%; bổ sung Meta_Description + internal link thứ 3 (thiếu sẵn)
  - `su-kien-bong-bong-hoa-tulip`: 70 → 100 — stdev 4.6, uniform_run 10, evidence 0.6/100w
  - `ty-so-thanh-toan-bang-tien-mat`: 70 → 97 — evidence 0.15/100w, vague 2.3/1000w; sửa thêm lỗi có sẵn: thiếu Meta_Description, thiếu CTA link, 11 câu >35 từ
  - `vong-quay-hang-ton-kho-la-gi`: 70 → 97 — anchor 72%, vague 2.1/1000w; sửa thêm lỗi có sẵn: 2 link file:///, residue block outline, H2 cuối, thiếu Meta_Description/CTA, lỗi “to verify”
  - `bieu-do-ky-thuat`: 71 → 97 — rhythm_gap 76, evidence 0.5/100w
  - `mo-hinh-tam-giac-mo-rong-la-gi`: 71 → 97 — evidence 0.4/100w, anchor 82%
  - `phan-phoi-dinh-la-gi`: 71 → 97 — rhythm_gap 72, anchor 74%
  - `tin-dung-doanh-nghiep-la-gi`: 71 → 91 — evidence 0.3/100w, anchor 83%; sửa thêm lỗi có sẵn: link file:///, residue block, thiếu Meta_Description/CTA, xưng hô “bạn đọc”

### 2026-09-21 - bieu-do-ky-thuat [learned 2026-09-21]
- Lỗi đã sửa: Sapo cứng và thiếu tính kêu gọi hành động; Anchor text internal link bị chèn gượng ép theo exact keyword ("phân tích kỹ thuật là gì", "nến Nhật là gì").
- Pattern: Viết Sapo cuốn hút nhấn mạnh nỗi đau F0 và mời gọi đọc tiếp; lồng anchor link tự nhiên theo ngữ nghĩa (partial match).
- Rule học được: Anchor text internal link phải hòa nhập tự nhiên vào ngữ cảnh câu, không giữ nguyên cụm từ khóa hỏi đáp thô ráp.
| 2026-09-21 | buy-the-dip-la-gi | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-09-21 | cach-doc-bieu-do-nen | 98 | 0/0/3 | anti_=100 seo=100 reada=91 link=100 brand=100 |
| 2026-09-21 | chi-bao-supertrend-la-gi | 94 | 0/0/10 | anti_=100 seo=100 reada=70 link=100 brand=100 |
| 2026-09-21 | chi-bao-uo | 96 | 0/0/7 | anti_=100 seo=97 reada=82 link=100 brand=100 |
| 2026-09-22 | duong-zigzag | 99 | 0/0/2 | anti_=100 seo=100 reada=94 link=100 brand=100 |
| 2026-09-22 | golden-cross-la-gi | 100 | 0/0/0 | anti_=100 seo=100 reada=100 link=100 brand=100 |
| 2026-09-22 | ichimoku-la-gi | 100 | 0/0/0 | anti_=100 seo=100 reada=100 link=100 brand=100 |
| 2026-09-22 | kenh-gia-la-gi | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-09-22 | kenh-gia-song-song | 95 | 0/0/8 | anti_=100 seo=100 reada=76 link=100 brand=100 |
| 2026-09-22 | ly-thuyet-dow | 90 | 0/2/9 | anti_=100 seo=90 reada=63 link=100 brand=100 |
| 2026-09-22 | mo-hinh-2-day | 100 | 0/0/1 | anti_=100 seo=100 reada=100 link=100 brand=97 |
| 2026-09-22 | mo-hinh-2-dinh-la-gi | 98 | 0/0/3 | anti_=100 seo=97 reada=94 link=100 brand=100 |
| 2026-09-22 | mo-hinh-3-chang-linh-ngu-lam | 99 | 0/0/1 | anti_=100 seo=100 reada=97 link=100 brand=100 |
| 2026-09-22 | mo-hinh-3-day | 97 | 0/0/5 | anti_=100 seo=100 reada=85 link=100 brand=100 |
| 2026-09-22 | mo-hinh-cai-nem-la-gi | 98 | 0/0/4 | anti_=100 seo=100 reada=88 link=100 brand=100 |
| 2026-09-22 | mo-hinh-nen-bua-nguoc | 91 | 0/1/12 | anti_=100 seo=97 reada=60 link=100 brand=100 |
| 2026-09-22 | mo-hinh-nen-engulfing | 93 | 0/1/7 | anti_=100 seo=87 reada=85 link=100 brand=97 |
| 2026-09-22 | mo-hinh-la-co-la-gi | 91 | 0/2/7 | anti_=100 seo=77 reada=85 link=100 brand=97 |
| 2026-09-22 | mo-hinh-co-duoi-nheo | 89 | 0/3/6 | anti_=90 seo=80 reada=85 link=100 brand=97 |
| 2026-09-22 | mo-hinh-tam-giac | 90 | 0/2/8 | anti_=100 seo=77 reada=82 link=100 brand=97 |
| 2026-09-22 | mo-hinh-chu-nhat | 96 | 0/0/7 | anti_=100 seo=97 reada=82 link=100 brand=100 |
| 2026-09-24 | mo-hinh-tam-giac-mo-rong-la-gi | 99 | 0/0/2 | anti_=100 seo=97 reada=97 link=100 brand=100 |
| 2026-09-24 | mo-hinh-vai-dau-vai | 100 | 0/0/0 | anti_=100 seo=100 reada=100 link=100 brand=100 |
| 2026-09-24 | mo-hinh-wyckoff | 99 | 0/0/2 | anti_=100 seo=100 reada=94 link=100 brand=100 |
| 2026-09-24 | nen-evening-star-la-gi | 97 | 0/0/5 | anti_=100 seo=97 reada=88 link=100 brand=100 |
| 2026-09-24 | nen-hanging-man | 99 | 0/0/1 | anti_=100 seo=100 reada=97 link=100 brand=100 |
| 2026-09-24 | nen-harami-la-gi | 96 | 0/0/7 | anti_=100 seo=100 reada=79 link=100 brand=100 |
| 2026-09-24 | nen-heikin-ashi | 99 | 0/0/2 | anti_=100 seo=100 reada=94 link=100 brand=100 |
| 2026-09-24 | nen-inside-bar | 100 | 0/0/0 | anti_=100 seo=100 reada=100 link=100 brand=100 |
| 2026-09-24 | nen-marubozu-la-gi | 99 | 0/0/2 | anti_=100 seo=100 reada=94 link=100 brand=100 |
| 2026-09-24 | nen-pin-bar | 96 | 0/0/6 | anti_=100 seo=100 reada=82 link=100 brand=100 |
| 2026-09-24 | nen-shooting-star | 99 | 0/0/2 | anti_=100 seo=100 reada=94 link=100 brand=100 |
| 2026-09-24 | phan-biet-phan-tich-co-ban-va-phan-tich-ky-thuat | 98 | 0/0/3 | anti_=100 seo=97 reada=94 link=100 brand=100 |
| 2026-09-24 | phan-ky-an | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-09-24 | phan-ky-rsi | 98 | 0/0/3 | anti_=100 seo=97 reada=94 link=100 brand=100 |
| 2026-09-24 | phan-phoi-dinh-la-gi | 97 | 0/0/6 | anti_=100 seo=100 reada=85 link=100 brand=97 |
| 2026-09-24 | pivot-point-la-gi | 93 | 0/0/12 | anti_=100 seo=97 reada=70 link=100 brand=100 |
| 2026-09-24 | pullback-trading-la-gi | 95 | 0/0/8 | anti_=100 seo=97 reada=79 link=100 brand=100 |
| 2026-09-24 | quy-tac-cua-richard-rhodes | 97 | 0/0/4 | anti_=100 seo=97 reada=91 link=100 brand=100 |
| 2026-09-24 | spread-la-gi | 96 | 0/1/2 | anti_=100 seo=90 reada=94 link=100 brand=100 |
| 2026-09-25 | su-kien-bong-bong-hoa-tulip | 98 | 0/0/3 | anti_=100 seo=97 reada=94 link=100 brand=100 |
| 2026-09-25 | swing-trading | 98 | 0/0/3 | anti_=100 seo=97 reada=94 link=100 brand=100 |
| 2026-09-25 | trend-following-la-gi | 100 | 0/0/0 | anti_=100 seo=100 reada=100 link=100 brand=100 |
| 2026-09-25 | vung-dinh-va-day-la-gi | 98 | 0/0/3 | anti_=100 seo=100 reada=91 link=100 brand=100 |
| 2026-09-25 | vung-qua-mua-la-gi | 98 | 0/0/3 | anti_=100 seo=100 reada=91 link=100 brand=100 |
| 2026-09-25 | washout-la-gi | 97 | 0/0/4 | anti_=100 seo=97 reada=91 link=100 brand=100 |
| 2026-09-25 | zero-sum-game | 98 | 0/0/4 | anti_=100 seo=100 reada=88 link=100 brand=100 |
| 2026-09-25 | wyckoff-la-gi | 97 | 0/0/5 | anti_=100 seo=100 reada=85 link=100 brand=100 |
| 2026-10-05 | mo-hinh-coc-tay-cam | 96 | 0/0/6 | anti_=100 seo=97 reada=85 link=100 brand=100 |
| 2026-10-05 | mo-hinh-nen-dark-cloud-cover-la-gi | 98 | 0/0/3 | anti_=100 seo=97 reada=94 link=100 brand=100 |
| 2026-10-06 | khoang-trong-gia-la-gi | 99 | 0/0/2 | anti_=100 seo=97 reada=97 link=100 brand=100 |
| 2026-10-15 | co-phieu-la-gi-mua-co-phieu-lai-tu-dau | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-10-15 | phan-biet-cac-loai-co-phieu | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-10-15 | cac-thanh-vien-va-cach-hoat-dong-trong-thi-truong-chung-khoan | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-10-15 | huong-dan-mo-tai-khoan-chung-khoan-don-gian-tai-nha | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-10-15 | lua-chon-mo-tai-khoan-o-cong-ty-chung-khoan-nao | 99 | 0/0/2 | anti_=100 seo=97 reada=97 link=100 brand=100 |
| 2026-10-15 | huong-dan-doc-bang-gia-chung-khoan | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-10-15 | huong-dan-dat-lenh-mua-ban-co-phieu | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-10-15 | giai-thich-cac-chi-so-vnindex-hnxindex-upcomindex | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-10-15 | quy-dinh-cua-cac-san-giao-dich-hose-hxn-upcom | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
| 2026-10-15 | tat-tan-tat-ve-margin | 99 | 0/0/1 | anti_=100 seo=97 reada=100 link=100 brand=100 |
