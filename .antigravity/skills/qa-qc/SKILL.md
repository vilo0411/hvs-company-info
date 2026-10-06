---
name: qa-qc
description: Quy trình QA 2 tầng — lint tất định (qa_lint.py) rồi Quality Guardian kiểm tra ngữ nghĩa. Máy đếm được thì máy làm.
---

# Skill: QA/QC — Lint → Quality Guardian

> **Việc gì máy bắt được → `python scripts/qa_lint.py` làm.** Người/LLM chỉ làm việc cần suy luận.
> Danh sách rule ↔ lint ID: `.antigravity/rules/seo-formatting.md §1`.

## Bước 0 — Lint (BLOCKING)

```
python scripts/qa_lint.py content/blog/2-user-review/Draft-<slug>.md --fix
# optimize: thêm --original content/blog/3-finalized/Final-<slug>.md
```

| Exit | Ý nghĩa | Làm gì |
|---|---|---|
| 0 | PASS (0 CRITICAL, 0 MAJOR) | sang Bước 1 |
| 1 | FAIL | sửa **đúng dòng** trong bảng CRITICAL/MAJOR → chạy lại. Tối đa 2 vòng. Không audit ngữ nghĩa khi lint FAIL. |
| 2 | lỗi IO/usage | báo user |

Lint đã bao phủ (KHÔNG kiểm tra lại bằng mắt): YAML, H1/meta/sapo/kết luận, từ cấm Tier 1/2, hedge, từ nghiệp dư, xưng hô, ngoặc kép, em-dash, LaTeX, code block, `---`, độ dài câu/đoạn, mật độ bảng, link (file:///, .md, sitemap, CTA, số lượng), % phí / lịch sử xử phạt cạnh "HVS", word count từng H2 (`wordcount.py`), PAA coverage, bảo toàn ảnh (`--original`).

## Bước 1 — Quality Guardian (ngữ nghĩa)

Gọi `.antigravity/agents/quality-guardian.md` với Draft + Outline. Chỉ các checklist sau:

| CL | Nội dung | Mức khi vi phạm |
|---|---|---|
| **CL1 SEO-semantic** | Answer First dưới mỗi H2; thực thể trong 5–7 từ đầu; entities từ `Entities_Gap_Analysis`; Content Gap rõ so với đối thủ | MAJOR |
| **CL2 Anti-AI cấu trúc** | FORBIDDEN_PATTERNS cần suy luận: bị động dồn dập, danh từ hóa, số mơ hồ, câu đều nhau, synonym cycling, inline header, generic source, bảng thừa; mở bài không dẫn dắt sáo | CRITICAL |
| **CL3 Glossary & Brand** | Tên sản phẩm đúng; phân tầng Thực tập số chính / Demo-Forum hỗ trợ; không mô tả Tài chính số là tool; không dạy thủ tục hành chính; ràng buộc `confirm-with-leadership.md` (ngoài 2 regex đã lint) | CRITICAL |
| **CL4 Persona** | Đúng nỗi đau/tone của persona đã chọn; xưng "bạn"/"HVS"; CTA hợp persona | MAJOR |
| **CL5 Facts** | Số liệu có nguồn + mốc thời gian; đúng thực tế sàn VN (T+2, biên độ HOSE ±7%, lô 100); nguồn pháp lý vanban.chinhphu.vn / vbpl.vn | CRITICAL |
| **CL6 So-What / Prove-It** | Mỗi claim có bằng chứng (mã CP, %, sàn); kịch bản "Nếu A → … Nếu B → …"; cảnh báo rủi ro kèm mọi khuyến nghị; value trap khi nêu P/E, P/B | MAJOR |
| **CL7 Holistic SEO** | 14 rule Koray (`holistic-seo-rules.md`): If-logic, plural examples, niche verbs, bold đúng chỗ, anchor khớp title bài đích | MAJOR |
| **CL8 Ảnh** | Alt/caption mô tả thực thể; vị trí hợp section; không text trong ảnh | MINOR |
| **CL9 HVS Bridge & CTA** | Nỗi đau TRƯỚC sản phẩm; 250–300 từ; benefit không feature-list; Kết luận đa dạng (không rập khuôn) | MAJOR |

**PASS** = 0 CRITICAL, 0 MAJOR. MINOR → ghi chú, không chặn.

## Bước 2 — Fix targeted

- Sửa đúng section/dòng được nêu. Không viết lại section đã PASS. Thiếu từ → thêm ví dụ/kịch bản/bảng MỚI (không chuyển list thành văn xuôi).
- Sau khi sửa: chạy lại lint (Bước 0) → QG re-audit chỉ các item đã FAIL.
- Vẫn FAIL sau 2 vòng → trình bày kèm `⚠️ Remaining issues`. >2 vòng = vấn đề ở Outline, không phải QA.

## Report template

```
**Lint:** PASS · Score 87/100 (anti_ai 90, seo 85, readability 80, link 100, brand 100)
**Quality Guardian:** PASSED | FAILED
- [CL5 CRITICAL] Dòng 42: "biên độ HOSE ±10%" sai — HOSE ±7%. Sửa: …
- [CL9 MAJOR] HVS Bridge 140 từ (<250) — thêm kịch bản F0 mua đuổi + cách Thực tập số giải quyết.
```

## Gotchas

- `wordcount.py` tách khối theo `^##`/`^###` — tiêu đề con bổ trợ dùng `####`.
- `## Revision Log` cuối Draft không tính vào word count và không bị lint; giữ lại để `/learn`.
- Bài vừa publish nhưng sitemap chưa cập nhật → `LINK-sitemap` CRITICAL: chạy `python scripts/fetch_sitemap.py --refresh` trước, hoặc `--no-sitemap` khi user xác nhận URL.
