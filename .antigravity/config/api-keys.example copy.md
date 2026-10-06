# API Keys — Template

> Copy thành `api-keys.md` (cùng thư mục, đã gitignore) và điền key thật. Hoặc đặt cùng tên biến trong `.env` ở root.

## DataForSEO (SERP research — có phí ~$0.002/keyword)

Dùng bởi `.antigravity/skills/seo-research/scripts/serp_research.py`: top 10 Google VN (tiếng Việt), People Also Ask, Featured Snippet, Related Searches. Cache 30 ngày tại `seo-strategy/raw/serp/` — 1 keyword = 1 call. Không dùng `--no-cache` trừ khi user yêu cầu.
Lấy login/password API tại https://app.dataforseo.com/api-access (password API ≠ password web).

```
DATAFORSEO_LOGIN=you@example.com
DATAFORSEO_PASSWORD=your_api_password
```

## Jina AI (tùy chọn)

Miễn phí, không cần key (`https://r.jina.ai/{url}`) — chỉ gọi khi parser local lấy <300 từ. Token chỉ để tăng rate limit:
```
JINA_API_KEY=jina_your_token_here
```

## Firecrawl (tùy chọn — fallback `scrape.py`)

```
FIRECRAWL_API_KEY=fc-your_key_here
```

## Google Drive (export /gdocs trên Antigravity)

```
GOOGLE_DRIVE_CREDENTIALS_FILE=.antigravity/secrets/credentials.json
```
