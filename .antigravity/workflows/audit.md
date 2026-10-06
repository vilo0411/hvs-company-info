---
name: audit
description: Kiểm tra sức khỏe pipeline & link. Args: [--fix] [--links] [--wrappers]
---

# /audit

```
python scripts/pipeline_audit.py            # outline/draft stale, backlog stale, dashboard, topic-clusters vs Final, raw chưa prefix, path hỏng trong rule
python scripts/pipeline_audit.py --wrappers # .claude/commands ↔ .agents/workflows ↔ .antigravity/workflows đồng bộ
python scripts/fetch_sitemap.py --refresh
python scripts/link_audit.py                # → internal-link-dashboard.md
python scripts/sprint_status.py --sync
```

1. Chạy lần lượt, gom output.
2. Trình bày bảng vấn đề: loại · file · đề xuất.
3. `--fix` → `pipeline_audit.py --fix` chỉ làm việc an toàn (xóa outline/draft đã có Final mới hơn, bỏ row backlog stale, recount). Việc khác → liệt kê để user quyết.
4. Bài 🔴 Orphan trong dashboard → gợi ý `/link <slug> --backfill`.
