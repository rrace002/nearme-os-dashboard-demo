# n8n API documentation (project copy)

Working copy of the official n8n **Connect** documentation, plus live OpenAPI specs, for building project docs and tooling against the public REST API.

Seed page: [https://docs.n8n.io/connect/n8n-api/](https://docs.n8n.io/connect/n8n-api/)

This folder is **not** a replacement for the live docs. n8n remains the source of truth. Use the copies here when you need offline/searchable pages, endpoint tables, and a snapshot of our RaceCS instance.

## Start here

| What you need | Where |
| --- | --- |
| All similar official URLs (HTML + `.md`) | [LINKS.md](LINKS.md) |
| Every HTTP operation from live OpenAPI | [ENDPOINTS.md](ENDPOINTS.md) |
| Machine-readable operations | [openapi/endpoints.json](openapi/endpoints.json) |
| Official page copies | [pages/](pages/) |
| RaceCS Swagger UI | https://n8n.racecs.com/api/v1/docs/ |
| RaceCS OpenAPI | https://n8n.racecs.com/api/v1/openapi.yml |
| n8n Cloud OpenAPI | https://internal.users.n8n.cloud/api/v1/openapi.yml |

## How n8n documents this API

n8n publishes three ways to talk to an instance from outside the editor:

1. **REST API** — HTTP against `/api/v1` with header `X-N8N-API-KEY`
2. **n8n CLI** (`@n8n/cli`) — wraps the same public API
3. **MCP server** — AI clients discover and run workflows

Official index (markdown): https://docs.n8n.io/sitemap.md  
Official AI index: https://docs.n8n.io/llms.txt  
Every docs page has a markdown twin: append `.md` to the URL.

## Our instance vs n8n Cloud

Both specs report `n8n Public API` **1.1.1**. The surfaces differ:

| | n8n.racecs.com | internal.users.n8n.cloud |
| --- | --- | --- |
| Paths | 26 | 81 |
| Operations | 41 | 131 |
| Tags | User, Audit, Execution, Workflow, Credential, Tags, SourceControl, Variables, Projects | those plus DataTable, Discover, Evaluation, Folders, GitConnections, Insights, LogStreaming, N8nPackage, CommunityPackage, Role, RoleMappingRule, SecurityPolicy, LDAP/OIDC/SAML/OTEL settings |

RaceCS currently matches the classic public API listed in the original prompt (users, audit, executions, workflows, credentials, tags, source-control, variables, projects). Cloud adds data tables, packages, folders, git connections, roles, SSO, evaluations, and related settings.

Base URL for RaceCS:

```
https://n8n.racecs.com/api/v1
```

Authenticate:

```
X-N8N-API-KEY: <key from n8n > Settings > n8n API>
```

Pagination: default 100, max 250, continue with `cursor` from `nextCursor`. See [pages/connect/n8n-api/pagination.md](pages/connect/n8n-api/pagination.md).

## Copied page map

### API guides

- [pages/connect/n8n-api.md](pages/connect/n8n-api.md) — overview
- [pages/connect/n8n-api/authentication.md](pages/connect/n8n-api/authentication.md)
- [pages/connect/n8n-api/pagination.md](pages/connect/n8n-api/pagination.md)
- [pages/connect/n8n-api/use-an-api-playground.md](pages/connect/n8n-api/use-an-api-playground.md)
- [pages/connect/n8n-api/api-reference.md](pages/connect/n8n-api/api-reference.md)
- [pages/connect/n8n-api/models.md](pages/connect/n8n-api/models.md)

### API resource pages (OpenAPI-generated)

Audit, Community Package, Credential, Data Table, Discover, Evaluation, Execution, Folders, Git Connections, Insights, Log Streaming, N8n Package, Projects, Role, Role Mapping Rule, Security Policy, Settings LDAP/OTEL/SSO OIDC/SAML, Source Control, Tags, User, Variables, Workflow.

All under `pages/connect/n8n-api/`.

### CLI, MCP, nodes, packages

- CLI: [pages/connect/n8n-cli.md](pages/connect/n8n-cli.md)
- Server CLI: [pages/deploy/host-n8n/configure-n8n/use-the-command-line.md](pages/deploy/host-n8n/configure-n8n/use-the-command-line.md)
- MCP: [pages/connect/connect-to-n8n-mcp-server.md](pages/connect/connect-to-n8n-mcp-server.md)
- Docs MCP: [pages/connect/connect-to-n8n-docs-mcp-server.md](pages/connect/connect-to-n8n-docs-mcp-server.md)
- n8n API node: [pages/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md](pages/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md)
- Create nodes: [pages/connect/create-nodes.md](pages/connect/create-nodes.md)
- Packages: [pages/build/manage-workflows/n8n-packages.md](pages/build/manage-workflows/n8n-packages.md)

**87 markdown pages** copied. Full URL list: [LINKS.md](LINKS.md).

## Quick curl against RaceCS

```bash
export N8N_URL=https://n8n.racecs.com
export N8N_API_KEY=YOUR_API_KEY

curl -sS "$N8N_URL/api/v1/workflows?limit=50" \
  -H "accept: application/json" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

CLI equivalent:

```bash
npx @n8n/cli --url=https://n8n.racecs.com --api-key="$N8N_API_KEY" workflow list
```

## Refreshing this copy

1. Official pages: `https://docs.n8n.io/<path>.md`
2. Sitemap of every docs URL: https://docs.n8n.io/sitemap.md
3. Live specs:
   - https://n8n.racecs.com/api/v1/openapi.yml
   - https://internal.users.n8n.cloud/api/v1/openapi.yml

Sources and the official sitemap snapshot live in [sources/](sources/).

## License / attribution

Copied pages are n8n documentation. n8n’s public API is offered under the Sustainable Use License. See [SOURCE.md](SOURCE.md).
