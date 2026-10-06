---
name: revise
description: Sửa đoạn / section cụ thể trong 1 bài — có context load + lint + self-audit bắt buộc. Args: <slug|path> ["yêu cầu"]
---

# /revise — Content Edit Rule entry point

Áp dụng cho **mọi** yêu cầu sửa nội dung (kể cả "sửa 1 câu" qua chat). Rule: `workflow-integrity.md §4`.

## 🔄 Bước 0: Context Load (nếu chưa có trong session)

`anti-ai-rules.md §0` · `glossary.md` · `.antigravity/memory/instincts.md` · file mục tiêu · `grep -n "<slug>" seo-strategy/content-plan/revision-log.md`.

## Bước 1 — Xác nhận phạm vi

Nêu lại: file, section/dòng sẽ sửa, không sửa gì. Nếu user chưa nói rõ → hỏi 1 câu.

## Bước 2 — Ghi log trước khi sửa

Append `seo-strategy/content-plan/revision-log.md`:
```
### [YYYY-MM-DD] - <slug>
- Yêu cầu: "<nguyên văn user>"
- Phạm vi: <H2/dòng>
```

## Bước 3 — Sửa

Chỉ trong phạm vi đã chốt. 3S (Specific · Story · Statistics), giữ persona, giữ `Word_Count` section (±10%).

## Bước 4 — Lint + Self-audit

```
python scripts/qa_lint.py <file> --fix
```
→ 0 CRITICAL/MAJOR mới (≤2 vòng). Self-audit 4 điểm: mở đoạn trực diện · nguồn số liệu · persona/xưng hô · HVS bridge không bị vỡ.

## Bước 5 — Trình bày

```
❌ BẢN CŨ
…
✅ BẢN SỬA
…
Lint: PASS · Score N/100
```
Chỉ ghi đè file sau khi user đồng ý (trừ khi user đã yêu cầu "sửa luôn"). Nếu lỗi là pattern mới → gợi ý `/learn`.
