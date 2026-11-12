# Deployment guide

## Docker
```bash
docker build -t hisaab .
docker run --rm -p 8080:8080 hisaab
```

## Render
1. Push this repository to GitHub.
2. Create a Render Blueprint from the repo (`render.yaml`).
3. Health check path: `/healthz`

## Production operations
- Terminate TLS and attach a custom domain at the hosting layer.
- Add edge rate limiting and WAF.
- Configure uptime monitoring on `/healthz` and `/readyz`.
- Engine stays on localhost; never expose `HISAAB_ENGINE_PORT` publicly.

## Runtime configuration
| Variable | Default | Purpose |
|---|---|---|
| `HISAAB_HTTP_PORT` | `8080` | Public gateway port |
| `HISAAB_ENGINE_PORT` | `8081` | Internal engine port |
| `HISAAB_BIND` | `0.0.0.0` | Gateway bind address |
| `HISAAB_RATE_LIMIT` | `60` | Max requests per IP per minute |
| `HISAAB_LLM_PROVIDER` | (empty) | `gemini` or `groq` |
| `HISAAB_LLM_API_KEY` | (empty) | Server-side only |

## PDF reports
`POST /api/report/pdf` with `{lang, inputs, result}` returns `application/pdf`.

## Official source monitor
- `POST /api/ingestion/monitor`
- `GET /api/ingestion/candidates`
- `POST /api/ingestion/approve`
