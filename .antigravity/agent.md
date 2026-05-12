# 🧠 Project Knowledge Hub (agent.md)

Chào mừng bạn đến với hệ sinh thái tri thức của HVS Securities SEO Content. Tệp này cung cấp cái nhìn tổng quan về dự án và cách phối hợp giữa con người và AI.

---

## 🎯 Mục tiêu dự án
Xây dựng hệ thống sản xuất nội dung SEO chuyên sâu, thực chiến và loại bỏ hoàn toàn "vibe AI" cho thương hiệu HVS Securities.

## 👥 Hệ thống Sub-Agents
- **SEO Collector** (`.antigravity/agents/seo-collector.md`): SERP research, tạo Content Brief
- **Brand Guardian** (`.antigravity/agents/brand-guardian.md`): Audit brand compliance cho `/optimize`
- **Quality Guardian** (`.antigravity/agents/quality-guardian.md`): QA độc lập
- **Research Agent** (`.antigravity/agents/research-agent.md`): Build Knowledge Base cho `/setup`

## 🔄 Content Pipeline (write-track.md)

Quy trình đầy đủ tại `.antigravity/rules/write-track.md`. Tóm tắt 6 phases:

1. **Phase 0 (Pre-flight):** Duplicate check + Cluster role check
2. **Phase 1 (Context):** SEO Collector (SERP) + Brand/Persona files song song
3. **Phase 2 (Outline):** Content Brief theo template — lưu `1-outlines/`
4. **Phase 3 (Draft):** Viết theo Brief sections — lưu `2-user-review/`
5. **Phase 4 (QA):** Verify checklist — fix targeted nếu Fail
6. **Phase 5 (Linking):** Topic Cluster → link obligations
7. **Phase 6 (Finalize):** Move → `3-finalized/` + sync 3 files + feedback loop

## 🏷️ Quy chuẩn đặt tên
- `Outline-[slug].md` → `content/blog/1-outlines/`
- `Draft-[slug].md` → `content/blog/2-user-review/`
- `Final-[slug].md` → `content/blog/3-finalized/`

## 🛠️ Commands

### Layer 1 — Knowledge Base
- `/setup [all|company|market|audience|icp]`: Build Knowledge Base

### Layer 2 — Keyword Strategy
- `/cluster [csv|raw file]`: Tạo Topic Cluster map
- `/keyword-plan [persona|N]`: Sprint Planner — chọn N bài viết tiếp

### Layer 3 — Content Pipeline
- `/write [keyword]`: Express mode — duyệt Outline, AI tự hoàn thiện
- `/write [keyword] --step`: Guided mode — duyệt Outline + Draft
- `/write [keyword] --auto`: Auto mode — không duyệt
- `/write [keyword] --no-serp`: Bỏ SERP research (kết hợp được với mọi mode)
- `/approve`: Duyệt giai đoạn hiện tại (mode-aware)
- `/optimize [path]`: Tối ưu bài cũ
- `/link`: Gắn internal links
- `/raw [path]`: Xử lý nội dung thô

*Alias: `/detailed` = `/write --step` | `/fast` = `/write --no-serp`*

## 🛑 QUY TẮC BẤT BIẾN (STRICT GUARDRAILS)
- **KHÔNG được bỏ qua SERP Research**: Trừ khi có flag `--no-serp`. Nếu không có dữ liệu thực, phải báo cáo Fail thay vì viết chung chung.
- **KHÔNG được dùng Template tự do**: Phải dùng 100% format tại `brief-template.md`.
- **Bible Anti-AI**: Mọi output văn bản (Outline/Draft/Final) phải được đối chiếu với `anti-ai-rules.md` TRƯỚC KHI hiển thị cho User.
- **Dữ liệu thật**: Mỗi H2/H3 trong Outline phải có ít nhất 1 Entity thực (mã cổ phiếu, con số, sàn giao dịch).

## 📚 Tài liệu quan trọng
- **Pipeline:** `.antigravity/rules/write-track.md`
- **Brief template:** `.antigravity/skills/seo-research/examples/brief-template.md`
- **Luồng B — Main Agent** đọc brand + persona files song song với Luồng A:
- Đọc company file (priority order)
- Đọc persona file (priority order)
- Xác định Persona phù hợp keyword → đọc 1-2 product files tương ứng
- **Đọc `seo-strategy/resources/content-strategy/anti-ai-rules.md` (BẮT BUỘC)**
- **Workspace:** `.antigravity/rules/structure.md`
