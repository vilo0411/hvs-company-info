# HVS Anti-AI Writing Rules & Vocabulary

> **Cấu trúc file:** Phần 0 = Quick Scan (skills/QA đọc phần này). Phần 1-4 = Full Rationale (tham khảo khi cần hiểu sâu).  
> Khi thêm rule mới: thêm vào **cả phần 0 (Quick Scan) VÀ phần tương ứng trong 1-4**.  
> `content-feedback-loop` tự động update phần 0 khi học rule mới từ Revision Log.

---

## 0. QUICK SCAN — Enforcement Patterns (Skills/QA chỉ đọc section này)

> Section ngắn, machine-readable. Full rationale → xem Phần 1-4 bên dưới.

### TIER 1 — Cấm tuyệt đối (flag & remove ngay, không exception)

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
  - "Hơn cả một"
  - "Đáng chú ý là,"
  - "Tôi hy vọng thông tin này"
  - "Bạn đã bao giờ tự hỏi"
  - "HVS Có Thể Giúp Gì"
  - "HVS Đồng Hành Cùng Bạn"
  - "Đánh dấu một bước ngoặt"
  - "Thay đổi cuộc chơi"
  - "Các chuyên gia tin rằng"
  - "Nhiều người cho rằng"
  - "Tương lai vẫn còn ở phía trước"
  - "Chỉ có thời gian mới trả lời"
  - "Để mà"
  - "Do thực tế là"
  - "Trong nỗ lực nhằm"
  - "Nghệ thuật săn tìm"
  - "Chữ cái vàng"
  - "Giải mã"

FORBIDDEN_PATTERNS:
  - ngoặc_kép_nhấn_mạnh: 'bất kỳ từ/cụm từ trong "..." mà không phải trích dẫn nguyên văn hoặc tên tài liệu pháp lý'
  - xưng_hô_sai: '"Quý nhà đầu tư" | "bạn đọc"'  → chỉ dùng "bạn"
  - bị_động_dồn_dập: '>2 câu chứa "được...là/xem/cho/thực hiện" trong 1 đoạn'
  - danh_từ_hóa: '"việc [động từ]" | "sự [tính từ]"'  → bỏ "việc"/"sự"
  - số_mơ_hồ: '"một khoản phí nhỏ" | "một doanh nghiệp lớn"' → dùng số thật
  - câu_đều_nhau: '>3 câu liên tiếp cùng độ dài 15-20 từ'
  - synonym_cycling: 'dùng >2 từ đồng nghĩa cho cùng một đối tượng' → chọn 1 từ chuẩn
  - inline_header: '"**[Từ]:** [Từ đó] giúp..."' → viết thành đoạn văn
  - generic_source: '"Các chuyên gia" | "Nhiều người"' → dùng tên tổ chức cụ thể
  - formula_latex: 'tránh dùng công thức dạng LaTeX ($$ hoặc $) gây lỗi định dạng khi chuyển sang Google Docs, thay bằng blockquote in đậm'
  - hvs_tai_chinh_so_sai_lech: 'mô tả HVS Tài chính số là công cụ theo dõi số liệu/bộ lọc tài chính tự động (thực tế: HVS Tài chính số là nền tảng đào tạo trực tuyến với các lộ trình thực chiến toàn diện)'
  - hvs_product_hierarchy_sai: 'giới thiệu HVS Thực tập số như sản phẩm riêng biệt ngang hàng HVS Tài chính số — thực tế HVS Thực tập số là chương trình/lộ trình đào tạo NẰM TRONG nền tảng HVS Tài chính số; HVS Demo và HVS Forum là công cụ hỗ trợ/bổ trợ, không phải sản phẩm đào tạo chính'
  - hvs_dao_tao_sai_lech: 'trình bày HVS Tài chính số / HVS Thực tập số dạy các thủ tục hành chính, biểu mẫu, cách tính thuế phí cụ thể hoặc quản trị danh mục nâng cao cho người mới bắt đầu (thực tế: tập trung đào tạo kiến thức đầu tư cốt lõi FA LV1 và TA LV1 giúp tự phân tích)'
```

### TIER 2 — Hạn chế (tối đa 1 lần/bài)

```
RESTRICTED_STRINGS:
  - "Tận dụng"       → "Dùng" / "Sử dụng"
  - "Mạnh mẽ"        → "Hiệu quả" / "Ổn định"
  - "Liền mạch"      → "Dễ dàng" / "Mượt mà"
  - "Đột phá"        → nêu kết quả cụ thể
  - "Cốt lõi"        → "Chính" / "Quan trọng"
  - "Hệ sinh thái"   → "Môi trường" / "Thị trường" / "Cộng đồng"
  - "Nhịp đập thị trường" → "Biến động" / "Diễn biến"
```

### REQUIRED — Thiếu = FAIL

```
REQUIRED:
  - direct_answer: 'câu đầu tiên dưới H2 phải trả lời trực tiếp heading, không dẫn dắt'
  - entity_first: 'thực thể quan trọng đứng trong 5-7 từ đầu câu'
  - specific_evidence: 'mã cổ phiếu (VCB/HPG...) | % cụ thể | sàn (HOSE/HNX)'
  - rhythm_break: 'có ít nhất 1 câu ≤7 từ mỗi 3-4 câu dài'
  - product_bridge: 'nêu nỗi đau/vấn đề TRƯỚC khi giới thiệu sản phẩm HVS'
  - source_legal: 'nguồn pháp lý chỉ dùng vanban.chinhphu.vn hoặc vbpl.vn'
  - active_voice_def: 'định nghĩa bằng câu chủ động, không bị động'
```

---

## 1. Danh sách từ vựng "Đen" — Full Rationale

### Tier 1: Cấm tuyệt đối (Flag & Remove)

| Từ/Cụm từ AI-vibe | Lý do | Cách thay thế |
| :--- | :--- | :--- |
| "Trong thế giới không ngừng phát triển..." | Mở đầu sáo rỗng. | Đi thẳng vào vấn đề/nỗi đau. |
| "Mở khóa tiềm năng..." | Dịch "Unlock potential" máy móc. | "Tối ưu lợi nhuận", "Gia tăng tài sản". |
| "Hành trình..." | Overused. | "Quá trình", "Lộ trình", "Bước đi". |
| "Hơn cả một..." | Kiểu quảng cáo AI. | Mô tả trực tiếp giá trị. |
| "Tóm lại," / "Kết luận là," | Chuyển đoạn cứng nhắc. | "Nhìn chung,", "Như vậy,". |
| "Đáng chú ý là," | Dịch "Notably,". | "Quan trọng là:", "Đặc biệt:". |
| "Nâng tầm..." | Sáo rỗng. | "Cải thiện", "Bứt phá", "Làm chủ". |
| "Giải pháp toàn diện" | Mơ hồ. | Liệt kê cụ thể giải quyết được gì. |
| "Cá nhân tôi thấy..." | AI giả vờ có cảm xúc. | Đưa ra nhận xét khách quan có bằng chứng. |
| "Đừng bỏ lỡ..." | FOMO kiểu AI. | Nêu lợi ích sát sườn. |
| "Hiểu một cách đơn giản," | Filler câu giờ của AI. | Đi thẳng vào định nghĩa. |
| "Chúng tôi thấu hiểu rằng..." | AI Empathy filler. | Xóa bỏ, nêu thẳng giải pháp. |
| "Đọc vị" | AI filler mơ hồ. | Dùng động từ cụ thể: "phân tích", "dự báo". |

### Tier 2: Hạn chế (tối đa 1 lần/bài)

| Từ/Cụm từ | Thay bằng |
| :--- | :--- |
| "Tận dụng" (Leverage) | "Dùng", "Sử dụng" |
| "Mạnh mẽ" (Robust) | "Hiệu quả", "Ổn định", "Chắc chắn" |
| "Liền mạch" (Seamless) | "Dễ dàng", "Mượt mà" |
| "Đột phá" (Breakthrough/Disrupt) | Nêu kết quả cụ thể |
| "Cốt lõi" (Core/Pivotal) | "Chính", "Quan trọng" |
| "Hệ sinh thái" (Ecosystem) | "Môi trường", "Thị trường", "Cộng đồng" |
| "Nhịp đập thị trường" | "Biến động", "Diễn biến", "Sức nóng" |

---

## 2. Pattern Categories (AI-isms Detection)

### A. Content Patterns (Nội dung sáo rỗng)
1. **Significance Inflation:** Tránh "đánh dấu một bước ngoặt", "thay đổi cuộc chơi". -> Thay bằng: "giúp giảm 20% chi phí".
2. **Vague Attributions:** Tránh "Các chuyên gia tin rằng", "Nhiều người cho rằng". -> Thay bằng: "Theo báo cáo của SSI năm 2023...".
3. **Superficial -ing analysis:** Tránh "phản ánh...", "tượng trưng cho...", "thể hiện...". -> Thay bằng số liệu hoặc sự thật cụ thể.
4. **Promotional Language:** Tránh tính từ hoa mỹ: "vibrant", "nestled", "thriving". -> Viết trung tính, khách quan.

### B. Language Patterns (Cách dùng từ)
1. **Copula Avoidance:** AI hay dùng "đóng vai trò là", "mang đặc điểm là", "tính năng nổi bật là". -> Thay bằng: "là", "có".
2. **Filler Phrases:** "Để mà", "Do thực tế là", "Trong nỗ lực nhằm". -> Thay bằng: "Để", "Vì", "Nhằm".
3. **Synonym Cycling:** AI cố tránh lặp từ bằng cách dùng 4-5 từ đồng nghĩa (nhà đầu tư, người chơi, trader, khách hàng). -> HVS: Dùng duy nhất 1 từ chính xác nhất (nhà đầu tư).

### C. Structure Patterns (Cấu trúc máy móc)
1. **Formatting Overuse:** Tránh lạm dụng Bold, Em-dashes (—), Emojis trong tiêu đề.
2. **Inline-header lists:** Tránh kiểu "**Tốc độ:** Tốc độ giúp...". -> Viết thành đoạn văn hoặc list đơn giản.
3. **Rhythm & Uniformity:** AI viết các câu có độ dài bằng nhau (15-20 chữ). -> HVS: Đan xen câu cực ngắn (5-7 chữ) và câu dài hơn.
4. **Rhetorical Questions:** Tránh mở đầu bằng câu hỏi tu từ: "Bạn đã bao giờ tự hỏi...?". -> Đi thẳng vào khẳng định.
5. **Active Voice Definitions:** Tránh định nghĩa kiểu bị động "Được khởi xướng bởi...", "Được xem là...". -> Thay bằng câu chủ động: "Benjamin Graham đã khởi xướng...", "Nhà đầu tư coi đây là...".
6. **Formula Formatting for Google Docs:** Tránh sử dụng định dạng LaTeX như `$$` hoặc `$` cho các công thức tài chính. Bản sao lưu/chuyển đổi sang Google Docs sẽ bị lỗi hiển thị. Bắt buộc dùng khối trích dẫn in đậm thuần túy (ví dụ: `> **Công thức = A / B**`).


### D. Communication Patterns (Dấu vết Chatbot)
1. **Chatbot Artifacts:** "Tôi hy vọng thông tin này hữu ích", "Hãy liên hệ nếu...". -> Xóa bỏ hoàn toàn.
2. **"Let's" constructions:** "Hãy cùng tìm hiểu", "Chúng ta hãy xem xét". -> Bắt đầu ngay bằng nội dung.
3. **Generic Conclusions:** "Tương lai vẫn còn ở phía trước", "Chỉ có thời gian mới trả lời". -> Đưa ra một hành động cụ thể cho người đọc.
4. **Generic Product Headings:** Tuyệt đối không dùng các tiêu đề lặp đi lặp lại như "HVS Có Thể Giúp Gì?", "HVS Đồng Hành Cùng Bạn". -> Thay bằng tiêu đề có tính ngữ cảnh bài viết (Ví dụ: "Làm chủ thao tác mua VCB cùng HVS").
5. **Introduction Pacing:** Tránh dùng tiêu đề khẳng định "Ưu điểm/Lợi ích khi học tại..." ngay khi người dùng chưa biết thương hiệu là ai. -> Thay bằng tiêu đề dẫn dắt: "Học đầu tư bài bản cùng...", "Giải pháp đầu tư thực chiến...".
6. **Logical Heading Coherence:** Đảm bảo sự liên kết chặt chẽ giữa các đối tượng trong tiêu đề. Nếu đoạn trên nói về Graham, đoạn dưới nói về Buffett, tiêu đề phải thể hiện được sự kế thừa hoặc mối quan hệ giữa hai người.
7. **Problem-Solution Product Bridge:** Tuyệt đối không giới thiệu sản phẩm HVS một cách hời hợt. BẮT BUỘC nêu bật vấn đề/thách thức/nỗi đau mà người đọc đang gặp phải trước khi đưa ra giải pháp từ HVS.
8. **HVS Educational Scope Coherence:** Tránh giới thiệu HVS Tài chính số / HVS Thực tập số như thể hướng dẫn các thủ tục hành chính, cách tính thuế phí hay quản trị danh mục chi tiết (đối với F0) — nền tảng này tập trung đào tạo kiến thức đầu tư nền tảng như Phân tích cơ bản FA Level 1 và Phân tích kỹ thuật TA Level 1 để giúp người học có năng lực tự phân tích.

---

## 3. Quy tắc viết Style Rules (Bổ sung)

1. **Sát thực tế:** Luôn kèm mã cổ phiếu (VCB, HPG), sàn (HOSE), hoặc con số cụ thể.
2. **Xưng hô:** "HVS" và "Bạn". Không dùng "Quý nhà đầu tư".
3. **Nguồn pháp lý:** Chỉ `vanban.chinhphu.vn` hoặc `vbpl.vn`.
4. **Cấm ngoặc kép nhấn mạnh:** Tuyệt đối không dùng dấu ngoặc kép để nhấn mạnh các từ ngữ, thuật ngữ (Ví dụ: ❌ "đúng giá", ❌ "quyền lực", ❌ "thần tốc"). Nếu cần nhấn mạnh, hãy dùng Bold hoặc viết lại câu để làm nổi bật ý nghĩa.
5. **Ngoặc kép hợp lệ:** Chỉ dùng cho trích dẫn nguyên văn lời nói hoặc tên tài liệu pháp lý cụ thể.

---

## 4. Nhật ký học hỏi (Feedback Learning Log)

- [2026-05-08]: Tối ưu toàn bộ rules dựa trên `avoid-ai-writing` framework. Thêm Tiered Vocabulary và Categorized Patterns (Content, Language, Structure, Communication).
- [2026-05-07]: Thêm quy tắc hạn chế ngoặc kép và cá nhân hóa sản phẩm theo Persona.
- [2026-05-07]: Bổ sung quy tắc về nguồn trích dẫn Chính phủ, cấm ẩn dụ hoa mỹ (đại dương, sóng dữ).
- [2026-05-13]: Cập nhật từ VN-Index feedback: Cấm "Hiểu một cách đơn giản" (filler), hạn chế "Nhịp đập thị trường" (cliché).
- [2026-05-13]: Cập nhật từ "Cách mở tài khoản" feedback: Cấm "Chúng tôi thấu hiểu rằng" (AI empathy filler), thêm quy tắc Pacing khi giới thiệu sản phẩm cho người dùng mới.
- [2026-05-14]: Cập nhật từ "Đầu tư giá trị" feedback: Ép dùng câu chủ động cho định nghĩa, yêu cầu tính mạch lạc giữa các Heading và cấu trúc Vấn đề - Giải pháp khi lồng ghép sản phẩm HVS.
- [2026-05-14]: Cập nhật từ "Tích sản" và "Định giá" feedback: Cấm tuyệt đối dấu ngoặc kép nhấn mạnh (Quy tắc 3.4), yêu cầu chia nhỏ phương pháp tính toán thành H3 để tăng trải nghiệm đọc.
- [2026-05-14]: Cập nhật từ "Hỗ trợ - Kháng cự" feedback: Cấm từ "Đọc vị" (AI filler), yêu cầu tách nhỏ các bước "Cách thực hiện" thành H3, và siết chặt cấu trúc Vấn đề - Giải pháp (phải nêu nỗi đau bẫy tâm lý/phá vỡ giả trước khi dẫn về HVS).
- [2026-05-18]: Tái cấu trúc file: Thêm Section 0 (Quick Scan) để skills/QA đọc trực tiếp — loại bỏ anti-ai-digest.md riêng biệt. Content-feedback-loop cập nhật cả Section 0 khi học rule mới.
- [2026-05-26]: Cập nhật từ "Dow Jones" feedback: Thay đổi tiêu đề H1 loại bỏ từ cấm "đọc vị"; cấm sử dụng công thức dạng LaTeX ($$ hoặc $) gây lỗi hiển thị khi chuyển sang Google Docs, bắt buộc dùng blockquote in đậm.
- [2026-05-29]: Cập nhật từ "Dệt may" feedback: Tối ưu hóa cấu trúc bài viết Toplist ngành bằng cách chuyển các phần phân tích chi tiết ("Luận điểm đầu tư", "Rủi ro đầu tư") của mỗi doanh nghiệp từ dạng danh sách bullet points thành tiêu đề H4 sub-headings để tăng trải nghiệm phân cấp trực quan và đồng bộ hóa chuyên sâu.
- [2026-05-29]: Cập nhật từ "Nhựa" feedback: Xây dựng cấu trúc danh mục cổ phiếu tiềm năng chuyên sâu (Comprehensive Stock Directory) bằng cách mở rộng từ 3 lên 5 mã cổ phiếu đặc trưng của ngành, triển khai đồng bộ thành tiêu đề H3 với các đề mục phân tích Luận điểm và Rủi ro chi tiết.
- [2026-05-29]: Cập nhật từ "Thực phẩm" feedback: Tiếp tục củng cố cấu trúc danh mục cổ phiếu tiềm năng chuyên sâu (Comprehensive Stock Directory) cho ngành tiêu dùng thiết yếu bằng cách bóc tách 5 mã cổ phiếu tiêu biểu (MCH, VNM, MSN, SAB, DBC) dưới dạng H3 với các kịch bản so sánh biến động giá hàng hóa và đòn bẩy tài chính.
- [2026-05-29]: Cập nhật từ "Thủy sản" feedback: Chuẩn hóa cấu trúc danh mục 5 mã cổ phiếu tiêu biểu (VHC, ANV, FMC, MPC, IDI), triệt tiêu các thuật từ học thuật AI-vibe ("Phân rã"), và rút gọn H1 tối ưu chuẩn SEO (< 65 ký tự) kết hợp định hướng kịch bản biến động giá cá đầu vào.
- [2026-05-29]: Cập nhật từ "Xây dựng" feedback: Đồng bộ hóa cấu trúc danh mục 5 mã cổ phiếu tiêu biểu (CTD, HBC, VCG, HHV, LCG), triệt tiêu thuật từ học thuật cấm "Phân rã", rút ngắn H1 tối ưu chuẩn SEO (< 65 ký tự) kết hợp định hình kịch bản biến động dòng tiền hoạt động CFO thực tế.
- [2026-05-29]: Cập nhật từ "Xuất nhập khẩu" feedback: Đồng bộ hóa cấu trúc danh mục Top 4 mã cổ phiếu tiềm năng (VHC, TNG, PTB, ANV) thành dạng H3 chi tiết, triệt tiêu sáo ngữ H1 "Hướng dẫn", và loại bỏ hoàn toàn mô hình tiêu đề H2 lặp lại "3 chất xúc tác" thành chuyên sâu theo ngành thực tế.
- [2026-06-02]: Cập nhật từ "Richard Donchian" và "CANSLIM" feedback: Cấm dấu ngoặc kép nhấn mạnh ở tiêu đề; cấm các từ sáo rỗng "Nghệ thuật săn tìm", "Chữ cái vàng", "Giải mã" ở tiêu đề; đính chính định nghĩa HVS Tài chính số là nền tảng đào tạo trực tuyến chứ không phải công cụ theo dõi số liệu tài chính.
- [2026-06-04]: Cập nhật từ "đầu tư thụ động" và "đầu tư chủ động" Revision Log (v1.3): Thêm rule hvs_product_hierarchy_sai — HVS Thực tập số là chương trình NẰM TRONG HVS Tài chính số, không phải sản phẩm độc lập; HVS Demo và HVS Forum là công cụ bổ trợ. User đã sửa lại nhiều lần vì AI thường trình bày 4 sản phẩm như ngang hàng nhau.
- [2026-06-04]: Cập nhật từ "hợp đồng mở tài khoản chứng khoán" Revision Log (v1.4): Đính chính HVS Tài chính số tập trung đào tạo kiến thức đầu tư (FA/TA) giúp nâng cao năng lực phân tích tự đọc hiểu pháp lý chứ không hướng dẫn đọc hiểu biểu mẫu hành chính cụ thể; HVS Forum gỡ rối vướng mắc pháp lý cụ thể của các công ty chứng khoán.
- [2026-06-04]: Cập nhật từ "mở tài khoản chứng khoán có mất phí không" Revision Log (v1.3): Đính chính phạm vi đào tạo của HVS Tài chính số (tập trung vào FA LV1 và TA LV1), cấm viết sai lệch rằng HVS Tài chính số trực tiếp hướng dẫn tính thuế phí hay quản trị danh mục cho F0.
- [2026-06-05]: Cập nhật từ "bán giải chấp cổ phiếu là gì" Revision Log (v1.1): Chuẩn hóa quy trình 3 bước Force Sell theo SERP ACBS/VFS, áp dụng cơ chế khớp lệnh thực tế sàn HOSE/HNX (lệnh MP, MTL, ATO/ATC), hiển thị công thức tính tiền nạp thêm/bán cổ phiếu bằng blockquote in đậm và đồng bộ HVS product hierarchy.




