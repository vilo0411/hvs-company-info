# Slop Audit — toàn bộ corpus Final (2026-10-15)

Công cụ: `python scripts/slop_check.py --baseline --csv seo-strategy/content-plan/slop-baseline.csv`
Phạm vi: **435 bài** trong `content/blog/3-finalized/` (toàn bộ, không lấy mẫu).
Số liệu chi tiết từng bài: `slop-baseline.csv` (sắp theo slop_score tăng dần).

Tầng kiểm tra: A = `qa_lint.py` (từ vựng + format) · **B = `slop_check.py` (hành vi văn bản)** · C = Quality Guardian CL1–CL10.

---

## 1. Phát hiện cốt lõi: tầng A không thấy được slop

| | |
|---|---|
| Bài PASS `qa_lint` (--no-sitemap) | 43 |
| Trong đó **FAIL slop_check** | **11 (26%)** |
| Bài có `qa_lint` ≥ 95 nhưng slop FAIL | 10 |
| Ví dụ cực đoan | `nen-inside-bar`: qa_lint **100/100**, slop **74** |
| | `nen-hanging-man`: qa_lint **99**, slop **67** |
| | `mo-hinh-cai-nem-la-gi`: qa_lint **98**, slop **61** |

→ Sạch 100% từ cấm vẫn có thể là slop. Đây là lý do tầng B tồn tại.

## 2. Phân bố metric trên 435 bài

| metric | hướng xấu | p10 | p25 | p50 | p75 | p90 | min | max |
|---|---|---|---|---|---|---|---|---|
| burstiness (stdev độ dài câu) | thấp | 6.5 | 7.8 | 9.4 | 10.8 | 12.3 | 4.4 | 16.5 |
| mean_sent (từ/câu) | – | 20.4 | 22.2 | 24.8 | 28.9 | 32.2 | 14.9 | 38.8 |
| uniform_run (câu liên tiếp 14–24 từ) | cao | 2 | 2 | 4 | 5 | 7 | 0 | 17 |
| **rhythm_gap** (câu liên tiếp không có câu ≤7 từ) | cao | 13 | 22 | **35** | 47 | 67 | 6 | 86 |
| **short_share** (tỷ lệ câu ≤7 từ) | thấp | 0.00 | 0.00 | **0.00** | 0.04 | 0.09 | 0.00 | 0.28 |
| **evidence_per_100w** | thấp | 0.54 | 0.94 | **1.58** | 2.42 | 3.40 | 0.00 | 6.55 |
| unanchored_ratio | cao | 0.23 | 0.35 | 0.47 | 0.61 | 0.71 | 0.04 | 0.94 |
| vague_per_1000w | cao | 0.00 | 0.00 | 0.00 | 0.62 | 1.02 | 0.00 | 3.06 |
| h2_def_open (H2 mở bằng "X là…") | cao | 0.00 | 0.00 | 0.20 | 0.29 | 0.40 | 0.00 | 1.00 |
| para_shape_sd | thấp | 0.63 | 0.74 | 0.89 | 1.10 | 1.32 | 0.38 | 2.86 |
| template_sim (khung H2 vs bài gần nhất) | cao | 0.25 | 0.29 | 0.34 | 0.42 | 0.63 | 0.17 | 0.90 |
| words | – | 946 | 1194 | 1480 | 1898 | 2300 | 225 | 3578 |

**Hai vấn đề hệ thống (median chứ không phải ngoại lệ):**

1. **Nhịp phẳng toàn corpus.** `short_share` median = **0.00** — bài trung bình **không có một câu nào ≤7 từ**. Median `rhythm_gap` = 35 câu liên tiếp. Rule `rhythm_break` trong `anti-ai-rules.md §0 REQUIRED` đã khai báo nhưng **chưa từng được enforce**, nên 100% corpus vi phạm.
2. **Mật độ bằng chứng thấp.** Median 1.58 token/100 từ → bài 1500 từ chỉ có ~24 mỏ neo (số, mã CP, sàn, mốc thời gian). 25% bài dưới 0.94.

## 3. Tỷ lệ flag theo rule (ngưỡng relative, MAJOR≈p90 / MINOR≈p75)

| rule | MAJOR | MINOR | % bài bị flag |
|---|---|---|---|
| SLOP-anchor | 37 | 86 | 28% |
| SLOP-evidence | 56 | 59 | 26% |
| SLOP-rhythm | 48 | 67 | 26% |
| SLOP-vague | 16 | 85 | 23% |
| SLOP-burstiness | 9 | 46 | 13% |
| SLOP-para-shape | 11 | 40 | 12% |
| SLOP-uniform-run | 15 | 20 | 8% |
| SLOP-inline-header | 9 | 21 | 7% |
| SLOP-h2-open | 4 | 23 | 6% |
| SLOP-table-thin | 0 | 20 | 5% |
| SLOP-template | 12 | 6 | 4% |
| SLOP-hedge-para | 1 | 8 | 2% |
| SLOP-synonym | 0 | 7 | 2% |

Slop score: p10 = 80 · p50 = 94 · p90 = 100 · **FAIL (score < 80): 34/435 = 8%**

## 4. Slop tập trung theo nhóm chủ đề

| nhóm | n | slop p50 | evidence p50 | burstiness p50 | FAIL% |
|---|---|---|---|---|---|
| `mo-hinh-*` (price pattern) | 19 | 81 | 0.60 | 6.8 | **26%** |
| phân tích cơ bản / BCTC | 26 | 87 | 1.40 | 9.5 | 19% |
| `nen-*` (mô hình nến) | 14 | 88 | 0.79 | 7.1 | 14% |
| `cach-mua-co-phieu-*` | 34 | 90 | 2.79 | 8.8 | 9% |
| khác | 265 | 94 | 1.45 | 9.4 | 8% |
| `co-phieu-*` (ngành) | 43 | 94 | 1.78 | 11.0 | 5% |
| chỉ báo kỹ thuật | 33 | 97 | 2.58 | 10.1 | **0%** |

**Kết luận chẩn đoán:** slop tập trung ở bài **khái niệm TA trừu tượng** (mô hình giá, mô hình nến) — nơi không có mã cổ phiếu, không có số, không có phiên giao dịch thật để bám vào, nên văn trôi thành mô tả lý thuyết đều đều. Bài có đối tượng cụ thể (ticker, ngành, chỉ báo có tham số) tự động sạch hơn.

→ Hành động đúng không phải "viết hay hơn" mà là **ép mỗi bài khái niệm phải có 1 ví dụ thực**: 1 mã + 1 mốc thời gian + biến động % cụ thể.

## 5. 12 bài cần ưu tiên sửa

| slop | slug | MAJOR |
|---|---|---|
| 44 | `kenh-gia-la-gi` | burstiness, uniform-run, rhythm, evidence, anchor |
| 61 | `mo-hinh-cai-nem-la-gi` | rhythm, anchor, para-shape |
| 67 | `nen-hanging-man` | burstiness, uniform-run, evidence |
| 68 | `vung-dinh-va-day-la-gi` | evidence, anchor |
| 70 | `chien-luoc-thi-truong-la-gi` | evidence, anchor, para-shape |
| 70 | `su-kien-bong-bong-hoa-tulip` | burstiness, uniform-run, evidence |
| 70 | `ty-so-thanh-toan-bang-tien-mat` | evidence, anchor, vague |
| 70 | `vong-quay-hang-ton-kho-la-gi` | evidence, anchor, vague |
| 71 | `bieu-do-ky-thuat` | rhythm, evidence |
| 71 | `mo-hinh-tam-giac-mo-rong-la-gi` | evidence, anchor |
| 71 | `phan-phoi-dinh-la-gi` | rhythm, anchor |
| 71 | `tin-dung-doanh-nghiep-la-gi` | evidence, anchor |

Danh sách đầy đủ 34 bài FAIL: `slop-baseline.csv`, cột `slop_score < 80`.

## 6. Giới hạn đã biết của tầng B

- Ngưỡng là **relative** (so với corpus hiện tại), không phải chuẩn tuyệt đối. Mục tiêu tuyệt đối ghi trong comment đầu `slop_check.py`: `rhythm_gap ≤ 12`, `evidence_per_100w ≥ 2.5`, `burstiness ≥ 8` — siết dần từng bước.
- `SLOP-anchor` là proxy: câu khái niệm có thể thiếu mỏ neo một cách hợp lý. Chỉ fire ở mật độ đuôi phân bố.
- `SLOP-vague` precision ~80%; hit trong câu đã có ≥2 mỏ neo được tha (trừ nhóm filler thuần).
- `SLOP-template` bỏ qua bài cùng series (`cach-mua-co-phieu-<ticker>` trùng khung 90% là chủ ý, không phải lỗi).
- Metric **không** đánh giá được: tính đúng của số liệu, POV, content gap thật so với SERP → vẫn thuộc tầng C.

---

## 7. Kết quả sau vòng sửa (2026-10-15)

12 bài ưu tiên đã sửa xong. Slop score trước → sau: 44→94 · 61→94 · 67→100 · 68→94 · 70→94 · 70→100 · 70→97 · 70→97 · 71→97 · 71→97 · 71→97 · 71→91. Chi tiết từng bài: `revision-log.md`, entry `2026-10-15 - batch slop-audit 12 bài`.

Corpus sau sửa (440 bài, gồm bài mới finalize trong ngày):

| | trước | sau |
|---|---|---|
| FAIL (slop < 80) | 34/435 = 8% | **19/440 = 4%** |
| Slop score p10 | 80 | **84** |
| SLOP-rhythm MAJOR | 48 | 44 |
| SLOP-evidence MAJOR | 56 | 39 |
| SLOP-anchor MAJOR | 37 | 25 |

Lỗi có sẵn (không thuộc slop) được sửa kèm trong lúc revise:
- `vong-quay-hang-ton-kho-la-gi`, `tin-dung-doanh-nghiep-la-gi`: xóa block residue `## 3. Chiến lược liên kết` còn sót từ outline (chứa link `file:///` — 2 CRITICAL `LINK-file`), chuẩn hóa H2 `## Kết luận` và `## Revision Log`.
- 4 bài thiếu `Meta_Description` trong YAML, 3 bài thiếu conversion link `thuc-tap-so` → đã bổ sung.
- `vong-quay-hang-ton-kho-la-gi`: còn chuỗi tiếng Anh `to verify` giữa câu tiếng Việt.
- `kenh-gia-la-gi`: mốc thời gian vô nghĩa "vào tháng 9/2026" trong định nghĩa.

## 8. Thay đổi detector trong quá trình sửa

- Bỏ metric `truism` (đoán ngữ nghĩa, false positive nặng với bài TA khái niệm) → thay bằng `SLOP-anchor` (đo được) + `SLOP-vague` (15 pattern precision cao, implement rule `số_mơ_hồ` / `generic_source`).
- `evidence_hits` bổ sung `RE_RATIO`: số thập phân không đơn vị và tên chỉ số (P/E, D/E, RSI, Cash Ratio…) nay tính là mỏ neo. Trước đó bài chỉ số tài chính bị đo sai (ví dụ `ty-so-thanh-toan-bang-tien-mat` báo 0.0/100 từ dù có ngưỡng 0.2–0.5).
- `SLOP-template` bỏ qua bài cùng series (`cach-mua-co-phieu-<ticker>`).
- `SLOP-uniform-run` / `SLOP-rhythm` nay in kèm số dòng bắt đầu chuỗi vi phạm.

## 9. Tích hợp pipeline (đã xong)

| Điểm nối | Thay đổi |
|---|---|
| `scripts/finalize.py` | Gate 1b: `slop_check --json`, từ chối khi score < 80 (trừ `--force`) |
| `.antigravity/workflows/write.md` · `rules/write-track.md` | Phase 3 bước 2b BLOCKING + bảng cách sửa theo từng rule `SLOP-*` |
| `.antigravity/workflows/revise.md` | Bước 4: chạy kèm `qa_lint`, slop score không được thấp hơn trước khi sửa |
| `.antigravity/workflows/optimize.md` | Baseline slop trước khi tối ưu |
| `.antigravity/workflows/approve.md` | Gate slop ở cả nhánh Draft và Optimize |
| `.antigravity/rules/workflow-integrity.md` | Bảng "dùng script thay vì đọc file" + Content Edit Rule bước 3 |
| `CLAUDE.md` | Bảng tra cứu + bảng Helper Scripts + Content Edit Rule |

## 10. Tầng dữ liệu (thêm 2026-10-15)

Tầng B chỉ biết một câu **có hay không có** mỏ neo, không biết mỏ neo đó **đúng hay cũ**. Hai script mới đóng khoảng trống đó:

| Script | Vai trò | Nguồn |
|---|---|---|
| `market_facts.py` | `--brief` lấy số liệu để viết · `--verify` kiểm chứng số trong bài | VNDirect dchart (OHLCV), SSI iboard (danh sách mã niêm yết) |
| `news_feed.py` | `--topic` tin tức có ngày quanh keyword | RSS CafeF ×2, VnExpress, Vietstock, Tuổi Trẻ, Dân Trí |

Rule ID mới (`FACT-*`): `FACT-index-wrong` (CRITICAL — mốc chỉ số sai so với dữ liệu thật), `FACT-ticker` (MAJOR — mã không có trên HOSE/HNX/UPCoM), `FACT-stale` (MAJOR — mọi mốc số liệu cũ hơn 18 tháng).

**Nguyên tắc thiết kế:** `qa_lint` và `slop_check` giữ nguyên trạng offline/tất định. Chỉ `market_facts.py` và `news_feed.py` có network, và cả hai fail mềm (exit 3) — nguồn dữ liệu chết thì bỏ qua bước đó chứ không chặn pipeline. Trong `finalize.py`, fact check là **advisory** (in cảnh báo, không chặn) vì endpoint là không chính thức; chỉ `qa_lint` CRITICAL và slop < 80 mới chặn.

Rule viết bài mới trong `anti-ai-rules.md §0 REQUIRED`: `data_anchor`, `data_freshness`, `data_structural_fallback`.

**Kết quả áp dụng ngay:** tool bắt được 3/12 bài vừa revise có `FACT-stale` — tôi đã chèn mốc 2022 (đúng: đỉnh 1.529 ngày 06/01/2022, đáy 912 ngày 15/11/2022) nhưng không có mốc hiện tại, trong khi VN-Index đã lập đỉnh 1.928 điểm ngày 18/05/2026 và đóng cửa 1.698 điểm ngày 15/10/2026. Đã sửa cả 3 bài: ghi rõ "đỉnh chu kỳ 2022" + bổ sung mốc 2026. Toàn bộ 12 bài hiện `FACT: clean`.
