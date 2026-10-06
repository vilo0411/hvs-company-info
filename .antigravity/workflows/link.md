---
name: link
description: Internal linking — chèn link vào bài đang viết hoặc backfill từ bài cũ. Args: [slug] [--backfill] [--cluster|--silo|--power|--conversion] [--audit]
---

# /link

Skill chi tiết: `.antigravity/skills/internal-linking/SKILL.md`. **Không đọc `anchor-index.md`** — dùng script.

## Modes

| Lệnh | Việc |
|---|---|
| `/link <slug>` | Đề xuất 3–6 link outbound cho bài (mặc định `--cluster`) |
| `/link <slug> --backfill` | Tìm bài cũ nên link tới bài này (sau khi live) |
| `/link --audit` | Dashboard in/out link + orphan |
| `--silo` / `--power` / `--conversion` | Ưu tiên cross-cluster / super pillar / trang `/thuc-tap-so` |

## Bước 1 — Tra cứu

```
python scripts/fetch_sitemap.py --refresh            # nếu cache >24h
python scripts/find_links.py "<keyword>" --exclude <slug> --top 8
```
Chỉ dùng dòng **Sitemap ✓**. Không đoán slug, không dùng `Final-*.md`/`file:///`/relative.

## Bước 2 — Đề xuất (chờ xác nhận)

```
🏛️ PRIMARY (cùng cluster): "anchor" → URL
🛰️ SECONDARY (cross-cluster): "anchor" → URL
🎁 CONVERSION: "anchor" → https://taichinhso.hvsvn.com/thuc-tap-so[/NHA-PHAN-TICH|/NHA-TU-VAN]
📊 Tổng N link · 100% Sitemap ✓
```
Anchor = partial match tự nhiên trong câu; **không ép "… là gì"**; mỗi URL đích 1 lần; 1 link / 150–250 từ.

## Bước 3 — Chèn & validate

Chèn inline → `python scripts/qa_lint.py <file> --no-sitemap=false` (mặc định có sitemap) → `LINK-*` = 0.

## Backfill (`--backfill`)

```
python scripts/find_links.py --backfill <slug> --top 5
```
Sửa đúng dòng được nêu trong mỗi bài nguồn (anchor lấy từ chính câu đó) → `qa_lint.py <file nguồn>` → ghi `revision-log.md` 1 dòng/bài.
Bài chưa có trong anchor-index → `python scripts/find_links.py --add-row <slug> --anchor "…" --partial "…" --cluster "CLUSTER X"` (finalize.py thường đã làm).

## Audit (`--audit`)

```
python scripts/link_audit.py
```
→ `seo-strategy/content-plan/internal-link-dashboard.md`. Ưu tiên xử lý 🔴 Orphan → `--backfill`.
