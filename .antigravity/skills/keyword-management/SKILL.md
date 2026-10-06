---
name: keyword-management
description: Chọn keyword từ keyword-hvs.csv và theo dõi trạng thái qua script — tránh trùng bài.
---

# Skill: Keyword Management

## Nguồn
- `seo-strategy/keywords/keyword-hvs.csv` — cột `Keyword`, `Search Volume`, `Đối tượng`, `Main Topic 1`/`Subtopic`. Không có cột Status — trạng thái nằm ở `topic-clusters.md`.
- `.antigravity/skills/keyword-management/resources/persona-mapping.md` — map Đối tượng → persona.

## Tra cứu / cập nhật (dùng script, không đọc file lớn)
- Đã có bài chưa: `python scripts/topic_status.py --find "<kw>"`
- Thêm vào cluster map: `python scripts/topic_status.py --add "<kw>" --cluster "<tên>"`
- Đưa vào sprint: `python scripts/sprint_status.py --add "<kw>" --cluster "<tên>" --persona "<P>"`
- Bắt đầu viết: `python scripts/topic_status.py <slug> --set "In Progress"`
