# n8n docs snapshot and runbook

**Start here:** [RUNBOOK.md](RUNBOOK.md) — full operations runbook compiled from all 1,343 official n8n docs pages.

## What’s in this folder

| File | What it is |
| --- | --- |
| [RUNBOOK.md](RUNBOOK.md) | Operational procedures (deploy, operate, API, CLI, MCP, admin, security) |
| [runbook/PAGE-INDEX.md](runbook/PAGE-INDEX.md) | Every official page → local copy + live URL |
| [runbook/NODES.md](runbook/NODES.md) | 945 node / credential / community-node pages |
| [runbook/CHEATSHEET.md](runbook/CHEATSHEET.md) | Commands extracted from install, Server CLI, n8n CLI, API, MCP |
| [runbook/ENV-VARS.md](runbook/ENV-VARS.md) | Self-hosted environment variable names by topic |
| [ENDPOINTS.md](ENDPOINTS.md) | Live OpenAPI operations (RaceCS vs n8n Cloud) |
| [LINKS.md](LINKS.md) | Connect/API similar-link list |
| [pages/](pages/) | Full markdown copies of the official docs |
| [openapi/](openapi/) | RaceCS + Cloud OpenAPI YAML + `endpoints.json` |
| [SOURCE.md](SOURCE.md) | Attribution and license |

## RaceCS

- https://n8n.racecs.com
- API docs: https://n8n.racecs.com/api/v1/docs/
- OpenAPI: https://n8n.racecs.com/api/v1/openapi.yml
- Header: `X-N8N-API-KEY`

## Refresh

1. `https://docs.n8n.io/sitemap.md` for the page list
2. Each page: `https://docs.n8n.io/<path>.md`
3. OpenAPI: RaceCS and `https://internal.users.n8n.cloud/api/v1/openapi.yml`
