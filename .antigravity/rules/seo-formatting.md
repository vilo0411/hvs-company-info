# SEO Formatting & Writing Standard — HVS

> Nguồn duy nhất cho quy tắc **hình thức** bài viết. Anti-AI từ vựng → `seo-strategy/resources/content-strategy/anti-ai-rules.md` §0.
> Mọi rule có **Lint ID** đã được `python scripts/qa_lint.py` bắt tự động — agent KHÔNG kiểm tra lại bằng mắt, chỉ sửa khi lint báo.

## 1. Bảng rule ↔ lint

| Rule | Lint ID | Mức |
|---|---|---|
| Đúng 1 H1, chứa target keyword, ≤65 ký tự, không hậu tố "| HVS" | `CL1-h1`, `CL1-h1-suffix` | CRITICAL / MINOR |
| Không nhảy cấp heading (H2 → H4) | `CL1-hierarchy` | MAJOR |
| Không icon/emoji, không **bold** trong heading | `FMT-heading-icon`, `FMT-heading-bold` | MINOR |
| YAML đủ field: Author, Status, Pipeline_Mode, Persona, Target_Keyword, Search_Intent, Word_Count_Target, Meta_Description | `FM-required` | MAJOR |
| `Pipeline_Mode` (không dùng `Mode:` cũ); `HVS_Products` là list chuỗi phẳng | `FM-mode-legacy`, `FM-products-shape` | MAJOR |
| Meta description 140–160 ký tự, chứa keyword | `CL1-meta` | MAJOR |
| Sapo trước H2 đầu: chứa keyword + "HVS", 80–100 từ (2 đoạn) | `CL1-sapo`, `BRAND-sapo`, `CL1-sapo-length` | MAJOR / MINOR |
| H2 cuối là `## Kết luận` (có thể `## Kết luận: …`), chứa "HVS", 150–200 từ | `BRAND-conclusion`, `BRAND-conclusion-length` | MAJOR / MINOR |
| Từ cấm Tier 1 (`FORBIDDEN_STRINGS`) | `CL2-hard` | CRITICAL |
| Từ hạn chế Tier 2 (`RESTRICTED_STRINGS`) tối đa 1 lần/bài | `CL2-soft` | MAJOR |
| Hedge words (nên/cần/có lẽ…) tối đa 3 lần trong prose | `CL2-hedge` | MAJOR |
| Từ nghiệp dư (glossary Amateur), xưng hô sai ("quý nhà đầu tư", "bạn đọc") | `CL3-amateur`, `CL3-address` | MAJOR |
| Ngoặc kép nhấn mạnh quanh từ thường | `FMT-quotes` | MAJOR |
| Dấu — làm từ nối câu (chỉ được dùng trong ô bảng = "không có") | `FMT-emdash` | MAJOR |
| LaTeX `$…$` / `$$…$$` / `\frac` | `FMT-latex` | CRITICAL |
| Code block ``` ; callout `> [!NOTE]` | `FMT-codeblock`, `FMT-callout` | MAJOR |
| Đường kẻ `---` giữa các phần | `FMT-hr` | MINOR |
| Đoạn ≤4 câu và ≤80 từ; câu ≤35 từ | `FMT-para`, `CL6-sentence` | MINOR (MAJOR khi >3 đoạn / >5 câu) |
| Không quá 2 đoạn prose liên tiếp không có list/bảng/ảnh/blockquote | `FMT-prose-run` | MINOR |
| ≥1 bảng Markdown / 1000 từ | `FMT-table-density` | MINOR |
| Link nội bộ: URL tuyệt đối `https://taichinhso.hvsvn.com/…` có trong sitemap-cache | `LINK-sitemap`, `LINK-relative`, `LINK-host` | CRITICAL / MAJOR |
| Cấm `file:///`, cấm link `Final-*.md` / `.md` — kể cả ảnh | `LINK-file`, `LINK-final` | CRITICAL |
| ≥3 internal link + ≥1 conversion link `/thuc-tap-so…` | `LINK-count`, `LINK-cta` | MAJOR |
| Anchor không chung chung ("xem thêm", "tại đây") | `LINK-anchor-generic` | MINOR |
| Câu nhắc HVS không kèm % phí; không kèm đình chỉ/xử phạt | `BRAND-fee`, `BRAND-regulatory` | CRITICAL |
| Mốc thời gian mơ hồ ("hiện nay,", "gần đây,") | `GEO-vague-time` | MINOR |
| Word count từng H2 ±10% so với `Word_Count` trong Outline; tổng ±10% `Word_Count_Target` | `WC-section`, `WC-total` | MAJOR |
| Mọi câu `PAA_Questions` trong Outline phải thành H2/H3 hoặc FAQ | `PAA-missing` | MAJOR |
| Mật độ mỏ neo kiểm chứng được / nhịp câu (tầng B, offline) | `SLOP-evidence`, `SLOP-anchor`, `SLOP-rhythm`, … | MAJOR / MINOR |
| Mốc chỉ số đúng thực tế; mã CP có niêm yết; không để mọi số liệu cũ hơn 18 tháng (tầng dữ liệu, cần mạng) | `FACT-index-wrong`, `FACT-ticker`, `FACT-stale` | CRITICAL / MAJOR |

## 2. Rule cần suy luận (Quality Guardian kiểm tra, lint không bắt được)

- **Answer First**: câu đầu dưới mỗi H2 trả lời trực tiếp heading; thực thể quan trọng trong 5–7 từ đầu.
- **Specificity**: mã cổ phiếu thật (VCB, HPG), % thật, sàn cụ thể (HOSE/HNX/UPCoM); không "một doanh nghiệp lớn".
- **Scenario logic**: "Nếu [A] → [Kịch bản 1]. Nếu [B] → [Kịch bản 2]"; mọi khuyến nghị kèm cảnh báo rủi ro (`financial-logic.md`).
- **HVS Bridge**: nêu nỗi đau TRƯỚC sản phẩm; 250–300 từ; **HVS Thực tập số** là phễu chính, Demo/Forum là công cụ hỗ trợ (`glossary.md §Sản phẩm HVS`).
- **Kết luận đa dạng**: không rập khuôn "Checklist 4 bước"; luân phiên *3 Nguyên tắc vàng*, *Đối chiếu bẫy F0 vs chuyên nghiệp*, *Lộ trình thực chiến*.
- **Chống padding**: thiếu từ → thêm ví dụ/kịch bản/bảng MỚI, không chuyển list thành văn xuôi.
- **Bold**: chỉ bôi đậm câu trả lời trực tiếp hoặc thông số quan trọng, không bôi keyword máy móc.
- **List**: đồng nhất từ loại; quy trình từng bước bắt buộc dạng list có đánh số.
- **H4** (`####`) cho tiêu đề con bổ trợ để không phá khối H2/H3 của `wordcount.py`.
- **Công thức**: Unicode thuần (`×`, `÷`, `=`) hoặc inline `code`; giải thích biến ngay dưới.
- **Ảnh**: path repo-relative `content/blog/assets/images/<slug>/<name>.webp`, alt mô tả, không text trong ảnh.

## 3. Độ dài theo loại bài (Word_Count_Target)

| Loại bài | Từ | Ghi chú |
|---|---|---|
| Chuỗi giá trị ngành (Deep Industry Value Chain) | 1.800–2.500 | tối thiểu 2.000 |
| Hướng dẫn tỷ số tài chính (Financial Ratio Guides) | 1.200–1.500 | mục tiêu 1.400 |
| Khái niệm chiến lược / chu kỳ thị trường | 1.200 | |
| Định nghĩa thuật ngữ cơ bản ("X là gì") | 1.100–1.200 | |
| Cách mua cổ phiếu [MÃ] | 1.200–1.500 | |

Phân bổ: MAIN sections 55–65% · HVS Bridge ≥250–300 từ · Kết luận 150–200 từ · Sapo 80–100 từ. Σ `Word_Count` các H2 trong Outline ≥ `Word_Count_Target`.

## 4. YAML schema chuẩn (Draft/Final)

```yaml
---
Author: Claude Code            # hoặc Antigravity
Status: Draft | Finalized
Pipeline_Mode: Express | Guided | Auto | Optimized
SERP_Research: true | false
Persona: Lan Newbie / Nhà đầu tư F0
Target_Keyword: sàn otc là gì
Search_Intent: Informational
Word_Count_Target: 1500
Meta_Description: ... (140–160 ký tự, chứa keyword)
HVS_Products: ["HVS Thực tập số", "HVS Tài chính số", "HVS Demo"]
Section_Targets: {"Sàn OTC là gì": 250, "Kết luận": 180}   # finalize.py tự sinh từ Outline
---
```

## 5. Khối thông tin thương hiệu cuối bài (Brand Footer Boilerplate)

Mọi bài viết xuất bản đều đính kèm khối thông tin giới thiệu và liên hệ chính thức của HVS Tài chính số ở cuối bài (sau Tuyên bố miễn trừ trách nhiệm, trước `## Revision Log`) dưới định dạng blockquote:

```markdown
> **Về HVS Tài chính số:**
> HVS Tài chính số là nền tảng toàn diện đồng hành cùng nhà đầu tư trong suốt hành trình chinh phục thị trường chứng khoán - từ trang bị kiến thức, cập nhật thông tin thị trường đến hỗ trợ ra quyết định và quản lý danh mục. Tích hợp trọn bộ công cụ trên một hệ sinh thái duy nhất, HVS giúp tối ưu thời gian, mang lại trải nghiệm đầu tư liền mạch và hiệu quả cho cả người mới bắt đầu lẫn nhà đầu tư giàu kinh nghiệm.
> 
> **Thông tin liên hệ:**
> * Website: https://taichinhso.hvsvn.com/
> * Hội sở: Tầng 4, TTTM Dịch vụ Cống Vị, Số 2 Liễu Giai, Phường Ngọc Hà, TP. Hà Nội
> * Điện thoại: (+84-24) 3886 9999
> * Email: info@hvsvn.com
```

