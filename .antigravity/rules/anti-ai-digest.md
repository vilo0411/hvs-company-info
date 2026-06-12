---
name: Anti-AI Digest
description: Bản rút gọn machine-readable của anti-ai-rules.md. Cập nhật file này ngay khi anti-ai-rules.md có thay đổi. Full rationale → anti-ai-rules.md.
source: seo-strategy/resources/content-strategy/anti-ai-rules.md
updated: 2026-06-11
---

# Anti-AI Digest — Enforcement Patterns

> File này là nguồn duy nhất để skills/agents check Anti-AI.  
> KHÔNG nhúng nội dung anti-ai-rules.md vào skills (tốn token, không cập nhật).  
> Khi anti-ai-rules.md thay đổi → cập nhật digest này.

---

## TIER 1 — CẤM TUYỆT ĐỐI (grep & remove ngay, không exception)

```
FORBIDDEN_STRINGS:
  - "Trong thế giới không ngừng"
  - "Mở khóa tiềm năng"
  - "Hành trình"
  - "Giải pháp toàn diện"
  - "Đóng vai trò là"
  - "Tóm lại,"
  - "Kết luận là,"
  - "Hãy cùng tìm hiểu"
  - "Hiểu một cách đơn giản,"
  - "Chúng tôi thấu hiểu rằng"
  - "Đọc vị"
  - "Nâng tầm"
  - "Đột phá"        # tier 2 nhưng cực phổ biến — treat as tier 1
  - "Hệ sinh thái"
  - "Cốt lõi"
  - "Hơn cả một"
  - "Đáng chú ý là,"
  - "Tôi hy vọng thông tin này"
  - "Bạn đã bao giờ tự hỏi"  # rhetorical question opener
  - "HVS Có Thể Giúp Gì"      # generic product heading
  - "HVS Đồng Hành Cùng Bạn"  # generic product heading
  - "Nghệ thuật săn tìm"
  - "Chữ cái vàng"
  - "Giải mã"
  - "Định hình phương pháp"
  - "Trang bị phương pháp"
  - "Đánh dấu một bước ngoặt"
  - "Thay đổi cuộc chơi"
  - "Các chuyên gia tin rằng"
  - "Nhiều người cho rằng"
  - "Tương lai vẫn còn ở phía trước"
  - "Chỉ có thời gian mới trả lời"
  - "Để mà"
  - "Do thực tế là"
  - "Trong nỗ lực nhằm"


FORBIDDEN_PATTERNS:
  - ngoặc_kép_nhấn_mạnh: 'bất kỳ từ/cụm từ trong "..." mà không phải trích dẫn nguyên văn'
  - xưng_hô_sai: '"Quý nhà đầu tư" | "bạn đọc"'  → chỉ dùng "bạn"
  - bị_động_dồn_dập: '>2 câu chứa "được...là/xem/cho/thực hiện" trong 1 đoạn'
  - danh_từ_hóa: '"việc [động từ]" | "sự [tính từ]"'  → bỏ "việc"/"sự"
  - số_mơ_hồ: '"một khoản phí nhỏ" | "một doanh nghiệp lớn"' → dùng số thật
  - câu_đều_nhau: '>3 câu liên tiếp cùng độ dài 15-20 từ'
  - formula_latex: 'tránh dùng công thức dạng LaTeX ($$ hoặc $) gây lỗi định dạng khi chuyển sang Google Docs, thay bằng blockquote in đậm'
  - h4_subheadings: 'Sử dụng H4 (####) cho các tiêu đề con bổ trợ để tránh làm gián đoạn việc phân tách khối H2/H3 của công cụ đếm từ wordcount'
  - hvs_tai_chinh_so_sai_lech: 'mô tả HVS Tài chính số là công cụ theo dõi số liệu/bộ lọc tài chính tự động (thực tế: HVS Tài chính số là nền tảng đào tạo trực tuyến với các lộ trình thực chiến toàn diện)'
  - hvs_product_hierarchy_sai: 'giới thiệu HVS Thực tập số như sản phẩm riêng biệt ngang hàng HVS Tài chính số — thực tế HVS Thực tập số là chương trình/lộ trình đào tạo NẰM TRONG nền tảng HVS Tài chính số; HVS Demo và HVS Forum là công cụ hỗ trợ/bổ trợ, không phải sản phẩm đào tạo chính'
  - hvs_dao_tao_sai_lech: 'trình bày HVS Tài chính số / HVS Thực tập số dạy các thủ tục hành chính, biểu mẫu, cách tính thuế phí cụ thể hoặc quản trị danh mục nâng cao cho người mới bắt đầu (thực tế: tập trung đào tạo kiến thức đầu tư cốt lõi FA LV1 và TA LV1 giúp tự phân tích)'
```

---

## TIER 2 — HẠN CHẾ (tối đa 1 lần/bài)

```
RESTRICTED_STRINGS:
  - "Tận dụng"      → "Dùng" / "Sử dụng"
  - "Mạnh mẽ"       → "Hiệu quả" / "Ổn định"
  - "Liền mạch"     → "Dễ dàng" / "Mượt mà"
  - "Nhịp đập thị trường"  → "Biến động" / "Diễn biến"
```

---

## MUST-HAVE (thiếu = FAIL)

```
REQUIRED:
  - direct_answer: 'câu đầu tiên dưới H2 phải trả lời trực tiếp heading, không dẫn dắt'
  - entity_first: 'thực thể quan trọng đứng trong 5-7 từ đầu câu'
  - specific_evidence: 'mã cổ phiếu (VCB/HPG...) | % cụ thể | sàn (HOSE/HNX)'
  - rhythm_break: 'có ít nhất 1 câu cực ngắn (≤7 từ) mỗi 3-4 câu dài'
  - product_bridge: 'nêu nỗi đau/vấn đề TRƯỚC khi giới thiệu sản phẩm HVS'
  - source_legal: 'nguồn pháp lý chỉ dùng vanban.chinhphu.vn hoặc vbpl.vn'
```

---

## CÁCH DÙNG TRONG SKILLS/QA

Agent đọc digest này và **scan toàn bộ draft** theo từng pattern:
1. Loop qua `FORBIDDEN_STRINGS` → flag bất kỳ match nào
2. Loop qua `FORBIDDEN_PATTERNS` → flag theo rule logic
3. Verify tất cả `REQUIRED` items
4. Fail nếu có bất kỳ TIER 1 match hoặc REQUIRED không đạt
