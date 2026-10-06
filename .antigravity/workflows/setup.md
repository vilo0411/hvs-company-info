---
name: setup
description: Build Knowledge Base lần đầu (Research Agent). Args: all | company | market | audience | icp
---

# /setup [all|company|market|audience|icp]

Agent: `.antigravity/agents/research-agent.md`. Trống → `all`. Knowledge Base hiện tại đã `Verified ✅` (2026-05) — chỉ chạy lại khi cần refresh 1 module.

## Bước 0 — Hỏi trước (không bỏ)

1. Website chính thức? (→ WebFetch thay vì WebSearch)
2. Có tài liệu nội bộ mới trong `resources/` không?

## Bước 1 — Research theo module

| Module | Output | Nhãn |
|---|---|---|
| company | `resources/company/hvs-profile.md` (+ `identity.md`, `usps.md`) | `[verified ✅]` internal/website · `[assumed ⚠️]` WebSearch · `[TBD ❓]` |
| market | `resources/market/market-landscape.md` | |
| audience | `resources/audience/personas-deep.md` | |
| icp | `resources/audience/icp.md` (cần company + audience) | |

Mỗi output ≤600 từ. Hierarchy of truth: tài liệu nội bộ > website chính thức > WebSearch.

## Bước 2 — Gap Form

Gom mọi `[TBD ❓]` + `[assumed ⚠️]` quan trọng thành 1 form → hỏi user 1 lần.

## Bước 3 — Ghi

- Điền câu trả lời, đổi nhãn → `[verified ✅]`.
- Cập nhật `resources/confirm-with-leadership.md` (giữ nguyên block `LINT_BLOCK` / `FEE_TERMS` — `qa_lint.py` đọc).
- Nếu thay đổi sản phẩm/học phí → cập nhật `glossary.md §Phân tầng sản phẩm` (chờ user xác nhận).
- Báo: file đã ghi, số nhãn từng loại, bước tiếp `/keyword-plan`.
