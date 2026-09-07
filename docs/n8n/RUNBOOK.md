# n8n complete operations runbook

One document: operations procedures, command cheat sheet, environment variables, public API catalog, documentation links, full page index, and nodes catalog.

Compiled from **1,343** official n8n docs pages ([sitemap](https://docs.n8n.io/sitemap.md)) plus live OpenAPI from RaceCS and n8n Cloud. Official docs remain the source of truth. Local page copies live in [`pages/`](pages/).

**RaceCS instance**

- Editor / API host: `https://n8n.racecs.com`
- Swagger: https://n8n.racecs.com/api/v1/docs/
- OpenAPI: https://n8n.racecs.com/api/v1/openapi.yml
- Auth header: `X-N8N-API-KEY`

## Contents

1. [Operations](#0-how-to-use-this-runbook)
2. [Command cheat sheet](#command-cheat-sheet)
3. [Self-hosted environment variables](#self-hosted-environment-variables)
4. [Public API endpoint catalog](#public-api-endpoint-catalog)
5. [Similar documentation links](#similar-n8n-documentation-links)
6. [Documentation page index](#documentation-page-index)
7. [Nodes and integrations catalog](#nodes-and-integrations-catalog)
8. [Source and attribution](#source-and-attribution)


## 0. How to use this runbook

1. Follow the numbered procedures in this file for day-to-day ops.
2. Open the linked `pages/...` file when you need the full official steps, flags, or screenshots.
3. For “is there a node for X?”, search [Nodes and integrations catalog](#nodes-and-integrations-catalog).
4. For HTTP against `/api/v1`, use [Public API endpoint catalog](#public-api-endpoint-catalog).
5. Refresh copies from `https://docs.n8n.io/<path>.md` and the two OpenAPI URLs when n8n ships a major version.

Corpus coverage (from sitemap):

| Section | Pages |
| --- | ---: |
| Get started | 5 |
| Deploy | 123 |
| Build | 137 |
| Nodes | 945 |
| Connect | 73 |
| Administer | 42 |
| Contribute | 5 |
| Privacy and security | 3 |
| Changelog | 9 |
| Community license | 1 |
| **Total** | **1,343** |

---

## 1. Choose how to run n8n

Source: [pages/choose-how-to-use-n8n.md](pages/choose-how-to-use-n8n.md)

| Situation | Choice |
| --- | --- |
| Need it today, no ops staff | n8n Cloud |
| Full control, custom networking, our RaceCS host | Self-hosted |
| Free / Community | Self-hosted Community edition |
| SSO, RBAC projects, source control, log streaming | Paid Cloud or self-hosted Business/Enterprise |

**RaceCS is self-hosted.** Treat Cloud docs as optional except when comparing features.

Plans/editions and limits: https://n8n.io/pricing/

---

## 2. Get started (first workflow)

Sources: [pages/welcome.md](pages/welcome.md), [pages/build-your-first-workflow.md](pages/build-your-first-workflow.md), [pages/key-concept-glossary.md](pages/key-concept-glossary.md), [pages/learning-paths.md](pages/learning-paths.md)

### 2.1 First access

1. Open the editor (`https://n8n.racecs.com` or `http://localhost:5678` for a local install).
2. Create the owner account if this is a fresh instance.
3. Create a workflow: **Overview → Create Workflow**, or **Start from Scratch**.

### 2.2 First workflow (official quickstart)

1. Add a **Schedule Trigger** (or run manually with **Execute Workflow**).
2. Add an app node (NASA DONKI in the official tutorial) and create **credentials**.
3. Use an **If** node for branching; use expressions such as `{{ $today.minus(7, 'days') }}`.
4. Execute, inspect output items, then publish when ready.

n8n 2.0 replaced active/inactive with **publish / unpublish**. Do not use deprecated `n8n update:workflow --active=...` on 2.x.

Glossary: [pages/key-concept-glossary.md](pages/key-concept-glossary.md).

---

## 3. Deploy

Source section: [Documentation page index](#documentation-page-index) → Deploy (123 pages). Overview: [pages/deploy/readme.md](pages/deploy/readme.md).

### 3.1 n8n Cloud (if used)

1. Start trial: [pages/deploy/use-n8n-cloud/start-your-free-trial.md](pages/deploy/use-n8n-cloud/start-your-free-trial.md)
2. Admin dashboard: [pages/deploy/use-n8n-cloud/use-the-admin-dashboard.md](pages/deploy/use-n8n-cloud/use-the-admin-dashboard.md)
3. Timezone, IPs, data, ownership: under `pages/deploy/use-n8n-cloud/configure-cloud/`
4. Gateway credits for hosted AI models: [pages/deploy/use-n8n-cloud/gateway-credits.md](pages/deploy/use-n8n-cloud/gateway-credits.md)
5. **The public API is not available on the free trial.** Upgrade before issuing API keys.

### 3.2 Self-hosted install (recommended path)

Official default from n8n 3.0 onward: **Docker**, not npm. npm installs still run on existing machines but new installs should use Docker.

**Fastest local / lab**

```bash
# Requires Docker Engine + Compose v2
curl -fsSL https://get.n8n.io | sh
# Editor: http://localhost:5678
# Stop:    docker compose -f ./n8n/compose.yml down
# Upgrade: curl -fsSL https://get.n8n.io | sh -s -- --upgrade
# Wipe:    docker compose -f ./n8n/compose.yml down -v && rm -rf ./n8n
```

Full page: [pages/deploy/host-n8n/install-options/one-line-setup.md](pages/deploy/host-n8n/install-options/one-line-setup.md)

**Hand-rolled Compose (production-shaped)**

1. `mkdir n8n && cd n8n`
2. Write `.env` (sandbox + SearXNG secrets). Keep it out of git.
3. Prefer **Postgres** over SQLite in production.
4. Follow [pages/deploy/host-n8n/install-options/install-using-docker-compose.md](pages/deploy/host-n8n/install-options/install-using-docker-compose.md)
5. Production AI sandbox: Daytona, not the bundled Docker-in-Docker runner.

**Quick Docker run (lab only; docs mark standalone `docker run` as outdated vs Compose)**

```bash
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 \
  -e GENERIC_TIMEZONE="America/New_York" \
  -e TZ="America/New_York" \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

Provider guides (DigitalOcean, AWS, Azure, GCP, Heroku, Hetzner, OpenShift): [pages/deploy/host-n8n/install-options/use-a-cloud-provider.md](pages/deploy/host-n8n/install-options/use-a-cloud-provider.md)

### 3.3 Configure the instance

Overview: [pages/deploy/host-n8n/configure-n8n.md](pages/deploy/host-n8n/configure-n8n.md)  
How to set vars: [pages/deploy/host-n8n/configure-n8n/basic-configuration.md](pages/deploy/host-n8n/configure-n8n/basic-configuration.md)  
Catalog: [Self-hosted environment variables](#self-hosted-environment-variables)

**Minimum production checklist**

| Item | What to set | Page |
| --- | --- | --- |
| Encryption key | `N8N_ENCRYPTION_KEY` (stable across rebuilds or credentials become unreadable) | [configure encryption key](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key.md) |
| Public URL | `N8N_EDITOR_BASE_URL`, `WEBHOOK_URL` / `N8N_WEBHOOK_URL` | [base URL](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url.md), [endpoints](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md) |
| Database | Postgres (`DB_*`) not SQLite | [database](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database.md) |
| Timezone | `GENERIC_TIMEZONE`, `TZ` | [timezone](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md) |
| Secrets via files | Append `_FILE` to vars / Docker secrets | [basic configuration](pages/deploy/host-n8n/configure-n8n/basic-configuration.md) |
| Task runners | Default on 2.x; required on 1.x via `N8N_RUNNERS_ENABLED` | [task runners](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners.md) |
| Execution prune | `EXECUTIONS_DATA_MAX_AGE` (also GDPR hygiene) | [executions](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions.md) |
| Public API | `N8N_PUBLIC_API_DISABLED` must stay unset/false | [endpoints](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md) |

Queue mode, scaling, binary data, logs, OpenTelemetry, SSRF, license: see env-var pages listed in ENV-VARS.md.

### 3.4 Scaling and hardening (self-hosted)

Follow pages under `pages/deploy/host-n8n/configure-n8n/` for:

- Queue mode / workers
- Task runners
- Security audits
- Isolate n8n (block n8n telemetry/servers)
- Custom SSL CAs
- Workflow timeouts
- Custom nodes location

---

## 4. Operate the instance (Server CLI)

The **Server CLI** runs **on the n8n host**, talks to the **database**, and bypasses API key scopes. Use it for backup, restore, license, emergency user reset.

Source: [pages/deploy/host-n8n/configure-n8n/use-the-command-line.md](pages/deploy/host-n8n/configure-n8n/use-the-command-line.md)

| | Server CLI (`n8n …`) | n8n CLI (`npx @n8n/cli`) |
| --- | --- | --- |
| Where | Same machine as n8n | Any machine with network |
| Auth | Database | API key |
| n8n must be up? | Usually no | Yes |
| Access control | Bypassed | Honors roles + key scopes |

Docker:

```bash
docker exec -u node -it <n8n-container-name> n8n <command>
```

### 4.1 Publish / unpublish (n8n 2.x)

These write the database. **Restart n8n** if the process is already running.

```bash
n8n publish:workflow --id=<ID>
n8n publish:workflow --id=<ID> --versionId=<VERSION_ID>
n8n unpublish:workflow --id=<ID>
n8n unpublish:workflow --all
```

There is **no** `--all` on publish (avoids mass-publishing prod). `update:workflow --active=` is deprecated from 2.0.

### 4.2 Execute a workflow from the host

```bash
n8n execute --id <ID>
```

### 4.3 Backup

```bash
# All entities including execution history / data tables
n8n export:entities --outputDir=./outputs --includeExecutionHistoryDataTables=true

# Workflows
n8n export:workflow --all
n8n export:workflow --id=<ID> --output=file.json
n8n export:workflow --backup --output=backups/latest/
n8n export:workflow --id=<ID> --published --output=published.json

# Credentials (encrypted unless --decrypted)
n8n export:credentials --all
n8n export:credentials --backup --output=backups/latest/
# DANGER: plaintext secrets
n8n export:credentials --all --decrypted --output=backups/decrypted.json
```

### 4.4 Restore

```bash
n8n import:entities --inputDir ./outputs --truncateTables true
n8n import:workflow --input=file.json
```

Names are limited to 128 characters. See the Server CLI page for credential import flags and SQLite caveats.

### 4.5 Other Server CLI jobs

The same page covers license, user management, community packages, LDAP reset, and more. Search headings in [use-the-command-line.md](pages/deploy/host-n8n/configure-n8n/use-the-command-line.md) or [Command cheat sheet](#command-cheat-sheet).

---

## 5. Public API (programmatic ops)

Sources: [pages/connect/n8n-api.md](pages/connect/n8n-api.md), [pages/connect/n8n-api/authentication.md](pages/connect/n8n-api/authentication.md), [pages/connect/n8n-api/pagination.md](pages/connect/n8n-api/pagination.md), [Public API endpoint catalog](#public-api-endpoint-catalog)

### 5.1 Create a key

1. Log in to n8n.
2. **Settings → n8n API → Create an API key**.
3. Label + expiration. Enterprise: assign **minimum scopes**.
4. Copy the key once. Send it as header `X-N8N-API-KEY`.

Non-enterprise keys have full access to that user’s resources.

### 5.2 Call RaceCS

```bash
export N8N_URL=https://n8n.racecs.com
export N8N_API_KEY=YOUR_API_KEY

curl -sS "$N8N_URL/api/v1/workflows?limit=50" \
  -H "accept: application/json" \
  -H "X-N8N-API-KEY: $N8N_API_KEY"
```

Playground (self-hosted): `{N8N_HOST}:{N8N_PORT}/{N8N_PATH}/api/v1/docs`  
RaceCS: https://n8n.racecs.com/api/v1/docs/

### 5.3 Pagination

- Default page size **100**, max **250**.
- Response includes `nextCursor` when more pages exist.
- Pass `cursor=<nextCursor>` on the next request.

### 5.4 What RaceCS exposes today vs Cloud

RaceCS OpenAPI: **26 paths / 41 operations** (classic public API).

Cloud OpenAPI: **81 paths / 131 operations** (adds data tables, packages, folders, git connections, roles, SSO/LDAP/OTEL, evaluations, insights, discover).

Full tables: [Public API endpoint catalog](#public-api-endpoint-catalog). Resource docs: `pages/connect/n8n-api/<resource>.md`.

**RaceCS operations (quick)**

| Method | Path |
| --- | --- |
| POST | `/audit` |
| POST/GET | `/users`, GET/DELETE `/users/{id}`, PATCH `/users/{id}/role` |
| GET/DELETE | `/executions`, GET/DELETE `/executions/{id}`, POST `/executions/{id}/retry` |
| POST/GET | `/workflows`, GET/PUT/DELETE `/workflows/{id}` |
| POST | `/workflows/{id}/activate`, `/workflows/{id}/deactivate` |
| GET/PUT | `/workflows/{id}/tags`, PUT `/workflows/{id}/transfer` |
| POST | `/credentials`, DELETE `/credentials/{id}`, GET `/credentials/schema/{credentialTypeName}`, PUT `/credentials/{id}/transfer` |
| POST/GET | `/tags`, GET/PUT/DELETE `/tags/{id}` |
| POST | `/source-control/pull` |
| POST/GET | `/variables`, PUT/DELETE `/variables/{id}` |
| POST/GET | `/projects`, PUT/DELETE `/projects/{projectId}` |
| POST | `/projects/{projectId}/users` |
| PATCH/DELETE | `/projects/{projectId}/users/{userId}` |

### 5.5 n8n API node (inside a workflow)

[pages/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md](pages/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md)  
Credential: API key + base URL `https://n8n.racecs.com/api/v1`.

Trigger on instance events: [n8n Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md).

---

## 6. n8n CLI (remote / CI / agents)

Source: [pages/connect/n8n-cli.md](pages/connect/n8n-cli.md)

```bash
npx @n8n/cli workflow list
# or
npm install -g @n8n/cli
```

```bash
n8n-cli config set-url https://n8n.racecs.com
n8n-cli config set-api-key YOUR_API_KEY
n8n-cli config show
# stored at ~/.n8n-cli/config.json mode 0600
```

Resolution order: `--url` / `--api-key` → `N8N_URL` / `N8N_API_KEY` → config file.

```bash
n8n-cli workflow list
n8n-cli workflow get <id>
cat workflow.json | n8n-cli workflow create --stdin
n8n-cli execution list --status=error --limit=10
n8n-cli credential schema gmailOAuth2
n8n-cli project create --name="My Project"
```

`--format=table|json|id-only`. Claude Code skill: `n8n-cli skill install --global`.

---

## 7. MCP

### 7.1 Instance MCP (talk to *our* n8n)

[pages/connect/connect-to-n8n-mcp-server.md](pages/connect/connect-to-n8n-mcp-server.md)  
Tools: [mcp-server-tools-reference.md](pages/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference.md)  
Client paste-config: [mcp-client-examples.md](pages/connect/connect-to-n8n-mcp-server/mcp-client-examples.md)

Typical HTTP URL: `{instance}/mcp-server/http` with a bearer token. Workflows must be **active/published**, have a **Webhook**, and `availableInMCP: true` to be executable by clients.

### 7.2 Docs MCP (talk to *documentation*)

[pages/connect/connect-to-n8n-docs-mcp-server.md](pages/connect/connect-to-n8n-docs-mcp-server.md)

| Server | URL | Use |
| --- | --- | --- |
| GitBook docs | `https://docs.n8n.io/~gitbook/mcp` | Exact docs |
| Kapa.ai | `https://n8n.mcp.kapa.ai` | Docs + forum + blog (auth on first use) |

Cursor `mcp.json`:

```json
{
  "mcpServers": {
    "n8n-docs": { "url": "https://docs.n8n.io/~gitbook/mcp" },
    "n8n-kapa": { "url": "https://n8n.mcp.kapa.ai" }
  }
}
```

Also: [pages/build/ways-of-building-workflows/connect-to-n8n-mcp-server.md](pages/build/ways-of-building-workflows/connect-to-n8n-mcp-server.md), [pages/build/integrate-ai/mcp-servers.md](pages/build/integrate-ai/mcp-servers.md).

---

## 8. Build workflows

137 pages under Build: [Documentation page index](#documentation-page-index) (Build section). Start: [pages/build/](pages/build/) via sitemap entries.

Typical operator path:

1. Understand canvas, nodes, connections, items, expressions.
2. Credentials per app — OAuth preferred.
3. Error workflows / Error Trigger; timeouts.
4. Data tables, evaluations, packages when the instance version supports them.
5. Export/import **n8n packages** (`.n8np`): [pages/build/manage-workflows/n8n-packages.md](pages/build/manage-workflows/n8n-packages.md)

Package ops (preview):

```bash
n8n-cli package export --workflow-id=<workflow-id> --output=export.n8np
n8n-cli package import --file=export.n8np --workflow-conflict-policy=fail
```

API (Cloud spec): `POST /n8n-packages/export`, `POST /n8n-packages/import`.

---

## 9. Nodes and credentials

945 pages: [Nodes and integrations catalog](#nodes-and-integrations-catalog)

- Core nodes: `pages/integrations/builtin/core-nodes/`
- App nodes: `pages/integrations/builtin/app-nodes/`
- Credentials: `pages/integrations/builtin/credentials/`
- Community nodes: [pages/integrations/community-nodes.md](pages/integrations/community-nodes.md) — read [risks](pages/integrations/community-nodes/risks.md) before enabling.
- Rate limits: [handle-rate-limits.md](pages/integrations/builtin/handle-rate-limits.md)
- Deprecated nodes: [deprecated-nodes.md](pages/integrations/builtin/deprecated-nodes.md)

**Create a custom node:** [pages/connect/create-nodes.md](pages/connect/create-nodes.md) (plan → build → test → deploy).

---

## 10. Administer

Source: [pages/administer/readme.md](pages/administer/readme.md) and 42 pages in PAGE-INDEX.

Official admin loop:

1. **Access** — users, instance roles, RBAC, projects, custom roles.
2. **Secrets** — share credentials, end-user credentials, overwrites, external vaults.
3. **Change control** — Git source control, environments, push/pull, diffs.
4. **Observe** — Insights, log streaming.

### 10.1 Users and RBAC

- [manage-users-and-access.md](pages/administer/manage-users-and-access.md)
- Add/remove: [add-and-remove-users.md](pages/administer/manage-users-and-access/add-and-remove-users.md)
- Instance roles: [understand-instance-roles.md](pages/administer/manage-users-and-access/understand-instance-roles.md)
- Projects / RBAC: [set-permissions-and-roles-rbac.md](pages/administer/manage-users-and-access/set-permissions-and-roles-rbac.md)
- 2FA: [require-two-factor-auth.md](pages/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth.md)
- LDAP / SAML / OIDC: under `pages/administer/manage-users-and-access/verify-user-identity/`
- Best practices: [follow-best-practices.md](pages/administer/manage-users-and-access/follow-best-practices.md)

### 10.2 Credentials

- Share: [share-credentials-securely.md](pages/administer/manage-credentials/share-credentials-securely.md)
- End-user (run as invoker): [end-user-credentials.md](pages/administer/manage-credentials/end-user-credentials.md)
- Overwrites (global client secrets): [credential-overwrites.md](pages/administer/manage-credentials/credential-overwrites.md)
- Vault: [use-external-secret-stores.md](pages/administer/manage-credentials/use-external-secret-stores.md)

### 10.3 Source control and environments

[pages/administer/use-source-control-and-environments.md](pages/administer/use-source-control-and-environments.md)

1. Link Git: [set-up-source-control.md](pages/administer/use-source-control-and-environments/set-up-source-control.md)
2. Pick a branching pattern: [choose-branching-patterns.md](pages/administer/use-source-control-and-environments/choose-branching-patterns.md)
3. Push/pull: [push-and-pull-changes.md](pages/administer/use-source-control-and-environments/push-and-pull-changes.md)
4. Promote between envs: [move-work-between-environments.md](pages/administer/use-source-control-and-environments/move-work-between-environments.md)
5. API: `POST /source-control/pull` (and Cloud git-connections APIs).

### 10.4 Observe

- Insights: [track-usage-with-insights.md](pages/administer/observe-and-log/track-usage-with-insights.md)
- Log streaming: [stream-logs-to-external-systems.md](pages/administer/observe-and-log/stream-logs-to-external-systems.md)
- API audit: `POST /audit` — [pages/connect/n8n-api/audit.md](pages/connect/n8n-api/audit.md)

---

## 11. Security and incident response

Sources: [pages/privacy-and-security/privacy.md](pages/privacy-and-security/privacy.md), [incident-response.md](pages/privacy-and-security/incident-response.md), [what-you-can-do.md](pages/privacy-and-security/what-you-can-do.md)

### 11.1 n8n-the-vendor

- Status: https://status.n8n.cloud/
- Data-breach notices: Data Processing Addendum at https://n8n.io/legal/#data
- Report issues: security@n8n.io

### 11.2 What we must do (especially self-hosted / RaceCS)

- User management + 2FA when more than one person uses the instance.
- OAuth for integrations whenever the service supports it.
- TLS at a reverse proxy; encrypt data at rest (disk/volume).
- Run a [security audit](pages/deploy/host-n8n/configure-n8n/security/run-security-audits.md) (`POST /audit` or Server CLI).
- Treat community nodes as untrusted; optionally disable them / block Execute Command and SSH via node env vars.
- Block Code-node external modules if policy requires it ([nodes env vars](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md)).
- Isolate n8n from n8n’s servers if required: [isolate-n8n.md](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n.md).
- Prune executions (`EXECUTIONS_DATA_MAX_AGE`) for GDPR-style deletion.

License: [Sustainable Use License](pages/n8n-community-license/sustainable-use-license.md).

---

## 12. Changelog and upgrades

- Narrative: [pages/changelog/readme.md](pages/changelog/readme.md)
- Release notes: [release-notes.md](pages/changelog/release-notes.md) (plus 2.x / 1.x / 0.x archives)
- **v3.0 breaking:** [v30-breaking-changes.md](pages/changelog/v30-breaking-changes.md) — npm install path goes away; Docker-only distribution
- **v2.0 breaking:** [v20-breaking-changes.md](pages/changelog/v20-breaking-changes.md) — publish/unpublish, task runners
- Migration tool: [v20-migration-tool.md](pages/changelog/v20-migration-tool.md)

**Upgrade (one-line install):**

```bash
curl -fsSL https://get.n8n.io | sh -s -- --upgrade
```

**Upgrade (Compose):** pull the new image, backup first (`export:entities`), then recreate. Confirm `N8N_ENCRYPTION_KEY` is unchanged.

---

## 13. RaceCS operator loop (daily / weekly)

### Daily

1. `n8n-cli execution list --status=error --limit=20 --format=json` (or Swagger `/executions?status=error`).
2. Retry or fix failed workflows; check credentials expiry.
3. Confirm webhooks still reachable at `https://n8n.racecs.com`.

### Weekly

1. `POST /audit` or UI security audit; file findings.
2. Review Insights if licensed.
3. Confirm backups: Server CLI `export:entities` or volume snapshots. Never commit `--decrypted` credential exports.

### After a workflow change

1. Edit in a non-prod project/instance when possible.
2. Source-control push/pull if Git is linked.
3. Publish explicitly (`publish:workflow` or API activate/publish).
4. Hit the webhook or `n8n-cli execution` to verify.

### Incident (instance down)

1. Check container/process, disk, Postgres.
2. Check reverse proxy / TLS.
3. Restore from last `export:entities` or volume snapshot **after** copying the current data aside.
4. Vendor status only if using Cloud: https://status.n8n.cloud/

---

## 14. Contribute / get help

- [Contribute](pages/contribute/contribute-to-n8n.md)
- Docs style: [style-guide-for-n8n-docs.md](pages/contribute/style-guide-for-n8n-docs.md)
- Help: [where-to-get-help.md](pages/contribute/where-to-get-help.md)
- Forum: https://community.n8n.io/

---

## 15. Full documentation map

Every official URL → local file: **[Documentation page index](#documentation-page-index)**

Section shortcuts:

| Section | Local root |
| --- | --- |
| Get started | `pages/welcome.md`, `pages/choose-how-to-use-n8n.md`, `pages/build-your-first-workflow.md` |
| Deploy | `pages/deploy/` |
| Build | `pages/build/` |
| Nodes | `pages/integrations/` |
| Connect | `pages/connect/` |
| Administer | `pages/administer/` |
| Contribute | `pages/contribute/` |
| Privacy | `pages/privacy-and-security/` |
| Changelog | `pages/changelog/` |
| License | `pages/n8n-community-license/` |

OpenAPI snapshots: [openapi/](openapi/).

---


## Command cheat sheet

Commands extracted from official docs. Prefer the source page when flags change.

### One-line setup

Source: [`deploy/host-n8n/install-options/one-line-setup.md`](pages/deploy/host-n8n/install-options/one-line-setup.md)

```
curl -fsSL https://get.n8n.io | sh
```

```
$ curl -fsSL https://get.n8n.io | sh

✓ Docker found (24.0.6)
✓ Docker Compose found (v2.24.0)
✓ Created ./n8n/compose.yml
✓ Created ./n8n/searxng-settings.yml
✓ Created ./n8n/.env (unique secrets generated)
Pulling images and starting (this can take a few minutes on first run)...
✓ Started n8n 2.32.0 and sandbox services

n8n is running at: http://localhost:5678
Data stored in:    ./n8n (Docker volume: n8n-data)
Config files:      ./n8n/compose.yml, ./n8n/.env

To stop:      docker compose -f ./n8n/compose.yml down
To upgrade:   curl -fsSL https://get.n8n.io | sh -s -- --upgrade
To uninstall: docker compose -f ./n8n/compose.yml down -v   # -v DELETES all n8n data
              rm -rf ./n8n
```

```
curl -fsSL https://get.n8n.io -o get-n8n.sh
less get-n8n.sh   # review it
sh get-n8n.sh
```

### Install with Docker

Source: [`deploy/host-n8n/install-options/install-with-docker.md`](pages/deploy/host-n8n/install-options/install-with-docker.md)

```
docker volume create n8n_data

docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e GENERIC_TIMEZONE="<YOUR_TIMEZONE>" \
 -e TZ="<YOUR_TIMEZONE>" \
 -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
 -e N8N_RUNNERS_ENABLED=true \
 -v n8n_data:/home/node/.n8n \
 n8nio/n8n
```

```
docker volume create n8n_data

docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e GENERIC_TIMEZONE="<YOUR_TIMEZONE>" \
 -e TZ="<YOUR_TIMEZONE>" \
 -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
 -e N8N_RUNNERS_ENABLED=true \
 -e DB_TYPE=postgresdb \
 -e DB_POSTGRESDB_DATABASE=<POSTGRES_DATABASE> \
 -e DB_POSTGRESDB_HOST=<POSTGRES_HOST> \
 -e DB_POSTGRESDB_PORT=<POSTGRES_PORT> \
 -e DB_POSTGRESDB_USER=<POSTGRES_USER> \
 -e DB_POSTGRESDB_SCHEMA=<POSTGRES_SCHEMA> \
 -e DB_POSTGRESDB_PASSWORD=<POSTGRES_PASSWORD> \
 -v n8n_data:/home/node/.n8n \
 n8nio/n8n
```

```
## Pull latest (stable) version 
docker pull n8nio/n8n

## Pull specific version 
docker pull n8nio/n8n:1.81.0

## Pull next (unstable) version 
docker pull n8nio/n8n:next
```

```
## Find your container ID 
docker ps -a

## Stop the container with the `<container_id>` 
docker stop <container_id>

## Remove the container with the `<container_id>` 
docker rm <container_id>

## Start the container 
docker run --name=<container_name> [options] -d n8nio/n8n
```

```
## Navigate to the directory containing your docker compose file 
cd </path/to/your/compose/file/directory>

## Pull latest version 
docker compose pull

## Stop and remove older version 
docker compose down

## Start the container 
docker compose up -d
```

```
pnpm stack --tunnel
```

```
## Terminal 1: Start the cloudflared tunnel service 
pnpm --filter n8n-containers services --services cloudflared

## Terminal 2: Start n8n locally 
pnpm dev
```

```
pnpm --filter n8n-containers services:clean
```

### Use the command line

Source: [`deploy/host-n8n/configure-n8n/use-the-command-line.md`](pages/deploy/host-n8n/configure-n8n/use-the-command-line.md)

```
docker exec -u node -it <n8n-container-name> <n8n-cli-command>
```

```
n8n execute --id <ID>
```

```
n8n publish:workflow --id=<ID>
```

```
n8n publish:workflow --id=<ID> --versionId=<VERSION_ID>
```

```
n8n unpublish:workflow --id=<ID>
```

```
n8n unpublish:workflow --all
```

```
n8n update:workflow --id=<ID> --active=false
```

```
n8n update:workflow --id=<ID> --active=true
```

```
n8n update:workflow --all --active=false
```

```
n8n update:workflow --all --active=true
```

```
n8n export:entities --outputDir=./outputs --includeExecutionHistoryDataTables=true
```

```
n8n export:workflow --all
```

### n8n CLI

Source: [`connect/n8n-cli.md`](pages/connect/n8n-cli.md)

```
## Use directly with npx (zero install) 
npx @n8n/cli workflow list

## Or install globally 
npm install -g @n8n/cli
```

```
n8n-cli config set-url https://your-instance.n8n.cloud
n8n-cli config set-api-key YOUR_API_KEY
n8n-cli config show
```

```
export N8N_URL=https://your-instance.n8n.cloud
export N8N_API_KEY=your_api_key
```

```
n8n-cli --url=https://my-n8n.app.n8n.cloud --api-key=n8n_api_xxxxx workflow list
```

```
n8n-cli workflow list
```

```
n8n-cli workflow list --format=json | jq '.[] | select(.active) | .id'
```

```
n8n-cli workflow list --format=id-only | xargs -I{} n8n-cli workflow deactivate {}
```

```
n8n-cli skill install --global
```

```
n8n-cli workflow list
n8n-cli workflow get <id>
```

```
cat workflow.json | n8n-cli workflow create --stdin
```

```
n8n-cli execution list --status=error --limit=10
```

```
n8n-cli credential schema gmailOAuth2  # see required fields first
n8n-cli credential create --type=gmailOAuth2 --name='My Gmail' --file=cred.json
```

### Authentication

Source: [`connect/n8n-api/authentication.md`](pages/connect/n8n-api/authentication.md)

```
## For a self-hosted n8n instance 
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'

## For n8n Cloud 
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'
```

### Pagination

Source: [`connect/n8n-api/pagination.md`](pages/connect/n8n-api/pagination.md)

```
## For a self-hosted n8n instance 
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'

## For n8n Cloud 
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'
```

```
Then to request the next page:
```

### Connect to the n8n docs MCP server

Source: [`connect/connect-to-n8n-docs-mcp-server.md`](pages/connect/connect-to-n8n-docs-mcp-server.md)

```
claude mcp add --transport http n8n-docs https://docs.n8n.io/~gitbook/mcp
claude mcp add --transport http n8n-kapa https://n8n.mcp.kapa.ai
```

```
{
	"mcpServers": {
		"n8n-docs": {
			"url": "https://docs.n8n.io/~gitbook/mcp"
		},
		"n8n-kapa": {
			"url": "https://n8n.mcp.kapa.ai"
		}
	}
}
```

```
{
	"servers": {
		"n8n-docs": {
			"type": "http",
			"url": "https://docs.n8n.io/~gitbook/mcp"
		},
		"n8n-kapa": {
			"type": "http",
			"url": "https://n8n.mcp.kapa.ai"
		}
	}
}
```

```
https://docs.n8n.io/~gitbook/mcp
https://n8n.mcp.kapa.ai
```

### MCP client connection examples

Source: [`connect/connect-to-n8n-mcp-server/mcp-client-examples.md`](pages/connect/connect-to-n8n-mcp-server/mcp-client-examples.md)

```
"mcpServers": {
  "n8n-mcp": {
    "command": "npx",
    "args": [
    "-y",
    "supergateway",
    "--streamableHttp",
    "https://<your-n8n-domain>/mcp-server/http",
    "--header",
    "Authorization:Bearer <YOUR_N8N_MCP_TOKEN>"
    ]
  }
}
```

```
claude mcp add --transport http n8n https://<your-n8n-domain>/mcp-server/http
```

```
{
    "mcpServers": {
        "n8n": {
            "type": "http",
            "url": "https://<your-n8n-domain>/mcp-server/http"
        }
    }
}
```

```
claude mcp add --transport http n8n-mcp https://<your-n8n-domain>/mcp-server/http \
  --header "Authorization: Bearer <YOUR_N8N_MCP_TOKEN>"
```

```
{
    "mcpServers": {
        "n8n-mcp": {
            "type": "http",
            "url": "https://<your-n8n-domain>/mcp-server/http",
            "headers": {
                "Authorization": "Bearer <YOUR_N8N_MCP_TOKEN>"
            }
        }
    }
}
```

```
codex mcp add n8n --url "https://<your-n8n-domain>/mcp-server/http"
```

```
{% hint style="info" %}
The `[features]` block enables Codex's HTTP MCP client. Older Codex builds require it; newer builds ignore it.
{% endhint %}

Here, replace:

* `<your-n8n-domain>`: Your n8n domain, for example `https://your-instance.app.n8n.cloud`, found in n8n under **Settings** > **Instance-level MCP > Connect a client > Server URL**.

Run `codex mcp login n8n` to complete the OAuth authorization.

**Option 2: Authenticate using API key**

Add the following entry to your `~/.codex/config.toml` file:
```

```
Here, replace:

* `<your-n8n-domain>`: Your n8n domain, for example `https://your-instance.app.n8n.cloud`, found in n8n under **Settings** > **Instance-level MCP > Connect a client > Server URL**.
* `<YOUR_N8N_MCP_TOKEN>`: Your generated token

### Connecting Gemini CLI to n8n MCP server 

Use the following CLI command:
```

```
Or add the following entry to your `~/.gemini/settings.json` file:
```

```
Here, replace:

* `<your-n8n-domain>`: Your n8n domain, for example `https://your-instance.app.n8n.cloud`, found in n8n under **Settings** > **Instance-level MCP > Connect a client > Server URL**.

Run `/mcp` in Gemini CLI and select **n8n** to complete the OAuth authorization.

### Connecting Cursor to n8n MCP server 

In the **Connect a client** dialog, select **Cursor** from **Your client**, then select **One-click setup** to open Cursor and add the n8n server automatically. Approve access when Cursor redirects you back to n8n.

Or add the following entry to your `~/.cursor/mcp.json` file (or the project's `.cursor/mcp.json`):
```

```
Here, replace:

* `<your-n8n-domain>`: Your n8n domain, for example `https://your-instance.app.n8n.cloud`, found in n8n under **Settings** > **Instance-level MCP > Connect a client > Server URL**.

### Connecting VS Code to n8n MCP server 

In the **Connect a client** dialog, select **VS Code** from **Your client**, then select **One-click setup** to open VS Code and add the n8n server automatically. Approve access when VS Code redirects you back to n8n.

Or add the following entry to your workspace's `.vscode/mcp.json` file:
```

```
Here, replace:

* `<your-n8n-domain>`: Your n8n domain, for example `https://your-instance.app.n8n.cloud`, found in n8n under **Settings** > **Instance-level MCP > Connect a client > Server URL**.

### Connecting Windsurf to n8n MCP server 

Add the following entry to your `~/.codeium/windsurf/mcp_config.json` file:
```

---


## Self-hosted environment variables

Variables named in the official env-var docs. Confirm against the live page before using in production.

### Ask n8n AI

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant.md)

`N8N_AI_ASSISTANT_BASE_URL`

### Binary data

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data.md)

`N8N_AVAILABLE_BINARY_DATA_MODES`, `N8N_BINARY_DATA_DATABASE_MAX_FILE_SIZE`, `N8N_DEFAULT_BINARY_DATA_MODE`, `N8N_BINARY_DATA_STORAGE_PATH`

### Credentials

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials.md)

`CREDENTIALS_OVERWRITE_ENDPOINT`, `CREDENTIALS_OVERWRITE_PERSISTENCE`, `N8N_MANAGED_OAUTH_SHOW_SCOPES`, `CREDENTIALS_DEFAULT_NAME`

### Database

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database.md)

`DB_TABLE_PREFIX`, `DB_PING_INTERVAL_SECONDS`, `DB_PING_TIMEOUT_MS`, `N8N_DB_PING_TIMEOUT`, `DB_PING_MAX_FAILURES_BEFORE_RECOVERY`, `DB_RECOVERY_BACKOFF_MIN_MS`, `DB_RECOVERY_BACKOFF_MAX_MS`, `DB_CONNECTION_ACQUISITION_TIMEOUT_MS`, `DB_POSTGRESDB_SSL_CA`, `DB_POSTGRESDB_SSL_CERT`, `DB_POSTGRESDB_SSL_KEY`, `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED`, `DB_SQLITE_POOL_SIZE`, `DB_SQLITE_VACUUM_ON_STARTUP`, `DB_POSTGRESDB_MAX_CONNECTION_LIFETIME_MS`, `DB_POSTGRESDB_KEEP_ALIVE`, `DB_POSTGRESDB_KEEP_ALIVE_INITIAL_DELAY_MS`

### Deployment

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md)

`N8N_ENFORCE_GLOBAL_USER_AGENT`, `N8N_GLOBAL_USER_AGENT_VALUE`, `N8N_EDITOR_BASE_URL`, `N8N_DISABLE_UI`, `N8N_PREVIEW_MODE`, `N8N_CANVAS_ONLY`, `N8N_TEMPLATES_ENABLED`, `N8N_TEMPLATES_HOST`, `N8N_ENCRYPTION_KEY`, `N8N_ENV_FEAT_ENCRYPTION_KEY_ROTATION`, `N8N_ENV_FEAT_OAUTH2_JWE`, `N8N_ENV_FEAT_TOKEN_EXCHANGE`, `N8N_OAUTH_JWE_JWKS_PER_MINUTE`, `N8N_MCP_BASE_URL`, `N8N_MCP_SERVER_RATE_LIMIT`, `N8N_OAUTH_SERVER_REGISTER_RATE_LIMIT`, `N8N_OAUTH_SERVER_AUTHORIZE_RATE_LIMIT`, `N8N_OAUTH_SERVER_TOKEN_RATE_LIMIT`, `N8N_OAUTH_SERVER_REVOKE_RATE_LIMIT`, `N8N_USER_FOLDER`, `N8N_PATH`, `N8N_HOST`, `N8N_PORT`, `N8N_LISTEN_ADDRESS`, `N8N_PROTOCOL`, `N8N_SSL_KEY`, `N8N_SSL_CERT`, `N8N_PERSONALIZATION_ENABLED`, `N8N_VERSION_NOTIFICATIONS_ENABLED`, `N8N_VERSION_NOTIFICATIONS_ENDPOINT`, `N8N_VERSION_NOTIFICATIONS_INFO_URL`, `N8N_DIAGNOSTICS_ENABLED`, `N8N_DIAGNOSTICS_CONFIG_FRONTEND`, `N8N_DIAGNOSTICS_CONFIG_BACKEND`, `N8N_PUSH_BACKEND`, `N8N_HIRING_BANNER_ENABLED`, `N8N_PUBLIC_API_SWAGGERUI_DISABLED`, `N8N_PUBLIC_API_DISABLED`, `N8N_PUBLIC_API_ENDPOINT`, `N8N_GRACEFUL_SHUTDOWN_TIMEOUT`, `N8N_DEV_RELOAD`, `N8N_REINSTALL_MISSING_PACKAGES`, `N8N_TUNNEL_SUBDOMAIN`, `N8N_PROXY_HOPS`

### Endpoints

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md)

`N8N_PAYLOAD_SIZE_MAX`, `N8N_FORMDATA_FILE_SIZE_MAX`, `N8N_METRICS`, `N8N_METRICS_PREFIX`, `N8N_METRICS_INCLUDE_DEFAULT_METRICS`, `N8N_METRICS_INCLUDE_CACHE_METRICS`, `N8N_METRICS_INCLUDE_MESSAGE_EVENT_BUS_METRICS`, `N8N_METRICS_INCLUDE_WORKFLOW_ID_LABEL`, `N8N_METRICS_INCLUDE_NODE_TYPE_LABEL`, `N8N_METRICS_INCLUDE_CREDENTIAL_TYPE_LABEL`, `N8N_METRICS_INCLUDE_API_ENDPOINTS`, `N8N_METRICS_INCLUDE_API_PATH_LABEL`, `N8N_METRICS_INCLUDE_API_METHOD_LABEL`, `N8N_METRICS_INCLUDE_API_STATUS_CODE_LABEL`, `N8N_METRICS_INCLUDE_QUEUE_METRICS`, `N8N_METRICS_QUEUE_METRICS_INTERVAL`, `N8N_METRICS_INCLUDE_SCHEDULER_METRICS`, `N8N_METRICS_SCHEDULER_INTERVAL`, `N8N_METRICS_INCLUDE_POLL_TRIGGER_METRICS`, `N8N_METRICS_INCLUDE_SSRF_METRICS`, `N8N_METRICS_INCLUDE_DNS_CACHE_METRICS`, `N8N_ENDPOINT_REST`, `N8N_ENDPOINT_WEBHOOK`, `N8N_ENDPOINT_WEBHOOK_TEST`, `N8N_ENDPOINT_WEBHOOK_WAIT`, `N8N_ENDPOINT_HEALTH`, `N8N_WEBHOOK_URL`, `WEBHOOK_URL`, `N8N_DISABLE_PRODUCTION_MAIN_PROCESS`

### Executions

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions.md)

`EXECUTIONS_MODE`, `EXECUTIONS_TIMEOUT`, `EXECUTIONS_TIMEOUT_MAX`, `N8N_AI_TIMEOUT_MAX`, `EXECUTIONS_DATA_SAVE_ON_ERROR`, `EXECUTIONS_DATA_SAVE_ON_SUCCESS`, `EXECUTIONS_DATA_SAVE_ON_PROGRESS`, `EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS`, `N8N_EXECUTION_DATA_STORAGE_MODE`, `N8N_STORAGE_PATH`, `EXECUTIONS_DATA_PRUNE`, `EXECUTIONS_DATA_MAX_AGE`, `EXECUTIONS_DATA_PRUNE_MAX_COUNT`, `EXECUTIONS_DATA_HARD_DELETE_BUFFER`, `EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL`, `EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL`, `EXECUTIONS_DATA_MAX_DISPLAY_SIZE`, `N8N_CONCURRENCY_PRODUCTION_LIMIT`, `N8N_CONCURRENCY_EVALUATION_LIMIT`, `N8N_WORKFLOW_AUTODEACTIVATION_ENABLED`, `N8N_WORKFLOW_AUTODEACTIVATION_MAX_LAST_EXECUTIONS`

### Expression engine

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/expression-engine.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/expression-engine.md)

`N8N_EXPRESSION_ENGINE`, `N8N_EXPRESSION_ENGINE_POOL_SIZE`, `N8N_EXPRESSION_ENGINE_MAX_CODE_CACHE_SIZE`, `N8N_EXPRESSION_ENGINE_TIMEOUT`, `N8N_EXPRESSION_ENGINE_MEMORY_LIMIT`, `N8N_EXPRESSION_ENGINE_IDLE_TIMEOUT`

### External data storage

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage.md)

`N8N_EXTERNAL_STORAGE_S3_HOST`, `N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME`, `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION`, `N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY`, `N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET`, `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT`, `N8N_EXECUTION_DATA_STORAGE_MODE`, `N8N_DEFAULT_BINARY_DATA_MODE`, `N8N_EXTERNAL_STORAGE_AZURE_CONTAINER_NAME`, `N8N_EXTERNAL_STORAGE_AZURE_CONNECTION_STRING`, `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_NAME`, `N8N_EXTERNAL_STORAGE_AZURE_AUTH_AUTO_DETECT`, `N8N_EXTERNAL_STORAGE_AZURE_ACCOUNT_KEY`, `N8N_EXTERNAL_STORAGE_AZURE_ENDPOINT`

### External hooks

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks.md)

_See source page for the full table._

### External secrets

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets.md)

`N8N_EXTERNAL_SECRETS_UPDATE_INTERVAL`

### Insights

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights.md)

`N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS`, `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS`, `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES`, `N8N_INSIGHTS_COMPACTION_BATCH_DELAY_MILLISECONDS`, `N8N_INSIGHTS_COMPACTION_MAX_BATCHES_PER_RUN`, `N8N_INSIGHTS_COMPACTION_MAX_RUNTIME_SECONDS`, `N8N_DISABLED_MODULES`, `N8N_INSIGHTS_COMPACTION_BATCH_SIZE`, `N8N_INSIGHTS_FLUSH_BATCH_SIZE`, `N8N_INSIGHTS_FLUSH_INTERVAL_SECONDS`, `N8N_INSIGHTS_MAX_AGE_DAYS`, `N8N_INSIGHTS_PRUNE_CHECK_INTERVAL_HOURS`

### License

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/license.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/license.md)

`N8N_HIDE_USAGE_PAGE`, `N8N_LICENSE_ACTIVATION_KEY`, `N8N_LICENSE_AUTO_RENEW_ENABLED`, `N8N_LICENSE_DETACH_FLOATING_ON_SHUTDOWN`, `N8N_LICENSE_SERVER_URL`, `N8N_LICENSE_TENANT_ID`

### Logs

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs.md)

`N8N_LOG_LEVEL`, `N8N_LOG_OUTPUT`, `N8N_LOG_FORMAT`, `N8N_LOG_CRON_ACTIVE_INTERVAL`, `N8N_LOG_FILE_COUNT_MAX`, `N8N_LOG_FILE_SIZE_MAX`, `N8N_LOG_FILE_LOCATION`, `DB_LOGGING_ENABLED`, `DB_LOGGING_OPTIONS`, `DB_LOGGING_MAX_EXECUTION_TIME`, `CODE_ENABLE_STDOUT`, `N8N_EVENTBUS_CHECKUNSENTINTERVAL`, `N8N_EVENTBUS_LOGWRITER_SYNCFILEACCESS`, `N8N_EVENTBUS_LOGWRITER_KEEPLOGCOUNT`, `N8N_EVENTBUS_LOGWRITER_MAXFILESIZEINKB`, `N8N_EVENTBUS_LOGWRITER_LOGBASENAME`, `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH`, `N8N_EVENTBUS_LOGWRITER_MAXTOTALMESSAGESPERFILE`, `N8N_LOG_STREAMING_MANAGED_BY_ENV`, `N8N_LOG_STREAMING_DESTINATIONS`

### Nodes

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md)

`N8N_COMMUNITY_PACKAGES_AUTH_TOKEN`, `N8N_COMMUNITY_PACKAGES_REGISTRY`, `N8N_COMMUNITY_PACKAGES_ENABLED`, `N8N_COMMUNITY_PACKAGES_PREVENT_LOADING`, `N8N_CUSTOM_EXTENSIONS`, `N8N_PYTHON_ENABLED`, `N8N_UNVERIFIED_PACKAGES_ENABLED`, `N8N_VERIFIED_PACKAGES_ENABLED`, `NODES_ERROR_TRIGGER_TYPE`, `NODES_EXCLUDE`, `NODES_INCLUDE`, `NODES_MERGE_SQL_SANDBOX_MEMORY_LIMIT_MB`, `N8N_COMPRESSION_NODE_MAX_DECOMPRESSED_SIZE_BYTES`, `N8N_COMPRESSION_NODE_MAX_ZIP_ENTRIES`, `N8N_COMMUNITY_PACKAGES_MANAGED_BY_ENV`, `N8N_COMMUNITY_PACKAGES`

### OpenTelemetry

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md)

`N8N_OTEL_ENABLED`, `N8N_OTEL_EXPORTER_OTLP_ENDPOINT`, `N8N_OTEL_EXPORTER_OTLP_TRACING_PATH`, `N8N_OTEL_EXPORTER_OTLP_HEADERS`, `N8N_OTEL_EXPORTER_SERVICE_NAME`, `N8N_OTEL_TRACES_SAMPLE_RATE`, `N8N_OTEL_TRACES_INCLUDE_NODE_SPANS`, `N8N_OTEL_TRACES_PRODUCTION_ONLY`, `N8N_OTEL_TRACES_INJECT_OUTBOUND`, `N8N_OTEL_STARTUP_CONNECTIVITY_TIMEOUT_MS`, `N8N_AGENTS_TRACING_ENABLED`, `N8N_AGENTS_TRACING_RECORD_INPUTS`, `N8N_AGENTS_TRACING_RECORD_OUTPUTS`

### Queue mode

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/queue-mode.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/queue-mode.md)

`OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS`, `QUEUE_BULL_PREFIX`, `QUEUE_BULL_REDIS_DB`, `QUEUE_BULL_REDIS_HOST`, `QUEUE_BULL_REDIS_PORT`, `QUEUE_BULL_REDIS_USERNAME`, `QUEUE_BULL_REDIS_PASSWORD`, `QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD`, `QUEUE_BULL_REDIS_CLUSTER_NODES`, `QUEUE_BULL_REDIS_TLS`, `QUEUE_BULL_REDIS_DUALSTACK`, `QUEUE_WORKER_TIMEOUT`, `N8N_GRACEFUL_SHUTDOWN_TIMEOUT`, `QUEUE_HEALTH_CHECK_ACTIVE`, `QUEUE_HEALTH_CHECK_PORT`, `QUEUE_WORKER_LOCK_DURATION`, `QUEUE_WORKER_LOCK_RENEW_TIME`, `QUEUE_WORKER_STALLED_INTERVAL`, `QUEUE_WORKER_MAX_STALLED_COUNT`, `N8N_WEBHOOK_RESPONSE_RELAY_SIZE_MAX`, `N8N_WEBHOOK_RESPONSE_RELAY_OFFLOAD_ENABLED`, `N8N_DEFAULT_BINARY_DATA_MODE`, `N8N_MULTI_MAIN_SETUP_ENABLED`, `N8N_MULTI_MAIN_SETUP_KEY_TTL`, `N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL`

### Scheduler

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/scheduler.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/scheduler.md)

`N8N_METRICS_INCLUDE_SCHEDULER_METRICS`, `N8N_METRICS_SCHEDULER_INTERVAL`, `N8N_SCHEDULER_ENABLED`, `N8N_USE_WORKFLOW_PUBLICATION_SERVICE`, `N8N_SCHEDULER_POLL_TRIGGERS_ENABLED`, `N8N_ENV_FEAT_SKIP_DURABLE_SCHEDULER`, `N8N_POLLER_DURABLE_CURSORS_ENABLED`, `N8N_SCHEDULER_POLL_TIMEOUT`, `N8N_SCHEDULER_LEASE_DURATION`, `N8N_SCHEDULER_MATERIALIZATION_WINDOW`, `N8N_SCHEDULER_MATERIALIZATION_INTERVAL`, `N8N_SCHEDULER_MATERIALIZATION_TIMEOUT`, `N8N_SCHEDULER_EXECUTOR_INTERVAL`, `N8N_SCHEDULER_EXECUTOR_TIMEOUT`, `N8N_SCHEDULER_CLAIM_BATCH_SIZE`, `N8N_SCHEDULER_REAPER_INTERVAL`, `N8N_SCHEDULER_REAPER_BATCH_SIZE`, `N8N_SCHEDULER_REAPER_TIMEOUT`, `N8N_SCHEDULER_MAX_ATTEMPTS`, `N8N_SCHEDULER_RETENTION`, `N8N_SCHEDULER_FAILED_RETENTION`, `N8N_SCHEDULER_RETENTION_INTERVAL`, `N8N_SCHEDULER_RETENTION_TIMEOUT`, `N8N_SCHEDULER_OWNER_RECONCILIATION_ENABLED`, `N8N_SCHEDULER_OWNER_RECONCILIATION_INTERVAL`, `N8N_SCHEDULER_OWNER_RECONCILIATION_TIMEOUT`, `N8N_SCHEDULER_OWNER_RECONCILIATION_BATCH_SIZE`, `N8N_SCHEDULER_OWNER_QUARANTINE_GRACE`, `N8N_SCHEDULER_OWNER_SETTLE_PERIOD`, `N8N_SCHEDULER_MAX_CONCURRENT_PASSES`, `N8N_SCHEDULER_JITTER_RATIO`, `N8N_SCHEDULER_MIN_INTERVAL`, `N8N_SCHEDULER_TRIGGER_NODE_MODE`, `N8N_SCHEDULER_MISFIRE_GRACE`

### Security

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security.md)

`N8N_BLOCK_ENV_ACCESS_IN_NODE`, `N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES`, `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS`, `N8N_RESTRICT_FILE_ACCESS_TO`, `N8N_SECURITY_AUDIT_DAYS_ABANDONED_WORKFLOW`, `N8N_CONTENT_SECURITY_POLICY`, `N8N_SECURE_COOKIE`, `N8N_SAMESITE_COOKIE`, `N8N_GIT_NODE_DISABLE_BARE_REPOS`, `N8N_GIT_NODE_ENABLE_HOOKS`, `N8N_POSTMESSAGE_ALLOWED_ORIGINS`, `N8N_SECURITY_POLICY_MANAGED_BY_ENV`, `N8N_MFA_ENFORCED_ENABLED`, `N8N_PERSONAL_SPACE_PUBLISHING_ENABLED`, `N8N_PERSONAL_SPACE_SHARING_ENABLED`

### Source control

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control.md)

`N8N_SOURCECONTROL_DEFAULT_SSH_KEY_TYPE`

### SSO

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso.md)

`N8N_SSO_MANAGED_BY_ENV`, `N8N_SSO_USER_ROLE_PROVISIONING`, `N8N_SSO_OIDC_LOGIN_ENABLED`, `N8N_SSO_OIDC_CLIENT_ID`, `N8N_SSO_OIDC_CLIENT_SECRET`, `N8N_SSO_OIDC_DISCOVERY_ENDPOINT`, `N8N_SSO_OIDC_PROMPT`, `N8N_SSO_OIDC_ACR_VALUES`, `N8N_SSO_SAML_LOGIN_ENABLED`, `N8N_SSO_SAML_METADATA`, `N8N_SSO_SAML_METADATA_URL`

### SSRF protection

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection.md)

`N8N_SSRF_PROTECTION_ENABLED`, `N8N_SSRF_BLOCKED_IP_RANGES`, `N8N_SSRF_ALLOWED_IP_RANGES`, `N8N_SSRF_ALLOWED_HOSTNAMES`, `N8N_SSRF_BLOCKED_HOSTNAMES`, `N8N_SSRF_DNS_CACHE_MAX_SIZE`

### Task runners

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners.md)

`N8N_RUNNERS_ENABLED`, `N8N_RUNNERS_MODE`, `N8N_RUNNERS_AUTH_TOKEN`, `N8N_RUNNERS_BROKER_PORT`, `N8N_RUNNERS_BROKER_LISTEN_ADDRESS`, `N8N_RUNNERS_MAX_PAYLOAD`, `N8N_RUNNERS_MAX_OLD_SPACE_SIZE`, `N8N_RUNNERS_MAX_CONCURRENCY`, `N8N_RUNNERS_TASK_TIMEOUT`, `N8N_RUNNERS_HEARTBEAT_INTERVAL`, `N8N_RUNNERS_INSECURE_MODE`, `N8N_RUNNERS_TASK_REQUEST_TIMEOUT`, `N8N_RUNNERS_LAUNCHER_LOG_LEVEL`, `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT`, `N8N_RUNNERS_TASK_BROKER_URI`, `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT`, `N8N_RUNNERS_GRANT_TOKEN`, `N8N_RUNNERS_ID`, `N8N_RUNNERS_ALLOW_PROTOTYPE_MUTATION`, `GENERIC_TIMEZONE`, `N8N_RUNNERS_STDLIB_ALLOW`, `N8N_RUNNERS_EXTERNAL_ALLOW`, `N8N_RUNNERS_ALLOW_TRANSITIVE_IMPORTS`, `N8N_RUNNERS_BUILTINS_DENY`, `N8N_BLOCK_RUNNER_ENV_ACCESS`

### Timezone and localization

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md)

`GENERIC_TIMEZONE`, `N8N_DEFAULT_LOCALE`

### User management and 2FA

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa.md)

`N8N_EMAIL_MODE`, `N8N_SMTP_HOST`, `N8N_SMTP_PORT`, `N8N_SMTP_USER`, `N8N_SMTP_PASS`, `N8N_SMTP_OAUTH_SERVICE_CLIENT`, `N8N_SMTP_OAUTH_PRIVATE_KEY`, `N8N_SMTP_SENDER`, `N8N_SMTP_SSL`, `N8N_SMTP_STARTTLS`, `N8N_UM_EMAIL_TEMPLATES_INVITE`, `N8N_UM_EMAIL_TEMPLATES_PWRESET`, `N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED`, `N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED`, `N8N_UM_EMAIL_TEMPLATES_PROJECT_SHARED`, `N8N_USER_MANAGEMENT_JWT_SECRET`, `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS`, `N8N_USER_MANAGEMENT_JWT_REFRESH_TIMEOUT_HOURS`, `N8N_MFA_ENABLED`, `N8N_INVITE_LINKS_EMAIL_ONLY`, `N8N_INSTANCE_OWNER_MANAGED_BY_ENV`, `N8N_INSTANCE_OWNER_EMAIL`, `N8N_INSTANCE_OWNER_FIRST_NAME`, `N8N_INSTANCE_OWNER_LAST_NAME`, `N8N_INSTANCE_OWNER_PASSWORD_HASH`

### Workflow history

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history.md)

`N8N_WORKFLOW_HISTORY_PRUNE_TIME`

### Workflows

Source: [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows.md)

`N8N_ONBOARDING_FLOW_DISABLED`, `N8N_WORKFLOW_ACTIVATION_BATCH_SIZE`, `N8N_WORKFLOW_CALLER_POLICY_DEFAULT_OPTION`, `N8N_WORKFLOW_TAGS_DISABLED`

---


## Public API endpoint catalog

Generated from live OpenAPI specs for project documentation.

- Auth header: `X-N8N-API-KEY`
- Base path: `/api/v1`
- Official docs: https://docs.n8n.io/connect/n8n-api/
- Official OpenAPI (n8n Cloud internal): https://internal.users.n8n.cloud/api/v1/openapi.yml
- Our instance docs: https://n8n.racecs.com/api/v1/docs/
- Our instance OpenAPI: https://n8n.racecs.com/api/v1/openapi.yml

### Instance comparison

| Source | Version | Paths | Operations | Tags |
| --- | --- | --- | --- | --- |
| n8n.racecs.com | 1.1.1 | 26 | 41 | 9 |
| internal.users.n8n.cloud | 1.1.1 | 81 | 131 | 25 |

Our RaceCS instance currently publishes the older public-API surface (workflows, executions, credentials, users, tags, variables, projects, audit, source-control). The n8n Cloud spec adds data tables, packages, folders, git connections, roles, SSO/LDAP/OTEL settings, evaluations, insights, and more.

### n8n.racecs.com operations (41)

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `POST` | `/audit` | Audit | Generate an audit |
| `POST` | `/credentials` | Credential | Create a credential |
| `GET` | `/credentials/schema/{credentialTypeName}` | Credential | Show credential data schema |
| `DELETE` | `/credentials/{id}` | Credential | Delete credential by ID |
| `PUT` | `/credentials/{id}/transfer` | Credential | Transfer a credential to another project. |
| `GET` | `/executions` | Execution | Retrieve all executions |
| `DELETE` | `/executions/{id}` | Execution | Delete an execution |
| `GET` | `/executions/{id}` | Execution | Retrieve an execution |
| `POST` | `/executions/{id}/retry` | Execution | Retry an execution |
| `GET` | `/projects` | Projects | Retrieve projects |
| `POST` | `/projects` | Projects | Create a project |
| `DELETE` | `/projects/{projectId}` | Projects | Delete a project |
| `PUT` | `/projects/{projectId}` | Projects | Update a project |
| `POST` | `/projects/{projectId}/users` | Projects | Add one or more users to a project |
| `DELETE` | `/projects/{projectId}/users/{userId}` | Projects | Delete a user from a project |
| `PATCH` | `/projects/{projectId}/users/{userId}` | Projects | Change a user's role in a project |
| `POST` | `/source-control/pull` | SourceControl | Pull changes from the remote repository |
| `GET` | `/tags` | Tags | Retrieve all tags |
| `POST` | `/tags` | Tags | Create a tag |
| `DELETE` | `/tags/{id}` | Tags | Delete a tag |
| `GET` | `/tags/{id}` | Tags | Retrieves a tag |
| `PUT` | `/tags/{id}` | Tags | Update a tag |
| `GET` | `/users` | User | Retrieve all users |
| `POST` | `/users` | User | Create multiple users |
| `DELETE` | `/users/{id}` | User | Delete a user |
| `GET` | `/users/{id}` | User | Get user by ID/Email |
| `PATCH` | `/users/{id}/role` | User | Change a user's global role |
| `GET` | `/variables` | Variables | Retrieve variables |
| `POST` | `/variables` | Variables | Create a variable |
| `DELETE` | `/variables/{id}` | Variables | Delete a variable |
| `PUT` | `/variables/{id}` | Variables | Update a variable |
| `GET` | `/workflows` | Workflow | Retrieve all workflows |
| `POST` | `/workflows` | Workflow | Create a workflow |
| `DELETE` | `/workflows/{id}` | Workflow | Delete a workflow |
| `GET` | `/workflows/{id}` | Workflow | Retrieves a workflow |
| `PUT` | `/workflows/{id}` | Workflow | Update a workflow |
| `POST` | `/workflows/{id}/activate` | Workflow | Activate a workflow |
| `POST` | `/workflows/{id}/deactivate` | Workflow | Deactivate a workflow |
| `GET` | `/workflows/{id}/tags` | Workflow | Get workflow tags |
| `PUT` | `/workflows/{id}/tags` | Workflow | Update tags of a workflow |
| `PUT` | `/workflows/{id}/transfer` | Workflow | Transfer a workflow to another project. |

### n8n Cloud operations (131)

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `POST` | `/audit` | Audit | Generate an audit |
| `GET` | `/community-packages` | CommunityPackage | List installed community packages |
| `POST` | `/community-packages` | CommunityPackage | Install a community package |
| `DELETE` | `/community-packages/{name}` | CommunityPackage | Uninstall a community package |
| `PATCH` | `/community-packages/{name}` | CommunityPackage | Update a community package |
| `GET` | `/credentials` | Credential | List credentials |
| `POST` | `/credentials` | Credential | Create a credential |
| `GET` | `/credentials/schema/{credentialTypeName}` | Credential | Show credential data schema |
| `DELETE` | `/credentials/{id}` | Credential | Delete credential by ID |
| `GET` | `/credentials/{id}` | Credential | Get credential by ID |
| `PATCH` | `/credentials/{id}` | Credential | Update credential by ID |
| `POST` | `/credentials/{id}/test` | Credential | Test credential by ID |
| `PUT` | `/credentials/{id}/transfer` | Credential | Transfer a credential to another project. |
| `GET` | `/data-tables` | DataTable | List all data tables |
| `POST` | `/data-tables` | DataTable | Create a new data table |
| `DELETE` | `/data-tables/{dataTableId}` | DataTable | Delete a data table |
| `GET` | `/data-tables/{dataTableId}` | DataTable | Get a data table |
| `PATCH` | `/data-tables/{dataTableId}` | DataTable | Update a data table |
| `GET` | `/data-tables/{dataTableId}/columns` | DataTable | List columns of a data table |
| `POST` | `/data-tables/{dataTableId}/columns` | DataTable | Add a column to a data table |
| `DELETE` | `/data-tables/{dataTableId}/columns/{columnId}` | DataTable | Delete a column |
| `PATCH` | `/data-tables/{dataTableId}/columns/{columnId}` | DataTable | Update a column |
| `GET` | `/data-tables/{dataTableId}/rows` | DataTable | Retrieve rows from a data table |
| `POST` | `/data-tables/{dataTableId}/rows` | DataTable | Insert rows into a data table |
| `DELETE` | `/data-tables/{dataTableId}/rows/clear` | DataTable | Clear all rows from a data table |
| `DELETE` | `/data-tables/{dataTableId}/rows/delete` | DataTable | Delete rows from a data table |
| `PATCH` | `/data-tables/{dataTableId}/rows/update` | DataTable | Update rows in a data table |
| `POST` | `/data-tables/{dataTableId}/rows/upsert` | DataTable | Upsert a row in a data table |
| `GET` | `/discover` | Discover | Discover available API capabilities |
| `GET` | `/workflows/{id}/test-runs` | Evaluation | Retrieve test runs |
| `POST` | `/workflows/{id}/test-runs` | Evaluation | Trigger a test run |
| `GET` | `/workflows/{id}/test-runs/{runId}` | Evaluation | Retrieve a test run |
| `POST` | `/workflows/{id}/test-runs/{runId}/cancel` | Evaluation | Cancel a test run |
| `GET` | `/workflows/{id}/test-runs/{runId}/test-cases` | Evaluation | Retrieve test run cases |
| `GET` | `/executions` | Execution | Retrieve all executions |
| `POST` | `/executions/stop` | Execution | Stop multiple executions |
| `DELETE` | `/executions/{id}` | Execution | Delete an execution |
| `GET` | `/executions/{id}` | Execution | Retrieve an execution |
| `POST` | `/executions/{id}/retry` | Execution | Retry an execution |
| `POST` | `/executions/{id}/stop` | Execution | Stop an execution |
| `GET` | `/executions/{id}/tags` | Execution | Get execution tags |
| `PUT` | `/executions/{id}/tags` | Execution | Update tags of an execution |
| `GET` | `/projects/{projectId}/folders` | Folders | Retrieve folders |
| `POST` | `/projects/{projectId}/folders` | Folders | Create a folder |
| `DELETE` | `/projects/{projectId}/folders/{folderId}` | Folders | Delete a folder |
| `GET` | `/projects/{projectId}/folders/{folderId}` | Folders | Get folder details |
| `PATCH` | `/projects/{projectId}/folders/{folderId}` | Folders | Update a folder |
| `GET` | `/git-connections` | GitConnections | List Git connections |
| `POST` | `/git-connections` | GitConnections | Create a Git connection |
| `DELETE` | `/git-connections/{id}` | GitConnections | Delete a Git connection |
| `GET` | `/git-connections/{id}` | GitConnections | Retrieve a Git connection |
| `PUT` | `/git-connections/{id}` | GitConnections | Update a Git connection |
| `POST` | `/git-connections/{id}/clone` | GitConnections | Clone a Git connection |
| `POST` | `/git-connections/{id}/disconnect` | GitConnections | Disconnect a Git connection |
| `GET` | `/git-connections/{id}/projects` | GitConnections | List projects added to a Git connection |
| `DELETE` | `/git-connections/{id}/projects/{projectId}` | GitConnections | Remove a project from a Git connection |
| `POST` | `/git-connections/{id}/projects/{projectId}` | GitConnections | Add a project to a Git connection |
| `POST` | `/git-connections/{id}/pull` | GitConnections | Import all projects from a Git connection working copy |
| `POST` | `/git-connections/{id}/push` | GitConnections | Push all team projects to a Git connection |
| `GET` | `/insights/summary` | Insights | Retrieve insights summary |
| `GET` | `/settings/log-streaming/destinations` | LogStreaming | List log streaming destinations |
| `POST` | `/settings/log-streaming/destinations` | LogStreaming | Create a log streaming destination |
| `DELETE` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Delete a log streaming destination |
| `GET` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Retrieve a log streaming destination |
| `PUT` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Update a log streaming destination |
| `POST` | `/settings/log-streaming/destinations/{id}/test` | LogStreaming | Send a test message to a log streaming destination |
| `GET` | `/settings/log-streaming/event-types` | LogStreaming | List streamable event types |
| `POST` | `/n8n-packages/export` | N8nPackage | Beta: Export workflows, folders, or projects as an n8n package |
| `POST` | `/n8n-packages/import` | N8nPackage | Beta: Import an n8n package into a project |
| `GET` | `/projects` | Projects | Retrieve projects |
| `POST` | `/projects` | Projects | Create a project |
| `DELETE` | `/projects/{projectId}` | Projects | Delete a project |
| `PUT` | `/projects/{projectId}` | Projects | Update a project |
| `GET` | `/projects/{projectId}/users` | Projects | List project members |
| `POST` | `/projects/{projectId}/users` | Projects | Add one or more users to a project |
| `DELETE` | `/projects/{projectId}/users/{userId}` | Projects | Delete a user from a project |
| `PATCH` | `/projects/{projectId}/users/{userId}` | Projects | Change a user's role in a project |
| `GET` | `/roles` | Role | Retrieve all roles |
| `POST` | `/roles` | Role | Create a custom role |
| `DELETE` | `/roles/{slug}` | Role | Delete a custom role |
| `GET` | `/roles/{slug}` | Role | Retrieve a role |
| `PUT` | `/roles/{slug}` | Role | Update a custom role |
| `GET` | `/role-mapping-rules` | RoleMappingRule | Retrieve role-mapping rules |
| `POST` | `/role-mapping-rules` | RoleMappingRule | Create a role-mapping rule |
| `DELETE` | `/role-mapping-rules/{roleMappingRuleId}` | RoleMappingRule | Delete a role-mapping rule |
| `PATCH` | `/role-mapping-rules/{roleMappingRuleId}` | RoleMappingRule | Update a role-mapping rule |
| `POST` | `/role-mapping-rules/{roleMappingRuleId}/move` | RoleMappingRule | Move a role-mapping rule |
| `GET` | `/settings/security-policy` | SecurityPolicy | Retrieve the security policy |
| `PUT` | `/settings/security-policy` | SecurityPolicy | Set the security policy |
| `GET` | `/settings/ldap` | SettingsLdap | Retrieve the LDAP configuration |
| `PUT` | `/settings/ldap` | SettingsLdap | Set the LDAP configuration |
| `GET` | `/settings/ldap/sync` | SettingsLdap | Retrieve LDAP synchronization history |
| `POST` | `/settings/ldap/sync` | SettingsLdap | Trigger an LDAP synchronization |
| `GET` | `/settings/otel` | SettingsOtel | Retrieve the OpenTelemetry configuration |
| `PUT` | `/settings/otel` | SettingsOtel | Set the OpenTelemetry configuration |
| `POST` | `/settings/otel/test-trace` | SettingsOtel | Test the connection to an OTLP collector |
| `GET` | `/settings/sso/oidc` | SettingsSsoOidc | Retrieve the OIDC SSO configuration |
| `PUT` | `/settings/sso/oidc` | SettingsSsoOidc | Set the OIDC SSO configuration |
| `GET` | `/settings/sso/saml` | SettingsSsoSaml | Retrieve the SAML SSO configuration |
| `PUT` | `/settings/sso/saml` | SettingsSsoSaml | Set the SAML SSO configuration |
| `POST` | `/source-control/pull` | SourceControl | Pull changes from the remote repository |
| `GET` | `/tags` | Tags | Retrieve all tags |
| `POST` | `/tags` | Tags | Create a tag |
| `DELETE` | `/tags/{id}` | Tags | Delete a tag |
| `GET` | `/tags/{id}` | Tags | Retrieves a tag |
| `PUT` | `/tags/{id}` | Tags | Update a tag |
| `GET` | `/users` | User | Retrieve all users |
| `POST` | `/users` | User | Create multiple users |
| `DELETE` | `/users/{id}` | User | Delete a user |
| `GET` | `/users/{id}` | User | Get user by ID/Email |
| `PATCH` | `/users/{id}/role` | User | Change a user's global role |
| `GET` | `/variables` | Variables | Retrieve variables |
| `POST` | `/variables` | Variables | Create a variable |
| `DELETE` | `/variables/{id}` | Variables | Delete a variable |
| `PUT` | `/variables/{id}` | Variables | Update a variable |
| `GET` | `/workflows` | Workflow | Retrieve all workflows |
| `POST` | `/workflows` | Workflow | Create a workflow |
| `GET` | `/workflows/{id}/{versionId}` | Workflow | Retrieves a specific version of a workflow |
| `DELETE` | `/workflows/{workflowId}` | Workflow | Delete a workflow |
| `GET` | `/workflows/{workflowId}` | Workflow | Retrieve a workflow |
| `PUT` | `/workflows/{workflowId}` | Workflow | Update a workflow |
| `POST` | `/workflows/{workflowId}/activate` | Workflow | Publish a workflow |
| `POST` | `/workflows/{workflowId}/archive` | Workflow | Archive a workflow |
| `POST` | `/workflows/{workflowId}/deactivate` | Workflow | Deactivate a workflow |
| `GET` | `/workflows/{workflowId}/history` | Workflow | Retrieve workflow version history |
| `POST` | `/workflows/{workflowId}/publish` | Workflow | Publish a workflow |
| `GET` | `/workflows/{workflowId}/tags` | Workflow | Get workflow tags |
| `PUT` | `/workflows/{workflowId}/tags` | Workflow | Update tags of a workflow |
| `PUT` | `/workflows/{workflowId}/transfer` | Workflow | Transfer a workflow to another project |
| `POST` | `/workflows/{workflowId}/unarchive` | Workflow | Unarchive a workflow |
| `POST` | `/workflows/{workflowId}/unpublish` | Workflow | Unpublish a workflow |

### Present on Cloud spec only (98)

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `GET` | `/community-packages` | CommunityPackage | List installed community packages |
| `POST` | `/community-packages` | CommunityPackage | Install a community package |
| `DELETE` | `/community-packages/{name}` | CommunityPackage | Uninstall a community package |
| `PATCH` | `/community-packages/{name}` | CommunityPackage | Update a community package |
| `GET` | `/credentials` | Credential | List credentials |
| `GET` | `/credentials/{id}` | Credential | Get credential by ID |
| `PATCH` | `/credentials/{id}` | Credential | Update credential by ID |
| `POST` | `/credentials/{id}/test` | Credential | Test credential by ID |
| `GET` | `/data-tables` | DataTable | List all data tables |
| `POST` | `/data-tables` | DataTable | Create a new data table |
| `DELETE` | `/data-tables/{dataTableId}` | DataTable | Delete a data table |
| `GET` | `/data-tables/{dataTableId}` | DataTable | Get a data table |
| `PATCH` | `/data-tables/{dataTableId}` | DataTable | Update a data table |
| `GET` | `/data-tables/{dataTableId}/columns` | DataTable | List columns of a data table |
| `POST` | `/data-tables/{dataTableId}/columns` | DataTable | Add a column to a data table |
| `DELETE` | `/data-tables/{dataTableId}/columns/{columnId}` | DataTable | Delete a column |
| `PATCH` | `/data-tables/{dataTableId}/columns/{columnId}` | DataTable | Update a column |
| `GET` | `/data-tables/{dataTableId}/rows` | DataTable | Retrieve rows from a data table |
| `POST` | `/data-tables/{dataTableId}/rows` | DataTable | Insert rows into a data table |
| `DELETE` | `/data-tables/{dataTableId}/rows/clear` | DataTable | Clear all rows from a data table |
| `DELETE` | `/data-tables/{dataTableId}/rows/delete` | DataTable | Delete rows from a data table |
| `PATCH` | `/data-tables/{dataTableId}/rows/update` | DataTable | Update rows in a data table |
| `POST` | `/data-tables/{dataTableId}/rows/upsert` | DataTable | Upsert a row in a data table |
| `GET` | `/discover` | Discover | Discover available API capabilities |
| `GET` | `/workflows/{id}/test-runs` | Evaluation | Retrieve test runs |
| `POST` | `/workflows/{id}/test-runs` | Evaluation | Trigger a test run |
| `GET` | `/workflows/{id}/test-runs/{runId}` | Evaluation | Retrieve a test run |
| `POST` | `/workflows/{id}/test-runs/{runId}/cancel` | Evaluation | Cancel a test run |
| `GET` | `/workflows/{id}/test-runs/{runId}/test-cases` | Evaluation | Retrieve test run cases |
| `POST` | `/executions/stop` | Execution | Stop multiple executions |
| `POST` | `/executions/{id}/stop` | Execution | Stop an execution |
| `GET` | `/executions/{id}/tags` | Execution | Get execution tags |
| `PUT` | `/executions/{id}/tags` | Execution | Update tags of an execution |
| `GET` | `/projects/{projectId}/folders` | Folders | Retrieve folders |
| `POST` | `/projects/{projectId}/folders` | Folders | Create a folder |
| `DELETE` | `/projects/{projectId}/folders/{folderId}` | Folders | Delete a folder |
| `GET` | `/projects/{projectId}/folders/{folderId}` | Folders | Get folder details |
| `PATCH` | `/projects/{projectId}/folders/{folderId}` | Folders | Update a folder |
| `GET` | `/git-connections` | GitConnections | List Git connections |
| `POST` | `/git-connections` | GitConnections | Create a Git connection |
| `DELETE` | `/git-connections/{id}` | GitConnections | Delete a Git connection |
| `GET` | `/git-connections/{id}` | GitConnections | Retrieve a Git connection |
| `PUT` | `/git-connections/{id}` | GitConnections | Update a Git connection |
| `POST` | `/git-connections/{id}/clone` | GitConnections | Clone a Git connection |
| `POST` | `/git-connections/{id}/disconnect` | GitConnections | Disconnect a Git connection |
| `GET` | `/git-connections/{id}/projects` | GitConnections | List projects added to a Git connection |
| `DELETE` | `/git-connections/{id}/projects/{projectId}` | GitConnections | Remove a project from a Git connection |
| `POST` | `/git-connections/{id}/projects/{projectId}` | GitConnections | Add a project to a Git connection |
| `POST` | `/git-connections/{id}/pull` | GitConnections | Import all projects from a Git connection working copy |
| `POST` | `/git-connections/{id}/push` | GitConnections | Push all team projects to a Git connection |
| `GET` | `/insights/summary` | Insights | Retrieve insights summary |
| `GET` | `/settings/log-streaming/destinations` | LogStreaming | List log streaming destinations |
| `POST` | `/settings/log-streaming/destinations` | LogStreaming | Create a log streaming destination |
| `DELETE` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Delete a log streaming destination |
| `GET` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Retrieve a log streaming destination |
| `PUT` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Update a log streaming destination |
| `POST` | `/settings/log-streaming/destinations/{id}/test` | LogStreaming | Send a test message to a log streaming destination |
| `GET` | `/settings/log-streaming/event-types` | LogStreaming | List streamable event types |
| `POST` | `/n8n-packages/export` | N8nPackage | Beta: Export workflows, folders, or projects as an n8n package |
| `POST` | `/n8n-packages/import` | N8nPackage | Beta: Import an n8n package into a project |
| `GET` | `/projects/{projectId}/users` | Projects | List project members |
| `GET` | `/roles` | Role | Retrieve all roles |
| `POST` | `/roles` | Role | Create a custom role |
| `DELETE` | `/roles/{slug}` | Role | Delete a custom role |
| `GET` | `/roles/{slug}` | Role | Retrieve a role |
| `PUT` | `/roles/{slug}` | Role | Update a custom role |
| `GET` | `/role-mapping-rules` | RoleMappingRule | Retrieve role-mapping rules |
| `POST` | `/role-mapping-rules` | RoleMappingRule | Create a role-mapping rule |
| `DELETE` | `/role-mapping-rules/{roleMappingRuleId}` | RoleMappingRule | Delete a role-mapping rule |
| `PATCH` | `/role-mapping-rules/{roleMappingRuleId}` | RoleMappingRule | Update a role-mapping rule |
| `POST` | `/role-mapping-rules/{roleMappingRuleId}/move` | RoleMappingRule | Move a role-mapping rule |
| `GET` | `/settings/security-policy` | SecurityPolicy | Retrieve the security policy |
| `PUT` | `/settings/security-policy` | SecurityPolicy | Set the security policy |
| `GET` | `/settings/ldap` | SettingsLdap | Retrieve the LDAP configuration |
| `PUT` | `/settings/ldap` | SettingsLdap | Set the LDAP configuration |
| `GET` | `/settings/ldap/sync` | SettingsLdap | Retrieve LDAP synchronization history |
| `POST` | `/settings/ldap/sync` | SettingsLdap | Trigger an LDAP synchronization |
| `GET` | `/settings/otel` | SettingsOtel | Retrieve the OpenTelemetry configuration |
| `PUT` | `/settings/otel` | SettingsOtel | Set the OpenTelemetry configuration |
| `POST` | `/settings/otel/test-trace` | SettingsOtel | Test the connection to an OTLP collector |
| `GET` | `/settings/sso/oidc` | SettingsSsoOidc | Retrieve the OIDC SSO configuration |
| `PUT` | `/settings/sso/oidc` | SettingsSsoOidc | Set the OIDC SSO configuration |
| `GET` | `/settings/sso/saml` | SettingsSsoSaml | Retrieve the SAML SSO configuration |
| `PUT` | `/settings/sso/saml` | SettingsSsoSaml | Set the SAML SSO configuration |
| `GET` | `/workflows/{id}/{versionId}` | Workflow | Retrieves a specific version of a workflow |
| `DELETE` | `/workflows/{workflowId}` | Workflow | Delete a workflow |
| `GET` | `/workflows/{workflowId}` | Workflow | Retrieve a workflow |
| `PUT` | `/workflows/{workflowId}` | Workflow | Update a workflow |
| `POST` | `/workflows/{workflowId}/activate` | Workflow | Publish a workflow |
| `POST` | `/workflows/{workflowId}/archive` | Workflow | Archive a workflow |
| `POST` | `/workflows/{workflowId}/deactivate` | Workflow | Deactivate a workflow |
| `GET` | `/workflows/{workflowId}/history` | Workflow | Retrieve workflow version history |
| `POST` | `/workflows/{workflowId}/publish` | Workflow | Publish a workflow |
| `GET` | `/workflows/{workflowId}/tags` | Workflow | Get workflow tags |
| `PUT` | `/workflows/{workflowId}/tags` | Workflow | Update tags of a workflow |
| `PUT` | `/workflows/{workflowId}/transfer` | Workflow | Transfer a workflow to another project |
| `POST` | `/workflows/{workflowId}/unarchive` | Workflow | Unarchive a workflow |
| `POST` | `/workflows/{workflowId}/unpublish` | Workflow | Unpublish a workflow |

### Present on RaceCS spec only (8)

These are the same workflow routes using `{id}` instead of `{workflowId}`.

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `DELETE` | `/workflows/{id}` | Workflow | Delete a workflow |
| `GET` | `/workflows/{id}` | Workflow | Retrieves a workflow |
| `PUT` | `/workflows/{id}` | Workflow | Update a workflow |
| `POST` | `/workflows/{id}/activate` | Workflow | Activate a workflow |
| `POST` | `/workflows/{id}/deactivate` | Workflow | Deactivate a workflow |
| `GET` | `/workflows/{id}/tags` | Workflow | Get workflow tags |
| `PUT` | `/workflows/{id}/tags` | Workflow | Update tags of a workflow |
| `PUT` | `/workflows/{id}/transfer` | Workflow | Transfer a workflow to another project. |

---


## Similar n8n documentation links

Seed page: https://docs.n8n.io/connect/n8n-api/

n8n publishes a full index at https://docs.n8n.io/sitemap.md and markdown for every page by appending `.md`. Copied 87 pages on 2026-09-06.


### Connect overview / CLI / MCP

- [mcp servers](https://docs.n8n.io/build/integrate-ai/mcp-servers) — markdown: https://docs.n8n.io/build/integrate-ai/mcp-servers.md — local: `pages/build/integrate-ai/mcp-servers.md`
- [connect to n8n mcp server](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server) — markdown: https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server.md — local: `pages/build/ways-of-building-workflows/connect-to-n8n-mcp-server.md`
- [connect to n8n docs mcp server](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server) — markdown: https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server.md — local: `pages/connect/connect-to-n8n-docs-mcp-server.md`
- [mcp client examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples) — markdown: https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples.md — local: `pages/connect/connect-to-n8n-mcp-server/mcp-client-examples.md`
- [mcp server tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) — markdown: https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference.md — local: `pages/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference.md`
- [connect to n8n mcp server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) — markdown: https://docs.n8n.io/connect/connect-to-n8n-mcp-server.md — local: `pages/connect/connect-to-n8n-mcp-server.md`
- [n8n cli](https://docs.n8n.io/connect/n8n-cli) — markdown: https://docs.n8n.io/connect/n8n-cli.md — local: `pages/connect/n8n-cli.md`
- [readme](https://docs.n8n.io/connect/readme) — markdown: https://docs.n8n.io/connect/readme.md — local: `pages/connect/readme.md`

### n8n Public API (guides)

- [api reference](https://docs.n8n.io/connect/n8n-api/api-reference) — markdown: https://docs.n8n.io/connect/n8n-api/api-reference.md — local: `pages/connect/n8n-api/api-reference.md`
- [authentication](https://docs.n8n.io/connect/n8n-api/authentication) — markdown: https://docs.n8n.io/connect/n8n-api/authentication.md — local: `pages/connect/n8n-api/authentication.md`
- [models](https://docs.n8n.io/connect/n8n-api/models) — markdown: https://docs.n8n.io/connect/n8n-api/models.md — local: `pages/connect/n8n-api/models.md`
- [pagination](https://docs.n8n.io/connect/n8n-api/pagination) — markdown: https://docs.n8n.io/connect/n8n-api/pagination.md — local: `pages/connect/n8n-api/pagination.md`
- [use an api playground](https://docs.n8n.io/connect/n8n-api/use-an-api-playground) — markdown: https://docs.n8n.io/connect/n8n-api/use-an-api-playground.md — local: `pages/connect/n8n-api/use-an-api-playground.md`
- [n8n api](https://docs.n8n.io/connect/n8n-api) — markdown: https://docs.n8n.io/connect/n8n-api.md — local: `pages/connect/n8n-api.md`

### n8n Public API (resource reference)

- [audit](https://docs.n8n.io/connect/n8n-api/audit) — markdown: https://docs.n8n.io/connect/n8n-api/audit.md — local: `pages/connect/n8n-api/audit.md`
- [community package](https://docs.n8n.io/connect/n8n-api/community-package) — markdown: https://docs.n8n.io/connect/n8n-api/community-package.md — local: `pages/connect/n8n-api/community-package.md`
- [credential](https://docs.n8n.io/connect/n8n-api/credential) — markdown: https://docs.n8n.io/connect/n8n-api/credential.md — local: `pages/connect/n8n-api/credential.md`
- [data table](https://docs.n8n.io/connect/n8n-api/data-table) — markdown: https://docs.n8n.io/connect/n8n-api/data-table.md — local: `pages/connect/n8n-api/data-table.md`
- [discover](https://docs.n8n.io/connect/n8n-api/discover) — markdown: https://docs.n8n.io/connect/n8n-api/discover.md — local: `pages/connect/n8n-api/discover.md`
- [evaluation](https://docs.n8n.io/connect/n8n-api/evaluation) — markdown: https://docs.n8n.io/connect/n8n-api/evaluation.md — local: `pages/connect/n8n-api/evaluation.md`
- [execution](https://docs.n8n.io/connect/n8n-api/execution) — markdown: https://docs.n8n.io/connect/n8n-api/execution.md — local: `pages/connect/n8n-api/execution.md`
- [folders](https://docs.n8n.io/connect/n8n-api/folders) — markdown: https://docs.n8n.io/connect/n8n-api/folders.md — local: `pages/connect/n8n-api/folders.md`
- [git connections](https://docs.n8n.io/connect/n8n-api/git-connections) — markdown: https://docs.n8n.io/connect/n8n-api/git-connections.md — local: `pages/connect/n8n-api/git-connections.md`
- [insights](https://docs.n8n.io/connect/n8n-api/insights) — markdown: https://docs.n8n.io/connect/n8n-api/insights.md — local: `pages/connect/n8n-api/insights.md`
- [log streaming](https://docs.n8n.io/connect/n8n-api/log-streaming) — markdown: https://docs.n8n.io/connect/n8n-api/log-streaming.md — local: `pages/connect/n8n-api/log-streaming.md`
- [n8n package](https://docs.n8n.io/connect/n8n-api/n8n-package) — markdown: https://docs.n8n.io/connect/n8n-api/n8n-package.md — local: `pages/connect/n8n-api/n8n-package.md`
- [projects](https://docs.n8n.io/connect/n8n-api/projects) — markdown: https://docs.n8n.io/connect/n8n-api/projects.md — local: `pages/connect/n8n-api/projects.md`
- [role mapping rule](https://docs.n8n.io/connect/n8n-api/role-mapping-rule) — markdown: https://docs.n8n.io/connect/n8n-api/role-mapping-rule.md — local: `pages/connect/n8n-api/role-mapping-rule.md`
- [role](https://docs.n8n.io/connect/n8n-api/role) — markdown: https://docs.n8n.io/connect/n8n-api/role.md — local: `pages/connect/n8n-api/role.md`
- [security policy](https://docs.n8n.io/connect/n8n-api/security-policy) — markdown: https://docs.n8n.io/connect/n8n-api/security-policy.md — local: `pages/connect/n8n-api/security-policy.md`
- [settings ldap](https://docs.n8n.io/connect/n8n-api/settings-ldap) — markdown: https://docs.n8n.io/connect/n8n-api/settings-ldap.md — local: `pages/connect/n8n-api/settings-ldap.md`
- [settings otel](https://docs.n8n.io/connect/n8n-api/settings-otel) — markdown: https://docs.n8n.io/connect/n8n-api/settings-otel.md — local: `pages/connect/n8n-api/settings-otel.md`
- [settings sso oidc](https://docs.n8n.io/connect/n8n-api/settings-sso-oidc) — markdown: https://docs.n8n.io/connect/n8n-api/settings-sso-oidc.md — local: `pages/connect/n8n-api/settings-sso-oidc.md`
- [settings sso saml](https://docs.n8n.io/connect/n8n-api/settings-sso-saml) — markdown: https://docs.n8n.io/connect/n8n-api/settings-sso-saml.md — local: `pages/connect/n8n-api/settings-sso-saml.md`
- [source control](https://docs.n8n.io/connect/n8n-api/source-control) — markdown: https://docs.n8n.io/connect/n8n-api/source-control.md — local: `pages/connect/n8n-api/source-control.md`
- [tags](https://docs.n8n.io/connect/n8n-api/tags) — markdown: https://docs.n8n.io/connect/n8n-api/tags.md — local: `pages/connect/n8n-api/tags.md`
- [user](https://docs.n8n.io/connect/n8n-api/user) — markdown: https://docs.n8n.io/connect/n8n-api/user.md — local: `pages/connect/n8n-api/user.md`
- [variables](https://docs.n8n.io/connect/n8n-api/variables) — markdown: https://docs.n8n.io/connect/n8n-api/variables.md — local: `pages/connect/n8n-api/variables.md`
- [workflow](https://docs.n8n.io/connect/n8n-api/workflow) — markdown: https://docs.n8n.io/connect/n8n-api/workflow.md — local: `pages/connect/n8n-api/workflow.md`

### Create custom nodes

- [declarative style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters.md — local: `pages/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters.md`
- [programmatic style execute method](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method.md — local: `pages/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method.md`
- [programmatic style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters.md — local: `pages/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters.md`
- [standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters.md — local: `pages/connect/create-nodes/build-your-node/reference/base-files/standard-parameters.md`
- [structure](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure.md — local: `pages/connect/create-nodes/build-your-node/reference/base-files/structure.md`
- [base files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files.md — local: `pages/connect/create-nodes/build-your-node/reference/base-files.md`
- [code standards](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/code-standards) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/code-standards.md — local: `pages/connect/create-nodes/build-your-node/reference/code-standards.md`
- [codex files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/codex-files) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/codex-files.md — local: `pages/connect/create-nodes/build-your-node/reference/codex-files.md`
- [credentials files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files.md — local: `pages/connect/create-nodes/build-your-node/reference/credentials-files.md`
- [error handling](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/error-handling) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/error-handling.md — local: `pages/connect/create-nodes/build-your-node/reference/error-handling.md`
- [http request helpers](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/http-request-helpers) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/http-request-helpers.md — local: `pages/connect/create-nodes/build-your-node/reference/http-request-helpers.md`
- [item linking](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/item-linking) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/item-linking.md — local: `pages/connect/create-nodes/build-your-node/reference/item-linking.md`
- [node ui elements](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements.md — local: `pages/connect/create-nodes/build-your-node/reference/node-ui-elements.md`
- [ux guidelines](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/ux-guidelines) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/ux-guidelines.md — local: `pages/connect/create-nodes/build-your-node/reference/ux-guidelines.md`
- [verification guidelines](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/verification-guidelines) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/verification-guidelines.md — local: `pages/connect/create-nodes/build-your-node/reference/verification-guidelines.md`
- [versioning](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning.md — local: `pages/connect/create-nodes/build-your-node/reference/versioning.md`
- [reference](https://docs.n8n.io/connect/create-nodes/build-your-node/reference) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/reference.md — local: `pages/connect/create-nodes/build-your-node/reference.md`
- [set up your development environment](https://docs.n8n.io/connect/create-nodes/build-your-node/set-up-your-development-environment) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/set-up-your-development-environment.md — local: `pages/connect/create-nodes/build-your-node/set-up-your-development-environment.md`
- [tutorial build a declarative style node](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node.md — local: `pages/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node.md`
- [tutorial build a programmatic style node](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node.md — local: `pages/connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node.md`
- [using the n8n node tool](https://docs.n8n.io/connect/create-nodes/build-your-node/using-the-n8n-node-tool) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node/using-the-n8n-node-tool.md — local: `pages/connect/create-nodes/build-your-node/using-the-n8n-node-tool.md`
- [build your node](https://docs.n8n.io/connect/create-nodes/build-your-node) — markdown: https://docs.n8n.io/connect/create-nodes/build-your-node.md — local: `pages/connect/create-nodes/build-your-node.md`
- [install private nodes](https://docs.n8n.io/connect/create-nodes/deploy-your-node/install-private-nodes) — markdown: https://docs.n8n.io/connect/create-nodes/deploy-your-node/install-private-nodes.md — local: `pages/connect/create-nodes/deploy-your-node/install-private-nodes.md`
- [submit community nodes](https://docs.n8n.io/connect/create-nodes/deploy-your-node/submit-community-nodes) — markdown: https://docs.n8n.io/connect/create-nodes/deploy-your-node/submit-community-nodes.md — local: `pages/connect/create-nodes/deploy-your-node/submit-community-nodes.md`
- [deploy your node](https://docs.n8n.io/connect/create-nodes/deploy-your-node) — markdown: https://docs.n8n.io/connect/create-nodes/deploy-your-node.md — local: `pages/connect/create-nodes/deploy-your-node.md`
- [overview](https://docs.n8n.io/connect/create-nodes/overview) — markdown: https://docs.n8n.io/connect/create-nodes/overview.md — local: `pages/connect/create-nodes/overview.md`
- [choose a node building style](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-building-style) — markdown: https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-building-style.md — local: `pages/connect/create-nodes/plan-your-node/choose-a-node-building-style.md`
- [choose a node type](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-type) — markdown: https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-type.md — local: `pages/connect/create-nodes/plan-your-node/choose-a-node-type.md`
- [choose node file structure](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-node-file-structure) — markdown: https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-node-file-structure.md — local: `pages/connect/create-nodes/plan-your-node/choose-node-file-structure.md`
- [node ui design](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design) — markdown: https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design.md — local: `pages/connect/create-nodes/plan-your-node/node-ui-design.md`
- [plan your node](https://docs.n8n.io/connect/create-nodes/plan-your-node) — markdown: https://docs.n8n.io/connect/create-nodes/plan-your-node.md — local: `pages/connect/create-nodes/plan-your-node.md`
- [node linter](https://docs.n8n.io/connect/create-nodes/test-your-node/node-linter) — markdown: https://docs.n8n.io/connect/create-nodes/test-your-node/node-linter.md — local: `pages/connect/create-nodes/test-your-node/node-linter.md`
- [run your node locally](https://docs.n8n.io/connect/create-nodes/test-your-node/run-your-node-locally) — markdown: https://docs.n8n.io/connect/create-nodes/test-your-node/run-your-node-locally.md — local: `pages/connect/create-nodes/test-your-node/run-your-node-locally.md`
- [troubleshooting](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting) — markdown: https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting.md — local: `pages/connect/create-nodes/test-your-node/troubleshooting.md`
- [test your node](https://docs.n8n.io/connect/create-nodes/test-your-node) — markdown: https://docs.n8n.io/connect/create-nodes/test-your-node.md — local: `pages/connect/create-nodes/test-your-node.md`
- [create nodes](https://docs.n8n.io/connect/create-nodes) — markdown: https://docs.n8n.io/connect/create-nodes.md — local: `pages/connect/create-nodes.md`

### n8n packages

- [export a package](https://docs.n8n.io/build/manage-workflows/n8n-packages/export-a-package) — markdown: https://docs.n8n.io/build/manage-workflows/n8n-packages/export-a-package.md — local: `pages/build/manage-workflows/n8n-packages/export-a-package.md`
- [how import works](https://docs.n8n.io/build/manage-workflows/n8n-packages/how-import-works) — markdown: https://docs.n8n.io/build/manage-workflows/n8n-packages/how-import-works.md — local: `pages/build/manage-workflows/n8n-packages/how-import-works.md`
- [import a package](https://docs.n8n.io/build/manage-workflows/n8n-packages/import-a-package) — markdown: https://docs.n8n.io/build/manage-workflows/n8n-packages/import-a-package.md — local: `pages/build/manage-workflows/n8n-packages/import-a-package.md`
- [limits and permissions](https://docs.n8n.io/build/manage-workflows/n8n-packages/limits-and-permissions) — markdown: https://docs.n8n.io/build/manage-workflows/n8n-packages/limits-and-permissions.md — local: `pages/build/manage-workflows/n8n-packages/limits-and-permissions.md`
- [package format](https://docs.n8n.io/build/manage-workflows/n8n-packages/package-format) — markdown: https://docs.n8n.io/build/manage-workflows/n8n-packages/package-format.md — local: `pages/build/manage-workflows/n8n-packages/package-format.md`
- [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages) — markdown: https://docs.n8n.io/build/manage-workflows/n8n-packages.md — local: `pages/build/manage-workflows/n8n-packages.md`

### Instance / hosting

- [configure the base url](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url) — markdown: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url.md — local: `pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url.md`
- [endpoints](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints) — markdown: https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md — local: `pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md`
- [manage settings using environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables) — markdown: https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables.md — local: `pages/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables.md`
- [use the command line](https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line) — markdown: https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line.md — local: `pages/deploy/host-n8n/configure-n8n/use-the-command-line.md`

### Built-in nodes

- [n8n nodes base.n8n](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n) — markdown: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md — local: `pages/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md`
- [n8n nodes base.n8ntrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger) — markdown: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md — local: `pages/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md`

### Live API specs and playgrounds

- Our instance Swagger UI: https://n8n.racecs.com/api/v1/docs/
- Our instance OpenAPI: https://n8n.racecs.com/api/v1/openapi.yml
- n8n Cloud internal OpenAPI: https://internal.users.n8n.cloud/api/v1/openapi.yml
- GitHub source (split $ref spec): https://github.com/n8n-io/n8n/blob/master/packages/cli/src/public-api/v1/openapi.yml
- Official docs MCP index: https://docs.n8n.io/llms.txt
- Official docs sitemap: https://docs.n8n.io/sitemap.md
- Full docs corpus: https://docs.n8n.io/llms-full.txt

---


## Documentation page index

Complete catalog of **1343** official pages copied into `docs/n8n/pages/`. Generated from https://docs.n8n.io/sitemap.md.

### Get started

| Page | Local copy | Official |
| --- | --- | --- |
| n8n Docs — Get set up on n8n, build your first workflow, and find inspiration for what to automate. | [`welcome.md`](pages/welcome.md) | [docs](https://docs.n8n.io/welcome) |
| Choose how to use n8n — Choose between n8n Cloud and self-hosting, and learn about licenses and plans. | [`choose-how-to-use-n8n.md`](pages/choose-how-to-use-n8n.md) | [docs](https://docs.n8n.io/choose-how-to-use-n8n) |
| Build your first workflow — Create your first workflow in n8n and learn some key concepts. | [`build-your-first-workflow.md`](pages/build-your-first-workflow.md) | [docs](https://docs.n8n.io/build-your-first-workflow) |
| Learning paths — Interactive courses to learn n8n through hands-on exercises, quizzes, and real workflow building. | [`learning-paths.md`](pages/learning-paths.md) | [docs](https://docs.n8n.io/learning-paths) |
| Key concept glossary — A glossary of terms commonly used when working with n8n and related software. | [`key-concept-glossary.md`](pages/key-concept-glossary.md) | [docs](https://docs.n8n.io/key-concept-glossary) |

### Deploy

| Page | Local copy | Official |
| --- | --- | --- |
| Deploy — Deploy n8n on n8n Cloud or self-host it, and find guides for installing, configuring, and maintaining your instance. | [`deploy/readme.md`](pages/deploy/readme.md) | [docs](https://docs.n8n.io/deploy/readme) |
| Use n8n Cloud — Manage your n8n Cloud trial, plan, and instance, including the admin dashboard and updates. | [`deploy/use-n8n-cloud.md`](pages/deploy/use-n8n-cloud.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud) |
| Try free then choose a plan — Start a free n8n Cloud trial, then compare the Starter, Pro, and Enterprise plans to choose the right one. | [`deploy/use-n8n-cloud/start-your-free-trial.md`](pages/deploy/use-n8n-cloud/start-your-free-trial.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/start-your-free-trial) |
| Use the admin dashboard — How to access the Cloud admin dashboard. | [`deploy/use-n8n-cloud/use-the-admin-dashboard.md`](pages/deploy/use-n8n-cloud/use-the-admin-dashboard.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/use-the-admin-dashboard) |
| Update your version — How to update your n8n version on Cloud. | [`deploy/use-n8n-cloud/update-your-version.md`](pages/deploy/use-n8n-cloud/update-your-version.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/update-your-version) |
| Configure Cloud | [`deploy/use-n8n-cloud/configure-cloud.md`](pages/deploy/use-n8n-cloud/configure-cloud.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud) |
| Set your timezone — How to set your timezone on n8n Cloud. | [`deploy/use-n8n-cloud/configure-cloud/set-your-timezone.md`](pages/deploy/use-n8n-cloud/configure-cloud/set-your-timezone.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/set-your-timezone) |
| Find your IP addresses | [`deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses.md`](pages/deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/find-your-ip-addresses) |
| Manage your data — How to manage your data on n8n Cloud. | [`deploy/use-n8n-cloud/configure-cloud/manage-your-data.md`](pages/deploy/use-n8n-cloud/configure-cloud/manage-your-data.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data) |
| Change instance ownership or username | [`deploy/use-n8n-cloud/configure-cloud/change-instance-ownership-or-username.md`](pages/deploy/use-n8n-cloud/configure-cloud/change-instance-ownership-or-username.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/change-instance-ownership-or-username) |
| Understand concurrency | [`deploy/use-n8n-cloud/understand-concurrency.md`](pages/deploy/use-n8n-cloud/understand-concurrency.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency) |
| Gateway credits — Use Gateway credits to run AI models and third-party services in your n8n workflows without provider accounts or API keys. | [`deploy/use-n8n-cloud/gateway-credits.md`](pages/deploy/use-n8n-cloud/gateway-credits.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits) |
| Top up Gateway credits — Add credit to your Gateway credits balance manually or with auto top-up in the n8n Cloud admin dashboard. | [`deploy/use-n8n-cloud/gateway-credits/top-up-gateway-credits.md`](pages/deploy/use-n8n-cloud/gateway-credits/top-up-gateway-credits.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits/top-up-gateway-credits) |
| Track Gateway credit spend — Monitor your Gateway credits balance, spend by model or workflow, and top-up history in the n8n Cloud admin dashboard. | [`deploy/use-n8n-cloud/gateway-credits/track-gateway-credit-spend.md`](pages/deploy/use-n8n-cloud/gateway-credits/track-gateway-credit-spend.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits/track-gateway-credit-spend) |
| Download workflows — How to download workflows from n8n Cloud with the admin dashboard. | [`deploy/use-n8n-cloud/download-workflows.md`](pages/deploy/use-n8n-cloud/download-workflows.md) | [docs](https://docs.n8n.io/deploy/use-n8n-cloud/download-workflows) |
| Host n8n — Access n8n hosting documentation and guides for setting up and managing self-hosted n8n instances. | [`deploy/host-n8n.md`](pages/deploy/host-n8n.md) | [docs](https://docs.n8n.io/deploy/host-n8n) |
| Install options — Compare ways to install self-hosted n8n, including one-line setup, Docker, Docker Compose, npm, and cloud providers. | [`deploy/host-n8n/install-options.md`](pages/deploy/host-n8n/install-options.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options) |
| One-line setup — Install n8n from the command line using a one-line setup. | [`deploy/host-n8n/install-options/one-line-setup.md`](pages/deploy/host-n8n/install-options/one-line-setup.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup) |
| Install using Docker Compose — Build a Docker Compose setup for self-hosted n8n, including the sandbox stack for the AI Assistant. | [`deploy/host-n8n/install-options/install-using-docker-compose.md`](pages/deploy/host-n8n/install-options/install-using-docker-compose.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose) |
| Install with npm | [`deploy/host-n8n/install-options/install-with-npm.md`](pages/deploy/host-n8n/install-options/install-with-npm.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm) |
| Install with Docker | [`deploy/host-n8n/install-options/install-with-docker.md`](pages/deploy/host-n8n/install-options/install-with-docker.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) |
| Use a cloud provider — Deploy self-hosted n8n to a cloud provider, including DigitalOcean, AWS, Azure, and Google Cloud. | [`deploy/host-n8n/install-options/use-a-cloud-provider.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider) |
| Deploy to Digital Ocean | [`deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-digital-ocean) |
| Deploy to Heroku | [`deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-heroku) |
| Deploy to Hetzner | [`deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-hetzner) |
| Deploy to AWS | [`deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-aws) |
| Deploy to Azure | [`deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-azure) |
| Deploy to Google Cloud Run | [`deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run) |
| Deploy to Google Kubernetes | [`deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-kubernetes) |
| Deploy to OpenShift Local (CRC) | [`deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-openshift-local-crc) |
| Use Docker Compose — Install and run n8n using Docker Compose | [`deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose.md`](pages/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose.md) | [docs](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose) |
| Configure n8n — Configure a self-hosted n8n instance, including database, security, scaling, and license settings. | [`deploy/host-n8n/configure-n8n.md`](pages/deploy/host-n8n/configure-n8n.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n) |
| Basic configuration — How to set environment variables for n8n. | [`deploy/host-n8n/configure-n8n/basic-configuration.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration) |
| Use environment variables — An overview of configuration environment variables for self-hosted n8n. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables) |
| Ask n8n AI — Environment variables to configure Ask n8n AI. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ai-assistant) |
| Binary data — Customize binary data storage modes and paths with environment variables for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data) |
| Credentials — Manage default credentials and override them through environment variables your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/credentials) |
| Database — Set up and configure databases with environment variables for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/database) |
| Deployment — Configure deployment options and application accessibility with environment variables for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment) |
| Endpoints — Customize the application's API and webhook endpoints with environment variables for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints) |
| Executions — Environment variables to configure settings related to workflow executions. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions) |
| Expression engine — Configure the expression evaluation engine and its V8 isolate pool for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/expression-engine.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/expression-engine.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/expression-engine) |
| External data storage — Environment variables to configure external data storage for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-data-storage) |
| External hooks — Environment variables to integrate external hooks into your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks) |
| External secrets — Configure the interval for checking updates to external secrets in self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-secrets) |
| Insights — Configure insights metrics collection with environment variables for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/insights) |
| Logs — Environment variables to configure logging and diagnostic data. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs) |
| License — Environment variables to configure license settings in n8n, including options to hide the usage page, manage license activation and auto-renewal settings, and specify the server URL for license retrie | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/license.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/license.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/license) |
| Nodes — Environment variables to configure nodes management and node-specific limits in self-hosted n8n. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes) |
| OpenTelemetry — Configure OpenTelemetry tracing with environment variables for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/opentelemetry) |
| Queue mode — Environment variables to configure queue mode on your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/queue-mode.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/queue-mode.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/queue-mode) |
| Scheduler — Environment variables to configure the durable scheduler for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/scheduler.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/scheduler.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/scheduler) |
| Security — Configure authentication and environment variable access in self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security) |
| Source control — Environment variable to set the default SSH key type for source control setup. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/source-control) |
| SSO — Configure single sign-on for self-hosted n8n using environment variables. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/sso) |
| SSRF protection — Configure SSRF protection for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection) |
| Task runners — Environment variables to confgure task runners your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners) |
| Timezone and localization — Set the timezone and default language locale for self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization) |
| User management and 2FA — Environment variables to set up user management and emails. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa) |
| Workflows — Environment variables to configure workflows in n8n, including default naming, onboarding flow preferences, tag management, and caller policy settings. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflows) |
| Workflow history — Environment variables to configure workflow history in n8n. | [`deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/workflow-history) |
| Configuration examples — An overview containing different configuration examples. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples) |
| Isolate n8n — Prevent your n8n instance from connecting with n8n's servers. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n) |
| Configure the Base URL — Configure the Base URL environment variable to define the front end's access path to the back end's REST API for n8n. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-the-base-url) |
| Configure custom SSL certificate authorities — Customize the n8n container to work with self signed certificates when connecting to services. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-custom-ssl-certificate-authorities) |
| Set a custom encryption key — Set a custom encryption key for n8n to securely encrypt credentials. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key) |
| Configure workflow timeouts — Set execution timeouts to determine how long workflows can run. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-workflow-timeouts.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-workflow-timeouts.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-workflow-timeouts) |
| Specify custom nodes location — Add folders and specify paths for your custom nodes. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-custom-nodes-location.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-custom-nodes-location.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-custom-nodes-location) |
| Enable modules in Code node — Allow the use of both built-in and external modules within the Code node. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-modules-in-code-node) |
| Set the timezone — Change the default timezone for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-the-timezone) |
| Specify user folder path — Specify location of the folder that stores user-specific data. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-user-folder-path.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-user-folder-path.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-user-folder-path) |
| Configure webhook URLs with reverse proxy — Customize n8n webhook URLs for compatibility with reverse proxy setups. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy) |
| Enable Prometheus metrics — Enable Prometheus metrics endpoint. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics) |
| Pre-configure Microsoft OAuth credentials — Use credential overwrites to pre-configure Microsoft OAuth2 credentials in n8n so users can connect without their own app registration. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/pre-configure-microsoft-oauth-credentials.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/pre-configure-microsoft-oauth-credentials.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/pre-configure-microsoft-oauth-credentials) |
| Configure a custom workflow templates library — Set up a custom workflow template library for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library.md`](pages/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library) |
| Choose n8n's database | [`deploy/host-n8n/configure-n8n/choose-n8ns-database.md`](pages/deploy/host-n8n/configure-n8n/choose-n8ns-database.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database) |
| External hooks — Use external hooks to execute custom code whenever n8n runs a specific operation. | [`deploy/host-n8n/configure-n8n/external-hooks.md`](pages/deploy/host-n8n/configure-n8n/external-hooks.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/external-hooks) |
| Use the command line — Commands available in the Server CLI, the built-in n8n command-line interface. | [`deploy/host-n8n/configure-n8n/use-the-command-line.md`](pages/deploy/host-n8n/configure-n8n/use-the-command-line.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line) |
| User management — Configure self-hosted n8n for user management | [`deploy/host-n8n/configure-n8n/user-management.md`](pages/deploy/host-n8n/configure-n8n/user-management.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management) |
| Change instance owner email — Change the owner email address for a self-hosted n8n instance using the UI or environment variables. | [`deploy/host-n8n/configure-n8n/change-instance-owner-email.md`](pages/deploy/host-n8n/configure-n8n/change-instance-owner-email.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email) |
| Manage settings using environment variables — Configure a self-hosted n8n instance owner, SSO, security policy, log streaming, MCP, and community packages from environment variables. | [`deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables.md`](pages/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables) |
| Set up task runners — How to configure task runners to execute tasks using internal or external runner processes. | [`deploy/host-n8n/configure-n8n/set-up-task-runners.md`](pages/deploy/host-n8n/configure-n8n/set-up-task-runners.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-task-runners) |
| Durable scheduler — How the durable scheduler runs time-based workflows from a database-backed queue for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/durable-scheduler.md`](pages/deploy/host-n8n/configure-n8n/durable-scheduler.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/durable-scheduler) |
| Set up AI Assistant — Set up the AI Assistant on self-hosted n8n using environment variables. | [`deploy/host-n8n/configure-n8n/set-up-ai-assistant.md`](pages/deploy/host-n8n/configure-n8n/set-up-ai-assistant.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-ai-assistant) |
| Deploy n8n in canvas-only mode — How the N8N\_CANVAS\_ONLY environment variable hides n8n's navigation and workflow settings to show only the workflow canvas. | [`deploy/host-n8n/configure-n8n/deploy-n8n-in-canvas-only-mode.md`](pages/deploy/host-n8n/configure-n8n/deploy-n8n-in-canvas-only-mode.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/deploy-n8n-in-canvas-only-mode) |
| Manage your license — How to activate your license key. | [`deploy/host-n8n/configure-n8n/manage-your-license.md`](pages/deploy/host-n8n/configure-n8n/manage-your-license.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-your-license) |
| Security | [`deploy/host-n8n/configure-n8n/security.md`](pages/deploy/host-n8n/configure-n8n/security.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security) |
| Manage security policies — Manage instance-wide security policies including MFA enforcement and personal space controls. | [`deploy/host-n8n/configure-n8n/security/manage-security-policies.md`](pages/deploy/host-n8n/configure-n8n/security/manage-security-policies.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/manage-security-policies) |
| Set up SSL — Set up SSL for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/security/set-up-ssl.md`](pages/deploy/host-n8n/configure-n8n/security/set-up-ssl.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/set-up-ssl) |
| Configure SSO — Set up SAML or OIDC Single Sign-On for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/security/configure-sso.md`](pages/deploy/host-n8n/configure-n8n/security/configure-sso.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/configure-sso) |
| Run security audits — Run a security audit on your n8n instance. | [`deploy/host-n8n/configure-n8n/security/run-security-audits.md`](pages/deploy/host-n8n/configure-n8n/security/run-security-audits.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/run-security-audits) |
| Disable the public API — Disable the n8n public REST API to prevent others from using it. | [`deploy/host-n8n/configure-n8n/security/disable-the-public-api.md`](pages/deploy/host-n8n/configure-n8n/security/disable-the-public-api.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api) |
| Control telemetry — Opt out of data telemetry collection on your n8n instance. | [`deploy/host-n8n/configure-n8n/security/control-telemetry.md`](pages/deploy/host-n8n/configure-n8n/security/control-telemetry.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry) |
| Block specific nodes — Prevent your n8n users from accessing specific nodes. | [`deploy/host-n8n/configure-n8n/security/block-specific-nodes.md`](pages/deploy/host-n8n/configure-n8n/security/block-specific-nodes.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes) |
| Harden task runners — Harden task runners for better isolation for your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/security/harden-task-runners.md`](pages/deploy/host-n8n/configure-n8n/security/harden-task-runners.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners) |
| Verify user emails — Require all new accounts to be verified by email. | [`deploy/host-n8n/configure-n8n/security/verify-user-emails.md`](pages/deploy/host-n8n/configure-n8n/security/verify-user-emails.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails) |
| Enable SSRF protection — Protect your self-hosted n8n instance from Server-Side Request Forgery (SSRF) attacks. | [`deploy/host-n8n/configure-n8n/security/enable-ssrf-protection.md`](pages/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection) |
| Rotate encryption keys — Enable and rotate the data encryption key that protects credentials and other sensitive data on your self-hosted n8n instance. | [`deploy/host-n8n/configure-n8n/security/rotate-encryption-keys.md`](pages/deploy/host-n8n/configure-n8n/security/rotate-encryption-keys.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/rotate-encryption-keys) |
| Decrypt OAuth 2.0 tokens with JWE — Enable JWE-encrypted OAuth 2.0 tokens on your n8n instance so your identity provider can encrypt access and ID tokens that only your instance can decrypt. | [`deploy/host-n8n/configure-n8n/security/decrypt-oauth-20-tokens-with-jwe.md`](pages/deploy/host-n8n/configure-n8n/security/decrypt-oauth-20-tokens-with-jwe.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/decrypt-oauth-20-tokens-with-jwe) |
| Redact execution data — Control the visibility of execution data in workflows to protect sensitive information and meet compliance requirements. | [`deploy/host-n8n/configure-n8n/security/redact-execution-data.md`](pages/deploy/host-n8n/configure-n8n/security/redact-execution-data.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/redact-execution-data) |
| Scaling | [`deploy/host-n8n/configure-n8n/scaling.md`](pages/deploy/host-n8n/configure-n8n/scaling.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling) |
| Measure performance — n8n performance and resource consumption benchmarking. | [`deploy/host-n8n/configure-n8n/scaling/measure-performance.md`](pages/deploy/host-n8n/configure-n8n/scaling/measure-performance.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/measure-performance) |
| Enable queue mode | [`deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md`](pages/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode) |
| Control concurrency | [`deploy/host-n8n/configure-n8n/scaling/control-concurrency.md`](pages/deploy/host-n8n/configure-n8n/scaling/control-concurrency.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency) |
| Manage execution data | [`deploy/host-n8n/configure-n8n/scaling/manage-execution-data.md`](pages/deploy/host-n8n/configure-n8n/scaling/manage-execution-data.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/manage-execution-data) |
| Handle binary data — How to handle large files without degrading n8n's performance. | [`deploy/host-n8n/configure-n8n/scaling/handle-binary-data.md`](pages/deploy/host-n8n/configure-n8n/scaling/handle-binary-data.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data) |
| Use external storage — External storage of binary data and execution data for your n8n instance. | [`deploy/host-n8n/configure-n8n/scaling/use-external-storage.md`](pages/deploy/host-n8n/configure-n8n/scaling/use-external-storage.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/use-external-storage) |
| Fix memory issues | [`deploy/host-n8n/configure-n8n/scaling/fix-memory-issues.md`](pages/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues.md) | [docs](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues) |
| Keep n8n running — Keep a self-hosted n8n instance running, including logging, monitoring, updates, and tracing. | [`deploy/host-n8n/keep-n8n-running.md`](pages/deploy/host-n8n/keep-n8n-running.md) | [docs](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running) |
| Set up logging | [`deploy/host-n8n/keep-n8n-running/set-up-logging.md`](pages/deploy/host-n8n/keep-n8n-running/set-up-logging.md) | [docs](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/set-up-logging) |
| Monitor n8n — Get metrics for a health check | [`deploy/host-n8n/keep-n8n-running/monitor-n8n.md`](pages/deploy/host-n8n/keep-n8n-running/monitor-n8n.md) | [docs](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n) |
| Visualize metrics with Grafana | [`deploy/host-n8n/keep-n8n-running/visualize-metrics-with-grafana.md`](pages/deploy/host-n8n/keep-n8n-running/visualize-metrics-with-grafana.md) | [docs](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/visualize-metrics-with-grafana) |
| Update n8n — Best practices for updating your self-hosted n8n | [`deploy/host-n8n/keep-n8n-running/update-n8n.md`](pages/deploy/host-n8n/keep-n8n-running/update-n8n.md) | [docs](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/update-n8n) |
| Trace executions with OpenTelemetry — Send workflow and node execution traces from n8n to an OpenTelemetry collector. | [`deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry.md`](pages/deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry.md) | [docs](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry) |
| Understand the architecture | [`deploy/host-n8n/understand-the-architecture.md`](pages/deploy/host-n8n/understand-the-architecture.md) | [docs](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture) |
| How n8n works — Understand n8n's architecture | [`deploy/host-n8n/understand-the-architecture/how-n8n-works.md`](pages/deploy/host-n8n/understand-the-architecture/how-n8n-works.md) | [docs](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/how-n8n-works) |
| Understand the database — Understand the n8n database structure | [`deploy/host-n8n/understand-the-architecture/understand-the-database.md`](pages/deploy/host-n8n/understand-the-architecture/understand-the-database.md) | [docs](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database) |
| Deploy as an OEM integration — Overview of OEM deployment - surfacing n8n's interface inside your own product's UI under an OEM agreement. | [`deploy/host-n8n/deploy-as-an-oem-integration.md`](pages/deploy/host-n8n/deploy-as-an-oem-integration.md) | [docs](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration) |
| Prerequisites — Infrastructure sizing guidance and deployment best practices for an OEM deployment of n8n. | [`deploy/host-n8n/deploy-as-an-oem-integration/prerequisites.md`](pages/deploy/host-n8n/deploy-as-an-oem-integration/prerequisites.md) | [docs](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration/prerequisites) |
| Manage workflows — Patterns for managing workflows across multiple users or organizations in an n8n OEM deployment. | [`deploy/host-n8n/deploy-as-an-oem-integration/manage-workflows.md`](pages/deploy/host-n8n/deploy-as-an-oem-integration/manage-workflows.md) | [docs](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration/manage-workflows) |
| Set up token exchange — Use OAuth 2.0 Token Exchange to authenticate users and act on their behalf inside an embedded n8n instance, through iframe SSO and delegated API access. | [`deploy/host-n8n/deploy-as-an-oem-integration/set-up-token-exchange.md`](pages/deploy/host-n8n/deploy-as-an-oem-integration/set-up-token-exchange.md) | [docs](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration/set-up-token-exchange) |
| Deploy with the AI starter kit — Use n8n's curated self-hosted AI Starter Kit to get a list of AI elements to quickly start building AI workflows. | [`deploy/host-n8n/deploy-with-the-ai-starter-kit.md`](pages/deploy/host-n8n/deploy-with-the-ai-starter-kit.md) | [docs](https://docs.n8n.io/deploy/host-n8n/deploy-with-the-ai-starter-kit) |
| Compare editions — Compare the self-hosted n8n plans and editions: Community, Registered Community, Business, and Enterprise. | [`deploy/host-n8n/community-edition-features.md`](pages/deploy/host-n8n/community-edition-features.md) | [docs](https://docs.n8n.io/deploy/host-n8n/community-edition-features) |

### Build

| Page | Local copy | Official |
| --- | --- | --- |
| Build — Build workflows in n8n, from first draft to production. | [`build/readme.md`](pages/build/readme.md) | [docs](https://docs.n8n.io/build/readme) |
| Understand workflows — Learn about the key components of a workflow in n8n. | [`build/understand-workflows.md`](pages/build/understand-workflows.md) | [docs](https://docs.n8n.io/build/understand-workflows) |
| Workflow components — Learn about the building blocks of workflows. | [`build/understand-workflows/workflow-components.md`](pages/build/understand-workflows/workflow-components.md) | [docs](https://docs.n8n.io/build/understand-workflows/workflow-components) |
| Work with nodes — A node is an entry point for retrieving data, a function to process data, or an exit for sending data. | [`build/understand-workflows/workflow-components/work-with-nodes.md`](pages/build/understand-workflows/workflow-components/work-with-nodes.md) | [docs](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes) |
| Connect nodes together — A connection establishes a link between nodes to route data through the workflow. | [`build/understand-workflows/workflow-components/connect-nodes-together.md`](pages/build/understand-workflows/workflow-components/connect-nodes-together.md) | [docs](https://docs.n8n.io/build/understand-workflows/workflow-components/connect-nodes-together) |
| Canvas Groups — Group related nodes together on the canvas to keep large workflows readable. | [`build/understand-workflows/workflow-components/canvas-groups.md`](pages/build/understand-workflows/workflow-components/canvas-groups.md) | [docs](https://docs.n8n.io/build/understand-workflows/workflow-components/canvas-groups) |
| Add notes and documentation — Annotate your workflows using sticky notes. | [`build/understand-workflows/workflow-components/add-notes-and-documentation.md`](pages/build/understand-workflows/workflow-components/add-notes-and-documentation.md) | [docs](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation) |
| Find your workflow ID — Find your workflow ID. | [`build/understand-workflows/workflow-components/find-your-workflow-id.md`](pages/build/understand-workflows/workflow-components/find-your-workflow-id.md) | [docs](https://docs.n8n.io/build/understand-workflows/workflow-components/find-your-workflow-id) |
| Understand executions — An execution is a single run of a workflow. | [`build/understand-workflows/understand-executions.md`](pages/build/understand-workflows/understand-executions.md) | [docs](https://docs.n8n.io/build/understand-workflows/understand-executions) |
| Types of executions — How manual, partial, and automatic workflow executions differ. | [`build/understand-workflows/understand-executions/types-of-executions.md`](pages/build/understand-workflows/understand-executions/types-of-executions.md) | [docs](https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions) |
| Understand dirty nodes — What dirty nodes are and how they affect workflow execution. | [`build/understand-workflows/understand-executions/understand-dirty-nodes.md`](pages/build/understand-workflows/understand-executions/understand-dirty-nodes.md) | [docs](https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes) |
| Debug executions — How to copy execution data into your current workflow in order to debug previous executions. | [`build/understand-workflows/understand-executions/debug-executions.md`](pages/build/understand-workflows/understand-executions/debug-executions.md) | [docs](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions) |
| View executions for a single workflow — View and filter all executions for the workflow currently open on the canvas. | [`build/understand-workflows/understand-executions/view-executions-for-a-single-workflow.md`](pages/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow.md) | [docs](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow) |
| View all executions — View and filter all executions for all workflows. | [`build/understand-workflows/understand-executions/view-all-executions.md`](pages/build/understand-workflows/understand-executions/view-all-executions.md) | [docs](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions) |
| Customize executions data — Add custom data to your workflow executions using the Code node. You can then filter executions by this data. | [`build/understand-workflows/understand-executions/customize-executions-data.md`](pages/build/understand-workflows/understand-executions/customize-executions-data.md) | [docs](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data) |
| Stream real-time responses — Build a workflow with streaming responses | [`build/understand-workflows/understand-executions/stream-real-time-responses.md`](pages/build/understand-workflows/understand-executions/stream-real-time-responses.md) | [docs](https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses) |
| Create and run workflows — Create, run, and publish workflows. | [`build/understand-workflows/create-and-run-workflows.md`](pages/build/understand-workflows/create-and-run-workflows.md) | [docs](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows) |
| Save and publish workflows — Save, publish, unpublish, and name workflow versions. | [`build/understand-workflows/save-and-publish-workflows.md`](pages/build/understand-workflows/save-and-publish-workflows.md) | [docs](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows) |
| Create and edit credentials — Creating and editing credentials. | [`build/understand-workflows/create-and-edit-credentials.md`](pages/build/understand-workflows/create-and-edit-credentials.md) | [docs](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials) |
| Use Gateway credits — Run AI models and third-party services in your n8n workflows with Gateway credits instead of setting up your own credentials. | [`build/understand-workflows/use-gateway-credits.md`](pages/build/understand-workflows/use-gateway-credits.md) | [docs](https://docs.n8n.io/build/understand-workflows/use-gateway-credits) |
| Build and manage agents — Build agents in n8n alongside your workflows, publish them,  and let people reach them through chat, channels, and schedules. | [`build/build-and-manage-agents.md`](pages/build/build-and-manage-agents.md) | [docs](https://docs.n8n.io/build/build-and-manage-agents) |
| Ways of building workflows | [`build/ways-of-building-workflows.md`](pages/build/ways-of-building-workflows.md) | [docs](https://docs.n8n.io/build/ways-of-building-workflows) |
| Use AI Assistant — Use the AI Assistant to create, edit, test, and troubleshoot n8n workflows from a chat. | [`build/ways-of-building-workflows/ai-assistant.md`](pages/build/ways-of-building-workflows/ai-assistant.md) | [docs](https://docs.n8n.io/build/ways-of-building-workflows/ai-assistant) |
| Use n8n MCP server — Understand what it means to build and run n8n workflows from MCP clients. | [`build/ways-of-building-workflows/connect-to-n8n-mcp-server.md`](pages/build/ways-of-building-workflows/connect-to-n8n-mcp-server.md) | [docs](https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server) |
| Use templates — Use workflow templates | [`build/ways-of-building-workflows/use-templates.md`](pages/build/ways-of-building-workflows/use-templates.md) | [docs](https://docs.n8n.io/build/ways-of-building-workflows/use-templates) |
| Use AI Workflow Builder — Create, refine, and debug workflows using natural language descriptions of your goals. | [`build/ways-of-building-workflows/ai-workflow-builder.md`](pages/build/ways-of-building-workflows/ai-workflow-builder.md) | [docs](https://docs.n8n.io/build/ways-of-building-workflows/ai-workflow-builder) |
| Use Ask n8n AI | [`build/ways-of-building-workflows/use-the-ai-assistant.md`](pages/build/ways-of-building-workflows/use-the-ai-assistant.md) | [docs](https://docs.n8n.io/build/ways-of-building-workflows/use-the-ai-assistant) |
| Use Chat Hub | [`build/ways-of-building-workflows/chat-hub.md`](pages/build/ways-of-building-workflows/chat-hub.md) | [docs](https://docs.n8n.io/build/ways-of-building-workflows/chat-hub) |
| Manage workflows | [`build/manage-workflows.md`](pages/build/manage-workflows.md) | [docs](https://docs.n8n.io/build/manage-workflows) |
| Configure workflow settings — Manage settings for an individual workflow. | [`build/manage-workflows/configure-workflow-settings.md`](pages/build/manage-workflows/configure-workflow-settings.md) | [docs](https://docs.n8n.io/build/manage-workflows/configure-workflow-settings) |
| Tag workflows — Use tags to label workflows, making it easier to browse your workflows. | [`build/manage-workflows/tag-workflows.md`](pages/build/manage-workflows/tag-workflows.md) | [docs](https://docs.n8n.io/build/manage-workflows/tag-workflows) |
| Favorite items — Favorite workflows, folders, projects, and data tables to pin them for quick access in the left menu. | [`build/manage-workflows/favorite-items.md`](pages/build/manage-workflows/favorite-items.md) | [docs](https://docs.n8n.io/build/manage-workflows/favorite-items) |
| View change history — View and restore previous versions of your workflow. | [`build/manage-workflows/view-change-history.md`](pages/build/manage-workflows/view-change-history.md) | [docs](https://docs.n8n.io/build/manage-workflows/view-change-history) |
| Review workflows — Submit a workflow version for review before publishing, compare changes with a visual diff, discuss in activity comments, and approve or request changes. | [`build/manage-workflows/workflow-reviews.md`](pages/build/manage-workflows/workflow-reviews.md) | [docs](https://docs.n8n.io/build/manage-workflows/workflow-reviews) |
| Export and import — Different ways to export and import workflows in n8n. | [`build/manage-workflows/export-and-import.md`](pages/build/manage-workflows/export-and-import.md) | [docs](https://docs.n8n.io/build/manage-workflows/export-and-import) |
| n8n packages — Bundle workflows and the structure they need into a portable .n8np file, and move them between n8n instances. | [`build/manage-workflows/n8n-packages.md`](pages/build/manage-workflows/n8n-packages.md) | [docs](https://docs.n8n.io/build/manage-workflows/n8n-packages) |
| Package format — What's inside a .n8np file: the three package shapes, the directory layout, and the manifest. | [`build/manage-workflows/n8n-packages/package-format.md`](pages/build/manage-workflows/n8n-packages/package-format.md) | [docs](https://docs.n8n.io/build/manage-workflows/n8n-packages/package-format) |
| Export a package — Export workflows, folders, or whole projects into a .n8np package, and control how n8n handles sub-workflow dependencies. | [`build/manage-workflows/n8n-packages/export-a-package.md`](pages/build/manage-workflows/n8n-packages/export-a-package.md) | [docs](https://docs.n8n.io/build/manage-workflows/n8n-packages/export-a-package) |
| Import a package — Import a .n8np package into an n8n instance, and control where its contents land and how n8n resolves what they depend on. | [`build/manage-workflows/n8n-packages/import-a-package.md`](pages/build/manage-workflows/n8n-packages/import-a-package.md) | [docs](https://docs.n8n.io/build/manage-workflows/n8n-packages/import-a-package) |
| How import works — How n8n checks a package before writing it, the order it writes things in, and how it resolves credentials, variables, data tables, tags, folders, and projects. | [`build/manage-workflows/n8n-packages/how-import-works.md`](pages/build/manage-workflows/n8n-packages/how-import-works.md) | [docs](https://docs.n8n.io/build/manage-workflows/n8n-packages/how-import-works) |
| Limits and permissions — Size limits, license features, API key scopes, and the events n8n emits when you export or import a package. | [`build/manage-workflows/n8n-packages/limits-and-permissions.md`](pages/build/manage-workflows/n8n-packages/limits-and-permissions.md) | [docs](https://docs.n8n.io/build/manage-workflows/n8n-packages/limits-and-permissions) |
| Share with others — Share workflows between users. | [`build/manage-workflows/share-with-others.md`](pages/build/manage-workflows/share-with-others.md) | [docs](https://docs.n8n.io/build/manage-workflows/share-with-others) |
| Flow logic — How to represent logic in n8n workflows. | [`build/flow-logic.md`](pages/build/flow-logic.md) | [docs](https://docs.n8n.io/build/flow-logic) |
| Split with conditionals — Split workflows into multiple paths using If and Switch | [`build/flow-logic/split-with-conditionals.md`](pages/build/flow-logic/split-with-conditionals.md) | [docs](https://docs.n8n.io/build/flow-logic/split-with-conditionals) |
| Merge data — Merge data streams in you n8n workflows. | [`build/flow-logic/merge-data.md`](pages/build/flow-logic/merge-data.md) | [docs](https://docs.n8n.io/build/flow-logic/merge-data) |
| Loop | [`build/flow-logic/loop.md`](pages/build/flow-logic/loop.md) | [docs](https://docs.n8n.io/build/flow-logic/loop) |
| Wait — How to make your workflow execution wait. | [`build/flow-logic/wait.md`](pages/build/flow-logic/wait.md) | [docs](https://docs.n8n.io/build/flow-logic/wait) |
| Break workflows into smaller parts — Call workflows from other workflows, and split large workflows into smaller components. | [`build/flow-logic/break-workflows-into-smaller-parts.md`](pages/build/flow-logic/break-workflows-into-smaller-parts.md) | [docs](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts) |
| Convert to sub-workflows — Select nodes in your workflow and convert them into a sub-workflow. | [`build/flow-logic/convert-to-sub-workflows.md`](pages/build/flow-logic/convert-to-sub-workflows.md) | [docs](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows) |
| Handle errors gracefully — How to handle execution errors. | [`build/flow-logic/handle-errors-gracefully.md`](pages/build/flow-logic/handle-errors-gracefully.md) | [docs](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully) |
| Understand execution order — How n8n decides the node execution order in multi-branch workflows. | [`build/flow-logic/understand-execution-order.md`](pages/build/flow-logic/understand-execution-order.md) | [docs](https://docs.n8n.io/build/flow-logic/understand-execution-order) |
| Work with data | [`build/work-with-data.md`](pages/build/work-with-data.md) | [docs](https://docs.n8n.io/build/work-with-data) |
| Overview | [`build/work-with-data/overview.md`](pages/build/work-with-data/overview.md) | [docs](https://docs.n8n.io/build/work-with-data/overview) |
| Understand n8n's data structure | [`build/work-with-data/understand-n8ns-data-structure.md`](pages/build/work-with-data/understand-n8ns-data-structure.md) | [docs](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure) |
| Expressions versus data nodes — Compare expressions, the Code node, the AI Transform node, and data transformation nodes for working with data in n8n. | [`build/work-with-data/expressions-versus-data-nodes.md`](pages/build/work-with-data/expressions-versus-data-nodes.md) | [docs](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes) |
| Reference data | [`build/work-with-data/reference-data.md`](pages/build/work-with-data/reference-data.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data) |
| Use the UI mapper | [`build/work-with-data/reference-data/use-the-ui-mapper.md`](pages/build/work-with-data/reference-data/use-the-ui-mapper.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data/use-the-ui-mapper) |
| Reference previous nodes — Methods for working with the input of the current node and the output of previous nodes. | [`build/work-with-data/reference-data/reference-previous-nodes.md`](pages/build/work-with-data/reference-data/reference-previous-nodes.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes) |
| Link data items | [`build/work-with-data/reference-data/link-data-items.md`](pages/build/work-with-data/reference-data/link-data-items.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items) |
| How items link through workflows | [`build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows.md`](pages/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows) |
| Accessing linked items in the Code node — How to use \`("\<node-name>").itemMatching(currentNodeinputIndex)\` | [`build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node.md`](pages/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node) |
| Preserving linking in the Code node | [`build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node.md`](pages/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node) |
| Item linking errors | [`build/work-with-data/reference-data/link-data-items/item-linking-errors.md`](pages/build/work-with-data/reference-data/link-data-items/item-linking-errors.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors) |
| Item linking for node creators | [`build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators.md`](pages/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators.md) | [docs](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators) |
| Transform data | [`build/work-with-data/transform-data.md`](pages/build/work-with-data/transform-data.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data) |
| Approaches for transforming data | [`build/work-with-data/transform-data/approaches-for-transforming-data.md`](pages/build/work-with-data/transform-data/approaches-for-transforming-data.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/approaches-for-transforming-data) |
| Expressions for data transformation | [`build/work-with-data/transform-data/expressions-for-data-transformation.md`](pages/build/work-with-data/transform-data/expressions-for-data-transformation.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expressions-for-data-transformation) |
| Expression reference | [`build/work-with-data/transform-data/expression-reference.md`](pages/build/work-with-data/transform-data/expression-reference.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference) |
| Array | [`build/work-with-data/transform-data/expression-reference/array.md`](pages/build/work-with-data/transform-data/expression-reference/array.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array) |
| Binaryfile | [`build/work-with-data/transform-data/expression-reference/binaryfile.md`](pages/build/work-with-data/transform-data/expression-reference/binaryfile.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/binaryfile) |
| Boolean | [`build/work-with-data/transform-data/expression-reference/boolean.md`](pages/build/work-with-data/transform-data/expression-reference/boolean.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean) |
| Customdata | [`build/work-with-data/transform-data/expression-reference/customdata.md`](pages/build/work-with-data/transform-data/expression-reference/customdata.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata) |
| Date | [`build/work-with-data/transform-data/expression-reference/date.md`](pages/build/work-with-data/transform-data/expression-reference/date.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/date) |
| Datetime | [`build/work-with-data/transform-data/expression-reference/datetime.md`](pages/build/work-with-data/transform-data/expression-reference/datetime.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime) |
| Execdata | [`build/work-with-data/transform-data/expression-reference/execdata.md`](pages/build/work-with-data/transform-data/expression-reference/execdata.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata) |
| Httpresponse | [`build/work-with-data/transform-data/expression-reference/httpresponse.md`](pages/build/work-with-data/transform-data/expression-reference/httpresponse.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/httpresponse) |
| Item | [`build/work-with-data/transform-data/expression-reference/item.md`](pages/build/work-with-data/transform-data/expression-reference/item.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/item) |
| Nodeinputdata | [`build/work-with-data/transform-data/expression-reference/nodeinputdata.md`](pages/build/work-with-data/transform-data/expression-reference/nodeinputdata.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeinputdata) |
| Nodeoutputdata | [`build/work-with-data/transform-data/expression-reference/nodeoutputdata.md`](pages/build/work-with-data/transform-data/expression-reference/nodeoutputdata.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/nodeoutputdata) |
| Number | [`build/work-with-data/transform-data/expression-reference/number.md`](pages/build/work-with-data/transform-data/expression-reference/number.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number) |
| Object | [`build/work-with-data/transform-data/expression-reference/object.md`](pages/build/work-with-data/transform-data/expression-reference/object.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object) |
| Prevnodedata | [`build/work-with-data/transform-data/expression-reference/prevnodedata.md`](pages/build/work-with-data/transform-data/expression-reference/prevnodedata.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata) |
| Root | [`build/work-with-data/transform-data/expression-reference/root.md`](pages/build/work-with-data/transform-data/expression-reference/root.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root) |
| String | [`build/work-with-data/transform-data/expression-reference/string.md`](pages/build/work-with-data/transform-data/expression-reference/string.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string) |
| Workflowdata | [`build/work-with-data/transform-data/expression-reference/workflowdata.md`](pages/build/work-with-data/transform-data/expression-reference/workflowdata.md) | [docs](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/workflowdata) |
| Filter out unwanted data | [`build/work-with-data/filter-out-unwanted-data.md`](pages/build/work-with-data/filter-out-unwanted-data.md) | [docs](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data) |
| Pin and mock data — Ways to mock and pin data in your n8n workflow during development. | [`build/work-with-data/pin-and-mock-data.md`](pages/build/work-with-data/pin-and-mock-data.md) | [docs](https://docs.n8n.io/build/work-with-data/pin-and-mock-data) |
| Handle special data types | [`build/work-with-data/handle-special-data-types.md`](pages/build/work-with-data/handle-special-data-types.md) | [docs](https://docs.n8n.io/build/work-with-data/handle-special-data-types) |
| Work with files and images — Understand and use binary data in n8n. | [`build/work-with-data/handle-special-data-types/work-with-files-and-images.md`](pages/build/work-with-data/handle-special-data-types/work-with-files-and-images.md) | [docs](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images) |
| Work with dates and times — Use Luxon to work with date and time in n8n. | [`build/work-with-data/handle-special-data-types/work-with-dates-and-times.md`](pages/build/work-with-data/handle-special-data-types/work-with-dates-and-times.md) | [docs](https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-dates-and-times) |
| Query JSON data — n8n supports the JMESPath library, to simplify working with JSON formatted data. | [`build/work-with-data/handle-special-data-types/query-json-data.md`](pages/build/work-with-data/handle-special-data-types/query-json-data.md) | [docs](https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data) |
| Data tables — Structured tabular data management for workflows within project boundaries | [`build/work-with-data/data-tables.md`](pages/build/work-with-data/data-tables.md) | [docs](https://docs.n8n.io/build/work-with-data/data-tables) |
| Code in n8n — Access documentation and guides on using code and expressions in n8n and other developer resources. | [`build/code-in-n8n.md`](pages/build/code-in-n8n.md) | [docs](https://docs.n8n.io/build/code-in-n8n) |
| Using the Code node | [`build/code-in-n8n/using-the-code-node.md`](pages/build/code-in-n8n/using-the-code-node.md) | [docs](https://docs.n8n.io/build/code-in-n8n/using-the-code-node) |
| Get coding help from AI — Use GPT to generate code in the Code node. | [`build/code-in-n8n/get-coding-help-from-ai.md`](pages/build/code-in-n8n/get-coding-help-from-ai.md) | [docs](https://docs.n8n.io/build/code-in-n8n/get-coding-help-from-ai) |
| Use built-in shortcuts — n8n's built-in custom methods and variables. | [`build/code-in-n8n/use-built-in-shortcuts.md`](pages/build/code-in-n8n/use-built-in-shortcuts.md) | [docs](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts) |
| JMESPath — A method for working with the JMESPath library in n8n. | [`build/code-in-n8n/use-built-in-shortcuts/jmespath.md`](pages/build/code-in-n8n/use-built-in-shortcuts/jmespath.md) | [docs](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/jmespath) |
| HTTP node — n8n provides these methods to make it easier to perform common tasks in expressions. | [`build/code-in-n8n/use-built-in-shortcuts/http-node.md`](pages/build/code-in-n8n/use-built-in-shortcuts/http-node.md) | [docs](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/http-node) |
| LangChain Code node — n8n provides these methods to make it easier to perform common tasks in the LangChain Code node. | [`build/code-in-n8n/use-built-in-shortcuts/langchain-code-node.md`](pages/build/code-in-n8n/use-built-in-shortcuts/langchain-code-node.md) | [docs](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/langchain-code-node) |
| n8n metadata — Methods for working with n8n metadata. | [`build/code-in-n8n/use-built-in-shortcuts/n8n-metadata.md`](pages/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata.md) | [docs](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata) |
| Define custom variables — Custom variables allow you to store and reuse values in n8n workflows. | [`build/code-in-n8n/define-custom-variables.md`](pages/build/code-in-n8n/define-custom-variables.md) | [docs](https://docs.n8n.io/build/code-in-n8n/define-custom-variables) |
| Cookbook | [`build/code-in-n8n/cookbook.md`](pages/build/code-in-n8n/cookbook.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook) |
| Built-in methods and variables examples | [`build/code-in-n8n/cookbook/built-in-methods-and-variables-examples.md`](pages/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples) |
| execution | [`build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution.md`](pages/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution) |
| getWorkflowStaticData | [`build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md`](pages/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata) |
| (node-name).all | [`build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/node-name-.all.md`](pages/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/node-name-.all.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/node-name-.all) |
| vars — Access your environment's custom variables. | [`build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/vars.md`](pages/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/vars.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/vars) |
| Code node — Code examples you can use in the Code node. | [`build/code-in-n8n/cookbook/code-node.md`](pages/build/code-in-n8n/cookbook/code-node.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node) |
| Get number of items returned by last node | [`build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node.md`](pages/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node) |
| Get the binary data buffer | [`build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer.md`](pages/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer) |
| Output to the browser console — How to use console.log() or print() | [`build/code-in-n8n/cookbook/code-node/output-to-the-browser-console.md`](pages/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console) |
| HTTP Request node | [`build/code-in-n8n/cookbook/http-request-node.md`](pages/build/code-in-n8n/cookbook/http-request-node.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node) |
| Pagination — Pagination examples for the HTTP Request node. | [`build/code-in-n8n/cookbook/http-request-node/pagination.md`](pages/build/code-in-n8n/cookbook/http-request-node/pagination.md) | [docs](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node/pagination) |
| Integrate AI — Build AI-powered workflows in n8n with LLM providers, agents, tools, memory, and MCP servers. | [`build/integrate-ai.md`](pages/build/integrate-ai.md) | [docs](https://docs.n8n.io/build/integrate-ai) |
| MCP servers — Connect an AI agent to an MCP registry server in one click. | [`build/integrate-ai/mcp-servers.md`](pages/build/integrate-ai/mcp-servers.md) | [docs](https://docs.n8n.io/build/integrate-ai/mcp-servers) |
| Understand AI components | [`build/integrate-ai/understand-ai-components.md`](pages/build/integrate-ai/understand-ai-components.md) | [docs](https://docs.n8n.io/build/integrate-ai/understand-ai-components) |
| What chains do — Understand chains in the context of AI. Learn about chains in n8n. | [`build/integrate-ai/understand-ai-components/what-chains-do.md`](pages/build/integrate-ai/understand-ai-components/what-chains-do.md) | [docs](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do) |
| What agents do — Understand agents in the context of AI. Learn how n8n provides agents. | [`build/integrate-ai/understand-ai-components/what-agents-do.md`](pages/build/integrate-ai/understand-ai-components/what-agents-do.md) | [docs](https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do) |
| How memory works — Understand memory in the context of AI. Learn what's special about memory in n8n. | [`build/integrate-ai/understand-ai-components/how-memory-works.md`](pages/build/integrate-ai/understand-ai-components/how-memory-works.md) | [docs](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works) |
| How tools work — Understand tools in the context of AI. Learn what's special about tools in n8n. | [`build/integrate-ai/understand-ai-components/how-tools-work.md`](pages/build/integrate-ai/understand-ai-components/how-tools-work.md) | [docs](https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work) |
| Store and search data with vectors — Understand vector databases. Learn how n8n provides vector databases, along with the key components to work with them, including embeddings, retrievers, and document loaders. | [`build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors.md`](pages/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors.md) | [docs](https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors) |
| Retrieve relevant context — With Retrieval-Augmented Generation (RAG), you can give your models access to context-specific resources to help generate relevant answers. Learn how it works and how to use RAG in n8n. | [`build/integrate-ai/understand-ai-components/retrieve-relevant-context.md`](pages/build/integrate-ai/understand-ai-components/retrieve-relevant-context.md) | [docs](https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context) |
| Agents vs chains — A workflow example that demonstrates key differences between agents and chains. | [`build/integrate-ai/understand-ai-components/agents-vs-chains.md`](pages/build/integrate-ai/understand-ai-components/agents-vs-chains.md) | [docs](https://docs.n8n.io/build/integrate-ai/understand-ai-components/agents-vs-chains) |
| LangChain in n8n — Understand how n8n implements LangChain concepts, and connect a self-hosted n8n instance to LangSmith for tracing. | [`build/integrate-ai/langchain-in-n8n.md`](pages/build/integrate-ai/langchain-in-n8n.md) | [docs](https://docs.n8n.io/build/integrate-ai/langchain-in-n8n) |
| Test and improve AI workflows | [`build/integrate-ai/test-and-improve-ai-workflows.md`](pages/build/integrate-ai/test-and-improve-ai-workflows.md) | [docs](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows) |
| Understand why to test — Use n8n evaluations to build reliable AI workflows. Build confidence in your LLM-powered workflows by comparing the output from known test cases. | [`build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test.md`](pages/build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test.md) | [docs](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test) |
| Run quick evaluations — Use light evaluations during development to build reliable LLM-based workflows by checking the results of executing against known test cases. | [`build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations.md`](pages/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations.md) | [docs](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations) |
| Use metrics to measure quality — Use metric-based evaluations to measure, score, and improve production AI-based workflow performance over time. | [`build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality.md`](pages/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality.md) | [docs](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality) |
| Fix common issues — Details of how to set up specific use cases and address common issues with workflow evaluations. | [`build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues.md`](pages/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues.md) | [docs](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues) |
| AI examples — Example workflows and use cases for building AI functionality using n8n. | [`build/integrate-ai/ai-examples.md`](pages/build/integrate-ai/ai-examples.md) | [docs](https://docs.n8n.io/build/integrate-ai/ai-examples) |
| Use Google Sheets as a data source — Use the n8n workflow tool to load data from Google Sheets into your AI workflow. | [`build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source.md`](pages/build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source.md) | [docs](https://docs.n8n.io/build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source) |
| Call APIs — Use the n8n workflow tool to load data from an API using the HTTP Request node into your AI workflow. | [`build/integrate-ai/ai-examples/call-apis.md`](pages/build/integrate-ai/ai-examples/call-apis.md) | [docs](https://docs.n8n.io/build/integrate-ai/ai-examples/call-apis) |
| Use website content — Scrape a website, load the data into Pinecone, then query it using a chat workflow. | [`build/integrate-ai/ai-examples/use-website-content.md`](pages/build/integrate-ai/ai-examples/use-website-content.md) | [docs](https://docs.n8n.io/build/integrate-ai/ai-examples/use-website-content) |
| Human-in-the-loop for tools — Learn how to require human approval before an AI Agent executes specific tools in n8n. | [`build/integrate-ai/ai-examples/human-in-the-loop-for-tools.md`](pages/build/integrate-ai/ai-examples/human-in-the-loop-for-tools.md) | [docs](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools) |
| Set a human fallback for AI workflows — Have a workflow that triggers a human answer when the AI can't help. | [`build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows.md`](pages/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows.md) | [docs](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows) |
| Use AI for parameters — Understand how n8n's \`$fromAI()\` function works and how to use it to dynamically populate parameters for AI app tools, or use the built-in automation to complete them instead. | [`build/integrate-ai/ai-examples/use-ai-for-parameters.md`](pages/build/integrate-ai/ai-examples/use-ai-for-parameters.md) | [docs](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters) |
| Keyboard shortcuts — Keyboard shortcuts available in n8n. | [`build/keyboard-shortcuts.md`](pages/build/keyboard-shortcuts.md) | [docs](https://docs.n8n.io/build/keyboard-shortcuts) |

### Nodes

| Page | Local copy | Official |
| --- | --- | --- |
| Nodes — Learn about n8n's built-in nodes, community nodes, MCP servers, and generic integrations. | [`integrations/readme.md`](pages/integrations/readme.md) | [docs](https://docs.n8n.io/integrations/readme) |
| Built-in nodes — Explore n8n's built-in core nodes, app nodes, trigger nodes, cluster nodes, and credentials. | [`integrations/builtin.md`](pages/integrations/builtin.md) | [docs](https://docs.n8n.io/integrations/builtin) |
| Node types — Learn about n8n's core nodes, cluster nodes, credentials, and community nodes. | [`integrations/builtin/node-types.md`](pages/integrations/builtin/node-types.md) | [docs](https://docs.n8n.io/integrations/builtin/node-types) |
| Core nodes | [`integrations/builtin/core-nodes.md`](pages/integrations/builtin/core-nodes.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes) |
| Activation Trigger — Learn how to use the Activation Trigger node in n8n. Follow technical documentation to integrate Activation Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger) |
| Aggregate — Documentation for the Aggregate node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate) |
| AI Transform — Documentation for the AI Transform node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aitransform) |
| Code — Documentation for the Code node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.code.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.code.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code) |
| Keyboard shortcuts — A list of the keyboard shortcuts, for multiple platforms, which are supported by the Code node editor. | [`integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts) |
| Common issues — Documentation for common issues and questions in the Code node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues) |
| Compare Datasets — Documentation for the Compare Datasets node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets) |
| Compression — Documentation for the Compression node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.compression.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.compression.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression) |
| Chat Trigger — Learn how to use the Chat Trigger node in n8n. Follow technical documentation to integrate Chat Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger) |
| Common issues — Documentation for common issues and questions in the Chat Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues.md`](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues) |
| Convert to File — Documentation for the Convert to File node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile) |
| Crypto — Documentation for the Crypto node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.crypto.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.crypto.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto) |
| Data Table — Documentation for the data table node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.datatable.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.datatable.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable) |
| Row operations — Reference documentation for Data Table node row operations, including delete, get, insert, update, and upsert. | [`integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows) |
| Table operations — Reference documentation for Data Table node table operations, including create, delete, list, and update. | [`integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables) |
| Date & Time — Documentation for the Date & Time node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.datetime.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.datetime.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datetime) |
| Debug Helper — Documentation for the Debug Helper node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.debughelper.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.debughelper.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.debughelper) |
| Edit Fields (Set) — Documentation for the Edit Fields node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.set.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.set.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set) |
| Edit Image — Documentation for the Edit Image node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.editimage.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.editimage.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage) |
| Email Trigger (IMAP) — Learn how to use the Email Trigger (IMAP) Trigger node in n8n. Follow technical documentation to integrate Email Trigger (IMAP) Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.emailimap.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.emailimap.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap) |
| Error Trigger — Learn how to use the Error Trigger node in n8n. Follow technical documentation to integrate Error Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger) |
| Evaluation — Documentation for the Evaluation node in n8n, a workflow automation platform. Includes guidance on usage and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.evaluation.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.evaluation.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation) |
| Evaluation Trigger — Learn how to use the Evaluation Trigger node in n8n. Follow technical documentation to integrate Evaluation Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger) |
| Execute Command — Documentation for the Execute Command node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.executecommand.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.executecommand.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand) |
| Common issues — Documentation for common issues and questions in the Execute Command node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues) |
| Execute Sub-workflow — Documentation for the Execute Sub-workflow node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow) |
| Execute Sub-workflow Trigger — Learn how to use the Execute Sub-workflow Trigger node in n8n. Follow technical documentation to integrate Execute Sub-workflow Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger) |
| Execution Data — Documentation for the Execution Data node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata) |
| Extract From File — Documentation for the Extract From File node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile) |
| Filter — Documentation for the Filter node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.filter.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.filter.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filter) |
| FTP — Documentation for the FTP node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.ftp.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.ftp.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ftp) |
| Git — Documentation for the Git node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.git.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.git.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.git) |
| GraphQL — Documentation for the GraphQL node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.graphql.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.graphql.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.graphql) |
| Guardrails — Documentation for the Guardrails node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails.md`](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails) |
| HTML — Documentation for the HTML node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.html.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.html.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html) |
| HTTP Request — Learn how to use the HTTP Request node in n8n. Follow technical documentation to integrate the HTTP Request node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.httprequest.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.httprequest.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest) |
| Common Issues — Documentation for common issues and questions in the HTTP Request node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues) |
| If — Documentation for the If node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.if.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.if.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if) |
| JWT — Documentation for the JWT node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.jwt.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.jwt.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt) |
| LDAP — Documentation for the LDAP node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.ldap.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.ldap.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ldap) |
| Limit — Documentation for the Limit node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.limit.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.limit.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit) |
| Local File Trigger — Learn how to use the Local File Trigger node in n8n. Follow technical documentation to integrate Local File Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger) |
| Loop Over Items (Split in Batches) — Documentation for the Loop Over Items node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches) |
| Manual Trigger — Learn how to use the Manual Trigger node in n8n. Follow technical documentation to integrate Manual Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger) |
| Markdown — Documentation for the Markdown node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.markdown.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.markdown.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.markdown) |
| MCP Client — Learn how to use the MCP Client node in n8n. Follow technical documentation to integrate MCP Client node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient.md`](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient) |
| MCP Server Trigger — Learn how to use the MCP Server Trigger node in n8n. Follow technical documentation to integrate the MCP Server Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger) |
| Merge — Documentation for the Merge node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.merge.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.merge.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge) |
| n8n — Documentation for the n8n node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.n8n.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n) |
| n8n Form — Documentation for the n8n Form node in n8n, a workflow automation platform. Includes guidance on usage and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.form.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.form.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.form) |
| n8n Form — Learn how to use the n8n Form Trigger node in n8n. Follow technical documentation to integrate n8n Form Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger) |
| n8n Trigger — Learn how to use the n8n Trigger node in n8n. Follow technical documentation to integrate n8n Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger) |
| No Operation, do nothing — Documentation for the No Operation, do nothing node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.noop.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.noop.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.noop) |
| Read/Write Files from Disk — Documentation for the Read/Write Files from Disk node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile) |
| Remove Duplicates — Documentation for the Remove Duplicates node in n8n, a workflow automation platform. Includes guidance on usage and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates) |
| Templates and examples — Documentation for templates and examples in the Remove Duplicates node in n8n, a workflow automation platform. Includes templates using the node and examples of how to use it. | [`integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples) |
| Rename Keys — Documentation for the Rename Keys node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.renamekeys.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys) |
| Chat — Learn how to use the Chat node in n8n. Follow technical documentation to integrate the Chat node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-langchain.chat.md`](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.chat.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat) |
| Respond to Webhook — Documentation for the Respond to Webhook node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook) |
| RSS Read — Documentation for the RSS Read node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.rssfeedread.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedread.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedread) |
| RSS Feed Trigger — Learn how to use the RSS Feed Trigger node in n8n. Follow technical documentation to integrate RSS Feed Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger) |
| Schedule Trigger — Learn how to use the Schedule Trigger node in n8n. Follow technical documentation to integrate Schedule Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger) |
| Common issues — Documentation for common issues and questions in the Schedule Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues) |
| Send Email — Documentation for the Send Email node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail) |
| Sort — Documentation for the Sort node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.sort.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.sort.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort) |
| Split Out — Documentation for the Split Out node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.splitout.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout) |
| SSE Trigger — Learn how to use the SSE Trigger node in n8n. Follow technical documentation to integrate SSE Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.ssetrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.ssetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssetrigger) |
| SSH — Documentation for the SSH node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.ssh.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.ssh.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh) |
| Stop And Error — Documentation for the Stop And Error node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror) |
| Summarize — Documentation for the Summarize node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.summarize.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.summarize.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize) |
| Switch — Documentation for the Switch node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.switch.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.switch.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch) |
| TOTP — Documentation for the TOTP node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.totp.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.totp.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp) |
| Wait — Documentation for the Wait node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.wait.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait) |
| Webhook — Learn how to use the Webhook node in n8n. Follow technical documentation to integrate Webhook node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.webhook.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.webhook.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook) |
| Workflow development — Learn how to build, test, and use the Webhook node in your workflows in n8n. | [`integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development) |
| Common issues — Documentation for common issues and questions in the Webhook node in n8n, a workflow automation platform. Includes details of the issues and suggested solutions. | [`integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues) |
| Workflow Trigger — Learn how to use the Workflow Trigger node in n8n. Follow technical documentation to integrate Workflow Trigger node into your workflows. | [`integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger) |
| XML — Documentation for the XML node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples. | [`integrations/builtin/core-nodes/n8n-nodes-base.xml.md`](pages/integrations/builtin/core-nodes/n8n-nodes-base.xml.md) | [docs](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml) |
| App nodes | [`integrations/builtin/app-nodes.md`](pages/integrations/builtin/app-nodes.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes) |
| Action Network — Learn how to use the Action Network node in n8n. Follow technical documentation to integrate Action Network node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.actionnetwork.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.actionnetwork.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.actionnetwork) |
| ActiveCampaign — Learn how to use the ActiveCampaign node in n8n. Follow technical documentation to integrate ActiveCampaign node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.activecampaign.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.activecampaign.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.activecampaign) |
| Adalo — Learn how to use the Adalo node in n8n. Follow technical documentation to integrate Adalo node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.adalo.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.adalo.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.adalo) |
| Affinity — Learn how to use the Affinity node in n8n. Follow technical documentation to integrate Affinity node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.affinity.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.affinity.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.affinity) |
| Agile CRM — Learn how to use the Agile CRM node in n8n. Follow technical documentation to integrate Agile CRM node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.agilecrm.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.agilecrm.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.agilecrm) |
| Airtable — Learn how to use the Airtable node in n8n. Follow technical documentation to integrate Airtable node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.airtable.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.airtable.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable) |
| Common issues — Documentation for common issues and questions in the Airtable node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues) |
| Airtop — Learn how to use the Airtop node in n8n. Follow technical documentation to integrate Airtop node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.airtop.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.airtop.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop) |
| Qwen Cloud — Interact with models available on Qwen Cloud. This page explains how to use the node in n8n workflows to generate text completions, analyze or generate images, and create videos from text | [`integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud) |
| AMQP Sender — Learn how to use the AMQP Sender node in n8n. Follow technical documentation to integrate AMQP Sender node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.amqp.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.amqp.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.amqp) |
| Anthropic — Learn how to use the Anthropic node in n8n. Follow technical documentation to integrate Anthropic node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic) |
| APITemplate.io — Learn how to use the APITemplate.io node in n8n. Follow technical documentation to integrate APITemplate.io node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.apitemplateio.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.apitemplateio.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.apitemplateio) |
| Asana — Learn how to use the Asana node in n8n. Follow technical documentation to integrate Asana node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.asana.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.asana.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana) |
| Autopilot — Learn how to use the Autopilot node in n8n. Follow technical documentation to integrate Autopilot node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.autopilot.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.autopilot.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.autopilot) |
| AWS Certificate Manager — Learn how to use the AWS Certificate Manager node in n8n. Follow technical documentation to integrate AAWS Certificage Manager node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager) |
| AWS Cognito — Learn how to use the AWS Cognito node in n8n. Follow technical documentation to integrate AWS Cognito node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awscognito.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awscognito.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscognito) |
| AWS Comprehend — Learn how to use the AWS Comprehend node in n8n. Follow technical documentation to integrate AWS Comprehend node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awscomprehend.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awscomprehend.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscomprehend) |
| AWS DynamoDB — Learn how to use the AWS DynamoDB node in n8n. Follow technical documentation to integrate AWS DynamoDB node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb) |
| AWS Elastic Load Balancing — Learn how to use the AWS Elastic Load Balancing node in n8n. Follow technical documentation to integrate AWS Elastic Load Balancing node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awselb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awselb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awselb) |
| AWS IAM — Learn how to use the AWS IAM node in n8n. Follow technical documentation to integrate AWS IAM node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awsiam.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awsiam.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsiam) |
| AWS Lambda — Learn how to use the AWS Lambda node in n8n. Follow technical documentation to integrate AWS Lambda node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awslambda.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awslambda.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awslambda) |
| AWS Rekognition — Learn how to use the AWS Rekognition node in n8n. Follow technical documentation to integrate AWS Rekognition node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awsrekognition.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awsrekognition.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsrekognition) |
| AWS S3 — Learn how to use the AWS S3 node in n8n. Follow technical documentation to integrate AWS S3 node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awss3.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awss3.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3) |
| AWS SES — Learn how to use the AWS SES node in n8n. Follow technical documentation to integrate AWS SES node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awsses.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awsses.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awsses) |
| AWS SNS — Learn how to use the AWS SNS node in n8n. Follow technical documentation to integrate AWS SNS node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awssns.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awssns.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awssns) |
| AWS SQS — Learn how to use the AWS SQS node in n8n. Follow technical documentation to integrate AWS SQS node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awssqs.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awssqs.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awssqs) |
| AWS Textract — Learn how to use the AWS Textract node in n8n. Follow technical documentation to integrate AWS Textract node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awstextract.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awstextract.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awstextract) |
| AWS Transcribe — Learn how to use the AWS Transcribe node in n8n. Follow technical documentation to integrate AWS Transcribe node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.awstranscribe.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.awstranscribe.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awstranscribe) |
| Azure Cosmos DB — Learn how to use the Azure Cosmos DB node in n8n. Follow technical documentation to integrate Azure Cosmos DB node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb) |
| Azure Storage — Learn how to use the Azure Storage node in n8n. Follow technical documentation to integrate Azure Storage node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.azurestorage.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage) |
| BambooHR — Learn how to use the BambooHR node in n8n. Follow technical documentation to integrate BambooHR node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.bamboohr.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.bamboohr.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.bamboohr) |
| Bannerbear — Learn how to use the Bannerbear node in n8n. Follow technical documentation to integrate Bannerbear node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.bannerbear.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.bannerbear.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.bannerbear) |
| Baserow — Learn how to use the Baserow node in n8n. Follow technical documentation to integrate Baserow node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.baserow.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.baserow.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.baserow) |
| Beeminder — Learn how to use the Beeminder node in n8n. Follow technical documentation to integrate Beeminder node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.beeminder.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.beeminder.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.beeminder) |
| Bitly — Learn how to use the Bitly node in n8n. Follow technical documentation to integrate Bitly node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.bitly.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.bitly.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.bitly) |
| Bitwarden — Learn how to use the Bitwarden node in n8n. Follow technical documentation to integrate Bitwarden node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.bitwarden.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.bitwarden.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.bitwarden) |
| Box — Learn how to use the Box node in n8n. Follow technical documentation to integrate Box node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.box.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.box.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.box) |
| Brandfetch — Learn how to use the Brandfetch node in n8n. Follow technical documentation to integrate Brandfetch node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.brandfetch.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.brandfetch.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.brandfetch) |
| Brevo — Learn how to use the Brevo node in n8n. Follow technical documentation to integrate Brevo node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.brevo.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.brevo.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.brevo) |
| Bubble — Learn how to use the Bubble node in n8n. Follow technical documentation to integrate Bubble node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.bubble.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.bubble.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.bubble) |
| Chargebee — Learn how to use the Chargebee node in n8n. Follow technical documentation to integrate Chargebee node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.chargebee.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.chargebee.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.chargebee) |
| CircleCI — Learn how to use the CircleCI node in n8n. Follow technical documentation to integrate CircleCI node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.circleci.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.circleci.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.circleci) |
| Webex by Cisco — Learn how to use the Webex by Cisco node in n8n. Follow technical documentation to integrate Webex by Cisco node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.ciscowebex.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.ciscowebex.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ciscowebex) |
| Clearbit — Learn how to use the Clearbit node in n8n. Follow technical documentation to integrate Clearbit node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.clearbit.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.clearbit.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clearbit) |
| ClickUp — Learn how to use the ClickUp node in n8n. Follow technical documentation to integrate ClickUp node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.clickup.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.clickup.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup) |
| Clockify — Learn how to use the Clockify node in n8n. Follow technical documentation to integrate Clockify node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.clockify.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.clockify.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clockify) |
| Cloudflare — Learn how to use the Cloudflare node in n8n. Follow technical documentation to integrate Cloudflare node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.cloudflare.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.cloudflare.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cloudflare) |
| Cockpit — Learn how to use the Cockpit node in n8n. Follow technical documentation to integrate Cockpit node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.cockpit.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.cockpit.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cockpit) |
| Coda — Learn how to use the Coda node in n8n. Follow technical documentation to integrate Coda node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.coda.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.coda.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.coda) |
| CoinGecko — Learn how to use the CoinGecko node in n8n. Follow technical documentation to integrate CoinGecko node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.coingecko.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.coingecko.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.coingecko) |
| Contentful — Learn how to use the Contentful node in n8n. Follow technical documentation to integrate Contentful node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.contentful.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.contentful.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.contentful) |
| ConvertKit — Learn how to use the ConvertKit node in n8n. Follow technical documentation to integrate ConvertKit node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.convertkit.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.convertkit.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.convertkit) |
| Copper — Learn how to use the Copper node in n8n. Follow technical documentation to integrate Copper node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.copper.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.copper.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.copper) |
| Cortex — Learn how to use the Cortex node in n8n. Follow technical documentation to integrate Cortex node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.cortex.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.cortex.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cortex) |
| CrateDB — Learn how to use the CrateDB node in n8n. Follow technical documentation to integrate CrateDB node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.cratedb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.cratedb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb) |
| Customer.io — Learn how to use the Customer.io node in n8n. Follow technical documentation to integrate Customer.io node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.customerio.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.customerio.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.customerio) |
| Databricks — Learn how to use the Databricks node in n8n. Follow technical documentation to integrate Databricks node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.databricks.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.databricks.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.databricks) |
| DeepL — Learn how to use the DeepL node in n8n. Follow technical documentation to integrate DeepL node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.deepl.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.deepl.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.deepl) |
| Demio — Learn how to use the Demio node in n8n. Follow technical documentation to integrate Demio node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.demio.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.demio.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.demio) |
| DHL — Learn how to use the DHL node in n8n. Follow technical documentation to integrate DHL node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.dhl.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.dhl.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dhl) |
| Discord — Learn how to use the Discord node in n8n. Follow technical documentation to integrate Discord node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.discord.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.discord.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord) |
| Common issues — Documentation for common issues and questions in the Discord node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues) |
| Discourse — Learn how to use the Discourse node in n8n. Follow technical documentation to integrate Discourse node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.discourse.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.discourse.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discourse) |
| Disqus — Learn how to use the Disqus node in n8n. Follow technical documentation to integrate Disqus node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.disqus.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.disqus.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.disqus) |
| Drift — Learn how to use the Drift node in n8n. Follow technical documentation to integrate Drift node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.drift.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.drift.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.drift) |
| Dropbox — Learn how to use the Dropbox node in n8n. Follow technical documentation to integrate Dropbox node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.dropbox.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.dropbox.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropbox) |
| Dropcontact — Learn how to use the Dropcontact node in n8n. Follow technical documentation to integrate Dropcontact node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.dropcontact.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.dropcontact.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropcontact) |
| E-goi — Learn how to use the E=goi node in n8n. Follow technical documentation to integrate E=goi node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.egoi.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.egoi.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.egoi) |
| Elasticsearch — Learn how to use the Elasticsearch node in n8n. Follow technical documentation to integrate Elasticsearch node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.elasticsearch.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.elasticsearch.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.elasticsearch) |
| Elastic Security — Learn how to use the Elastic Security node in n8n. Follow technical documentation to integrate Elastic Security node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.elasticsecurity.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.elasticsecurity.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.elasticsecurity) |
| Emelia — Learn how to use the Emelia node in n8n. Follow technical documentation to integrate Emelia node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.emelia.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.emelia.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.emelia) |
| ERPNext — Learn how to use the ERPNext node in n8n. Follow technical documentation to integrate ERPNext node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.erpnext.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.erpnext.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.erpnext) |
| Facebook Graph API — Learn how to use the Facebook Graph API node in n8n. Follow technical documentation to integrate Facebook Graph API node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi) |
| FileMaker — Learn how to use the FileMaker node in n8n. Follow technical documentation to integrate FileMaker node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.filemaker.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.filemaker.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.filemaker) |
| Flow — Learn how to use the Flow node in n8n. Follow technical documentation to integrate Flow node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.flow.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.flow.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.flow) |
| Freshdesk — Learn how to use the Freshdesk node in n8n. Follow technical documentation to integrate Freshdesk node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.freshdesk.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.freshdesk.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.freshdesk) |
| Freshservice — Learn how to use the Freshservice node in n8n. Follow technical documentation to integrate Freshservice node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.freshservice.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.freshservice.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.freshservice) |
| Freshworks CRM — Learn how to use the Freshworks CRM node in n8n. Follow technical documentation to integrate Freshworks CRM node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.freshworkscrm.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.freshworkscrm.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.freshworkscrm) |
| GetResponse — Learn how to use the GetResponse node in n8n. Follow technical documentation to integrate GetResponse node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.getresponse.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.getresponse.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.getresponse) |
| Ghost — Learn how to use the Ghost node in n8n. Follow technical documentation to integrate Ghost node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.ghost.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.ghost.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost) |
| GitHub — Learn how to use the GitHub node in n8n. Follow technical documentation to integrate GitHub node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.github.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.github.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github) |
| GitLab — Learn how to use the GitLab node in n8n. Follow technical documentation to integrate GitLab node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab) |
| Gmail — Learn how to use the Gmail node in n8n. Follow technical documentation to integrate Gmail node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gmail.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail) |
| Draft Operations — Learn how to use the Draft Operations of the Gmail node in n8n. Follow technical documentation to integrate Draft Operations into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations) |
| Label Operations — Learn how to use the Label Operations of the Gmail node in n8n. Follow technical documentation to integrate Label Operations into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations) |
| Message Operations — Learn how to use the Message Operations of the Gmail node in n8n. Follow technical documentation to integrate Message Operations into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations) |
| Thread Operations — Learn how to use the Thread Operations of the Gmail node in n8n. Follow technical documentation to integrate Thread Operations into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations) |
| Common issues — Documentation for common issues and questions in the Gmail node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues) |
| Gong — Learn how to use the Gong node in n8n. Follow technical documentation to integrate Gong node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gong.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gong.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gong) |
| Google Ads — Learn how to use the Google Ads node in n8n. Follow technical documentation to integrate Google Ads node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googleads.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googleads.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleads) |
| Google Analytics — Learn how to use the Google Analytics node in n8n. Follow technical documentation to integrate Google Analytics node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googleanalytics.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googleanalytics.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleanalytics) |
| Google BigQuery — Learn how to use the Google BigQuery node in n8n. Follow technical documentation to integrate Google BigQuery node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery) |
| Google Books — Learn how to use the Google Books node in n8n. Follow technical documentation to integrate Google Books node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks) |
| Google Business Profile — Learn how to use the Google Business Profile node in n8n. Follow technical documentation to integrate Google Business Profile node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile) |
| Google Calendar — Learn how to use the Google Calendar node in n8n. Follow technical documentation to integrate Google Calendar node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar) |
| Calendar operations — Documentation for the Calendar operations in Google Calendar node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials inform | [`integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations) |
| Event operations — Documentation for the Event operations in Google Calendar node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials informati | [`integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations) |
| Google Chat — Learn how to use the Google Chat node in n8n. Follow technical documentation to integrate Google Chat node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat) |
| Google Cloud Firestore — Learn how to use the Google Cloud Firestore node in n8n. Follow technical documentation to integrate Google Cloud Firestore node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlecloudfirestore.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudfirestore.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudfirestore) |
| Google Cloud Natural Language — Learn how to use the Google Cloud Natural Language node in n8n. Follow technical documentation to integrate Google Cloud Natural Language node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlecloudnaturallanguage.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudnaturallanguage.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudnaturallanguage) |
| Google Cloud Realtime Database — Learn how to use the Google Cloud Realtime Database node in n8n. Follow technical documentation to integrate Google Cloud Realtime Database node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudrealtimedatabase) |
| Google Cloud Storage — Learn how to use the Google Cloud Storage node in n8n. Follow technical documentation to integrate Google Cloud Storage node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage) |
| Google Contacts — Learn how to use the Google Contacts node in n8n. Follow technical documentation to integrate Google Contacts node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlecontacts.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecontacts.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecontacts) |
| Google Docs — Learn how to use the Google Docs node in n8n. Follow technical documentation to integrate Google Docs node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googledocs.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledocs.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledocs) |
| Google Drive — Learn how to use the Google Drive node in n8n. Follow technical documentation to integrate Google Drive node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googledrive.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive) |
| File operations — Documentation for the File operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations) |
| File and Folder operations — Documentation for the File and Folder operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials in | [`integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations) |
| Folder operations — Documentation for the Folder operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information | [`integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations) |
| Shared Drive operations — Documentation for the Shared Drive operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials infor | [`integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations) |
| Common issues — Documentation for common questions and solutions in the Google Drive node in n8n, a workflow automation platform. Includes details of the issue and suggested resolutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues) |
| Google Gemini — Learn how to use the Google Gemini node in n8n. Follow technical documentation to integrate Google Gemini node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini) |
| Google Perspective — Learn how to use the Google Perspective node in n8n. Follow technical documentation to integrate Google Perspective node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googleperspective.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googleperspective.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleperspective) |
| Google Sheets — Documentation for the Google Sheets node in n8n. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlesheets.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets) |
| Document operations — Documentation for the Document operations in Google Sheets node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials informat | [`integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations) |
| Sheet Within Document operations — Documentation for the Sheet operations in Google Sheets node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information | [`integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations) |
| Common issues — Documentation for common questions and solutions in the Google Sheets node in n8n, a workflow automation platform. Includes details of the issue and suggested resolutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues) |
| Google Slides — Learn how to use the Google Slides node in n8n. Follow technical documentation to integrate Google Slides node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googleslides.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googleslides.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides) |
| Google Tasks — Learn how to use the Google Tasks node in n8n. Follow technical documentation to integrate Google Tasks node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googletasks.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googletasks.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googletasks) |
| Google Translate — Learn how to use the Google Translate node in n8n. Follow technical documentation to integrate Google Translate node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.googletranslate.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.googletranslate.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googletranslate) |
| Google Workspace Admin — Learn how to use the Google Workspace Admin node in n8n. Follow technical documentation to integrate Google Workspace Admin node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin) |
| Gotify — Learn how to use the Gotify node in n8n. Follow technical documentation to integrate Gotify node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gotify.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gotify.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotify) |
| GoToWebinar — Learn how to use the GoToWebinar node in n8n. Follow technical documentation to integrate GoToWebinar node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.gotowebinar.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.gotowebinar.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gotowebinar) |
| Grafana — Learn how to use the Grafana node in n8n. Follow technical documentation to integrate Grafana node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.grafana.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.grafana.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana) |
| Grist — Learn how to use the Grist node in n8n. Follow technical documentation to integrate Grist node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.grist.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.grist.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grist) |
| Hacker News — Learn how to use the Hacker News node in n8n. Follow technical documentation to integrate Hacker News node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.hackernews.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.hackernews.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hackernews) |
| HaloPSA — Learn how to use the HaloPSA node in n8n. Follow technical documentation to integrate HaloPSA node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.halopsa.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.halopsa.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.halopsa) |
| Harvest — Learn how to use the Harvest node in n8n. Follow technical documentation to integrate Harvest node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.harvest.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.harvest.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest) |
| Help Scout — Learn how to use the Help Scout node in n8n. Follow technical documentation to integrate Help Scout node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.helpscout.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.helpscout.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.helpscout) |
| HighLevel — Learn how to use the HighLevel node in n8n. Follow technical documentation to integrate HighLevel node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.highlevel.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.highlevel.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.highlevel) |
| Home Assistant — Learn how to use the Home Assistant node in n8n. Follow technical documentation to integrate Home Assistant node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.homeassistant.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant) |
| HubSpot — Learn how to use the HubSpot node in n8n. Follow technical documentation to integrate HubSpot node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot) |
| Humantic AI — Learn how to use the Humantic AI node in n8n. Follow technical documentation to integrate Humantic AI node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.humanticai.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.humanticai.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.humanticai) |
| Hunter — Learn how to use the Hunter node in n8n. Follow technical documentation to integrate Hunter node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.hunter.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.hunter.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hunter) |
| Intercom — Learn how to use the Intercom node in n8n. Follow technical documentation to integrate Intercom node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.intercom.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.intercom.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.intercom) |
| Invoice Ninja — Learn how to use the Invoice Ninja node in n8n. Follow technical documentation to integrate Invoice Ninja node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja) |
| Iterable — Learn how to use the Iterable node in n8n. Follow technical documentation to integrate Iterable node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.iterable.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.iterable.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.iterable) |
| Jenkins — Learn how to use the Jenkins node in n8n. Follow technical documentation to integrate Jenkins node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.jenkins.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.jenkins.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jenkins) |
| Jina AI — Learn how to use the Jina AI node in n8n. Follow technical documentation to integrate Jina AI node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.jinaai.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.jinaai.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jinaai) |
| Jira Software — Learn how to use the Jira Software node in n8n. Follow technical documentation to integrate Jira Software node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.jira.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.jira.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira) |
| Kafka — Learn how to use the Kafka node in n8n. Follow technical documentation to integrate Kafka node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.kafka.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.kafka.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kafka) |
| Keap — Learn how to use the Keap node in n8n. Follow technical documentation to integrate Keap node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.keap.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.keap.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.keap) |
| Kitemaker — Learn how to use the Kitemaker node in n8n. Follow technical documentation to integrate Kitemaker node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.kitemaker.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.kitemaker.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kitemaker) |
| KoboToolbox — Learn how to use the KoboToolbox node in n8n. Follow technical documentation to integrate KoboToolbox node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox) |
| Lemlist — Learn how to use the Lemlist node in n8n. Follow technical documentation to integrate Lemlist node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.lemlist.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.lemlist.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist) |
| Line — Learn how to use the Line node in n8n. Follow technical documentation to integrate Line node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.line.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.line.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.line) |
| Linear — Learn how to use the Linear node in n8n. Follow technical documentation to integrate Linear node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.linear.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.linear.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linear) |
| LingvaNex — Learn how to use the LingvaNex node in n8n. Follow technical documentation to integrate LingvaNex node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.lingvanex.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.lingvanex.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lingvanex) |
| LinkedIn — Learn how to use the LinkedIn node in n8n. Follow technical documentation to integrate LinkedIn node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.linkedin.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.linkedin.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linkedin) |
| LoneScale — Learn how to use the LoneScale node in n8n. Follow technical documentation to integrate LoneScale node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.lonescale.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.lonescale.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lonescale) |
| Magento 2 — Learn how to use the Magento 2 node in n8n. Follow technical documentation to integrate Magento 2 node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.magento2.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.magento2.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.magento2) |
| Mailcheck — Learn how to use the Mailcheck node in n8n. Follow technical documentation to integrate Mailcheck node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mailcheck.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailcheck.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailcheck) |
| Mailchimp — Learn how to use the Mailchimp node in n8n. Follow technical documentation to integrate Mailchimp node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mailchimp.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp) |
| MailerLite — Learn how to use the MailerLite node in n8n. Follow technical documentation to integrate MailerLite node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mailerlite.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailerlite.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailerlite) |
| Mailgun — Learn how to use the Mailgun node in n8n. Follow technical documentation to integrate Mailgun node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mailgun.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailgun.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailgun) |
| Mailjet — Learn how to use the Mailjet node in n8n. Follow technical documentation to integrate Mailjet node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mailjet.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailjet.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailjet) |
| Mandrill — Learn how to use the Mandrill node in n8n. Follow technical documentation to integrate Mandrill node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mandrill.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mandrill.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mandrill) |
| marketstack — Learn how to use the marketstack node in n8n. Follow technical documentation to integrate marketstack node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.marketstack.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.marketstack.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.marketstack) |
| Matrix — Learn how to use the Matrix node in n8n. Follow technical documentation to integrate Matrix node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.matrix.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.matrix.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.matrix) |
| Mattermost — Learn how to use the Mattermost node in n8n. Follow technical documentation to integrate Mattermost node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mattermost.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mattermost.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mattermost) |
| Mautic — Learn how to use the Mautic node in n8n. Follow technical documentation to integrate Mautic node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mautic.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mautic.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mautic) |
| Medium — Learn how to use the Medium node in n8n. Follow technical documentation to integrate Medium node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.medium.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.medium.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.medium) |
| MessageBird — Learn how to use the MessageBird node in n8n. Follow technical documentation to integrate MessageBird node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.messagebird.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.messagebird.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.messagebird) |
| Metabase — Learn how to use the Metabase node in n8n. Follow technical documentation to integrate Metabase node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.metabase.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.metabase.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.metabase) |
| Microsoft Dynamics CRM — Learn how to use the Microsoft Dynamics CRM node in n8n. Follow technical documentation to integrate Microsoft Dynamics CRM node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftdynamicscrm.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftdynamicscrm.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftdynamicscrm) |
| Microsoft Entra ID — Learn how to use the Microsoft Entra ID node in n8n. Follow technical documentation to integrate Microsoft Entra ID node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra) |
| Microsoft Excel (OneDrive) — Learn how to use the Microsoft Excel (OneDrive) node in n8n. Follow technical documentation to integrate Microsoft Excel (OneDrive) node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel) |
| Microsoft Excel (SharePoint) — Learn how to use the Microsoft Excel (SharePoint) node in n8n. Follow technical documentation to integrate Microsoft Excel (SharePoint) node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcelsharepoint.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcelsharepoint.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcelsharepoint) |
| Microsoft Graph Security — Learn how to use the Microsoft Graph Security node in n8n. Follow technical documentation to integrate Microsoft Graph Security node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity) |
| Microsoft OneDrive — Learn how to use the Microsoft OneDrive node in n8n. Follow technical documentation to integrate Microsoft OneDrive node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive) |
| Microsoft Outlook — Learn how to use the Microsoft Outlook node in n8n. Follow technical documentation to integrate Microsoft Outlook node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook) |
| Microsoft SharePoint — Learn how to use the Microsoft SharePoint node in n8n. Follow technical documentation to integrate Microsoft SharePoint node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint) |
| Microsoft SQL — Learn how to use the Microsoft SQL node in n8n. Follow technical documentation to integrate Microsoft SQL node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftsql.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsql.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsql) |
| Microsoft Teams — Learn how to use the Microsoft Teams node in n8n. Follow technical documentation to integrate Microsoft Teams node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams) |
| Microsoft To Do — Learn how to use the Microsoft To Do node in n8n. Follow technical documentation to integrate Microsoft To Do node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo) |
| Mindee — Learn how to use the Mindee node in n8n. Follow technical documentation to integrate Mindee node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mindee.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mindee.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mindee) |
| MISP — Learn how to use the MISP node in n8n. Follow technical documentation to integrate MISP node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.misp.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.misp.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.misp) |
| Mistral AI — Learn how to use the Mistral AI node in n8n. Follow technical documentation to integrate Mistral AI node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mistralai.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mistralai.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai) |
| MiniMax — The MiniMax node lets you interact with MiniMax AI models from n8n. This documentation explains how to integrate MiniMax into your n8n workflows to generate images, produce speech from text, generate | [`integrations/builtin/app-nodes/n8n-nodes-langchain.minimax.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.minimax.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.minimax) |
| Mocean — Learn how to use the Mocean node in n8n. Follow technical documentation to integrate Mocean node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mocean.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mocean.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mocean) |
| monday.com — Learn how to use the monday.com node in n8n. Follow technical documentation to integrate monday.com node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mondaycom.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom) |
| MongoDB — Learn how to use the MongoDB node in n8n. Follow technical documentation to integrate MongoDB node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mongodb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mongodb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mongodb) |
| Monica CRM — Learn how to use the Monica CRM node in n8n. Follow technical documentation to integrate Monica CRM node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.monicacrm.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.monicacrm.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.monicacrm) |
| Moonshot Kimi — The Moonshot Kimi node lets you interact with Moonshot Kimi AI models from n8n. This documentation explains how to send messages to models, attach images, and analyze images using the node's operation | [`integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot) |
| MQTT — Learn how to use the MQTT node in n8n. Follow technical documentation to integrate MQTT node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mqtt.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mqtt.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mqtt) |
| MSG91 — Learn how to use the MSG91 node in n8n. Follow technical documentation to integrate MSG91 node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.msg91.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.msg91.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.msg91) |
| MySQL — Learn how to use the MySQL node in n8n. Follow technical documentation to integrate MySQL node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.mysql.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mysql.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql) |
| Common issues — Documentation for common issues and questions in the MySQL node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues) |
| Customer Datastore (n8n Training) — Learn how to use the Customer Datastore (n8n Training) node in n8n. Follow technical documentation to integrate Customer Datastore (n8n Training) node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomerdatastore.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomerdatastore.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomerdatastore) |
| Customer Messenger (n8n Training) — Learn how to use the Customer Messenger (n8n Training) node in n8n. Follow technical documentation to integrate Customer Messenger (n8n Training) node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomermessenger.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomermessenger.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomermessenger) |
| NASA — Learn how to use the NASA node in n8n. Follow technical documentation to integrate NASA node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.nasa.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.nasa.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nasa) |
| Netlify — Learn how to use the Netlify node in n8n. Follow technical documentation to integrate Netlify node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.netlify.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.netlify.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.netlify) |
| Netscaler ADC — Learn how to use the Netscaler ADC node in n8n. Follow technical documentation to integrate Netscaler ADC node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.netscaleradc.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.netscaleradc.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.netscaleradc) |
| Nextcloud — Learn how to use the Nextcloud node in n8n. Follow technical documentation to integrate Nextcloud node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.nextcloud.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud) |
| NocoDB — Learn how to use the NocoDB node in n8n. Follow technical documentation to integrate NocoDB node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.nocodb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.nocodb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nocodb) |
| Notion — Learn how to use the Notion node in n8n. Follow technical documentation to integrate Notion node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.notion.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.notion.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion) |
| Common issues — Documentation for common issues and questions in the Notion node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues) |
| npm — Learn how to use the npm node in n8n. Follow technical documentation to integrate npm node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.npm.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.npm.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.npm) |
| Odoo — Learn how to use the Odoo node in n8n. Follow technical documentation to integrate Odoo node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.odoo.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.odoo.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.odoo) |
| Okta — Learn how to use the Okta node in n8n. Follow technical documentation to integrate Okta node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.okta.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.okta.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.okta) |
| One Simple API — Learn how to use the One Simple API node in n8n. Follow technical documentation to integrate One Simple API node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.onesimpleapi.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.onesimpleapi.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.onesimpleapi) |
| Onfleet — Learn how to use the Onfleet node in n8n. Follow technical documentation to integrate Onfleet node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.onfleet.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.onfleet.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.onfleet) |
| OpenAI — Learn how to use the OpenAI node in n8n. Follow technical documentation to integrate OpenAI node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai) |
| Assistant operations — Documentation for the Assistant operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations) |
| Audio operations — Documentation for the Audio operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations) |
| Conversation operations — Documentation for the Conversation operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations) |
| File operations — Documentation for the File operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations) |
| Image operations — Documentation for the Image operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations) |
| Text operations — Documentation for the Text operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations) |
| Video operations — Documentation for the Video operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations) |
| Common issues — Documentation for common issues and questions in the OpenAI node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues) |
| OpenThesaurus — Learn how to use the OpenThesaurus node in n8n. Follow technical documentation to integrate OpenThesaurus node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.openthesaurus.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.openthesaurus.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.openthesaurus) |
| OpenWeatherMap — Learn how to use the OpenWeatherMap node in n8n. Follow technical documentation to integrate OpenWeatherMap node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.openweathermap.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.openweathermap.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.openweathermap) |
| Oracle Database — Learn how to use the Oracle Database node in n8n. Follow technical documentation to integrate Oracle Database node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.oracledb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.oracledb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oracledb) |
| Oura — Learn how to use the Oura node in n8n. Follow technical documentation to integrate Oura node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.oura.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.oura.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.oura) |
| Paddle — Learn how to use the Paddle node in n8n. Follow technical documentation to integrate Paddle node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.paddle.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.paddle.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.paddle) |
| PagerDuty — Learn how to use the PagerDuty node in n8n. Follow technical documentation to integrate PagerDuty node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.pagerduty.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.pagerduty.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pagerduty) |
| PayPal — Learn how to use the PayPal node in n8n. Follow technical documentation to integrate PayPal node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.paypal.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.paypal.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.paypal) |
| Peekalink — Learn how to use the Peekalink node in n8n. Follow technical documentation to integrate Peekalink node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.peekalink.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.peekalink.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.peekalink) |
| Perplexity — Learn how to use the Perplexity node in n8n. Follow technical documentation to integrate Perplexity node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-langchain.perplexity.md`](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.perplexity.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.perplexity) |
| PhantomBuster — Learn how to use the PhantomBuster node in n8n. Follow technical documentation to integrate PhantomBuster node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.phantombuster.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster) |
| Philips Hue — Learn how to use the Philips Hue node in n8n. Follow technical documentation to integrate Philips Hue node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.philipshue.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.philipshue.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.philipshue) |
| Pipedrive — Learn how to use the Pipedrive node in n8n. Follow technical documentation to integrate Pipedrive node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.pipedrive.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive) |
| Plivo — Learn how to use the Plivo node in n8n. Follow technical documentation to integrate Plivo node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.plivo.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.plivo.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.plivo) |
| PostBin — Learn how to use the PostBin node in n8n. Follow technical documentation to integrate PostBin node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.postbin.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.postbin.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin) |
| Postgres — Learn how to use the Postgres node in n8n. Follow technical documentation to integrate Postgres node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.postgres.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.postgres.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres) |
| Common issues — Documentation for common issues and questions in the Postgres node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues) |
| PostHog — Learn how to use the PostHog node in n8n. Follow technical documentation to integrate PostHog node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.posthog.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.posthog.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.posthog) |
| ProfitWell — Learn how to use the ProfitWell node in n8n. Follow technical documentation to integrate ProfitWell node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.profitwell.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.profitwell.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.profitwell) |
| Pushbullet — Learn how to use the Pushbullet node in n8n. Follow technical documentation to integrate Pushbullet node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.pushbullet.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.pushbullet.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pushbullet) |
| Pushcut — Learn how to use the Pushcut node in n8n. Follow technical documentation to integrate Pushcut node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.pushcut.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.pushcut.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pushcut) |
| Pushover — Learn how to use the Pushover node in n8n. Follow technical documentation to integrate Pushover node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.pushover.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.pushover.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pushover) |
| QuestDB — Learn how to use the QuestDB node in n8n. Follow technical documentation to integrate QuestDB node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.questdb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.questdb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb) |
| Quick Base — Learn how to use the Quick Base node in n8n. Follow technical documentation to integrate Quick Base node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.quickbase.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.quickbase.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickbase) |
| QuickBooks Online — Learn how to use the QuickBooks Online node in n8n. Follow technical documentation to integrate QuickBooks Online node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.quickbooks.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.quickbooks.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickbooks) |
| QuickChart — Learn how to use the QuickChart node in n8n. Follow technical documentation to integrate QuickChart node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.quickchart.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.quickchart.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickchart) |
| RabbitMQ — Learn how to use the RabbitMQ node in n8n. Follow technical documentation to integrate RabbitMQ node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.rabbitmq.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.rabbitmq.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.rabbitmq) |
| Raindrop — Learn how to use the Raindrop node in n8n. Follow technical documentation to integrate Raindrop node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.raindrop.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.raindrop.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.raindrop) |
| Reddit — Learn how to use the Reddit node in n8n. Follow technical documentation to integrate Reddit node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.reddit.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.reddit.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit) |
| Redis — Learn how to use the Redis node in n8n. Follow technical documentation to integrate Redis node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.redis.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.redis.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.redis) |
| Rocket.Chat — Learn how to use the Rocket.Chat node in n8n. Follow technical documentation to integrate Rocket.Chat node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.rocketchat.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.rocketchat.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.rocketchat) |
| Rundeck — Learn how to use the Rundeck node in n8n. Follow technical documentation to integrate Rundeck node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.rundeck.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.rundeck.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.rundeck) |
| S3 — Learn how to use the S3 node in n8n. Follow technical documentation to integrate S3 node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.s3.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.s3.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3) |
| Salesforce — Learn how to use the Salesforce node in n8n. Follow technical documentation to integrate Salesforce node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.salesforce.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.salesforce.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce) |
| Salesmate — Learn how to use the Salesmate node in n8n. Follow technical documentation to integrate Salesmate node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.salesmate.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.salesmate.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesmate) |
| SeaTable — Learn how to use the SeaTable node in n8n. Follow technical documentation to integrate SeaTable node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.seatable.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.seatable.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.seatable) |
| SecurityScorecard — Learn how to use the SecurityScorecard node in n8n. Follow technical documentation to integrate SecurityScorecard node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard) |
| Segment — Learn how to use the Segment node in n8n. Follow technical documentation to integrate Segment node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.segment.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.segment.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment) |
| SendGrid — Learn how to use the SendGrid node in n8n. Follow technical documentation to integrate SendGrid node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.sendgrid.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.sendgrid.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sendgrid) |
| Sendy — Learn how to use the Sendy node in n8n. Follow technical documentation to integrate Sendy node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.sendy.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.sendy.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sendy) |
| Sentry.io — Learn how to use the Sentry.io node in n8n. Follow technical documentation to integrate Sentry.io node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.sentryio.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.sentryio.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio) |
| ServiceNow — Learn how to use the ServiceNow node in n8n. Follow technical documentation to integrate ServiceNow node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.servicenow.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.servicenow.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.servicenow) |
| seven — Learn how to use the seven node in n8n. Follow technical documentation to integrate seven node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.sms77.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.sms77.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sms77) |
| Shopify — Learn how to use the Shopify node in n8n. Follow technical documentation to integrate Shopify node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.shopify.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.shopify.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.shopify) |
| SIGNL4 — Learn how to use the SIGNL4 node in n8n. Follow technical documentation to integrate SIGNL4 node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.signl4.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.signl4.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.signl4) |
| Slack — Learn how to use the Slack node in n8n. Follow technical documentation to integrate Slack node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.slack.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.slack.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack) |
| Approvals — Learn how approvers can approve or decline n8n workflow actions directly inside Slack with the Slack node's Send and Wait for Response operation. | [`integrations/builtin/app-nodes/n8n-nodes-base.slack/approvals.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.slack/approvals.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/approvals) |
| Snowflake — Learn how to use the Snowflake node in n8n. Follow technical documentation to integrate Snowflake node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.snowflake.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.snowflake.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.snowflake) |
| Splunk — Learn how to use the Splunk node in n8n. Follow technical documentation to integrate Splunk node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.splunk.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.splunk.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.splunk) |
| Spotify — Learn how to use the Spotify node in n8n. Follow technical documentation to integrate Spotify node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.spotify.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.spotify.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.spotify) |
| Stackby — Learn how to use the Stackby node in n8n. Follow technical documentation to integrate Stackby node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.stackby.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.stackby.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stackby) |
| Storyblok — Learn how to use the Storyblok node in n8n. Follow technical documentation to integrate Storyblok node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.storyblok.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.storyblok.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.storyblok) |
| Strapi — Learn how to use the Strapi node in n8n. Follow technical documentation to integrate Strapi node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.strapi.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.strapi.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.strapi) |
| Strava — Learn how to use the Strava node in n8n. Follow technical documentation to integrate Strava node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.strava.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.strava.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.strava) |
| Stripe — Learn how to use the Stripe node in n8n. Follow technical documentation to integrate Stripe node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.stripe.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.stripe.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.stripe) |
| Supabase — Learn how to use the Supabase node in n8n. Follow technical documentation to integrate Supabase node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.supabase.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.supabase.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase) |
| Common issues — Documentation for common issues and questions in the Supabase node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues) |
| SyncroMSP — Learn how to use the SyncroMSP node in n8n. Follow technical documentation to integrate SyncroMSP node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.syncromsp.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.syncromsp.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.syncromsp) |
| Taiga — Learn how to use the Taiga node in n8n. Follow technical documentation to integrate Taiga node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.taiga.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.taiga.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.taiga) |
| Tapfiliate — Learn how to use the Tapfiliate node in n8n. Follow technical documentation to integrate Tapfiliate node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.tapfiliate.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.tapfiliate.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.tapfiliate) |
| Telegram — Documentation for the Telegram node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information. | [`integrations/builtin/app-nodes/n8n-nodes-base.telegram.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram) |
| Chat operations — Documentation for the Chat operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all Chat operations. | [`integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations) |
| Callback operations — Documentation for the Callback operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all Callback operations. | [`integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations) |
| File operations — Documentation for the File operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all File operations. | [`integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations) |
| Message operations — Documentation for the Message operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all Message operations. | [`integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations) |
| Common issues — Documentation for common issues and questions in the Telegram node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues) |
| TheHive — Learn how to use the TheHive node in n8n. Follow technical documentation to integrate TheHive node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.thehive.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.thehive.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive) |
| TheHive 5 — Learn how to use the TheHive 5 node in n8n. Follow technical documentation to integrate TheHive 5 node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5) |
| TimescaleDB — Learn how to use the TimescaleDB node in n8n. Follow technical documentation to integrate TimescaleDB node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.timescaledb.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb) |
| Todoist — Learn how to use the Todoist node in n8n. Follow technical documentation to integrate Todoist node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.todoist.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.todoist.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.todoist) |
| Travis CI — Learn how to use the Travis CI node in n8n. Follow technical documentation to integrate Travis CI node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.travisci.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.travisci.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.travisci) |
| Trello — Learn how to use the Trello node in n8n. Follow technical documentation to integrate Trello node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.trello.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.trello.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.trello) |
| Twake — Learn how to use the Twake node in n8n. Follow technical documentation to integrate Twake node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.twake.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.twake.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twake) |
| Twilio — Learn how to use the Twilio node in n8n. Follow technical documentation to integrate Twilio node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.twilio.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.twilio.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twilio) |
| Twist — Learn how to use the Twist node in n8n. Follow technical documentation to integrate Twist node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.twist.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.twist.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twist) |
| Unleashed Software — Learn how to use the Unleashed Software node in n8n. Follow technical documentation to integrate Unleashed Software node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.unleashedsoftware.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.unleashedsoftware.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.unleashedsoftware) |
| UpLead — Learn how to use the UpLead node in n8n. Follow technical documentation to integrate UpLead node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.uplead.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.uplead.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.uplead) |
| uProc — Learn how to use the uProc node in n8n. Follow technical documentation to integrate uProc node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.uproc.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.uproc.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.uproc) |
| UptimeRobot — Learn how to use the UptimeRobot node in n8n. Follow technical documentation to integrate UptimeRobot node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.uptimerobot.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.uptimerobot.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.uptimerobot) |
| urlscan.io — Learn how to use the urlscan.io node in n8n. Follow technical documentation to integrate urlscan.io node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.urlscanio.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.urlscanio.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.urlscanio) |
| Venafi TLS Protect Cloud — Learn how to use the Venafi TLS Protect Cloud node in n8n. Follow technical documentation to integrate Venafi TLS Protect Cloud node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud) |
| Venafi TLS Protect Datacenter — Learn how to use the Venafi TLS Protect Datacenter node in n8n. Follow technical documentation to integrate Venafi TLS Protect Datacenter node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectdatacenter.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectdatacenter.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectdatacenter) |
| Vero — Learn how to use the Vero node in n8n. Follow technical documentation to integrate Vero node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.vero.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.vero.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.vero) |
| Vonage — Learn how to use the Vonage node in n8n. Follow technical documentation to integrate Vonage node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.vonage.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.vonage.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.vonage) |
| Webflow — Learn how to use the Webflow node in n8n. Follow technical documentation to integrate Webflow node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.webflow.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.webflow.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.webflow) |
| Wekan — Learn how to use the Wekan node in n8n. Follow technical documentation to integrate Wekan node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.wekan.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.wekan.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan) |
| WhatsApp Business Cloud — Learn how to use the WhatsApp Business Cloud node in n8n. Follow technical documentation to integrate WhatsApp Business Cloud node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.whatsapp.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp) |
| Common issues — Documentation for common issues and questions in the WhatsApp Business Cloud node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues) |
| Wise — Learn how to use the Wise node in n8n. Follow technical documentation to integrate Wise node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.wise.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.wise.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wise) |
| WooCommerce — Learn how to use the WooCommerce node in n8n. Follow technical documentation to integrate WooCommerce node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.woocommerce.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.woocommerce.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.woocommerce) |
| WordPress — Learn how to use the WordPress node in n8n. Follow technical documentation to integrate WordPress node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.wordpress.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.wordpress.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wordpress) |
| X (Formerly Twitter) — Learn how to use the X (Formerly Twitter) node in n8n. Follow technical documentation to integrate X (Formerly Twitter) node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.twitter.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.twitter.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twitter) |
| Xero — Learn how to use the Xero node in n8n. Follow technical documentation to integrate Xero node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.xero.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.xero.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.xero) |
| Yourls — Learn how to use the Yourls node in n8n. Follow technical documentation to integrate Yourls node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.yourls.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.yourls.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.yourls) |
| YouTube — Learn how to use the YouTube node in n8n. Follow technical documentation to integrate YouTube node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.youtube.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.youtube.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube) |
| Zammad — Learn how to use the Zammad node in n8n. Follow technical documentation to integrate Zammad node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.zammad.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.zammad.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zammad) |
| Zendesk — Learn how to use the Zendesk node in n8n. Follow technical documentation to integrate Zendesk node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.zendesk.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.zendesk.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk) |
| Zoho CRM — Learn how to use the Zoho CRM node in n8n. Follow technical documentation to integrate Zoho CRM node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.zohocrm.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.zohocrm.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zohocrm) |
| Zoom — Learn how to use the Zoom node in n8n. Follow technical documentation to integrate Zoom node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.zoom.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.zoom.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zoom) |
| Zulip — Learn how to use the Zulip node in n8n. Follow technical documentation to integrate Zulip node into your workflows. | [`integrations/builtin/app-nodes/n8n-nodes-base.zulip.md`](pages/integrations/builtin/app-nodes/n8n-nodes-base.zulip.md) | [docs](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zulip) |
| Trigger nodes | [`integrations/builtin/trigger-nodes.md`](pages/integrations/builtin/trigger-nodes.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes) |
| ActiveCampaign Trigger — Learn how to use the ActiveCampaign Trigger node in n8n. Follow technical documentation to integrate ActiveCampaign Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.activecampaigntrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.activecampaigntrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.activecampaigntrigger) |
| Acuity Scheduling Trigger — Learn how to use the Acuity Scheduling Trigger node in n8n. Follow technical documentation to integrate Acuity Scheduling Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.acuityschedulingtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.acuityschedulingtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.acuityschedulingtrigger) |
| Affinity Trigger — Learn how to use the Affinity Trigger node in n8n. Follow technical documentation to integrate Affinity Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.affinitytrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.affinitytrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.affinitytrigger) |
| Airtable Trigger — Learn how to use the Airtable Trigger node in n8n. Follow technical documentation to integrate Airtable Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger) |
| AMQP Trigger — Learn how to use the AMQP Trigger node in n8n. Follow technical documentation to integrate AMQP Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.amqptrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.amqptrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.amqptrigger) |
| Asana Trigger — Learn how to use the Asana Trigger node in n8n. Follow technical documentation to integrate Asana Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.asanatrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.asanatrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.asanatrigger) |
| Autopilot Trigger — Learn how to use the Autopilot Trigger node in n8n. Follow technical documentation to integrate Autopilot Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.autopilottrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.autopilottrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.autopilottrigger) |
| AWS SNS Trigger — Learn how to use the AWS SNS Trigger node in n8n. Follow technical documentation to integrate AWS SNS Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.awssnstrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.awssnstrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.awssnstrigger) |
| Bitbucket Trigger — Learn how to use the Bitbucket Trigger node in n8n. Follow technical documentation to integrate Bitbucket Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.bitbuckettrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.bitbuckettrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.bitbuckettrigger) |
| Box Trigger — Learn how to use the Box Trigger node in n8n. Follow technical documentation to integrate Box Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger) |
| Brevo Trigger — Learn how to use the Brevo Trigger node in n8n. Follow technical documentation to integrate Brevo Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.brevotrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.brevotrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.brevotrigger) |
| Calendly Trigger — Learn how to use the Calendly Trigger node in n8n. Follow technical documentation to integrate Calendly Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger) |
| Cal Trigger — Learn how to use the Cal Trigger node in n8n. Follow technical documentation to integrate Cal Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger) |
| Chargebee Trigger — Learn how to use the Chargebee Trigger node in n8n. Follow technical documentation to integrate Chargebee Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger) |
| ClickUp Trigger — Learn how to use the ClickUp Trigger node in n8n. Follow technical documentation to integrate ClickUp Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger) |
| Clockify Trigger — Learn how to use the Clockify Trigger node in n8n. Follow technical documentation to integrate Clockify Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger) |
| ConvertKit Trigger — Learn how to use the ConvertKit Trigger node in n8n. Follow technical documentation to integrate ConvertKit Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.convertkittrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.convertkittrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.convertkittrigger) |
| Copper Trigger — Learn how to use the Copper Trigger node in n8n. Follow technical documentation to integrate Copper Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.coppertrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.coppertrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.coppertrigger) |
| Customer.io Trigger — Learn how to use the Customer.io Trigger node in n8n. Follow technical documentation to integrate Customer.io Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger) |
| Emelia Trigger — Learn how to use the Emelia Trigger node in n8n. Follow technical documentation to integrate Emelia Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.emeliatrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.emeliatrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.emeliatrigger) |
| Eventbrite Trigger — Learn how to use the Eventbrite Trigger node in n8n. Follow technical documentation to integrate Eventbrite Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.eventbritetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.eventbritetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.eventbritetrigger) |
| Facebook Lead Ads Trigger — Learn how to use the Facebook Lead Ads Trigger node in n8n. Follow technical documentation to integrate Facebook Lead Ads Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger) |
| Facebook Trigger — Learn how to use the Facebook Trigger node in n8n. Follow technical documentation to integrate Facebook Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger) |
| Ad Account — Learn how to use the Ad Account object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Ad Account object into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account) |
| Application — Learn how to use the Application object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Application object into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/application.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/application.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/application) |
| Certificate Transparency — Learn how to use the Certificate Transparency object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Certificate Transparency object into y | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency) |
| Group — Learn how to use the Group object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Group object into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/group.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/group.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/group) |
| Instagram — Learn how to use the Instagram object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Instagram object into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram) |
| Link — Learn how to use the Link object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Link object into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link) |
| Page — Learn how to use the Page object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Page object into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page) |
| Permissions — Learn how to use the Permissions object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Permissions object into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/permissions.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/permissions.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/permissions) |
| User — Learn how to use the User object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's User object into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/user.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/user.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/user) |
| WhatsApp Business Account — Learn how to use the WhatsApp Business Account object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's WhatsApp Business Account object into | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp) |
| Workplace Security — Learn how to use the Workplace Security object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Workplace Security object into your workflow | [`integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/workplace-security.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/workplace-security.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/workplace-security) |
| Figma Trigger (Beta) — Learn how to use the Figma Trigger node in n8n. Follow technical documentation to integrate Figma Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger) |
| Flow Trigger — Learn how to use the Flow Trigger node in n8n. Follow technical documentation to integrate Flow Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.flowtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.flowtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.flowtrigger) |
| Form.io Trigger — Learn how to use the Form.io Trigger node in n8n. Follow technical documentation to integrate Form.io Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.formiotrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.formiotrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.formiotrigger) |
| Formstack Trigger — Learn how to use the Formstack Trigger node in n8n. Follow technical documentation to integrate Formstack Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.formstacktrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.formstacktrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.formstacktrigger) |
| GetResponse Trigger — Learn how to use the GetResponse Trigger node in n8n. Follow technical documentation to integrate GetResponse Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.getresponsetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.getresponsetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.getresponsetrigger) |
| GitHub Trigger — Learn how to use the GitHub Trigger node in n8n. Follow technical documentation to integrate GitHub Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger) |
| GitLab Trigger — Learn how to use the GitLab Trigger node in n8n. Follow technical documentation to integrate GitLab Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger) |
| Gmail Trigger — Learn how to use the Gmail Trigger node in n8n. Follow technical documentation to integrate Gmail Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger) |
| Poll mode options — Learn about the poll mode options available to the Gmail Trigger node in n8n and how to configure them. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/poll-mode-options.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/poll-mode-options.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/poll-mode-options) |
| Common issues — Documentation for common issues and questions in the Gmail Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/common-issues.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/common-issues) |
| Google Calendar Trigger — Learn how to use the Google Calendar Trigger node in n8n. Follow technical documentation to integrate Google Calendar Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.googlecalendartrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googlecalendartrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlecalendartrigger) |
| Google Drive Trigger — Learn how to use the Google Drive Trigger node in n8n. Follow technical documentation to integrate Google Drive Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger) |
| Common issues — Documentation for common issues and questions in the Google Drive Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues) |
| Google Business Profile Trigger — Learn how to use the Google Business Profile Trigger node in n8n. Follow technical documentation to integrate Google Business Profile Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.googlebusinessprofiletrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googlebusinessprofiletrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlebusinessprofiletrigger) |
| Google Sheets Trigger — Learn how to use the Google Sheets Trigger node in n8n. Follow technical documentation to integrate Google Sheets Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger) |
| Common issues — Documentation for common issues and questions in the Google Sheets Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/common-issues.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/common-issues) |
| Gumroad Trigger — Learn how to use the Gumroad Trigger node in n8n. Follow technical documentation to integrate Gumroad Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.gumroadtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gumroadtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gumroadtrigger) |
| Help Scout Trigger — Learn how to use the Help Scout Trigger node in n8n. Follow technical documentation to integrate Help Scout Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.helpscouttrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.helpscouttrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.helpscouttrigger) |
| HubSpot Trigger — Learn how to use the HubSpot Trigger node in n8n. Follow technical documentation to integrate HubSpot Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger) |
| Invoice Ninja Trigger — Learn how to use the Invoice Ninja Trigger node in n8n. Follow technical documentation to integrate Invoice Ninja Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.invoiceninjatrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.invoiceninjatrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.invoiceninjatrigger) |
| Jira Trigger — Learn how to use the Jira Trigger node in n8n. Follow technical documentation to integrate Jira Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.jiratrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.jiratrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.jiratrigger) |
| Jotform Trigger — Learn how to use the Jotform Trigger node in n8n. Follow technical documentation to integrate Jotform Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.jotformtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.jotformtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.jotformtrigger) |
| Kafka Trigger — Learn how to use the Kafka Trigger node in n8n. Follow technical documentation to integrate Kafka Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger) |
| Keap Trigger — Learn how to use the Keap Trigger node in n8n. Follow technical documentation to integrate Keap Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.keaptrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.keaptrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.keaptrigger) |
| KoboToolbox Trigger — Learn how to use the KoboToolbox Trigger node in n8n. Follow technical documentation to integrate KoboToolbox Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger) |
| Lemlist Trigger — Learn how to use the Lemlist Trigger node in n8n. Follow technical documentation to integrate Lemlist Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.lemlisttrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.lemlisttrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.lemlisttrigger) |
| Linear Trigger — Learn how to use the Linear Trigger node in n8n. Follow technical documentation to integrate Linear Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger) |
| LoneScale Trigger — Learn how to use the LoneScale Trigger node in n8n. Follow technical documentation to integrate LoneScale Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.lonescaletrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.lonescaletrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.lonescaletrigger) |
| Mailchimp Trigger — Learn how to use the Mailchimp Trigger node in n8n. Follow technical documentation to integrate Mailchimp Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.mailchimptrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mailchimptrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.mailchimptrigger) |
| MailerLite Trigger — Learn how to use the MailerLite Trigger node in n8n. Follow technical documentation to integrate MailerLite Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.mailerlitetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mailerlitetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.mailerlitetrigger) |
| Mailjet Trigger — Learn how to use the Mailjet Trigger node in n8n. Follow technical documentation to integrate Mailjet Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.mailjettrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mailjettrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.mailjettrigger) |
| Mautic Trigger — Learn how to use the Mautic Trigger node in n8n. Follow technical documentation to integrate Mautic Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.mautictrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mautictrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.mautictrigger) |
| Microsoft OneDrive Trigger — Learn how to use the Microsoft OneDrive Trigger node in n8n. Follow technical documentation to integrate Microsoft OneDrive Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger) |
| Microsoft Outlook Trigger — Learn how to use the Microsoft Outlook Trigger node in n8n. Follow technical documentation to integrate Microsoft Outlook Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger) |
| Microsoft Teams Trigger — Learn how to use the Microsoft Teams Trigger node in n8n. Follow technical documentation to integrate Microsoft Teams Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger) |
| MQTT Trigger — Learn how to use the MQTT Trigger node in n8n. Follow technical documentation to integrate MQTT Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.mqtttrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mqtttrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.mqtttrigger) |
| Netlify Trigger — Learn how to use the Netlify Trigger node in n8n. Follow technical documentation to integrate Netlify Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.netlifytrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.netlifytrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.netlifytrigger) |
| Notion Trigger — Learn how to use the Notion Trigger node in n8n. Follow technical documentation to integrate Notion Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.notiontrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.notiontrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.notiontrigger) |
| Onfleet Trigger — Learn how to use the Onfleet Trigger node in n8n. Follow technical documentation to integrate Onfleet Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.onfleettrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.onfleettrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.onfleettrigger) |
| PayPal Trigger — Learn how to use the PayPal Trigger node in n8n. Follow technical documentation to integrate PayPal Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.paypaltrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.paypaltrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.paypaltrigger) |
| Pipedrive Trigger — Learn how to use the Pipedrive Trigger node in n8n. Follow technical documentation to integrate Pipedrive Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.pipedrivetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.pipedrivetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.pipedrivetrigger) |
| Postgres Trigger — Learn how to use the Postgres Trigger node in n8n. Follow technical documentation to integrate Postgres Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger) |
| Postmark Trigger — Learn how to use the Postmark Trigger node in n8n. Follow technical documentation to integrate Postmark Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.postmarktrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.postmarktrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.postmarktrigger) |
| Pushcut Trigger — Learn how to use the Pushcut Trigger node in n8n. Follow technical documentation to integrate Pushcut Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger) |
| RabbitMQ Trigger — Learn how to use the RabbitMQ Trigger node in n8n. Follow technical documentation to integrate RabbitMQ Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.rabbitmqtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.rabbitmqtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.rabbitmqtrigger) |
| Redis Trigger — Learn how to use the Redis Trigger node in n8n. Follow technical documentation to integrate Redis Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.redistrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.redistrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.redistrigger) |
| Salesforce Trigger — Learn how to use the Salesforce Trigger node in n8n. Follow technical documentation to integrate Salesforce Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger) |
| SeaTable Trigger — Learn how to use the SeaTable Trigger node in n8n. Follow technical documentation to integrate SeaTable Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.seatabletrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.seatabletrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.seatabletrigger) |
| Shopify Trigger — Learn how to use the Shopify Trigger node in n8n. Follow technical documentation to integrate Shopify Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.shopifytrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.shopifytrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.shopifytrigger) |
| Slack Trigger — Learn how to use the Slack Trigger node in n8n. Follow technical documentation to integrate Slack Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger) |
| Strava Trigger — Learn how to use the Strava Trigger node in n8n. Follow technical documentation to integrate Strava Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.stravatrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.stravatrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.stravatrigger) |
| Stripe Trigger — Learn how to use the Stripe Trigger node in n8n. Follow technical documentation to integrate Stripe Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger) |
| SurveyMonkey Trigger — Learn how to use the SurveyMonkey Trigger node in n8n. Follow technical documentation to integrate SurveyMonkey Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.surveymonkeytrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.surveymonkeytrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.surveymonkeytrigger) |
| Taiga Trigger — Learn how to use the Taiga Trigger node in n8n. Follow technical documentation to integrate Taiga Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.taigatrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.taigatrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.taigatrigger) |
| Telegram Trigger — Learn how to use the Telegram Trigger node in n8n. Follow technical documentation to integrate Telegram Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger) |
| Common issues — Documentation for common issues and questions in the Telegram Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues) |
| TheHive 5 Trigger — Learn how to use the TheHive 5 Trigger node in n8n. Follow technical documentation to integrate TheHive 5 Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger) |
| TheHive Trigger — Learn how to use the TheHive Trigger node in n8n. Follow technical documentation to integrate TheHive Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger) |
| Toggl Trigger — Learn how to use the Toggl Trigger node in n8n. Follow technical documentation to integrate Toggl Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.toggltrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.toggltrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.toggltrigger) |
| Trello Trigger — Learn how to use the Trello Trigger node in n8n. Follow technical documentation to integrate Trello Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger) |
| Twilio Trigger — Learn how to use the Twilio Trigger node in n8n. Follow technical documentation to integrate Twilio Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger) |
| Typeform Trigger — Learn how to use the Typeform Trigger node in n8n. Follow technical documentation to integrate Typeform Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.typeformtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.typeformtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.typeformtrigger) |
| Venafi TLS Protect Cloud Trigger — Learn how to use the Venafi TLS Protect Cloud Trigger node in n8n. Follow technical documentation to integrate Venafi TLS Protect Cloud Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger) |
| Webex by Cisco Trigger — Learn how to use the Webex by Cisco Trigger node in n8n. Follow technical documentation to integrate Webex by Cisco Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.ciscowebextrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.ciscowebextrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.ciscowebextrigger) |
| Webflow Trigger — Learn how to use the Webflow Trigger node in n8n. Follow technical documentation to integrate Webflow Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.webflowtrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.webflowtrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.webflowtrigger) |
| WhatsApp Trigger — Learn how to use the WhatsApp Trigger node in n8n. Follow technical documentation to integrate WhatsApp Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger) |
| Wise Trigger — Learn how to use the Wise Trigger node in n8n. Follow technical documentation to integrate Wise Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.wisetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.wisetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.wisetrigger) |
| WooCommerce Trigger — Learn how to use the WooCommerce Trigger node in n8n. Follow technical documentation to integrate WooCommerce Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.woocommercetrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.woocommercetrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.woocommercetrigger) |
| Workable Trigger — Learn how to use the Workable Trigger node in n8n. Follow technical documentation to integrate Workable Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.workabletrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.workabletrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.workabletrigger) |
| Wufoo Trigger — Learn how to use the Wufoo Trigger node in n8n. Follow technical documentation to integrate Wufoo Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.wufootrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.wufootrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.wufootrigger) |
| Zendesk Trigger — Learn how to use the Zendesk Trigger node in n8n. Follow technical documentation to integrate Zendesk Trigger node into your workflows. | [`integrations/builtin/trigger-nodes/n8n-nodes-base.zendesktrigger.md`](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.zendesktrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.zendesktrigger) |
| Cluster nodes — Understand cluster nodes in n8n, and browse the cluster nodes library. | [`integrations/builtin/cluster-nodes.md`](pages/integrations/builtin/cluster-nodes.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes) |
| Root nodes — Understand root nodes in n8n, and browse the root nodes library. | [`integrations/builtin/cluster-nodes/root-nodes.md`](pages/integrations/builtin/cluster-nodes/root-nodes.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes) |
| AI Agent — Learn how to use the AI Agent node in n8n. Follow technical documentation to integrate AI Agent node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent) |
| Conversational Agent — Learn how to use the Conversational Agent of the AI Agent node in n8n. Follow technical documentation to integrate the Conversational Agent into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent) |
| OpenAI Functions Agent — Learn how to use the OpenAI Functions Agent of the AI Agent node in n8n. Follow technical documentation to integrate the OpenAI Functions Agent into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent) |
| Plan and Execute Agent — Learn how to use the Plan and Execute Agent of the AI Agent node in n8n. Follow technical documentation to integrate the Plan and Execute Agent into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent) |
| ReAct Agent — Learn how to use the ReAct Agent of the AI Agent node in n8n. Follow technical documentation to integrate the ReAct Agent into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent) |
| SQL Agent — Learn how to use the SQL Agent of the AI Agent node in n8n. Follow technical documentation to integrate the SQL Agent into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent) |
| Tools Agent — Learn how to use the Tools Agent of the AI Agent node in n8n. Follow technical documentation to integrate the Tools Agent into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent) |
| Common issues — Documentation for common issues and questions in the AI Agent node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues) |
| Basic LLM Chain — Learn how to use the Basic LLM Chain node in n8n. Follow technical documentation to integrate Basic LLM Chain node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm) |
| Question and Answer Chain — Learn how to use the Question and Answer Chain node in n8n. Follow technical documentation to integrate Question and Answer Chain node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa) |
| Common issues — Documentation for common issues and questions in the Question and Answer Chain node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues) |
| Summarization Chain — Learn how to use the Summarize Chain node in n8n. Follow technical documentation to integrate Summarize Chain node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization) |
| Information Extractor — Learn how to use the Information Extractor node in n8n. Follow technical documentation to integrate Information Extractor node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor) |
| Text Classifier — Learn how to use the Text Classifier node in n8n. Follow technical documentation to integrate Text Classifier node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier) |
| Sentiment Analysis — Learn how to use the Sentiment Analysis node in n8n. Follow technical documentation to integrate Sentiment Analysis node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis) |
| LangChain Code — Learn how to use the LangChain Code node in n8n. Follow technical documentation to integrate LangChain Code node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code) |
| Microsoft Agent 365 Trigger — Learn how to use the Microsoft Agent 365 Trigger node in n8n. Follow technical documentation to integrate Microsoft Agent 365 Trigger node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger) |
| Azure AI Search Vector Store — Learn how to use the Azure AI Search Vector Store node in n8n. Follow technical documentation to integrate Azure AI Search Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch) |
| Simple Vector Store — Learn how to use the Simple Vector Store node in n8n. Follow technical documentation to integrate Simple Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory) |
| Milvus Vector Store — Learn how to use the Milvus Vector Store node in n8n. Follow technical documentation to integrate Milvus Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus) |
| MongoDB Atlas Vector Store — Learn how to use the MongoDB Atlas Vector Store node in n8n. Follow technical documentation to integrate MongoDB Atlas Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas) |
| PGVector Vector Store — Learn how to use the PGVector Vector Store node in n8n. Follow technical documentation to integrate PGVector Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector) |
| Oracle Database Vector Store — Learn how to use the Oracle Database Vector Store node in n8n. Follow technical documentation to integrate Oracle Database Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb) |
| Chroma Vector Store — Learn how to use the Chroma Vector Store node in n8n. Follow technical documentation to integrate Chroma Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma) |
| Pinecone Vector Store — Learn how to use the Pinecone Vector Store node in n8n. Follow technical documentation to integrate Pinecone Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone) |
| Qdrant Vector Store — Learn how to use the Qdrant Vector Store node in n8n. Follow technical documentation to integrate Qdrant Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant) |
| Redis Vector Store — Learn how to use the Redis Vector Store node in n8n. Follow technical documentation to integrate Redis Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis) |
| Supabase Vector Store — Learn how to use the Supabase Vector Store node in n8n. Follow technical documentation to integrate Supabase Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase) |
| Weaviate Vector Store — Learn how to use the Weaviate Vector Store node in n8n. Follow technical documentation to integrate Weaviate Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate) |
| Zep Vector Store — Learn how to use the Zep Vector Store node in n8n. Follow technical documentation to integrate Zep Vector Store node into your workflows. | [`integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep.md`](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep) |
| Sub-nodes — Understand sub-nodes in n8n, and browse the sub-nodes library. | [`integrations/builtin/cluster-nodes/sub-nodes.md`](pages/integrations/builtin/cluster-nodes/sub-nodes.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes) |
| Default Data Loader — Learn how to use the Default Data Loader node in n8n. Follow technical documentation to integrate Default Data Loader node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader) |
| GitHub Document Loader — Learn how to use the GitHub Document Loader node in n8n. Follow technical documentation to integrate GitHub Document Loader node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader) |
| Embeddings AWS Bedrock — Learn how to use the Embeddings AWS Bedrock node in n8n. Follow technical documentation to integrate Embeddings AWS Bedrock node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock) |
| Embeddings Azure OpenAI — Learn how to use the Embeddings Azure OpenAI node in n8n. Follow technical documentation to integrate Embeddings Azure OpenAI node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai) |
| Embeddings Cohere — Learn how to use the Embeddings Cohere node in n8n. Follow technical documentation to integrate Embeddings Cohere node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere) |
| Embeddings Google Gemini — Learn how to use the Embeddings Google Gemini node in n8n. Follow technical documentation to integrate Embeddings Google Gemini node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini) |
| Embeddings Google PaLM — Learn how to use the Embeddings Google PaLM node in n8n. Follow technical documentation to integrate Embeddings Google PaLM node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm) |
| Embeddings Google Vertex — Learn how to use the Embeddings Google Vertex node in n8n. Follow technical documentation to integrate Embeddings Google Gemini node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex) |
| Embeddings HuggingFace Inference — Learn how to use the Embeddings HuggingFace Inference node in n8n. Follow technical documentation to integrate Embeddings HuggingFace Inference node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference) |
| Embeddings Lemonade — Learn how to use the Embeddings Lemonade node in n8n. Follow technical documentation to integrate Embeddings Lemonade node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade) |
| Embeddings Mistral Cloud — Learn how to use the Embeddings Mistral Cloud node in n8n. Follow technical documentation to integrate Embeddings Mistral Cloud node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud) |
| Embeddings Ollama — Learn how to use the Embeddings Ollama node in n8n. Follow technical documentation to integrate Embeddings Ollama node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama) |
| Embeddings OpenAI — Learn how to use the Embeddings OpenAI node in n8n. Follow technical documentation to integrate Embeddings OpenAI node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai) |
| Embeddings Oracle Database — Learn how to use the Embeddings Oracle Database node in n8n. Follow technical documentation to integrate Embeddings Oracle Database node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb) |
| Qwen Cloud Chat Model — The Qwen Cloud Chat Model node sends prompts to conversational models available on Qwen Cloud (for advanced AI chains). This page explains how to configure the node in n8n workflows and covers common | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud) |
| Anthropic Chat Model — Learn how to use the Anthropic Chat Model node in n8n. Follow technical documentation to integrate Anthropic Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic) |
| AWS Bedrock Chat Model — Learn how to use the AWS Bedrock Chat Model node in n8n. Follow technical documentation to integrate AWS Bedrock Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock) |
| Azure OpenAI Chat Model — Learn how to use the Azure OpenAI Chat Model node in n8n. Follow technical documentation to integrate Azure OpenAI Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai) |
| Cohere Chat Model — Learn how to use the Cohere Chat Model node in n8n. Follow technical documentation to integrate Cohere Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere) |
| DeepSeek Chat Model — Learn how to use the DeepSeek Chat Model node in n8n. Follow technical documentation to integrate DeepSeek Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek) |
| Google Gemini Chat Model — Learn how to use the Google Gemini Chat Model node in n8n. Follow technical documentation to integrate Google Gemini Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini) |
| Google Vertex Chat Model — Learn how to use the Google Vertex Chat Model node in n8n. Follow technical documentation to integrate Google Vertex Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex) |
| Groq Chat Model — Learn how to use the Groq Chat Model node in n8n. Follow technical documentation to integrate Groq Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq) |
| Lemonade Chat Model — Learn how to use the Lemonade Chat Model node in n8n. Follow technical documentation to integrate Lemonade Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade) |
| MiniMax Chat Model — Learn how to use the MiniMax Chat Model node in n8n. Follow technical documentation to integrate MiniMax Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax) |
| Mistral Cloud Chat Model — Learn how to use the Mistral Cloud Chat Model node in n8n. Follow technical documentation to integrate Mistral Cloud Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud) |
| Moonshot Kimi Chat Model node — Integrate the Moonshot Kimi Chat Model into n8n workflows to generate chat responses for AI chains. Common uses include generating conversational replies, integrating with LangChain-style workflows, a | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot) |
| NVIDIA Nemotron Chat Model — Learn how to use the NVIDIA Nemotron Chat Model node in n8n. Follow technical documentation to integrate NVIDIA Nemotron Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia) |
| Ollama Chat Model — Learn how to use the Ollama Chat Model node in n8n. Follow technical documentation to integrate Ollama Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama) |
| Common issues — Documentation for common issues and questions in the Ollama Chat Model node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues) |
| OpenAI Chat Model — Learn how to use the OpenAI Chat Model node in n8n. Follow technical documentation to integrate OpenAI Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai) |
| Common issues — Documentation for common issues and questions in the OpenAI Chat Model node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues) |
| OpenRouter Chat Model — Learn how to use the OpenRouter Chat Model node in n8n. Follow technical documentation to integrate OpenRouter Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter) |
| Vercel AI Gateway Chat Model — Learn how to use the Vercel AI Gateway Chat Model node in n8n. Follow technical documentation to integrate Vercel AI Gateway Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatvercel.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatvercel.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatvercel) |
| xAI Grok Chat Model — Learn how to use the xAI Grok Chat Model node in n8n. Follow technical documentation to integrate xAI Grok Chat Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok) |
| Cohere Model — Learn how to use the Cohere Model node in n8n. Follow technical documentation to integrate Cohere Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere) |
| Lemonade Model — Learn how to use the Lemonade Model node in n8n. Follow technical documentation to integrate Lemonade Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade) |
| Ollama Model — Learn how to use the Ollama Model node in n8n. Follow technical documentation to integrate Ollama Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama) |
| Common issues — Documentation for common issues and questions in the Ollama Model node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/common-issues.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/common-issues) |
| Hugging Face Inference Model — Learn how to use the Hugging Face Inference Model node in n8n. Follow technical documentation to integrate Hugging Face Inference Model node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference) |
| Chat Memory Manager — Learn how to use the Chat Memory Manager node in n8n. Follow technical documentation to integrate Chat Memory Manager node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager) |
| Simple Memory — Learn how to use the Simple Memory node in n8n. Follow technical documentation to integrate Simple Memory node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow) |
| Common issues — Documentation for common issues and questions in the Simple Memory node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues) |
| Motorhead — Learn how to use the Motorhead node in n8n. Follow technical documentation to integrate Motorhead node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead) |
| MongoDB Chat Memory — Learn how to use the MongoDB Chat Memory node in n8n. Follow technical documentation to integrate MongoDB Chat Memory node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat) |
| Redis Chat Memory — Learn how to use the Redis Chat Memory node in n8n. Follow technical documentation to integrate Redis Chat Memory node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat) |
| Postgres Chat Memory — Learn how to use the Postgres Chat Memory node in n8n. Follow technical documentation to integrate Postgres Chat Memory node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat) |
| Xata — Learn how to use the Xata node in n8n. Follow technical documentation to integrate Xata node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata) |
| Zep — Learn how to use the Zep node in n8n. Follow technical documentation to integrate Zep node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep) |
| Auto-fixing Output Parser — Learn how to use the Auto-fixing Output Parser node in n8n. Follow technical documentation to integrate Auto-fixing Output Parser node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing) |
| Item List Output Parser — Learn how to use the Item List Output Parser node in n8n. Follow technical documentation to integrate Item List Output Parser node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist) |
| Structured Output Parser — Learn how to use the Structured Output Parser node in n8n. Follow technical documentation to integrate Structured Output Parser node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured) |
| Common issues — Documentation for common issues and questions in the Structured Output Parser node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues) |
| Contextual Compression Retriever — Learn how to use the Contextual Compression Retriever node in n8n. Follow technical documentation to integrate Contextual Compression Retriever node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression) |
| MultiQuery Retriever — Learn how to use the MultiQuery Retriever node in n8n. Follow technical documentation to integrate MultiQuery Retriever node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery) |
| Vector Store Retriever — Learn how to use the Vector Store Retriever node in n8n. Follow technical documentation to integrate Vector Store Retriever node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore) |
| Workflow Retriever — Learn how to use the Workflow Retriever node in n8n. Follow technical documentation to integrate Workflow Retriever node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow) |
| Character Text Splitter — Learn how to use the Character Text Splitter node in n8n. Follow technical documentation to integrate Character Text Splitter node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter) |
| Recursive Character Text Splitter — Learn how to use the Recursive Character Text Splitter node in n8n. Follow technical documentation to integrate Recursive Character Text Splitter node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter) |
| Token Splitter — Learn how to use the Token Splitter node in n8n. Follow technical documentation to integrate Token Splitter node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter) |
| AI Agent Tool — Learn how to use the AI Agent Tool node in n8n. Follow technical documentation to integrate the AI Agent Tool node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent) |
| Calculator — Learn how to use the Calculator node in n8n. Follow technical documentation to integrate Calculator node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcalculator.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcalculator.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcalculator) |
| Custom Code Tool — Learn how to use the Custom Code Tool node in n8n. Follow technical documentation to integrate Custom Code Tool node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode) |
| MCP Client Tool — Learn how to use the MCP Client Tool node in n8n. Follow technical documentation to integrate MCP Client Tool node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp) |
| SearXNG Tool — Learn how to use the SearXNG Tool node in n8n. Follow technical documentation to integrate SearXNG Tool node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng) |
| SerpApi (Google Search) — Learn how to use the SerpApi (Google Search) node in n8n. Follow technical documentation to integrate SerpApi (Google Search) node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi) |
| Think Tool — Learn how to use the Think Tool node in n8n. Follow technical documentation to integrate the Tool Think node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink) |
| Vector Store Question Answer Tool — Learn how to use the Vector Store Question Answer Tool node in n8n. Follow technical documentation to integrate Vector Store Question Answer Tool node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore) |
| Wikipedia — Learn how to use the Wikipedia node in n8n. Follow technical documentation to integrate Wikipedia node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia) |
| Wolfram|Alpha tool — Learn how to use the Wolfram\|Alpha tool node in n8n. Follow technical documentation to integrate Wolfram\|Alpha tool node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha) |
| Call n8n Workflow Tool — Learn how to use the Call n8n Workflow Tool node in n8n. Follow technical documentation to integrate Call n8n Workflow Tool node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow) |
| Reranker Cohere — Learn how to use the Reranker Cohere node in n8n. Follow technical documentation to integrate Cohere reranking into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere) |
| Model Selector — Learn how to use the Model Selector node in n8n. Follow technical documentation to integrate Model Selector node into your workflows. | [`integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector.md`](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector.md) | [docs](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector) |
| Credentials | [`integrations/builtin/credentials.md`](pages/integrations/builtin/credentials.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials) |
| Action Network credentials — Documentation for Action Network credentials. Use these credentials to authenticate Action Network in n8n, a workflow automation platform. | [`integrations/builtin/credentials/actionnetwork.md`](pages/integrations/builtin/credentials/actionnetwork.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/actionnetwork) |
| ActiveCampaign credentials — Documentation for ActiveCampaign credentials. Use these credentials to authenticate ActiveCampaign in n8n, a workflow automation platform. | [`integrations/builtin/credentials/activecampaign.md`](pages/integrations/builtin/credentials/activecampaign.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/activecampaign) |
| Acuity Scheduling credentials — Documentation for Acuity Scheduling credentials. Use these credentials to authenticate Acuity Scheduling in n8n, a workflow automation platform. | [`integrations/builtin/credentials/acuityscheduling.md`](pages/integrations/builtin/credentials/acuityscheduling.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/acuityscheduling) |
| Adalo credentials — Documentation for Adalo credentials. Use these credentials to authenticate Adalo in n8n, a workflow automation platform. | [`integrations/builtin/credentials/adalo.md`](pages/integrations/builtin/credentials/adalo.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/adalo) |
| Affinity credentials — Documentation for the Affinity credentials. Use these credentials to authenticate Affinity in n8n, a workflow automation platform. | [`integrations/builtin/credentials/affinity.md`](pages/integrations/builtin/credentials/affinity.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/affinity) |
| Agile CRM credentials — Documentation for Agile CRM credentials. Use these credentials to authenticate Agile CRM in n8n, a workflow automation platform. | [`integrations/builtin/credentials/agilecrm.md`](pages/integrations/builtin/credentials/agilecrm.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/agilecrm) |
| Airtable credentials — Documentation for Airtable credentials. Use these credentials to authenticate Airtable in n8n, a workflow automation platform. | [`integrations/builtin/credentials/airtable.md`](pages/integrations/builtin/credentials/airtable.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/airtable) |
| Airtop credentials — Documentation for the Airtop credentials. Use these credentials to authenticate Airtop in n8n, a workflow automation platform. | [`integrations/builtin/credentials/airtop.md`](pages/integrations/builtin/credentials/airtop.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/airtop) |
| Qwen Cloud credentials — Documentation for Qwen Cloud credentials. Use these credentials to authenticate Qwen Cloud in n8n, a workflow automation platform. | [`integrations/builtin/credentials/alibaba.md`](pages/integrations/builtin/credentials/alibaba.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/alibaba) |
| AlienVault credentials — Documentation for the AlienVault credentials. Use these credentials to authenticate AlienVault in n8n, a workflow automation platform. | [`integrations/builtin/credentials/alienvault.md`](pages/integrations/builtin/credentials/alienvault.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/alienvault) |
| AMQP credentials — Documentation for AMQP credentials. Use these credentials to authenticate AMQP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/amqp.md`](pages/integrations/builtin/credentials/amqp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/amqp) |
| Anthropic credentials — Documentation for the Anthropic credentials. Use these credentials to authenticate Anthropic in n8n, a workflow automation platform. | [`integrations/builtin/credentials/anthropic.md`](pages/integrations/builtin/credentials/anthropic.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/anthropic) |
| APITemplate.io credentials — Documentation for APITemplate.io credentials. Use these credentials to authenticate APITemplate.io in n8n, a workflow automation platform. | [`integrations/builtin/credentials/apitemplateio.md`](pages/integrations/builtin/credentials/apitemplateio.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/apitemplateio) |
| Asana credentials — Documentation for Asana credentials. Use these credentials to authenticate Asana in n8n, a workflow automation platform. | [`integrations/builtin/credentials/asana.md`](pages/integrations/builtin/credentials/asana.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/asana) |
| Auth0 Management credentials — Documentation for the Auth0 Management credentials. Use these credentials to authenticate Auth0 Management in n8n, a workflow automation platform. | [`integrations/builtin/credentials/auth0management.md`](pages/integrations/builtin/credentials/auth0management.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/auth0management) |
| Autopilot credentials — Documentation for Autopilot credentials. Use these credentials to authenticate Autopilot in n8n, a workflow automation platform. | [`integrations/builtin/credentials/autopilot.md`](pages/integrations/builtin/credentials/autopilot.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/autopilot) |
| AWS credentials — Documentation for AWS credentials. Use these credentials to authenticate AWS in n8n, a workflow automation platform. | [`integrations/builtin/credentials/aws.md`](pages/integrations/builtin/credentials/aws.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/aws) |
| Azure OpenAI credentials — Documentation for Azure OpenAI credentials. Use these credentials to authenticate OpenAI in n8n, a workflow automation platform. | [`integrations/builtin/credentials/azureopenai.md`](pages/integrations/builtin/credentials/azureopenai.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/azureopenai) |
| Azure Cosmos DB credentials — Documentation for the Azure Cosmos DB credentials. Use these credentials to authenticate Azure Cosmos DB in n8n, a workflow automation platform. | [`integrations/builtin/credentials/azurecosmosdb.md`](pages/integrations/builtin/credentials/azurecosmosdb.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/azurecosmosdb) |
| Azure AI Search credentials — Documentation for Azure AI Search credentials. Use these credentials to authenticate Azure AI Search in n8n, a workflow automation platform. | [`integrations/builtin/credentials/azureaisearch.md`](pages/integrations/builtin/credentials/azureaisearch.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/azureaisearch) |
| Azure Storage credentials — Documentation for the Azure Storage credentials. Use these credentials to authenticate Azure Storage in n8n, a workflow automation platform. | [`integrations/builtin/credentials/azurestorage.md`](pages/integrations/builtin/credentials/azurestorage.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/azurestorage) |
| BambooHR credentials — Documentation for BambooHR credentials. Use these credentials to authenticate BambooHR in n8n, a workflow automation platform. | [`integrations/builtin/credentials/bamboohr.md`](pages/integrations/builtin/credentials/bamboohr.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/bamboohr) |
| Bannerbear credentials — Documentation for Bannerbear credentials. Use these credentials to authenticate Bannerbear in n8n, a workflow automation platform. | [`integrations/builtin/credentials/bannerbear.md`](pages/integrations/builtin/credentials/bannerbear.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/bannerbear) |
| Baserow credentials — Documentation for Baserow credentials. Use these credentials to authenticate Baserow in n8n, a workflow automation platform. | [`integrations/builtin/credentials/baserow.md`](pages/integrations/builtin/credentials/baserow.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/baserow) |
| Beeminder credentials — Documentation for Beeminder credentials. Use these credentials to authenticate Beeminder in n8n, a workflow automation platform. | [`integrations/builtin/credentials/beeminder.md`](pages/integrations/builtin/credentials/beeminder.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/beeminder) |
| Bitbucket credentials — Documentation for Bitbucket credentials. Use these credentials to authenticate Bitbucket in n8n, a workflow automation platform. | [`integrations/builtin/credentials/bitbucket.md`](pages/integrations/builtin/credentials/bitbucket.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/bitbucket) |
| Bitly credentials — Documentation for Bitly credentials. Use these credentials to authenticate Bitly in n8n, a workflow automation platform. | [`integrations/builtin/credentials/bitly.md`](pages/integrations/builtin/credentials/bitly.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/bitly) |
| Bitwarden credentials — Documentation for Bitwarden credentials. Use these credentials to authenticate Bitwarden in n8n, a workflow automation platform. | [`integrations/builtin/credentials/bitwarden.md`](pages/integrations/builtin/credentials/bitwarden.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/bitwarden) |
| Box credentials — Documentation for Box credentials. Use these credentials to authenticate Box in n8n, a workflow automation platform. | [`integrations/builtin/credentials/box.md`](pages/integrations/builtin/credentials/box.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/box) |
| Brandfetch credentials — Documentation for Brandfetch credentials. Use these credentials to authenticate Brandfetch in n8n, a workflow automation platform. | [`integrations/builtin/credentials/brandfetch.md`](pages/integrations/builtin/credentials/brandfetch.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/brandfetch) |
| Brave Search credentials — Documentation for the Brave Search credentials. Use these credentials to authenticate Brave Search in n8n, a workflow automation platform. | [`integrations/builtin/credentials/bravesearch.md`](pages/integrations/builtin/credentials/bravesearch.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/bravesearch) |
| Brevo credentials — Documentation for Brevo credentials. Use these credentials to authenticate Brevo in n8n, a workflow automation platform. | [`integrations/builtin/credentials/brevo.md`](pages/integrations/builtin/credentials/brevo.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/brevo) |
| Bubble credentials — Documentation for Bubble credentials. Use these credentials to authenticate Bubble in n8n, a workflow automation platform. | [`integrations/builtin/credentials/bubble.md`](pages/integrations/builtin/credentials/bubble.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/bubble) |
| Cal.com credentials — Documentation for Cal.com credentials. Use these credentials to authenticate Cal.com in n8n, a workflow automation platform. | [`integrations/builtin/credentials/cal.md`](pages/integrations/builtin/credentials/cal.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/cal) |
| Calendly credentials — Documentation for Calendly credentials. Use these credentials to authenticate Calendly in n8n, a workflow automation platform. | [`integrations/builtin/credentials/calendly.md`](pages/integrations/builtin/credentials/calendly.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/calendly) |
| Carbon Black credentials — Documentation for the Carbon Black credentials. Use these credentials to authenticate Carbon Black in n8n, a workflow automation platform. | [`integrations/builtin/credentials/carbonblack.md`](pages/integrations/builtin/credentials/carbonblack.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/carbonblack) |
| Chargebee credentials — Documentation for Chargebee credentials. Use these credentials to authenticate Chargebee in n8n, a workflow automation platform. | [`integrations/builtin/credentials/chargebee.md`](pages/integrations/builtin/credentials/chargebee.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/chargebee) |
| CircleCI credentials — Documentation for CircleCI credentials. Use these credentials to authenticate CircleCI in n8n, a workflow automation platform. | [`integrations/builtin/credentials/circleci.md`](pages/integrations/builtin/credentials/circleci.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/circleci) |
| Cisco Meraki credentials — Documentation for the Cisco Meraki credentials. Use these credentials to authenticate Cisco Meraki in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ciscomeraki.md`](pages/integrations/builtin/credentials/ciscomeraki.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ciscomeraki) |
| Cisco Secure Endpoint credentials — Documentation for the Cisco Secure Endpoint credentials. Use these credentials to authenticate Cisco Secure Endpoint in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ciscosecureendpoint.md`](pages/integrations/builtin/credentials/ciscosecureendpoint.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ciscosecureendpoint) |
| Cisco Umbrella credentials — Documentation for the Cisco Umbrella credentials. Use these credentials to authenticate Cisco Umbrella in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ciscoumbrella.md`](pages/integrations/builtin/credentials/ciscoumbrella.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ciscoumbrella) |
| Clearbit credentials — Documentation for Clearbit credentials. Use these credentials to authenticate Clearbit in n8n, a workflow automation platform. | [`integrations/builtin/credentials/clearbit.md`](pages/integrations/builtin/credentials/clearbit.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/clearbit) |
| ClickUp credentials — Documentation for ClickUp credentials. Use these credentials to authenticate ClickUp in n8n, a workflow automation platform. | [`integrations/builtin/credentials/clickup.md`](pages/integrations/builtin/credentials/clickup.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/clickup) |
| Clockify credentials — Documentation for Clockify credentials. Use these credentials to authenticate Clockify in n8n, a workflow automation platform. | [`integrations/builtin/credentials/clockify.md`](pages/integrations/builtin/credentials/clockify.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/clockify) |
| Cloudflare credentials — Documentation for Cloudflare credentials. Use these credentials to authenticate Cloudflare in n8n, a workflow automation platform. | [`integrations/builtin/credentials/cloudflare.md`](pages/integrations/builtin/credentials/cloudflare.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/cloudflare) |
| Cockpit credentials — Documentation for Cockpit credentials. Use these credentials to authenticate Cockpit in n8n, a workflow automation platform. | [`integrations/builtin/credentials/cockpit.md`](pages/integrations/builtin/credentials/cockpit.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/cockpit) |
| Coda credentials — Documentation for Coda credentials. Use these credentials to authenticate Coda in n8n, a workflow automation platform. | [`integrations/builtin/credentials/coda.md`](pages/integrations/builtin/credentials/coda.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/coda) |
| Cohere credentials — Documentation for the Cohere credentials. Use these credentials to authenticate Cohere in n8n, a workflow automation platform. | [`integrations/builtin/credentials/cohere.md`](pages/integrations/builtin/credentials/cohere.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/cohere) |
| Contentful credentials — Documentation for Contentful credentials. Use these credentials to authenticate Contentful in n8n, a workflow automation platform. | [`integrations/builtin/credentials/contentful.md`](pages/integrations/builtin/credentials/contentful.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/contentful) |
| ConvertAPI credentials — Documentation for the ConvertAPI credentials. Use these credentials to authenticate ConvertAPI in n8n, a workflow automation platform. | [`integrations/builtin/credentials/convertapi.md`](pages/integrations/builtin/credentials/convertapi.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/convertapi) |
| ConvertKit credentials — Documentation for ConvertKit credentials. Use these credentials to authenticate ConvertKit in n8n, a workflow automation platform. | [`integrations/builtin/credentials/convertkit.md`](pages/integrations/builtin/credentials/convertkit.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/convertkit) |
| Copper credentials — Documentation for Copper credentials. Use these credentials to authenticate Copper in n8n, a workflow automation platform. | [`integrations/builtin/credentials/copper.md`](pages/integrations/builtin/credentials/copper.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/copper) |
| Cortex credentials — Documentation for the Cortex credentials. Use these credentials to authenticate Cortex in n8n, a workflow automation platform. | [`integrations/builtin/credentials/cortex.md`](pages/integrations/builtin/credentials/cortex.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/cortex) |
| CrateDB credentials — Documentation for CrateDB credentials. Use these credentials to authenticate CrateDB in n8n, a workflow automation platform. | [`integrations/builtin/credentials/cratedb.md`](pages/integrations/builtin/credentials/cratedb.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/cratedb) |
| CrowdStrike credentials — Documentation for the CrowdStrike credentials. Use these credentials to authenticate CrowdStrike in n8n, a workflow automation platform. | [`integrations/builtin/credentials/crowdstrike.md`](pages/integrations/builtin/credentials/crowdstrike.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/crowdstrike) |
| Crypto credentials — Documentation for the Crypto credentials. Use these credentials to authenticate the Crypto node in n8n, a workflow automation platform. | [`integrations/builtin/credentials/crypto.md`](pages/integrations/builtin/credentials/crypto.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/crypto) |
| Customer.io credentials — Documentation for Customer.io credentials. Use these credentials to authenticate Customer.io in n8n, a workflow automation platform. | [`integrations/builtin/credentials/customerio.md`](pages/integrations/builtin/credentials/customerio.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/customerio) |
| Databricks credentials — Documentation for Databricks credentials. Use these credentials to authenticate Databricks in n8n, a workflow automation platform. | [`integrations/builtin/credentials/databricks.md`](pages/integrations/builtin/credentials/databricks.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/databricks) |
| Datadog credentials — Documentation for the Datadog credentials. Use these credentials to authenticate Datadog in n8n, a workflow automation platform. | [`integrations/builtin/credentials/datadog.md`](pages/integrations/builtin/credentials/datadog.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/datadog) |
| Daytona credentials — Documentation for the Daytona credentials. Use these credentials to authenticate Daytona in n8n, a workflow automation platform. | [`integrations/builtin/credentials/daytona.md`](pages/integrations/builtin/credentials/daytona.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/daytona) |
| DeepL credentials — Documentation for DeepL credentials. Use these credentials to authenticate DeepL in n8n, a workflow automation platform. | [`integrations/builtin/credentials/deepl.md`](pages/integrations/builtin/credentials/deepl.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/deepl) |
| DeepSeek credentials — Documentation for DeepSeek credentials. Use these credentials to authenticate Deepseek in n8n, a workflow automation platform. | [`integrations/builtin/credentials/deepseek.md`](pages/integrations/builtin/credentials/deepseek.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/deepseek) |
| Demio credentials — Documentation for Demio credentials. Use these credentials to authenticate Demio in n8n, a workflow automation platform. | [`integrations/builtin/credentials/demio.md`](pages/integrations/builtin/credentials/demio.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/demio) |
| DFIR-IRIS credentials — Documentation for the DFIR-IRIS credentials. Use these credentials to authenticate DFIR-IRIS in n8n, a workflow automation platform. | [`integrations/builtin/credentials/dfiriris.md`](pages/integrations/builtin/credentials/dfiriris.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/dfiriris) |
| DHL credentials — Documentation for DHL credentials. Use these credentials to authenticate DHL in n8n, a workflow automation platform. | [`integrations/builtin/credentials/dhl.md`](pages/integrations/builtin/credentials/dhl.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/dhl) |
| Discord credentials — Documentation for Discord credentials. Use these credentials to authenticate Discord in n8n, a workflow automation platform. | [`integrations/builtin/credentials/discord.md`](pages/integrations/builtin/credentials/discord.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/discord) |
| Discourse credentials — Documentation for Discourse credentials. Use these credentials to authenticate Discourse in n8n, a workflow automation platform. | [`integrations/builtin/credentials/discourse.md`](pages/integrations/builtin/credentials/discourse.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/discourse) |
| Disqus credentials — Documentation for Disqus credentials. Use these credentials to authenticate Disqus in n8n, a workflow automation platform. | [`integrations/builtin/credentials/disqus.md`](pages/integrations/builtin/credentials/disqus.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/disqus) |
| Drift credentials — Documentation for Drift credentials. Use these credentials to authenticate Drift in n8n, a workflow automation platform. | [`integrations/builtin/credentials/drift.md`](pages/integrations/builtin/credentials/drift.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/drift) |
| Dropbox credentials — Documentation for Dropbox credentials. Use these credentials to authenticate Dropbox in n8n, a workflow automation platform. | [`integrations/builtin/credentials/dropbox.md`](pages/integrations/builtin/credentials/dropbox.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/dropbox) |
| Dropcontact credentials — Documentation for Dropcontact credentials. Use these credentials to authenticate Dropcontact in n8n, a workflow automation platform. | [`integrations/builtin/credentials/dropcontact.md`](pages/integrations/builtin/credentials/dropcontact.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/dropcontact) |
| Dynatrace credentials — Documentation for the Dynatrace credentials. Use these credentials to authenticate Dynatrace in n8n, a workflow automation platform. | [`integrations/builtin/credentials/dynatrace.md`](pages/integrations/builtin/credentials/dynatrace.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/dynatrace) |
| E-goi credentials — Documentation for E-goi credentials. Use these credentials to authenticate E-goi in n8n, a workflow automation platform. | [`integrations/builtin/credentials/egoi.md`](pages/integrations/builtin/credentials/egoi.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/egoi) |
| Elasticsearch credentials — Documentation for Elasticsearch credentials. Use these credentials to authenticate Elasticsearch in n8n, a workflow automation platform. | [`integrations/builtin/credentials/elasticsearch.md`](pages/integrations/builtin/credentials/elasticsearch.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/elasticsearch) |
| Elastic Security credentials — Documentation for Elastic Security credentials. Use these credentials to authenticate Elastic Security in n8n, a workflow automation platform. | [`integrations/builtin/credentials/elasticsecurity.md`](pages/integrations/builtin/credentials/elasticsecurity.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/elasticsecurity) |
| Emelia credentials — Documentation for Emelia credentials. Use these credentials to authenticate Emelia in n8n, a workflow automation platform. | [`integrations/builtin/credentials/emelia.md`](pages/integrations/builtin/credentials/emelia.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/emelia) |
| ERPNext credentials — Documentation for ERPNext credentials. Use these credentials to authenticate ERPNext in n8n, a workflow automation platform. | [`integrations/builtin/credentials/erpnext.md`](pages/integrations/builtin/credentials/erpnext.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/erpnext) |
| Eventbrite credentials — Documentation for Eventbrite credentials. Use these credentials to authenticate Eventbrite in n8n, a workflow automation platform. | [`integrations/builtin/credentials/eventbrite.md`](pages/integrations/builtin/credentials/eventbrite.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/eventbrite) |
| F5 Big-IP credentials — Documentation for the F5 Big-IP credentials. Use these credentials to authenticate F5 Big-IP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/f5bigip.md`](pages/integrations/builtin/credentials/f5bigip.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/f5bigip) |
| Facebook App credentials — Documentation for Facebook App credentials. Use these credentials to authenticate Facebook App in n8n, a workflow automation platform. | [`integrations/builtin/credentials/facebookapp.md`](pages/integrations/builtin/credentials/facebookapp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/facebookapp) |
| Facebook Graph API credentials — Documentation for Facebook Graph API credentials. Use these credentials to authenticate Facebook Graph API in n8n, a workflow automation platform. | [`integrations/builtin/credentials/facebookgraph.md`](pages/integrations/builtin/credentials/facebookgraph.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/facebookgraph) |
| Facebook Lead Ads credentials — Documentation for the Facebook Lead Ads credentials. Use these credentials to authenticate Facebook Lead Ads in n8n, a workflow automation platform. | [`integrations/builtin/credentials/facebookleadads.md`](pages/integrations/builtin/credentials/facebookleadads.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/facebookleadads) |
| Figma credentials — Documentation for Figma credentials. Use these credentials to authenticate Figma in n8n, a workflow automation platform. | [`integrations/builtin/credentials/figma.md`](pages/integrations/builtin/credentials/figma.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/figma) |
| FileMaker credentials — Documentation for FileMaker credentials. Use these credentials to authenticate FileMaker in n8n, a workflow automation platform. | [`integrations/builtin/credentials/filemaker.md`](pages/integrations/builtin/credentials/filemaker.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/filemaker) |
| Filescan credentials — Documentation for the Filescan credentials. Use these credentials to authenticate Filescan in n8n, a workflow automation platform. | [`integrations/builtin/credentials/filescan.md`](pages/integrations/builtin/credentials/filescan.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/filescan) |
| Flow credentials — Documentation for Flow credentials. Use these credentials to authenticate Flow in n8n, a workflow automation platform. | [`integrations/builtin/credentials/flow.md`](pages/integrations/builtin/credentials/flow.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/flow) |
| Form.io Trigger credentials — Documentation for Form.io Trigger credentials. Use these credentials to authenticate Form.io Trigger in n8n, a workflow automation platform. | [`integrations/builtin/credentials/formiotrigger.md`](pages/integrations/builtin/credentials/formiotrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/formiotrigger) |
| Formstack Trigger credentials — Documentation for Formstack Trigger credentials. Use these credentials to authenticate Formstack Trigger in n8n, a workflow automation platform. | [`integrations/builtin/credentials/formstacktrigger.md`](pages/integrations/builtin/credentials/formstacktrigger.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/formstacktrigger) |
| Fortinet FortiGate credentials — Documentation for the Fortinet FortiGate credentials. Use these credentials to authenticate Fortinet FortiGate in n8n, a workflow automation platform. | [`integrations/builtin/credentials/fortigate.md`](pages/integrations/builtin/credentials/fortigate.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/fortigate) |
| Freshdesk credentials — Documentation for Freshdesk credentials. Use these credentials to authenticate Freshdesk in n8n, a workflow automation platform. | [`integrations/builtin/credentials/freshdesk.md`](pages/integrations/builtin/credentials/freshdesk.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/freshdesk) |
| Freshservice credentials — Documentation for Freshservice credentials. Use these credentials to authenticate Freshservice in n8n, a workflow automation platform. | [`integrations/builtin/credentials/freshservice.md`](pages/integrations/builtin/credentials/freshservice.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/freshservice) |
| Freshworks CRM credentials — Documentation for Freshworks CRM credentials. Use these credentials to authenticate Freshworks CRM in n8n, a workflow automation platform. | [`integrations/builtin/credentials/freshworkscrm.md`](pages/integrations/builtin/credentials/freshworkscrm.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/freshworkscrm) |
| FTP credentials — Documentation for FTP credentials. Use these credentials to authenticate FTP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ftp.md`](pages/integrations/builtin/credentials/ftp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ftp) |
| GetResponse credentials — Documentation for GetResponse credentials. Use these credentials to authenticate GetResponse in n8n, a workflow automation platform. | [`integrations/builtin/credentials/getresponse.md`](pages/integrations/builtin/credentials/getresponse.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/getresponse) |
| Ghost credentials — Documentation for Ghost credentials. Use these credentials to authenticate Ghost in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ghost.md`](pages/integrations/builtin/credentials/ghost.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ghost) |
| Git credentials — Documentation for Git credentials. Use these credentials to authenticate Git in n8n, a workflow automation platform. | [`integrations/builtin/credentials/git.md`](pages/integrations/builtin/credentials/git.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/git) |
| GitHub credentials — Documentation for GitHub credentials. Use these credentials to authenticate GitHub in n8n, a workflow automation platform. | [`integrations/builtin/credentials/github.md`](pages/integrations/builtin/credentials/github.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/github) |
| GitLab credentials — Documentation for GitLab credentials. Use these credentials to authenticate GitLab in n8n, a workflow automation platform. | [`integrations/builtin/credentials/gitlab.md`](pages/integrations/builtin/credentials/gitlab.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/gitlab) |
| Gong credentials — Documentation for the Gong credentials. Use these credentials to authenticate Gong in n8n, a workflow automation platform. | [`integrations/builtin/credentials/gong.md`](pages/integrations/builtin/credentials/gong.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/gong) |
| Google — Documentation for Google credentials. Use these credentials to authenticate with Google in n8n. | [`integrations/builtin/credentials/google.md`](pages/integrations/builtin/credentials/google.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/google) |
| Google OAuth2 single service — Documentation for single service OAuth2 Google credentials. Use these credentials to authenticate with Google in n8n. | [`integrations/builtin/credentials/google/oauth-single-service.md`](pages/integrations/builtin/credentials/google/oauth-single-service.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service) |
| Google OAuth2 generic — Documentation for generic OAuth2 Google credentials. Use these credentials to authenticate Google services in n8n, a workflow automation platform. | [`integrations/builtin/credentials/google/oauth-generic.md`](pages/integrations/builtin/credentials/google/oauth-generic.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-generic) |
| Google Service Account — Documentation for service account Google credentials. Use these credentials to authenticate Google in n8n, a workflow automation platform. | [`integrations/builtin/credentials/google/service-account.md`](pages/integrations/builtin/credentials/google/service-account.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/google/service-account) |
| Google Gemini(PaLM) credentials — Documentation for the Google Gemini(PaLM) credentials. Use these credentials to authenticate Google Gemini and Google PaLM AI nodes in n8n, a workflow automation platform. | [`integrations/builtin/credentials/googleai.md`](pages/integrations/builtin/credentials/googleai.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/googleai) |
| Gotify credentials — Documentation for Gotify credentials. Use these credentials to authenticate Gotify in n8n, a workflow automation platform. | [`integrations/builtin/credentials/gotify.md`](pages/integrations/builtin/credentials/gotify.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/gotify) |
| GoToWebinar credentials — Documentation for GoToWebinar credentials. Use these credentials to authenticate GoToWebinar in n8n, a workflow automation platform. | [`integrations/builtin/credentials/gotowebinar.md`](pages/integrations/builtin/credentials/gotowebinar.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/gotowebinar) |
| Grafana credentials — Documentation for Grafana credentials. Use these credentials to authenticate Grafana in n8n, a workflow automation platform. | [`integrations/builtin/credentials/grafana.md`](pages/integrations/builtin/credentials/grafana.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/grafana) |
| Grist credentials — Documentation for Grist credentials. Use these credentials to authenticate Grist in n8n, a workflow automation platform. | [`integrations/builtin/credentials/grist.md`](pages/integrations/builtin/credentials/grist.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/grist) |
| Groq credentials — Documentation for the Groq credentials. Use these credentials to authenticate Groq in n8n, a workflow automation platform. | [`integrations/builtin/credentials/groq.md`](pages/integrations/builtin/credentials/groq.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/groq) |
| Gumroad credentials — Documentation for Gumroad credentials. Use these credentials to authenticate Gumroad in n8n, a workflow automation platform. | [`integrations/builtin/credentials/gumroad.md`](pages/integrations/builtin/credentials/gumroad.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/gumroad) |
| HaloPSA credentials — Documentation for HaloPSA credentials. Use these credentials to authenticate HaloPSA in n8n, a workflow automation platform. | [`integrations/builtin/credentials/halopsa.md`](pages/integrations/builtin/credentials/halopsa.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/halopsa) |
| Harvest credentials — Documentation for Harvest credentials. Use these credentials to authenticate Harvest in n8n, a workflow automation platform. | [`integrations/builtin/credentials/harvest.md`](pages/integrations/builtin/credentials/harvest.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/harvest) |
| Help Scout credentials — Documentation for Help Scout credentials. Use these credentials to authenticate Help Scout in n8n, a workflow automation platform. | [`integrations/builtin/credentials/helpscout.md`](pages/integrations/builtin/credentials/helpscout.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/helpscout) |
| HighLevel credentials — Documentation for HighLevel credentials. Use these credentials to authenticate HighLevel in n8n, a workflow automation platform. | [`integrations/builtin/credentials/highlevel.md`](pages/integrations/builtin/credentials/highlevel.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/highlevel) |
| Home Assistant credentials — Documentation for Home Assistant credentials. Use these credentials to authenticate Home Assistant in n8n, a workflow automation platform. | [`integrations/builtin/credentials/homeassistant.md`](pages/integrations/builtin/credentials/homeassistant.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/homeassistant) |
| HTTP Request credentials — Documentation for HTTP Request credentials. Use these credentials to authenticate the HTTP Request node in n8n. | [`integrations/builtin/credentials/httprequest.md`](pages/integrations/builtin/credentials/httprequest.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/httprequest) |
| HubSpot credentials — Documentation for HubSpot credentials. Use these credentials to authenticate HubSpot in n8n, a workflow automation platform. | [`integrations/builtin/credentials/hubspot.md`](pages/integrations/builtin/credentials/hubspot.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/hubspot) |
| Hugging Face credentials — Documentation for the Hugging Face credentials. Use these credentials to authenticate Hugging Face in n8n, a workflow automation platform. | [`integrations/builtin/credentials/huggingface.md`](pages/integrations/builtin/credentials/huggingface.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/huggingface) |
| Humantic AI credentials — Documentation for Humantic AI credentials. Use these credentials to authenticate Humantic AI in n8n, a workflow automation platform. | [`integrations/builtin/credentials/humanticai.md`](pages/integrations/builtin/credentials/humanticai.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/humanticai) |
| Hunter credentials — Documentation for Hunter credentials. Use these credentials to authenticate Hunter in n8n, a workflow automation platform. | [`integrations/builtin/credentials/hunter.md`](pages/integrations/builtin/credentials/hunter.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/hunter) |
| Hybrid Analysis credentials — Documentation for the Hybrid Analysis credentials. Use these credentials to authenticate Hybrid Analysis in n8n, a workflow automation platform. | [`integrations/builtin/credentials/hybridanalysis.md`](pages/integrations/builtin/credentials/hybridanalysis.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/hybridanalysis) |
| IMAP — Documentation for IMAP credentials. Use these credentials to authenticate IMAP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/imap.md`](pages/integrations/builtin/credentials/imap.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/imap) |
| Gmail — Documentation for Gmail IMAP credentials. Use these credentials to authenticate Gmail IMAP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/imap/gmail.md`](pages/integrations/builtin/credentials/imap/gmail.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/imap/gmail) |
| Outlook.com — Documentation for Outlook.com IMAP credentials. Use these credentials to authenticate Outlook.com IMAP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/imap/outlook.md`](pages/integrations/builtin/credentials/imap/outlook.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/imap/outlook) |
| Yahoo — Documentation for Yahoo IMAP credentials. Use these credentials to authenticate Yahoo IMAP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/imap/yahoo.md`](pages/integrations/builtin/credentials/imap/yahoo.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/imap/yahoo) |
| Imperva WAF credentials — Documentation for the Imperva WAF credentials. Use these credentials to authenticate Imperva WAF in n8n, a workflow automation platform. | [`integrations/builtin/credentials/impervawaf.md`](pages/integrations/builtin/credentials/impervawaf.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/impervawaf) |
| Intercom credentials — Documentation for Intercom credentials. Use these credentials to authenticate Intercom in n8n, a workflow automation platform. | [`integrations/builtin/credentials/intercom.md`](pages/integrations/builtin/credentials/intercom.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/intercom) |
| Invoice Ninja credentials — Documentation for Invoice Ninja credentials. Use these credentials to authenticate Invoice Ninja in n8n, a workflow automation platform. | [`integrations/builtin/credentials/invoiceninja.md`](pages/integrations/builtin/credentials/invoiceninja.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/invoiceninja) |
| Iterable credentials — Documentation for Iterable credentials. Use these credentials to authenticate Iterable in n8n, a workflow automation platform. | [`integrations/builtin/credentials/iterable.md`](pages/integrations/builtin/credentials/iterable.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/iterable) |
| Jenkins credentials — Documentation for Jenkins credentials. Use these credentials to authenticate Jenkins in n8n, a workflow automation platform. | [`integrations/builtin/credentials/jenkins.md`](pages/integrations/builtin/credentials/jenkins.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/jenkins) |
| Jina AI credentials — Documentation for the Jina AI credentials. Use these credentials to authenticate Jina AI in n8n, a workflow automation platform. | [`integrations/builtin/credentials/jinaai.md`](pages/integrations/builtin/credentials/jinaai.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/jinaai) |
| Jira credentials — Documentation for Jira credentials. Use these credentials to authenticate Jira in n8n, a workflow automation platform. | [`integrations/builtin/credentials/jira.md`](pages/integrations/builtin/credentials/jira.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/jira) |
| Jotform credentials — Documentation for Jotform credentials. Use these credentials to authenticate Jotform in n8n, a workflow automation platform. | [`integrations/builtin/credentials/jotform.md`](pages/integrations/builtin/credentials/jotform.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/jotform) |
| JWT credentials — Documentation for the JWT credentials. Use these credentials to authenticate JWT in n8n, a workflow automation platform. | [`integrations/builtin/credentials/jwt.md`](pages/integrations/builtin/credentials/jwt.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/jwt) |
| Kafka credentials — Documentation for Kafka credentials. Use these credentials to authenticate Kafka in n8n, a workflow automation platform. | [`integrations/builtin/credentials/kafka.md`](pages/integrations/builtin/credentials/kafka.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/kafka) |
| Keap credentials — Documentation for Keap credentials. Use these credentials to authenticate Keap in n8n, a workflow automation platform. | [`integrations/builtin/credentials/keap.md`](pages/integrations/builtin/credentials/keap.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/keap) |
| Kibana credentials — Documentation for the Kibana credentials. Use these credentials to authenticate Kibana in n8n, a workflow automation platform. | [`integrations/builtin/credentials/kibana.md`](pages/integrations/builtin/credentials/kibana.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/kibana) |
| Kitemaker credentials — Documentation for Kitemaker credentials. Use these credentials to authenticate Kitemaker in n8n, a workflow automation platform. | [`integrations/builtin/credentials/kitemaker.md`](pages/integrations/builtin/credentials/kitemaker.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/kitemaker) |
| KoboToolbox credentials — Documentation for KoboToolbox credentials. Use these credentials to authenticate KoboToolbox in n8n, a workflow automation platform. | [`integrations/builtin/credentials/kobotoolbox.md`](pages/integrations/builtin/credentials/kobotoolbox.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/kobotoolbox) |
| LDAP credentials — Documentation for the LDAP credentials. Use these credentials to authenticate LDAP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ldap.md`](pages/integrations/builtin/credentials/ldap.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ldap) |
| Lemlist credentials — Documentation for Lemlist credentials. Use these credentials to authenticate Lemlist in n8n, a workflow automation platform. | [`integrations/builtin/credentials/lemlist.md`](pages/integrations/builtin/credentials/lemlist.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/lemlist) |
| Lemonade credentials — Documentation for Lemonade credentials. Use these credentials to authenticate Lemonade in n8n, a workflow automation platform. | [`integrations/builtin/credentials/lemonade.md`](pages/integrations/builtin/credentials/lemonade.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/lemonade) |
| Line credentials — Documentation for Line credentials. Use these credentials to authenticate the Line node in n8n, a workflow automation platform. | [`integrations/builtin/credentials/line.md`](pages/integrations/builtin/credentials/line.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/line) |
| Linear credentials — Documentation for Linear credentials. Use these credentials to authenticate Linear in n8n, a workflow automation platform. | [`integrations/builtin/credentials/linear.md`](pages/integrations/builtin/credentials/linear.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/linear) |
| LingvaNex credentials — Documentation for LingvaNex credentials. Use these credentials to authenticate LingvaNex in n8n, a workflow automation platform. | [`integrations/builtin/credentials/lingvanex.md`](pages/integrations/builtin/credentials/lingvanex.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/lingvanex) |
| LinkedIn credentials — Documentation for LinkedIn credentials. Use these credentials to authenticate LinkedIn in n8n, a workflow automation platform. | [`integrations/builtin/credentials/linkedin.md`](pages/integrations/builtin/credentials/linkedin.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/linkedin) |
| LoneScale credentials — Documentation for LoneScale credentials. Use these credentials to authenticate LoneScale in n8n, a workflow automation platform. | [`integrations/builtin/credentials/lonescale.md`](pages/integrations/builtin/credentials/lonescale.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/lonescale) |
| Magento 2 credentials — Documentation for Magento 2 credentials. Use these credentials to authenticate Magento 2 in n8n, a workflow automation platform. | [`integrations/builtin/credentials/magento2.md`](pages/integrations/builtin/credentials/magento2.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/magento2) |
| Mailcheck credentials — Documentation for Mailcheck credentials. Use these credentials to authenticate Mailcheck in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mailcheck.md`](pages/integrations/builtin/credentials/mailcheck.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mailcheck) |
| Mailchimp credentials — Documentation for Mailchimp credentials. Use these credentials to authenticate Mailchimp in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mailchimp.md`](pages/integrations/builtin/credentials/mailchimp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mailchimp) |
| MailerLite credentials — Documentation for MailerLite credentials. Use these credentials to authenticate MailerLite in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mailerlite.md`](pages/integrations/builtin/credentials/mailerlite.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mailerlite) |
| Mailgun credentials — Documentation for Mailgun credentials. Use these credentials to authenticate Mailgun in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mailgun.md`](pages/integrations/builtin/credentials/mailgun.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mailgun) |
| Mailjet credentials — Documentation for Mailjet credentials. Use these credentials to authenticate Mailjet in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mailjet.md`](pages/integrations/builtin/credentials/mailjet.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mailjet) |
| Malcore credentials — Documentation for the Malcore credentials. Use these credentials to authenticate Malcore in n8n, a workflow automation platform. | [`integrations/builtin/credentials/malcore.md`](pages/integrations/builtin/credentials/malcore.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/malcore) |
| Mandrill credentials — Documentation for Mandrill credentials. Use these credentials to authenticate Mandrill in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mandrill.md`](pages/integrations/builtin/credentials/mandrill.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mandrill) |
| Marketstack credentials — Documentation for Marketstack credentials. Use these credentials to authenticate Marketstack in n8n, a workflow automation platform. | [`integrations/builtin/credentials/marketstack.md`](pages/integrations/builtin/credentials/marketstack.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/marketstack) |
| Matrix credentials — Documentation for Matrix credentials. Use these credentials to authenticate Matrix in n8n, a workflow automation platform. | [`integrations/builtin/credentials/matrix.md`](pages/integrations/builtin/credentials/matrix.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/matrix) |
| Mattermost credentials — Documentation for Mattermost credentials. Use these credentials to authenticate Mattermost in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mattermost.md`](pages/integrations/builtin/credentials/mattermost.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mattermost) |
| Mautic credentials — Documentation for Mautic credentials. Use these credentials to authenticate Mautic in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mautic.md`](pages/integrations/builtin/credentials/mautic.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mautic) |
| MCP credentials — Documentation for MCP credentials. Use these credentials to authenticate MCP servers in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mcp.md`](pages/integrations/builtin/credentials/mcp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mcp) |
| Medium credentials — Documentation for Medium credentials. Use these credentials to authenticate Medium in n8n, a workflow automation platform. | [`integrations/builtin/credentials/medium.md`](pages/integrations/builtin/credentials/medium.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/medium) |
| MessageBird credentials — Documentation for MessageBird credentials. Use these credentials to authenticate MessageBird in n8n, a workflow automation platform. | [`integrations/builtin/credentials/messagebird.md`](pages/integrations/builtin/credentials/messagebird.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/messagebird) |
| Metabase credentials — Documentation for Metabase credentials. Use these credentials to authenticate Metabase in n8n, a workflow automation platform. | [`integrations/builtin/credentials/metabase.md`](pages/integrations/builtin/credentials/metabase.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/metabase) |
| Microsoft credentials — Documentation for Microsoft credentials. Use these credentials to authenticate with Microsoft in n8n. | [`integrations/builtin/credentials/microsoft.md`](pages/integrations/builtin/credentials/microsoft.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/microsoft) |
| Microsoft Azure Monitor credentials — Documentation for the Microsoft Azure Monitor credentials. Use these credentials to authenticate Microsoft Azure Monitor in n8n, a workflow automation platform. | [`integrations/builtin/credentials/microsoftazuremonitor.md`](pages/integrations/builtin/credentials/microsoftazuremonitor.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/microsoftazuremonitor) |
| Microsoft Entra ID credentials — Documentation for the Microsoft Entra ID credentials. Use these credentials to authenticate Microsoft Entra ID in n8n, a workflow automation platform. | [`integrations/builtin/credentials/microsoftentra.md`](pages/integrations/builtin/credentials/microsoftentra.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/microsoftentra) |
| Microsoft Entra Service Principal credentials — Documentation for the Microsoft Entra Service Principal credentials. Use these credentials to authenticate Microsoft services in n8n, a workflow automation platform. | [`integrations/builtin/credentials/microsoftentraserviceprincipal.md`](pages/integrations/builtin/credentials/microsoftentraserviceprincipal.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal) |
| Microsoft SQL credentials — Documentation for Microsoft SQL credentials. Use these credentials to authenticate Microsoft SQL in n8n, a workflow automation platform. | [`integrations/builtin/credentials/microsoftsql.md`](pages/integrations/builtin/credentials/microsoftsql.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/microsoftsql) |
| Microsoft Agent 365 credentials — Documentation for Microsoft Agent 365 credentials. Use these credentials to authenticate Microsoft Agent 365 in n8n, a workflow automation platform. | [`integrations/builtin/credentials/microsoftagent365.md`](pages/integrations/builtin/credentials/microsoftagent365.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365) |
| Milvus credentials — Documentation for the Milvus credentials. Use these credentials to authenticate Milvus in n8n, a workflow automation platform. | [`integrations/builtin/credentials/milvus.md`](pages/integrations/builtin/credentials/milvus.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/milvus) |
| Mindee credentials — Documentation for Mindee credentials. Use these credentials to authenticate Mindee in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mindee.md`](pages/integrations/builtin/credentials/mindee.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mindee) |
| Miro credentials — Documentation for the Miro credentials. Use these credentials to authenticate Miro in n8n, a workflow automation platform. | [`integrations/builtin/credentials/miro.md`](pages/integrations/builtin/credentials/miro.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/miro) |
| MISP credentials — Documentation for MISP credentials. Use these credentials to authenticate MISP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/misp.md`](pages/integrations/builtin/credentials/misp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/misp) |
| Mist credentials — Documentation for the Mist credentials. Use these credentials to authenticate Mist in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mist.md`](pages/integrations/builtin/credentials/mist.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mist) |
| MiniMax credentials — Documentation for MiniMax credentials. Use these credentials to authenticate MiniMax in n8n, a workflow automation platform. | [`integrations/builtin/credentials/minimax.md`](pages/integrations/builtin/credentials/minimax.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/minimax) |
| Mistral Cloud credentials — Documentation for the Mistral Cloud credentials. Use these credentials to authenticate Mistral Cloud in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mistral.md`](pages/integrations/builtin/credentials/mistral.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mistral) |
| Mocean credentials — Documentation for Mocean credentials. Use these credentials to authenticate Mocean in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mocean.md`](pages/integrations/builtin/credentials/mocean.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mocean) |
| monday.com credentials — Documentation for monday.com credentials. Use these credentials to authenticate monday.com in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mondaycom.md`](pages/integrations/builtin/credentials/mondaycom.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mondaycom) |
| MongoDB credentials — Documentation for MongoDB credentials. Use these credentials to authenticate MongoDB in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mongodb.md`](pages/integrations/builtin/credentials/mongodb.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mongodb) |
| Monica CRM credentials — Documentation for Monica CRM credentials. Use these credentials to authenticate Monica CRM in n8n, a workflow automation platform. | [`integrations/builtin/credentials/monicacrm.md`](pages/integrations/builtin/credentials/monicacrm.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/monicacrm) |
| Moonshot credentials — Documentation for Moonshot credentials. Use these credentials to authenticate Moonshot in n8n, a workflow automation platform. | [`integrations/builtin/credentials/moonshot.md`](pages/integrations/builtin/credentials/moonshot.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/moonshot) |
| Motorhead credentials — Documentation for the Motorhead credentials. Use these credentials to authenticate Motorhead in n8n, a workflow automation platform. | [`integrations/builtin/credentials/motorhead.md`](pages/integrations/builtin/credentials/motorhead.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/motorhead) |
| MQTT credentials — Documentation for MQTT credentials. Use these credentials to authenticate MQTT in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mqtt.md`](pages/integrations/builtin/credentials/mqtt.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mqtt) |
| MSG91 credentials — Documentation for MSG91 credentials. Use these credentials to authenticate MSG91 in n8n, a workflow automation platform. | [`integrations/builtin/credentials/msg91.md`](pages/integrations/builtin/credentials/msg91.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/msg91) |
| MySQL credentials — Documentation for MySQL credentials. Use these credentials to authenticate MySQL in n8n, a workflow automation platform. | [`integrations/builtin/credentials/mysql.md`](pages/integrations/builtin/credentials/mysql.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/mysql) |
| NASA credentials — Documentation for NASA credentials. Use these credentials to authenticate NASA in n8n, a workflow automation platform. | [`integrations/builtin/credentials/nasa.md`](pages/integrations/builtin/credentials/nasa.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/nasa) |
| Netlify credentials — Documentation for Netlify credentials. Use these credentials to authenticate Netlify in n8n, a workflow automation platform. | [`integrations/builtin/credentials/netlify.md`](pages/integrations/builtin/credentials/netlify.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/netlify) |
| Netscaler ADC credentials — Documentation for Netscaler ADC credentials. Use these credentials to authenticate Netscaler ADC in n8n, a workflow automation platform. | [`integrations/builtin/credentials/netscaleradc.md`](pages/integrations/builtin/credentials/netscaleradc.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/netscaleradc) |
| Nextcloud credentials — Documentation for Nextcloud credentials. Use these credentials to authenticate Nextcloud in n8n, a workflow automation platform. | [`integrations/builtin/credentials/nextcloud.md`](pages/integrations/builtin/credentials/nextcloud.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/nextcloud) |
| NocoDB credentials — Documentation for NocoDB credentials. Use these credentials to authenticate NocoDB in n8n, a workflow automation platform. | [`integrations/builtin/credentials/nocodb.md`](pages/integrations/builtin/credentials/nocodb.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/nocodb) |
| Notion credentials — Documentation for Notion credentials. Use these credentials to authenticate Notion in n8n, a workflow automation platform. | [`integrations/builtin/credentials/notion.md`](pages/integrations/builtin/credentials/notion.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/notion) |
| npm credentials — Documentation for the npm credentials. Use these credentials to authenticate npm in n8n, a workflow automation platform. | [`integrations/builtin/credentials/npm.md`](pages/integrations/builtin/credentials/npm.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/npm) |
| NVIDIA Nemotron credentials — Documentation for NVIDIA Nemotron credentials. Use these credentials to authenticate NVIDIA Nemotron in n8n, a workflow automation platform. | [`integrations/builtin/credentials/nvidia.md`](pages/integrations/builtin/credentials/nvidia.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/nvidia) |
| Odoo credentials — Documentation for Odoo credentials. Use these credentials to authenticate Odoo in n8n, a workflow automation platform. | [`integrations/builtin/credentials/odoo.md`](pages/integrations/builtin/credentials/odoo.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/odoo) |
| Okta credentials — Documentation for the Okta credentials. Use these credentials to authenticate Okta in n8n, a workflow automation platform. | [`integrations/builtin/credentials/okta.md`](pages/integrations/builtin/credentials/okta.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/okta) |
| Ollama credentials — Documentation for the Ollama credentials. Use these credentials to authenticate Ollama in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ollama.md`](pages/integrations/builtin/credentials/ollama.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ollama) |
| One Simple API credentials — Documentation for One Simple API credentials. Use these credentials to authenticate One Simple API in n8n, a workflow automation platform. | [`integrations/builtin/credentials/onesimpleapi.md`](pages/integrations/builtin/credentials/onesimpleapi.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/onesimpleapi) |
| Onfleet credentials — Documentation for Onfleet credentials. Use these credentials to authenticate Onfleet in n8n, a workflow automation platform. | [`integrations/builtin/credentials/onfleet.md`](pages/integrations/builtin/credentials/onfleet.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/onfleet) |
| OpenAI credentials — Documentation for OpenAI credentials. Use these credentials to authenticate with OpenAI in n8n. | [`integrations/builtin/credentials/openai.md`](pages/integrations/builtin/credentials/openai.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/openai) |
| OpenCTI credentials — Documentation for the OpenCTI credentials. Use these credentials to authenticate OpenCTI in n8n, a workflow automation platform. | [`integrations/builtin/credentials/opencti.md`](pages/integrations/builtin/credentials/opencti.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/opencti) |
| OpenRouter credentials — Documentation for OpenRouter credentials. Use these credentials to authenticate OpenRouter in n8n, a workflow automation platform. | [`integrations/builtin/credentials/openrouter.md`](pages/integrations/builtin/credentials/openrouter.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/openrouter) |
| OpenWeatherMap credentials — Documentation for OpenWeatherMap credentials. Use these credentials to authenticate OpenWeatherMap in n8n, a workflow automation platform. | [`integrations/builtin/credentials/openweathermap.md`](pages/integrations/builtin/credentials/openweathermap.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/openweathermap) |
| Oracle Database credentials — Documentation for Oracle Database credentials. Use these credentials to authenticate Oracle Database in n8n, a workflow automation platform. | [`integrations/builtin/credentials/oracledb.md`](pages/integrations/builtin/credentials/oracledb.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/oracledb) |
| Oura credentials — Documentation for Oura credentials. Use these credentials to authenticate Oura in n8n, a workflow automation platform. | [`integrations/builtin/credentials/oura.md`](pages/integrations/builtin/credentials/oura.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/oura) |
| Paddle credentials — Documentation for Paddle credentials. Use these credentials to authenticate Paddle in n8n, a workflow automation platform. | [`integrations/builtin/credentials/paddle.md`](pages/integrations/builtin/credentials/paddle.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/paddle) |
| PagerDuty credentials — Documentation for PagerDuty credentials. Use these credentials to authenticate PagerDuty in n8n, a workflow automation platform. | [`integrations/builtin/credentials/pagerduty.md`](pages/integrations/builtin/credentials/pagerduty.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/pagerduty) |
| PayPal credentials — Documentation for PayPal credentials. Use these credentials to authenticate PayPal in n8n, a workflow automation platform. | [`integrations/builtin/credentials/paypal.md`](pages/integrations/builtin/credentials/paypal.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/paypal) |
| Peekalink credentials — Documentation for Peekalink credentials. Use these credentials to authenticate Peekalink in n8n, a workflow automation platform. | [`integrations/builtin/credentials/peekalink.md`](pages/integrations/builtin/credentials/peekalink.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/peekalink) |
| Perplexity credentials — Documentation for the Perplexity credentials. Use these credentials to authenticate Perplexity in n8n, a workflow automation platform. | [`integrations/builtin/credentials/perplexity.md`](pages/integrations/builtin/credentials/perplexity.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/perplexity) |
| PhantomBuster credentials — Documentation for PhantomBuster credentials. Use these credentials to authenticate PhantomBuster in n8n, a workflow automation platform. | [`integrations/builtin/credentials/phantombuster.md`](pages/integrations/builtin/credentials/phantombuster.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/phantombuster) |
| Philips Hue credentials — Documentation for Philips Hue credentials. Use these credentials to authenticate Philips Hue in n8n, a workflow automation platform. | [`integrations/builtin/credentials/philipshue.md`](pages/integrations/builtin/credentials/philipshue.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/philipshue) |
| Chroma credentials — Documentation for the Chroma credentials. Use these credentials to authenticate Chroma in n8n, a workflow automation platform. | [`integrations/builtin/credentials/chroma.md`](pages/integrations/builtin/credentials/chroma.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/chroma) |
| Pinecone credentials — Documentation for the Pinecone credentials. Use these credentials to authenticate Pinecone in n8n, a workflow automation platform. | [`integrations/builtin/credentials/pinecone.md`](pages/integrations/builtin/credentials/pinecone.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/pinecone) |
| Pipedrive credentials — Documentation for Pipedrive credentials. Use these credentials to authenticate Pipedrive in n8n, a workflow automation platform. | [`integrations/builtin/credentials/pipedrive.md`](pages/integrations/builtin/credentials/pipedrive.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/pipedrive) |
| Plivo credentials — Documentation for Plivo credentials. Use these credentials to authenticate Plivo in n8n, a workflow automation platform. | [`integrations/builtin/credentials/plivo.md`](pages/integrations/builtin/credentials/plivo.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/plivo) |
| Postgres credentials — Documentation for Postgres credentials. Use these credentials to authenticate Postgres in n8n, a workflow automation platform. | [`integrations/builtin/credentials/postgres.md`](pages/integrations/builtin/credentials/postgres.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/postgres) |
| PostHog credentials — Documentation for PostHog credentials. Use these credentials to authenticate PostHog in n8n, a workflow automation platform. | [`integrations/builtin/credentials/posthog.md`](pages/integrations/builtin/credentials/posthog.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/posthog) |
| Postmark credentials — Documentation for Postmark credentials. Use these credentials to authenticate Postmark in n8n, a workflow automation platform. | [`integrations/builtin/credentials/postmark.md`](pages/integrations/builtin/credentials/postmark.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/postmark) |
| ProfitWell credentials — Documentation for ProfitWell credentials. Use these credentials to authenticate ProfitWell in n8n, a workflow automation platform. | [`integrations/builtin/credentials/profitwell.md`](pages/integrations/builtin/credentials/profitwell.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/profitwell) |
| Pushbullet credentials — Documentation for Pushbullet credentials. Use these credentials to authenticate Pushbullet in n8n, a workflow automation platform. | [`integrations/builtin/credentials/pushbullet.md`](pages/integrations/builtin/credentials/pushbullet.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/pushbullet) |
| Pushcut credentials — Documentation for Pushcut credentials. Use these credentials to authenticate Pushcut in n8n, a workflow automation platform. | [`integrations/builtin/credentials/pushcut.md`](pages/integrations/builtin/credentials/pushcut.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/pushcut) |
| Pushover credentials — Documentation for Pushover credentials. Use these credentials to authenticate Pushover in n8n, a workflow automation platform. | [`integrations/builtin/credentials/pushover.md`](pages/integrations/builtin/credentials/pushover.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/pushover) |
| QRadar credentials — Documentation for the QRadar credentials. Use these credentials to authenticate QRadar in n8n, a workflow automation platform. | [`integrations/builtin/credentials/qradar.md`](pages/integrations/builtin/credentials/qradar.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/qradar) |
| Qdrant credentials — Documentation for the Qdrant credentials. Use these credentials to authenticate Qdrant in n8n, a workflow automation platform. | [`integrations/builtin/credentials/qdrant.md`](pages/integrations/builtin/credentials/qdrant.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/qdrant) |
| Qualys credentials — Documentation for the Qualys credentials. Use these credentials to authenticate Qualys in n8n, a workflow automation platform. | [`integrations/builtin/credentials/qualys.md`](pages/integrations/builtin/credentials/qualys.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/qualys) |
| QuestDB credentials — Documentation for QuestDB credentials. Use these credentials to authenticate QuestDB in n8n, a workflow automation platform. | [`integrations/builtin/credentials/questdb.md`](pages/integrations/builtin/credentials/questdb.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/questdb) |
| Quick Base credentials — Documentation for Quick Base credentials. Use these credentials to authenticate Quick Base in n8n, a workflow automation platform. | [`integrations/builtin/credentials/quickbase.md`](pages/integrations/builtin/credentials/quickbase.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/quickbase) |
| QuickBooks credentials — Documentation for QuickBooks credentials. Use these credentials to authenticate QuickBooks in n8n, a workflow automation platform. | [`integrations/builtin/credentials/quickbooks.md`](pages/integrations/builtin/credentials/quickbooks.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/quickbooks) |
| RabbitMQ credentials — Documentation for RabbitMQ credentials. Use these credentials to authenticate RabbitMQ in n8n, a workflow automation platform. | [`integrations/builtin/credentials/rabbitmq.md`](pages/integrations/builtin/credentials/rabbitmq.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/rabbitmq) |
| Raindrop credentials — Documentation for Raindrop credentials. Use these credentials to authenticate Raindrop in n8n, a workflow automation platform. | [`integrations/builtin/credentials/raindrop.md`](pages/integrations/builtin/credentials/raindrop.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/raindrop) |
| Rapid7 InsightVM credentials — Documentation for the Rapid7 InsightVM credentials. Use these credentials to authenticate Rapid7 InsightVm in n8n, a workflow automation platform. | [`integrations/builtin/credentials/rapid7insightvm.md`](pages/integrations/builtin/credentials/rapid7insightvm.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/rapid7insightvm) |
| Recorded Future credentials — Documentation for the Recorded Future credentials. Use these credentials to authenticate Recorded Future in n8n, a workflow automation platform. | [`integrations/builtin/credentials/recordedfuture.md`](pages/integrations/builtin/credentials/recordedfuture.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/recordedfuture) |
| Reddit credentials — Documentation for Reddit credentials. Use these credentials to authenticate Reddit in n8n, a workflow automation platform. | [`integrations/builtin/credentials/reddit.md`](pages/integrations/builtin/credentials/reddit.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/reddit) |
| Redis credentials — Documentation for Redis credentials. Use these credentials to authenticate Redis in n8n, a workflow automation platform. | [`integrations/builtin/credentials/redis.md`](pages/integrations/builtin/credentials/redis.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/redis) |
| Rocket.Chat credentials — Documentation for Rocket.Chat credentials. Use these credentials to authenticate Rocket.Chat in n8n, a workflow automation platform. | [`integrations/builtin/credentials/rocketchat.md`](pages/integrations/builtin/credentials/rocketchat.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/rocketchat) |
| Rundeck credentials — Documentation for Rundeck credentials. Use these credentials to authenticate Rundeck in n8n, a workflow automation platform. | [`integrations/builtin/credentials/rundeck.md`](pages/integrations/builtin/credentials/rundeck.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/rundeck) |
| S3 credentials — Documentation for S3 credentials. Use these credentials to authenticate S3 in n8n, a workflow automation platform. | [`integrations/builtin/credentials/s3.md`](pages/integrations/builtin/credentials/s3.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/s3) |
| Salesforce credentials — Documentation for Salesforce credentials. Use these credentials to authenticate Salesforce in n8n, a workflow automation platform. | [`integrations/builtin/credentials/salesforce.md`](pages/integrations/builtin/credentials/salesforce.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/salesforce) |
| Salesmate credentials — Documentation for Salesmate credentials. Use these credentials to authenticate Salesmate in n8n, a workflow automation platform. | [`integrations/builtin/credentials/salesmate.md`](pages/integrations/builtin/credentials/salesmate.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/salesmate) |
| Schema Registry credentials — Documentation for Schema Registry credentials. Use these credentials to authenticate Schema Registry in n8n, a workflow automation platform. | [`integrations/builtin/credentials/schemaregistry.md`](pages/integrations/builtin/credentials/schemaregistry.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/schemaregistry) |
| SearXNG credentials — Documentation for the SearXNG credentials. Use these credentials to authenticate SearXNG in n8n, a workflow automation platform. | [`integrations/builtin/credentials/searxng.md`](pages/integrations/builtin/credentials/searxng.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/searxng) |
| SeaTable credentials — Documentation for SeaTable credentials. Use these credentials to authenticate SeaTable in n8n, a workflow automation platform. | [`integrations/builtin/credentials/seatable.md`](pages/integrations/builtin/credentials/seatable.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/seatable) |
| SecurityScorecard credentials — Documentation for SecurityScorecard credentials. Use these credentials to authenticate SecurityScorecard in n8n, a workflow automation platform. | [`integrations/builtin/credentials/securityscorecard.md`](pages/integrations/builtin/credentials/securityscorecard.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/securityscorecard) |
| Segment credentials — Documentation for Segment credentials. Use these credentials to authenticate Segment in n8n, a workflow automation platform. | [`integrations/builtin/credentials/segment.md`](pages/integrations/builtin/credentials/segment.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/segment) |
| Sekoia credentials — Documentation for the Sekoia credentials. Use these credentials to authenticate Sekoia in n8n, a workflow automation platform. | [`integrations/builtin/credentials/sekoia.md`](pages/integrations/builtin/credentials/sekoia.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/sekoia) |
| Send Email — Documentation for Send Email credentials. Use these credentials to authenticate Send Email in n8n, a workflow automation platform. | [`integrations/builtin/credentials/send-email.md`](pages/integrations/builtin/credentials/send-email.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/send-email) |
| Gmail — Documentation for Gmail Send Email credentials. Use these credentials to authenticate Send Email with Gmail in n8n, a workflow automation platform. | [`integrations/builtin/credentials/send-email/gmail.md`](pages/integrations/builtin/credentials/send-email/gmail.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/send-email/gmail) |
| Outlook.com — Documentation for Outlook.com Send Email credentials. Use these credentials to authenticate Send Email with Outlook.com in n8n, a workflow automation platform. | [`integrations/builtin/credentials/send-email/outlook.md`](pages/integrations/builtin/credentials/send-email/outlook.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/send-email/outlook) |
| Yahoo — Documentation for Yahoo Send Email credentials. Use these credentials to authenticate Send Email with Yahoo in n8n, a workflow automation platform. | [`integrations/builtin/credentials/send-email/yahoo.md`](pages/integrations/builtin/credentials/send-email/yahoo.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/send-email/yahoo) |
| SendGrid credentials — Documentation for SendGrid credentials. Use these credentials to authenticate SendGrid in n8n, a workflow automation platform. | [`integrations/builtin/credentials/sendgrid.md`](pages/integrations/builtin/credentials/sendgrid.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/sendgrid) |
| Sendy credentials — Documentation for Sendy credentials. Use these credentials to authenticate Sendy in n8n, a workflow automation platform. | [`integrations/builtin/credentials/sendy.md`](pages/integrations/builtin/credentials/sendy.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/sendy) |
| Sentry.io credentials — Documentation for Sentry.io credentials. Use these credentials to authenticate Sentry.io in n8n, a workflow automation platform. | [`integrations/builtin/credentials/sentryio.md`](pages/integrations/builtin/credentials/sentryio.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/sentryio) |
| Serp credentials — Documentation for the Serp credentials. Use these credentials to authenticate Serp in n8n, a workflow automation platform. | [`integrations/builtin/credentials/serp.md`](pages/integrations/builtin/credentials/serp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/serp) |
| ServiceNow credentials — Documentation for ServiceNow credentials. Use these credentials to authenticate ServiceNow in n8n, a workflow automation platform. | [`integrations/builtin/credentials/servicenow.md`](pages/integrations/builtin/credentials/servicenow.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/servicenow) |
| seven credentials — Documentation for seven credentials. Use these credentials to authenticate seven in n8n, a workflow automation platform. | [`integrations/builtin/credentials/sms77.md`](pages/integrations/builtin/credentials/sms77.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/sms77) |
| Shopify credentials — Documentation for Shopify credentials. Use these credentials to authenticate Shopify in n8n, a workflow automation platform. | [`integrations/builtin/credentials/shopify.md`](pages/integrations/builtin/credentials/shopify.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/shopify) |
| Shuffler credentials — Documentation for the Shuffler credentials. Use these credentials to authenticate Shuffle in n8n, a workflow automation platform. | [`integrations/builtin/credentials/shuffler.md`](pages/integrations/builtin/credentials/shuffler.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/shuffler) |
| SIGNL4 credentials — Documentation for SIGNL4 credentials. Use these credentials to authenticate SIGNL4 in n8n, a workflow automation platform. | [`integrations/builtin/credentials/signl4.md`](pages/integrations/builtin/credentials/signl4.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/signl4) |
| Slack credentials — Documentation for Slack credentials. Use these credentials to authenticate Slack in n8n, a workflow automation platform. | [`integrations/builtin/credentials/slack.md`](pages/integrations/builtin/credentials/slack.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/slack) |
| Snowflake credentials — Documentation for Snowflake credentials. Use these credentials to authenticate Snowflake in n8n, a workflow automation platform. | [`integrations/builtin/credentials/snowflake.md`](pages/integrations/builtin/credentials/snowflake.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/snowflake) |
| SolarWinds IPAM credentials — Documentation for the SolarWinds IPAM credentials. Use these credentials to authenticate SolarWinds IPAM in n8n, a workflow automation platform. | [`integrations/builtin/credentials/solarwindsipam.md`](pages/integrations/builtin/credentials/solarwindsipam.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/solarwindsipam) |
| SolarWinds Observability SaaS credentials — Documentation for the SolarWinds Observability SaaS credential, Use these credentials to authenticate SolarWinds Observability SaaS in n8n, a workflow automation platform | [`integrations/builtin/credentials/solarwindsobservability.md`](pages/integrations/builtin/credentials/solarwindsobservability.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/solarwindsobservability) |
| Splunk credentials — Documentation for Splunk credentials. Use these credentials to authenticate Splunk in n8n, a workflow automation platform. | [`integrations/builtin/credentials/splunk.md`](pages/integrations/builtin/credentials/splunk.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/splunk) |
| Spotify credentials — Documentation for Spotify credentials. Use these credentials to authenticate Spotify in n8n, a workflow automation platform. | [`integrations/builtin/credentials/spotify.md`](pages/integrations/builtin/credentials/spotify.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/spotify) |
| SSH credentials — Documentation for SSH credentials. Use these credentials to authenticate SSH in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ssh.md`](pages/integrations/builtin/credentials/ssh.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ssh) |
| Stackby credentials — Documentation for Stackby credentials. Use these credentials to authenticate Stackby in n8n, a workflow automation platform. | [`integrations/builtin/credentials/stackby.md`](pages/integrations/builtin/credentials/stackby.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/stackby) |
| Storyblok credentials — Documentation for Storyblok credentials. Use these credentials to authenticate Storyblok in n8n, a workflow automation platform. | [`integrations/builtin/credentials/storyblok.md`](pages/integrations/builtin/credentials/storyblok.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/storyblok) |
| Strapi credentials — Documentation for Strapi credentials. Use these credentials to authenticate Strapi in n8n, a workflow automation platform. | [`integrations/builtin/credentials/strapi.md`](pages/integrations/builtin/credentials/strapi.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/strapi) |
| Strava credentials — Documentation for Strava credentials. Use these credentials to authenticate Strava in n8n, a workflow automation platform. | [`integrations/builtin/credentials/strava.md`](pages/integrations/builtin/credentials/strava.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/strava) |
| Stripe credentials — Documentation for Stripe credentials. Use these credentials to authenticate Stripe in n8n, a workflow automation platform. | [`integrations/builtin/credentials/stripe.md`](pages/integrations/builtin/credentials/stripe.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/stripe) |
| Supabase credentials — Documentation for Supabase credentials. Use these credentials to authenticate Supabase in n8n, a workflow automation platform. | [`integrations/builtin/credentials/supabase.md`](pages/integrations/builtin/credentials/supabase.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/supabase) |
| SurveyMonkey credentials — Documentation for SurveyMonkey credentials. Use these credentials to authenticate SurveyMonkey in n8n, a workflow automation platform. | [`integrations/builtin/credentials/surveymonkey.md`](pages/integrations/builtin/credentials/surveymonkey.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/surveymonkey) |
| SyncroMSP credentials — Documentation for SyncroMSP credentials. Use these credentials to authenticate SyncroMSP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/syncromsp.md`](pages/integrations/builtin/credentials/syncromsp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/syncromsp) |
| Sysdig credentials — Documentation for the Sysdig credentials. Use these credentials to authenticate Sysdig in n8n, a workflow automation platform. | [`integrations/builtin/credentials/sysdig.md`](pages/integrations/builtin/credentials/sysdig.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/sysdig) |
| Taiga credentials — Documentation for Taiga credentials. Use these credentials to authenticate Taiga in n8n, a workflow automation platform. | [`integrations/builtin/credentials/taiga.md`](pages/integrations/builtin/credentials/taiga.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/taiga) |
| Tapfiliate credentials — Documentation for Tapfiliate credentials. Use these credentials to authenticate Tapfiliate in n8n, a workflow automation platform. | [`integrations/builtin/credentials/tapfiliate.md`](pages/integrations/builtin/credentials/tapfiliate.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/tapfiliate) |
| Telegram credentials — Documentation for Telegram credentials. Use these credentials to authenticate with Telegram in n8n. | [`integrations/builtin/credentials/telegram.md`](pages/integrations/builtin/credentials/telegram.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/telegram) |
| TheHive credentials — Documentation for TheHive credentials. Use these credentials to authenticate TheHive in n8n, a workflow automation platform. | [`integrations/builtin/credentials/thehive.md`](pages/integrations/builtin/credentials/thehive.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/thehive) |
| TheHive 5 credentials — Documentation for TheHive 5 credentials. Use these credentials to authenticate TheHive in n8n, a workflow automation platform. | [`integrations/builtin/credentials/thehive5.md`](pages/integrations/builtin/credentials/thehive5.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/thehive5) |
| TimescaleDB credentials — Documentation for TimescaleDB credentials. Use these credentials to authenticate TimescaleDB in n8n, a workflow automation platform. | [`integrations/builtin/credentials/timescaledb.md`](pages/integrations/builtin/credentials/timescaledb.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/timescaledb) |
| Todoist credentials — Documentation for Todoist credentials. Use these credentials to authenticate Todoist in n8n, a workflow automation platform. | [`integrations/builtin/credentials/todoist.md`](pages/integrations/builtin/credentials/todoist.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/todoist) |
| Toggl credentials — Documentation for Toggl credentials. Use these credentials to authenticate Toggl in n8n, a workflow automation platform. | [`integrations/builtin/credentials/toggl.md`](pages/integrations/builtin/credentials/toggl.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/toggl) |
| TOTP credentials — Documentation for TOTP credentials. Use these credentials to authenticate TOTP in n8n, a workflow automation platform. | [`integrations/builtin/credentials/totp.md`](pages/integrations/builtin/credentials/totp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/totp) |
| Travis CI credentials — Documentation for Travis CI credentials. Use these credentials to authenticate Travis CI in n8n, a workflow automation platform. | [`integrations/builtin/credentials/travisci.md`](pages/integrations/builtin/credentials/travisci.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/travisci) |
| Trellix ePO credentials — Documentation for the Trellix ePO credentials. Use these credentials to authenticate Trellix ePO in n8n, a workflow automation platform. | [`integrations/builtin/credentials/trellixepo.md`](pages/integrations/builtin/credentials/trellixepo.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/trellixepo) |
| Trello credentials — Documentation for Trello credentials. Use these credentials to authenticate Trello in n8n, a workflow automation platform. | [`integrations/builtin/credentials/trello.md`](pages/integrations/builtin/credentials/trello.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/trello) |
| Twake credentials — Documentation for Twake credentials. Use these credentials to authenticate Twake in n8n, a workflow automation platform. | [`integrations/builtin/credentials/twake.md`](pages/integrations/builtin/credentials/twake.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/twake) |
| Twilio credentials — Documentation for Twilio credentials. Use these credentials to authenticate Twilio in n8n, a workflow automation platform. | [`integrations/builtin/credentials/twilio.md`](pages/integrations/builtin/credentials/twilio.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/twilio) |
| Twist credentials — Documentation for Twist credentials. Use these credentials to authenticate Twist in n8n, a workflow automation platform. | [`integrations/builtin/credentials/twist.md`](pages/integrations/builtin/credentials/twist.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/twist) |
| Typeform credentials — Documentation for Typeform credentials. Use these credentials to authenticate Typeform in n8n, a workflow automation platform. | [`integrations/builtin/credentials/typeform.md`](pages/integrations/builtin/credentials/typeform.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/typeform) |
| Unleashed Software credentials — Documentation for Unleashed Software credentials. Use these credentials to authenticate Unleashed Software in n8n, a workflow automation platform. | [`integrations/builtin/credentials/unleashedsoftware.md`](pages/integrations/builtin/credentials/unleashedsoftware.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/unleashedsoftware) |
| UpLead credentials — Documentation for UpLead credentials. Use these credentials to authenticate UpLead in n8n, a workflow automation platform. | [`integrations/builtin/credentials/uplead.md`](pages/integrations/builtin/credentials/uplead.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/uplead) |
| uProc credentials — Documentation for uProc credentials. Use these credentials to authenticate uProc in n8n, a workflow automation platform. | [`integrations/builtin/credentials/uproc.md`](pages/integrations/builtin/credentials/uproc.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/uproc) |
| UptimeRobot credentials — Documentation for UptimeRobot credentials. Use these credentials to authenticate UptimeRobot in n8n, a workflow automation platform. | [`integrations/builtin/credentials/uptimerobot.md`](pages/integrations/builtin/credentials/uptimerobot.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/uptimerobot) |
| urlscan.io credentials — Documentation for urlscan.io credentials. Use these credentials to authenticate urlscan.io in n8n, a workflow automation platform. | [`integrations/builtin/credentials/urlscanio.md`](pages/integrations/builtin/credentials/urlscanio.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/urlscanio) |
| Venafi TLS Protect Cloud credentials — Documentation for Venafi TLS Protect Cloud credentials. Use these credentials to authenticate Venafi TLS Protect Cloud in n8n, a workflow automation platform. | [`integrations/builtin/credentials/venafitlsprotectcloud.md`](pages/integrations/builtin/credentials/venafitlsprotectcloud.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectcloud) |
| Venafi TLS Protect Datacenter credentials — Documentation for Venafi TLS Protect Datacenter credentials. Use these credentials to authenticate Venafi TLS Protect Datacenter in n8n, a workflow automation platform. | [`integrations/builtin/credentials/venafitlsprotectdatacenter.md`](pages/integrations/builtin/credentials/venafitlsprotectdatacenter.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter) |
| Vercel AI Gateway credentials — Documentation for the Vercel AI Gateway credentials. Use these credentials to authenticate the Vercel AI Gateway in n8n, a workflow automation platform. | [`integrations/builtin/credentials/vercel.md`](pages/integrations/builtin/credentials/vercel.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/vercel) |
| Vero credentials — Documentation for Vero credentials. Use these credentials to authenticate Vero in n8n, a workflow automation platform. | [`integrations/builtin/credentials/vero.md`](pages/integrations/builtin/credentials/vero.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/vero) |
| VirusTotal credentials — Documentation for the VirusTotal credentials. Use these credentials to authenticate VirusTotal in n8n, a workflow automation platform. | [`integrations/builtin/credentials/virustotal.md`](pages/integrations/builtin/credentials/virustotal.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/virustotal) |
| Vonage credentials — Documentation for Vonage credentials. Use these credentials to authenticate Vonage in n8n, a workflow automation platform. | [`integrations/builtin/credentials/vonage.md`](pages/integrations/builtin/credentials/vonage.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/vonage) |
| Weaviate credentials — Documentation for Weaviate credentials. Use these credentials to authenticate Weaviate in n8n, a workflow automation platform. | [`integrations/builtin/credentials/weaviate.md`](pages/integrations/builtin/credentials/weaviate.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/weaviate) |
| Webex by Cisco credentials — Documentation for Webex by Cisco credentials. Use these credentials to authenticate Webex by Cisco in n8n, a workflow automation platform. | [`integrations/builtin/credentials/ciscowebex.md`](pages/integrations/builtin/credentials/ciscowebex.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/ciscowebex) |
| Webflow credentials — Documentation for Webflow credentials. Use these credentials to authenticate Webflow in n8n, a workflow automation platform. | [`integrations/builtin/credentials/webflow.md`](pages/integrations/builtin/credentials/webflow.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/webflow) |
| Webhook credentials — Documentation for Webhook credentials. Use these credentials to authenticate Webhook in n8n, a workflow automation platform. | [`integrations/builtin/credentials/webhook.md`](pages/integrations/builtin/credentials/webhook.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/webhook) |
| Wekan credentials — Documentation for Wekan credentials. Use these credentials to authenticate Wekan in n8n, a workflow automation platform. | [`integrations/builtin/credentials/wekan.md`](pages/integrations/builtin/credentials/wekan.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/wekan) |
| WhatsApp Business Cloud credentials — Documentation for WhatsApp Business Cloud credentials. Use these credentials to authenticate with WhatsApp Business Cloud in n8n. | [`integrations/builtin/credentials/whatsapp.md`](pages/integrations/builtin/credentials/whatsapp.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/whatsapp) |
| Wise credentials — Documentation for Wise credentials. Use these credentials to authenticate Wise in n8n, a workflow automation platform. | [`integrations/builtin/credentials/wise.md`](pages/integrations/builtin/credentials/wise.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/wise) |
| Wolfram|Alpha credentials — Documentation for the Wolfram\|Alpha credentials. Use these credentials to authenticate Wolfram\|Alpha in n8n, a workflow automation platform. | [`integrations/builtin/credentials/wolframalpha.md`](pages/integrations/builtin/credentials/wolframalpha.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/wolframalpha) |
| WooCommerce credentials — Documentation for WooCommerce credentials. Use these credentials to authenticate WooCommerce in n8n, a workflow automation platform. | [`integrations/builtin/credentials/woocommerce.md`](pages/integrations/builtin/credentials/woocommerce.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/woocommerce) |
| WordPress credentials — Documentation for WordPress credentials. Use these credentials to authenticate WordPress in n8n, a workflow automation platform. | [`integrations/builtin/credentials/wordpress.md`](pages/integrations/builtin/credentials/wordpress.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/wordpress) |
| Workable credentials — Documentation for Workable credentials. Use these credentials to authenticate Workable in n8n, a workflow automation platform. | [`integrations/builtin/credentials/workable.md`](pages/integrations/builtin/credentials/workable.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/workable) |
| Wufoo credentials — Documentation for Wufoo credentials. Use these credentials to authenticate Wufoo in n8n, a workflow automation platform. | [`integrations/builtin/credentials/wufoo.md`](pages/integrations/builtin/credentials/wufoo.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/wufoo) |
| X (formerly Twitter) credentials — Documentation for X credentials. Use these credentials to authenticate X in n8n, a workflow automation platform. | [`integrations/builtin/credentials/twitter.md`](pages/integrations/builtin/credentials/twitter.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/twitter) |
| xAI credentials — Documentation for xAI credentials. Use these credentials to authenticate xAI in n8n, a workflow automation platform. | [`integrations/builtin/credentials/xai.md`](pages/integrations/builtin/credentials/xai.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/xai) |
| Xata credentials — Documentation for the Xata credentials. Use these credentials to authenticate Xata in n8n, a workflow automation platform. | [`integrations/builtin/credentials/xata.md`](pages/integrations/builtin/credentials/xata.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/xata) |
| Xero credentials — Documentation for Xero credentials. Use these credentials to authenticate Xero in n8n, a workflow automation platform. | [`integrations/builtin/credentials/xero.md`](pages/integrations/builtin/credentials/xero.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/xero) |
| Yourls credentials — Documentation for Yourls credentials. Use these credentials to authenticate Yourls in n8n, a workflow automation platform. | [`integrations/builtin/credentials/yourls.md`](pages/integrations/builtin/credentials/yourls.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/yourls) |
| Zabbix credentials — Documentation for the Zabbix credentials. Use these credentials to authenticate Zabbix in n8n, a workflow automation platform. | [`integrations/builtin/credentials/zabbix.md`](pages/integrations/builtin/credentials/zabbix.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/zabbix) |
| Zammad credentials — Documentation for Zammad credentials. Use these credentials to authenticate Zammad in n8n, a workflow automation platform. | [`integrations/builtin/credentials/zammad.md`](pages/integrations/builtin/credentials/zammad.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/zammad) |
| Zendesk credentials — Documentation for Zendesk credentials. Use these credentials to authenticate Zendesk in n8n, a workflow automation platform. | [`integrations/builtin/credentials/zendesk.md`](pages/integrations/builtin/credentials/zendesk.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/zendesk) |
| Zep credentials — Documentation for the Zep credentials. Use these credentials to authenticate Zep in n8n, a workflow automation platform. | [`integrations/builtin/credentials/zep.md`](pages/integrations/builtin/credentials/zep.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/zep) |
| Zoho credentials — Documentation for Zoho credentials. Use these credentials to authenticate Zoho in n8n, a workflow automation platform. | [`integrations/builtin/credentials/zoho.md`](pages/integrations/builtin/credentials/zoho.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/zoho) |
| Zoom credentials — Documentation for Zoom credentials. Use these credentials to authenticate Zoom in n8n, a workflow automation platform. | [`integrations/builtin/credentials/zoom.md`](pages/integrations/builtin/credentials/zoom.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/zoom) |
| Zscaler ZIA credentials — Documentation for the Zscaler ZIA credentials. Use these credentials to authenticate Zscaler ZIA in n8n, a workflow automation platform. | [`integrations/builtin/credentials/zscalerzia.md`](pages/integrations/builtin/credentials/zscalerzia.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/zscalerzia) |
| Zulip credentials — Documentation for Zulip credentials. Use these credentials to authenticate Zulip in n8n, a workflow automation platform. | [`integrations/builtin/credentials/zulip.md`](pages/integrations/builtin/credentials/zulip.md) | [docs](https://docs.n8n.io/integrations/builtin/credentials/zulip) |
| Custom API actions for existing nodes | [`integrations/builtin/custom-api-actions-for-existing-nodes.md`](pages/integrations/builtin/custom-api-actions-for-existing-nodes.md) | [docs](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes) |
| Handle rate limits — How to handle API rate limits when using n8n integrations. | [`integrations/builtin/handle-rate-limits.md`](pages/integrations/builtin/handle-rate-limits.md) | [docs](https://docs.n8n.io/integrations/builtin/handle-rate-limits) |
| Deprecated nodes | [`integrations/builtin/deprecated-nodes.md`](pages/integrations/builtin/deprecated-nodes.md) | [docs](https://docs.n8n.io/integrations/builtin/deprecated-nodes) |
| Community nodes | [`integrations/community-nodes.md`](pages/integrations/community-nodes.md) | [docs](https://docs.n8n.io/integrations/community-nodes) |
| Installation and management | [`integrations/community-nodes/installation-and-management.md`](pages/integrations/community-nodes/installation-and-management.md) | [docs](https://docs.n8n.io/integrations/community-nodes/installation-and-management) |
| Install verified community nodes | [`integrations/community-nodes/installation-and-management/install-verified-community-nodes.md`](pages/integrations/community-nodes/installation-and-management/install-verified-community-nodes.md) | [docs](https://docs.n8n.io/integrations/community-nodes/installation-and-management/install-verified-community-nodes) |
| GUI installation | [`integrations/community-nodes/installation-and-management/gui-installation.md`](pages/integrations/community-nodes/installation-and-management/gui-installation.md) | [docs](https://docs.n8n.io/integrations/community-nodes/installation-and-management/gui-installation) |
| Manual installation | [`integrations/community-nodes/installation-and-management/manual-installation.md`](pages/integrations/community-nodes/installation-and-management/manual-installation.md) | [docs](https://docs.n8n.io/integrations/community-nodes/installation-and-management/manual-installation) |
| Environment variable installation | [`integrations/community-nodes/installation-and-management/environment-variable-installation.md`](pages/integrations/community-nodes/installation-and-management/environment-variable-installation.md) | [docs](https://docs.n8n.io/integrations/community-nodes/installation-and-management/environment-variable-installation) |
| Risks | [`integrations/community-nodes/risks.md`](pages/integrations/community-nodes/risks.md) | [docs](https://docs.n8n.io/integrations/community-nodes/risks) |
| Blocklist | [`integrations/community-nodes/blocklist.md`](pages/integrations/community-nodes/blocklist.md) | [docs](https://docs.n8n.io/integrations/community-nodes/blocklist) |
| Using community nodes | [`integrations/community-nodes/using-community-nodes.md`](pages/integrations/community-nodes/using-community-nodes.md) | [docs](https://docs.n8n.io/integrations/community-nodes/using-community-nodes) |
| Troubleshooting | [`integrations/community-nodes/troubleshooting.md`](pages/integrations/community-nodes/troubleshooting.md) | [docs](https://docs.n8n.io/integrations/community-nodes/troubleshooting) |
| Building community nodes | [`integrations/community-nodes/building-community-nodes.md`](pages/integrations/community-nodes/building-community-nodes.md) | [docs](https://docs.n8n.io/integrations/community-nodes/building-community-nodes) |

### Connect

| Page | Local copy | Official |
| --- | --- | --- |
| Connect — Use the API, CLI, and MCP server to connect to n8n programmatically. | [`connect/readme.md`](pages/connect/readme.md) | [docs](https://docs.n8n.io/connect/readme) |
| n8n API — Use n8n's public REST API to perform tasks programmatically instead of through the GUI. | [`connect/n8n-api.md`](pages/connect/n8n-api.md) | [docs](https://docs.n8n.io/connect/n8n-api) |
| Authentication — Authentication for n8n's public REST API. | [`connect/n8n-api/authentication.md`](pages/connect/n8n-api/authentication.md) | [docs](https://docs.n8n.io/connect/n8n-api/authentication) |
| Pagination — Pagination in n8n's public REST API. | [`connect/n8n-api/pagination.md`](pages/connect/n8n-api/pagination.md) | [docs](https://docs.n8n.io/connect/n8n-api/pagination) |
| Use an API playground — How to use an API playground to try out n8n's public REST API. | [`connect/n8n-api/use-an-api-playground.md`](pages/connect/n8n-api/use-an-api-playground.md) | [docs](https://docs.n8n.io/connect/n8n-api/use-an-api-playground) |
| Endpoint reference — Endpoint reference for n8n's public REST API, generated from the OpenAPI specification. | [`connect/n8n-api/api-reference.md`](pages/connect/n8n-api/api-reference.md) | [docs](https://docs.n8n.io/connect/n8n-api/api-reference) |
| Audit | [`connect/n8n-api/audit.md`](pages/connect/n8n-api/audit.md) | [docs](https://docs.n8n.io/connect/n8n-api/audit) |
| Community Package | [`connect/n8n-api/community-package.md`](pages/connect/n8n-api/community-package.md) | [docs](https://docs.n8n.io/connect/n8n-api/community-package) |
| Credential | [`connect/n8n-api/credential.md`](pages/connect/n8n-api/credential.md) | [docs](https://docs.n8n.io/connect/n8n-api/credential) |
| Data Table | [`connect/n8n-api/data-table.md`](pages/connect/n8n-api/data-table.md) | [docs](https://docs.n8n.io/connect/n8n-api/data-table) |
| Discover | [`connect/n8n-api/discover.md`](pages/connect/n8n-api/discover.md) | [docs](https://docs.n8n.io/connect/n8n-api/discover) |
| Evaluation | [`connect/n8n-api/evaluation.md`](pages/connect/n8n-api/evaluation.md) | [docs](https://docs.n8n.io/connect/n8n-api/evaluation) |
| Execution | [`connect/n8n-api/execution.md`](pages/connect/n8n-api/execution.md) | [docs](https://docs.n8n.io/connect/n8n-api/execution) |
| Folders | [`connect/n8n-api/folders.md`](pages/connect/n8n-api/folders.md) | [docs](https://docs.n8n.io/connect/n8n-api/folders) |
| Git Connections | [`connect/n8n-api/git-connections.md`](pages/connect/n8n-api/git-connections.md) | [docs](https://docs.n8n.io/connect/n8n-api/git-connections) |
| Insights | [`connect/n8n-api/insights.md`](pages/connect/n8n-api/insights.md) | [docs](https://docs.n8n.io/connect/n8n-api/insights) |
| Log Streaming | [`connect/n8n-api/log-streaming.md`](pages/connect/n8n-api/log-streaming.md) | [docs](https://docs.n8n.io/connect/n8n-api/log-streaming) |
| N8n Package | [`connect/n8n-api/n8n-package.md`](pages/connect/n8n-api/n8n-package.md) | [docs](https://docs.n8n.io/connect/n8n-api/n8n-package) |
| Projects | [`connect/n8n-api/projects.md`](pages/connect/n8n-api/projects.md) | [docs](https://docs.n8n.io/connect/n8n-api/projects) |
| Role | [`connect/n8n-api/role.md`](pages/connect/n8n-api/role.md) | [docs](https://docs.n8n.io/connect/n8n-api/role) |
| Role Mapping Rule | [`connect/n8n-api/role-mapping-rule.md`](pages/connect/n8n-api/role-mapping-rule.md) | [docs](https://docs.n8n.io/connect/n8n-api/role-mapping-rule) |
| Security Policy | [`connect/n8n-api/security-policy.md`](pages/connect/n8n-api/security-policy.md) | [docs](https://docs.n8n.io/connect/n8n-api/security-policy) |
| Settings Ldap | [`connect/n8n-api/settings-ldap.md`](pages/connect/n8n-api/settings-ldap.md) | [docs](https://docs.n8n.io/connect/n8n-api/settings-ldap) |
| Settings Otel | [`connect/n8n-api/settings-otel.md`](pages/connect/n8n-api/settings-otel.md) | [docs](https://docs.n8n.io/connect/n8n-api/settings-otel) |
| Settings Sso Oidc | [`connect/n8n-api/settings-sso-oidc.md`](pages/connect/n8n-api/settings-sso-oidc.md) | [docs](https://docs.n8n.io/connect/n8n-api/settings-sso-oidc) |
| Settings Sso Saml | [`connect/n8n-api/settings-sso-saml.md`](pages/connect/n8n-api/settings-sso-saml.md) | [docs](https://docs.n8n.io/connect/n8n-api/settings-sso-saml) |
| Source Control | [`connect/n8n-api/source-control.md`](pages/connect/n8n-api/source-control.md) | [docs](https://docs.n8n.io/connect/n8n-api/source-control) |
| Tags | [`connect/n8n-api/tags.md`](pages/connect/n8n-api/tags.md) | [docs](https://docs.n8n.io/connect/n8n-api/tags) |
| User | [`connect/n8n-api/user.md`](pages/connect/n8n-api/user.md) | [docs](https://docs.n8n.io/connect/n8n-api/user) |
| Variables | [`connect/n8n-api/variables.md`](pages/connect/n8n-api/variables.md) | [docs](https://docs.n8n.io/connect/n8n-api/variables) |
| Workflow | [`connect/n8n-api/workflow.md`](pages/connect/n8n-api/workflow.md) | [docs](https://docs.n8n.io/connect/n8n-api/workflow) |
| Models | [`connect/n8n-api/models.md`](pages/connect/n8n-api/models.md) | [docs](https://docs.n8n.io/connect/n8n-api/models) |
| n8n CLI — n8n CLI is a lightweight client for interacting with n8n programmatically through the Public API. | [`connect/n8n-cli.md`](pages/connect/n8n-cli.md) | [docs](https://docs.n8n.io/connect/n8n-cli) |
| Connect to n8n MCP server — Connect, authenticate, and integrate MCP clients to build and execute n8n workflows programmatically | [`connect/connect-to-n8n-mcp-server.md`](pages/connect/connect-to-n8n-mcp-server.md) | [docs](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) |
| MCP client connection examples — Copy-paste connection commands and configuration for Lovable, Claude Desktop, Claude Code, Codex, Gemini CLI, Cursor, VS Code, Windsurf, and Google ADK agents. | [`connect/connect-to-n8n-mcp-server/mcp-client-examples.md`](pages/connect/connect-to-n8n-mcp-server/mcp-client-examples.md) | [docs](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples) |
| MCP server tools reference — Complete reference for all tools exposed by the n8n MCP server, including workflow management, workflow builder, agent management, and data table tools. | [`connect/connect-to-n8n-mcp-server/mcp-server-tools-reference.md`](pages/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference.md) | [docs](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) |
| Connect to the n8n docs MCP server — Connect an AI tool to an n8n docs Model Context Protocol (MCP) server to search and answer questions from the documentation and wider knowledge base. | [`connect/connect-to-n8n-docs-mcp-server.md`](pages/connect/connect-to-n8n-docs-mcp-server.md) | [docs](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server) |
| Create nodes — Plan, build, test, and deploy a custom n8n node. | [`connect/create-nodes.md`](pages/connect/create-nodes.md) | [docs](https://docs.n8n.io/connect/create-nodes) |
| Overview | [`connect/create-nodes/overview.md`](pages/connect/create-nodes/overview.md) | [docs](https://docs.n8n.io/connect/create-nodes/overview) |
| Plan your node | [`connect/create-nodes/plan-your-node.md`](pages/connect/create-nodes/plan-your-node.md) | [docs](https://docs.n8n.io/connect/create-nodes/plan-your-node) |
| Choose a node type | [`connect/create-nodes/plan-your-node/choose-a-node-type.md`](pages/connect/create-nodes/plan-your-node/choose-a-node-type.md) | [docs](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-type) |
| Choose a node building style | [`connect/create-nodes/plan-your-node/choose-a-node-building-style.md`](pages/connect/create-nodes/plan-your-node/choose-a-node-building-style.md) | [docs](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-building-style) |
| Node UI design | [`connect/create-nodes/plan-your-node/node-ui-design.md`](pages/connect/create-nodes/plan-your-node/node-ui-design.md) | [docs](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design) |
| Choose node file structure | [`connect/create-nodes/plan-your-node/choose-node-file-structure.md`](pages/connect/create-nodes/plan-your-node/choose-node-file-structure.md) | [docs](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-node-file-structure) |
| Build your node | [`connect/create-nodes/build-your-node.md`](pages/connect/create-nodes/build-your-node.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node) |
| Set up your development environment | [`connect/create-nodes/build-your-node/set-up-your-development-environment.md`](pages/connect/create-nodes/build-your-node/set-up-your-development-environment.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/set-up-your-development-environment) |
| Using the n8n-node tool | [`connect/create-nodes/build-your-node/using-the-n8n-node-tool.md`](pages/connect/create-nodes/build-your-node/using-the-n8n-node-tool.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/using-the-n8n-node-tool) |
| Tutorial: Build a declarative-style node | [`connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node.md`](pages/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node) |
| Tutorial: Build a programmatic-style node | [`connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node.md`](pages/connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node) |
| Reference | [`connect/create-nodes/build-your-node/reference.md`](pages/connect/create-nodes/build-your-node/reference.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference) |
| Node UI elements | [`connect/create-nodes/build-your-node/reference/node-ui-elements.md`](pages/connect/create-nodes/build-your-node/reference/node-ui-elements.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements) |
| Code standards | [`connect/create-nodes/build-your-node/reference/code-standards.md`](pages/connect/create-nodes/build-your-node/reference/code-standards.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/code-standards) |
| Error handling | [`connect/create-nodes/build-your-node/reference/error-handling.md`](pages/connect/create-nodes/build-your-node/reference/error-handling.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/error-handling) |
| Versioning | [`connect/create-nodes/build-your-node/reference/versioning.md`](pages/connect/create-nodes/build-your-node/reference/versioning.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning) |
| Base files | [`connect/create-nodes/build-your-node/reference/base-files.md`](pages/connect/create-nodes/build-your-node/reference/base-files.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files) |
| Structure — A reference document detailing the basic structure of the node base file. | [`connect/create-nodes/build-your-node/reference/base-files/structure.md`](pages/connect/create-nodes/build-your-node/reference/base-files/structure.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure) |
| Standard parameters — A reference document listing the standard parameters of the node base file. | [`connect/create-nodes/build-your-node/reference/base-files/standard-parameters.md`](pages/connect/create-nodes/build-your-node/reference/base-files/standard-parameters.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters) |
| Declarative-style parameters — A reference document listing the declarative-style parameters of the node base file. | [`connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters.md`](pages/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters) |
| Programmatic-style parameters — A reference document listing the programmatic-style parameters of the node base file. | [`connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters.md`](pages/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters) |
| Programmatic-style execute method — A reference document for the programmatic-style execute() method of the node base file. | [`connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method.md`](pages/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method) |
| Codex files | [`connect/create-nodes/build-your-node/reference/codex-files.md`](pages/connect/create-nodes/build-your-node/reference/codex-files.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/codex-files) |
| Credentials files | [`connect/create-nodes/build-your-node/reference/credentials-files.md`](pages/connect/create-nodes/build-your-node/reference/credentials-files.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/credentials-files) |
| HTTP request helpers | [`connect/create-nodes/build-your-node/reference/http-request-helpers.md`](pages/connect/create-nodes/build-your-node/reference/http-request-helpers.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/http-request-helpers) |
| Item linking | [`connect/create-nodes/build-your-node/reference/item-linking.md`](pages/connect/create-nodes/build-your-node/reference/item-linking.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/item-linking) |
| UX guidelines | [`connect/create-nodes/build-your-node/reference/ux-guidelines.md`](pages/connect/create-nodes/build-your-node/reference/ux-guidelines.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/ux-guidelines) |
| Verification guidelines | [`connect/create-nodes/build-your-node/reference/verification-guidelines.md`](pages/connect/create-nodes/build-your-node/reference/verification-guidelines.md) | [docs](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/verification-guidelines) |
| Test your node | [`connect/create-nodes/test-your-node.md`](pages/connect/create-nodes/test-your-node.md) | [docs](https://docs.n8n.io/connect/create-nodes/test-your-node) |
| Run your node locally | [`connect/create-nodes/test-your-node/run-your-node-locally.md`](pages/connect/create-nodes/test-your-node/run-your-node-locally.md) | [docs](https://docs.n8n.io/connect/create-nodes/test-your-node/run-your-node-locally) |
| Node linter | [`connect/create-nodes/test-your-node/node-linter.md`](pages/connect/create-nodes/test-your-node/node-linter.md) | [docs](https://docs.n8n.io/connect/create-nodes/test-your-node/node-linter) |
| Troubleshooting | [`connect/create-nodes/test-your-node/troubleshooting.md`](pages/connect/create-nodes/test-your-node/troubleshooting.md) | [docs](https://docs.n8n.io/connect/create-nodes/test-your-node/troubleshooting) |
| Deploy your node | [`connect/create-nodes/deploy-your-node.md`](pages/connect/create-nodes/deploy-your-node.md) | [docs](https://docs.n8n.io/connect/create-nodes/deploy-your-node) |
| Submit community nodes | [`connect/create-nodes/deploy-your-node/submit-community-nodes.md`](pages/connect/create-nodes/deploy-your-node/submit-community-nodes.md) | [docs](https://docs.n8n.io/connect/create-nodes/deploy-your-node/submit-community-nodes) |
| Install private nodes | [`connect/create-nodes/deploy-your-node/install-private-nodes.md`](pages/connect/create-nodes/deploy-your-node/install-private-nodes.md) | [docs](https://docs.n8n.io/connect/create-nodes/deploy-your-node/install-private-nodes) |

### Administer

| Page | Local copy | Official |
| --- | --- | --- |
| Administer — Secure, manage, and operate your n8n instance. | [`administer/readme.md`](pages/administer/readme.md) | [docs](https://docs.n8n.io/administer/readme) |
| Manage users and access — User management in n8n | [`administer/manage-users-and-access.md`](pages/administer/manage-users-and-access.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access) |
| Set up for Cloud — Set up user management on n8n Cloud | [`administer/manage-users-and-access/set-up-for-cloud.md`](pages/administer/manage-users-and-access/set-up-for-cloud.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/set-up-for-cloud) |
| Add and remove users | [`administer/manage-users-and-access/add-and-remove-users.md`](pages/administer/manage-users-and-access/add-and-remove-users.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/add-and-remove-users) |
| Understand instance roles — n8n instance roles | [`administer/manage-users-and-access/understand-instance-roles.md`](pages/administer/manage-users-and-access/understand-instance-roles.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/understand-instance-roles) |
| Set permissions and roles (RBAC) — Set up and use role-based access control (RBAC) in n8n. | [`administer/manage-users-and-access/set-permissions-and-roles-rbac.md`](pages/administer/manage-users-and-access/set-permissions-and-roles-rbac.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac) |
| See available roles — Understand the RBAC roles available in n8n, and the access they have. | [`administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md`](pages/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles) |
| Organize work in projects — Understand how n8n uses project for RBAC. Learn how to create and manage projects. | [`administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md`](pages/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects) |
| Custom roles — Overview of custom roles in n8n, project-level and instance-level. | [`administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles.md`](pages/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles) |
| Create custom project roles — Create and manage custom project roles with granular permissions in n8n. | [`administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles/create-custom-project-roles.md`](pages/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles/create-custom-project-roles.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles/create-custom-project-roles) |
| Create custom instance roles — Create and manage custom instance roles with granular permissions in n8n. | [`administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles/create-custom-instance-roles.md`](pages/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles/create-custom-instance-roles.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles/create-custom-instance-roles) |
| Verify user identity | [`administer/manage-users-and-access/verify-user-identity.md`](pages/administer/manage-users-and-access/verify-user-identity.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity) |
| Require two-factor auth — How to enable 2FA for your n8n account | [`administer/manage-users-and-access/verify-user-identity/require-two-factor-auth.md`](pages/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth) |
| Connect LDAP — Using LDAP with n8n. | [`administer/manage-users-and-access/verify-user-identity/connect-ldap.md`](pages/administer/manage-users-and-access/verify-user-identity/connect-ldap.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/connect-ldap) |
| Use SAML | [`administer/manage-users-and-access/verify-user-identity/use-saml.md`](pages/administer/manage-users-and-access/verify-user-identity/use-saml.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml) |
| Set up SAML — Generic setup instructions for using SAML SSO with n8n. | [`administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml.md`](pages/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-saml) |
| Manage users with SAML — How to manage users and user logins with SAML enabled. | [`administer/manage-users-and-access/verify-user-identity/use-saml/manage-users-with-saml.md`](pages/administer/manage-users-and-access/verify-user-identity/use-saml/manage-users-with-saml.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/manage-users-with-saml) |
| Set up Okta Workforce Identity SAML — Use Okta Workforce Identity with n8n. | [`administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml.md`](pages/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-okta-workforce-identity-saml) |
| Set up Azure AD SAML — Use Azure AD with n8n. | [`administer/manage-users-and-access/verify-user-identity/use-saml/set-up-azure-ad-saml.md`](pages/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-azure-ad-saml.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/set-up-azure-ad-saml) |
| Troubleshoot SAML — A list of things to check if you encounter issues with SAML. | [`administer/manage-users-and-access/verify-user-identity/use-saml/troubleshoot-saml.md`](pages/administer/manage-users-and-access/verify-user-identity/use-saml/troubleshoot-saml.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml/troubleshoot-saml) |
| Use OIDC | [`administer/manage-users-and-access/verify-user-identity/use-oidc.md`](pages/administer/manage-users-and-access/verify-user-identity/use-oidc.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc) |
| Set up OIDC — Set up instructions for enabling OIDC SSO with n8n. | [`administer/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc.md`](pages/administer/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/set-up-oidc) |
| Troubleshoot OIDC — Things to be aware of and troubleshooting OIDC within n8n | [`administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc.md`](pages/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-oidc/troubleshoot-oidc) |
| Follow best practices — User management best practices. | [`administer/manage-users-and-access/follow-best-practices.md`](pages/administer/manage-users-and-access/follow-best-practices.md) | [docs](https://docs.n8n.io/administer/manage-users-and-access/follow-best-practices) |
| Use source control and environments — Overview of source control and environments in n8n | [`administer/use-source-control-and-environments.md`](pages/administer/use-source-control-and-environments.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments) |
| Understand source control — Understand how source control and environments work in n8n. | [`administer/use-source-control-and-environments/understand-source-control.md`](pages/administer/use-source-control-and-environments/understand-source-control.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/understand-source-control) |
| Work with environments — Understand the concepts behind environments in n8n. | [`administer/use-source-control-and-environments/work-with-environments.md`](pages/administer/use-source-control-and-environments/work-with-environments.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments) |
| Use Git in n8n — Git concepts and limitations in n8n. | [`administer/use-source-control-and-environments/use-git-in-n8n.md`](pages/administer/use-source-control-and-environments/use-git-in-n8n.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n) |
| Choose branching patterns — Understand the different relationships between n8n instances and Git branches that are possible with source control. | [`administer/use-source-control-and-environments/choose-branching-patterns.md`](pages/administer/use-source-control-and-environments/choose-branching-patterns.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns) |
| Set up source control — Link n8n to your Git provider. | [`administer/use-source-control-and-environments/set-up-source-control.md`](pages/administer/use-source-control-and-environments/set-up-source-control.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control) |
| Push and pull changes — Send work to Git, and fetch work from Git to your instance. | [`administer/use-source-control-and-environments/push-and-pull-changes.md`](pages/administer/use-source-control-and-environments/push-and-pull-changes.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes) |
| Compare versions — Use workflow diffs to compare local and remote changes | [`administer/use-source-control-and-environments/compare-versions.md`](pages/administer/use-source-control-and-environments/compare-versions.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions) |
| Move work between environments — How to get changes from one environment into another. | [`administer/use-source-control-and-environments/move-work-between-environments.md`](pages/administer/use-source-control-and-environments/move-work-between-environments.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments) |
| Tutorial: Create environments with source control — How to use n8n's source control feature to create environments. | [`administer/use-source-control-and-environments/tutorial-create-environments-with-source-control.md`](pages/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control.md) | [docs](https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control) |
| Manage credentials | [`administer/manage-credentials.md`](pages/administer/manage-credentials.md) | [docs](https://docs.n8n.io/administer/manage-credentials) |
| Share credentials securely — Share credentials within an organization. | [`administer/manage-credentials/share-credentials-securely.md`](pages/administer/manage-credentials/share-credentials-securely.md) | [docs](https://docs.n8n.io/administer/manage-credentials/share-credentials-securely) |
| End-user credentials — Let each user connect their own account to a credential, so a workflow runs with the credentials of the person who triggers it. | [`administer/manage-credentials/end-user-credentials.md`](pages/administer/manage-credentials/end-user-credentials.md) | [docs](https://docs.n8n.io/administer/manage-credentials/end-user-credentials) |
| Credential overwrites — Set credential data globally on a self-hosted n8n instance so users can authenticate without seeing or entering client secrets. | [`administer/manage-credentials/credential-overwrites.md`](pages/administer/manage-credentials/credential-overwrites.md) | [docs](https://docs.n8n.io/administer/manage-credentials/credential-overwrites) |
| Use external secret stores — Use an external secrets vault with n8n. | [`administer/manage-credentials/use-external-secret-stores.md`](pages/administer/manage-credentials/use-external-secret-stores.md) | [docs](https://docs.n8n.io/administer/manage-credentials/use-external-secret-stores) |
| Observe and log | [`administer/observe-and-log.md`](pages/administer/observe-and-log.md) | [docs](https://docs.n8n.io/administer/observe-and-log) |
| Track usage with Insights — Insights | [`administer/observe-and-log/track-usage-with-insights.md`](pages/administer/observe-and-log/track-usage-with-insights.md) | [docs](https://docs.n8n.io/administer/observe-and-log/track-usage-with-insights) |
| Stream logs to external systems — Stream events from n8n to your logging tools. | [`administer/observe-and-log/stream-logs-to-external-systems.md`](pages/administer/observe-and-log/stream-logs-to-external-systems.md) | [docs](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems) |

### Contribute

| Page | Local copy | Official |
| --- | --- | --- |
| Contribute to n8n — Learn how to contribute to n8n. | [`contribute/contribute-to-n8n.md`](pages/contribute/contribute-to-n8n.md) | [docs](https://docs.n8n.io/contribute/contribute-to-n8n) |
| Contribution guide for n8n Docs | [`contribute/contribution-guide-for-n8n-docs.md`](pages/contribute/contribution-guide-for-n8n-docs.md) | [docs](https://docs.n8n.io/contribute/contribution-guide-for-n8n-docs) |
| Style guide for n8n Docs | [`contribute/style-guide-for-n8n-docs.md`](pages/contribute/style-guide-for-n8n-docs.md) | [docs](https://docs.n8n.io/contribute/style-guide-for-n8n-docs) |
| Terminology and naming — The official n8n terms to use in documentation, with the non-official terms to avoid. | [`contribute/terminology.md`](pages/contribute/terminology.md) | [docs](https://docs.n8n.io/contribute/terminology) |
| Where to get help — How to get help and support with n8n. | [`contribute/where-to-get-help.md`](pages/contribute/where-to-get-help.md) | [docs](https://docs.n8n.io/contribute/where-to-get-help) |

### Privacy and security

| Page | Local copy | Official |
| --- | --- | --- |
| Privacy — n8n's privacy policies | [`privacy-and-security/privacy.md`](pages/privacy-and-security/privacy.md) | [docs](https://docs.n8n.io/privacy-and-security/privacy) |
| Incident response — n8n's incident response procedures. | [`privacy-and-security/incident-response.md`](pages/privacy-and-security/incident-response.md) | [docs](https://docs.n8n.io/privacy-and-security/incident-response) |
| What you can do — What you can do to improve privacy and data security when using n8n. | [`privacy-and-security/what-you-can-do.md`](pages/privacy-and-security/what-you-can-do.md) | [docs](https://docs.n8n.io/privacy-and-security/what-you-can-do) |

### Changelog

| Page | Local copy | Official |
| --- | --- | --- |
| Changelog — A curated, narrative summary of the most important new n8n features as they roll out. | [`changelog/readme.md`](pages/changelog/readme.md) | [docs](https://docs.n8n.io/changelog/readme) |
| Release notes — A running log of feature-level updates from each n8n release, newest first. | [`changelog/release-notes.md`](pages/changelog/release-notes.md) | [docs](https://docs.n8n.io/changelog/release-notes) |
| Release notes 2.x — Archived release notes detailing new features and bug fixes for n8n 2.x. | [`changelog/release-notes-2.x.md`](pages/changelog/release-notes-2.x.md) | [docs](https://docs.n8n.io/changelog/release-notes-2.x) |
| Release notes 1.x — Release notes detailing new features and bug fixes for n8n. | [`changelog/release-notes-1.x.md`](pages/changelog/release-notes-1.x.md) | [docs](https://docs.n8n.io/changelog/release-notes-1.x) |
| Release notes 0.x — Release notes detailing new features and bug fixes for n8n. | [`changelog/release-notes-0.x.md`](pages/changelog/release-notes-0.x.md) | [docs](https://docs.n8n.io/changelog/release-notes-0.x) |
| v3.0 Breaking changes — Breaking changes coming in n8n 3.0 | [`changelog/v30-breaking-changes.md`](pages/changelog/v30-breaking-changes.md) | [docs](https://docs.n8n.io/changelog/v30-breaking-changes) |
| v2.0 Breaking changes — Breaking changes coming in n8n 2.0 | [`changelog/v20-breaking-changes.md`](pages/changelog/v20-breaking-changes.md) | [docs](https://docs.n8n.io/changelog/v20-breaking-changes) |
| v2.0 Migration tool — Tool to help you migrate to n8n 2.0 | [`changelog/v20-migration-tool.md`](pages/changelog/v20-migration-tool.md) | [docs](https://docs.n8n.io/changelog/v20-migration-tool) |
| v1.0 Migration guide — What's new in n8n 1.0 | [`changelog/v10-migration-guide.md`](pages/changelog/v10-migration-guide.md) | [docs](https://docs.n8n.io/changelog/v10-migration-guide) |

### n8n Community License

| Page | Local copy | Official |
| --- | --- | --- |
| Sustainable Use License | [`n8n-community-license/sustainable-use-license.md`](pages/n8n-community-license/sustainable-use-license.md) | [docs](https://docs.n8n.io/n8n-community-license/sustainable-use-license) |

---


## Nodes and integrations catalog

945 node, credential, and community-node pages from the official docs.

### `integrations` (3)

- [Nodes](pages/integrations/readme.md) — Learn about n8n's built-in nodes, community nodes, MCP servers, and generic integrations.
- [Built-in nodes](pages/integrations/builtin.md) — Explore n8n's built-in core nodes, app nodes, trigger nodes, cluster nodes, and credentials.
- [Community nodes](pages/integrations/community-nodes.md)

### `builtin/node-types.md` (1)

- [Node types](pages/integrations/builtin/node-types.md) — Learn about n8n's core nodes, cluster nodes, credentials, and community nodes.

### `builtin/core-nodes.md` (1)

- [Core nodes](pages/integrations/builtin/core-nodes.md)

### `builtin/core-nodes` (78)

- [Activation Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger.md) — Learn how to use the Activation Trigger node in n8n. Follow technical documentation to integrate Activation Trigger node into your workflows.
- [Aggregate](pages/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md) — Documentation for the Aggregate node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [AI Transform](pages/integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md) — Documentation for the AI Transform node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Code](pages/integrations/builtin/core-nodes/n8n-nodes-base.code.md) — Documentation for the Code node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Keyboard shortcuts](pages/integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md) — A list of the keyboard shortcuts, for multiple platforms, which are supported by the Code node editor.
- [Common issues](pages/integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues.md) — Documentation for common issues and questions in the Code node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Compare Datasets](pages/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md) — Documentation for the Compare Datasets node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Compression](pages/integrations/builtin/core-nodes/n8n-nodes-base.compression.md) — Documentation for the Compression node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Chat Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger.md) — Learn how to use the Chat Trigger node in n8n. Follow technical documentation to integrate Chat Trigger node into your workflows.
- [Common issues](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues.md) — Documentation for common issues and questions in the Chat Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Convert to File](pages/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md) — Documentation for the Convert to File node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Crypto](pages/integrations/builtin/core-nodes/n8n-nodes-base.crypto.md) — Documentation for the Crypto node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Data Table](pages/integrations/builtin/core-nodes/n8n-nodes-base.datatable.md) — Documentation for the data table node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Row operations](pages/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows.md) — Reference documentation for Data Table node row operations, including delete, get, insert, update, and upsert.
- [Table operations](pages/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables.md) — Reference documentation for Data Table node table operations, including create, delete, list, and update.
- [Date & Time](pages/integrations/builtin/core-nodes/n8n-nodes-base.datetime.md) — Documentation for the Date & Time node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Debug Helper](pages/integrations/builtin/core-nodes/n8n-nodes-base.debughelper.md) — Documentation for the Debug Helper node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Edit Fields (Set)](pages/integrations/builtin/core-nodes/n8n-nodes-base.set.md) — Documentation for the Edit Fields node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Edit Image](pages/integrations/builtin/core-nodes/n8n-nodes-base.editimage.md) — Documentation for the Edit Image node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Email Trigger (IMAP)](pages/integrations/builtin/core-nodes/n8n-nodes-base.emailimap.md) — Learn how to use the Email Trigger (IMAP) Trigger node in n8n. Follow technical documentation to integrate Email Trigger (IMAP) Trigger node into your workflows.
- [Error Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md) — Learn how to use the Error Trigger node in n8n. Follow technical documentation to integrate Error Trigger node into your workflows.
- [Evaluation](pages/integrations/builtin/core-nodes/n8n-nodes-base.evaluation.md) — Documentation for the Evaluation node in n8n, a workflow automation platform. Includes guidance on usage and links to examples.
- [Evaluation Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger.md) — Learn how to use the Evaluation Trigger node in n8n. Follow technical documentation to integrate Evaluation Trigger node into your workflows.
- [Execute Command](pages/integrations/builtin/core-nodes/n8n-nodes-base.executecommand.md) — Documentation for the Execute Command node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Common issues](pages/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues.md) — Documentation for common issues and questions in the Execute Command node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Execute Sub-workflow](pages/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) — Documentation for the Execute Sub-workflow node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Execute Sub-workflow Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md) — Learn how to use the Execute Sub-workflow Trigger node in n8n. Follow technical documentation to integrate Execute Sub-workflow Trigger node into your workflows.
- [Execution Data](pages/integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md) — Documentation for the Execution Data node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Extract From File](pages/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md) — Documentation for the Extract From File node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Filter](pages/integrations/builtin/core-nodes/n8n-nodes-base.filter.md) — Documentation for the Filter node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [FTP](pages/integrations/builtin/core-nodes/n8n-nodes-base.ftp.md) — Documentation for the FTP node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Git](pages/integrations/builtin/core-nodes/n8n-nodes-base.git.md) — Documentation for the Git node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [GraphQL](pages/integrations/builtin/core-nodes/n8n-nodes-base.graphql.md) — Documentation for the GraphQL node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Guardrails](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails.md) — Documentation for the Guardrails node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [HTML](pages/integrations/builtin/core-nodes/n8n-nodes-base.html.md) — Documentation for the HTML node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [HTTP Request](pages/integrations/builtin/core-nodes/n8n-nodes-base.httprequest.md) — Learn how to use the HTTP Request node in n8n. Follow technical documentation to integrate the HTTP Request node into your workflows.
- [Common Issues](pages/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues.md) — Documentation for common issues and questions in the HTTP Request node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [If](pages/integrations/builtin/core-nodes/n8n-nodes-base.if.md) — Documentation for the If node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [JWT](pages/integrations/builtin/core-nodes/n8n-nodes-base.jwt.md) — Documentation for the JWT node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [LDAP](pages/integrations/builtin/core-nodes/n8n-nodes-base.ldap.md) — Documentation for the LDAP node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Limit](pages/integrations/builtin/core-nodes/n8n-nodes-base.limit.md) — Documentation for the Limit node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Local File Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger.md) — Learn how to use the Local File Trigger node in n8n. Follow technical documentation to integrate Local File Trigger node into your workflows.
- [Loop Over Items (Split in Batches)](pages/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) — Documentation for the Loop Over Items node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Manual Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md) — Learn how to use the Manual Trigger node in n8n. Follow technical documentation to integrate Manual Trigger node into your workflows.
- [Markdown](pages/integrations/builtin/core-nodes/n8n-nodes-base.markdown.md) — Documentation for the Markdown node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [MCP Client](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient.md) — Learn how to use the MCP Client node in n8n. Follow technical documentation to integrate MCP Client node into your workflows.
- [MCP Server Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger.md) — Learn how to use the MCP Server Trigger node in n8n. Follow technical documentation to integrate the MCP Server Trigger node into your workflows.
- [Merge](pages/integrations/builtin/core-nodes/n8n-nodes-base.merge.md) — Documentation for the Merge node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [n8n](pages/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md) — Documentation for the n8n node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [n8n Form](pages/integrations/builtin/core-nodes/n8n-nodes-base.form.md) — Documentation for the n8n Form node in n8n, a workflow automation platform. Includes guidance on usage and links to examples.
- [n8n Form](pages/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md) — Learn how to use the n8n Form Trigger node in n8n. Follow technical documentation to integrate n8n Form Trigger node into your workflows.
- [n8n Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md) — Learn how to use the n8n Trigger node in n8n. Follow technical documentation to integrate n8n Trigger node into your workflows.
- [No Operation, do nothing](pages/integrations/builtin/core-nodes/n8n-nodes-base.noop.md) — Documentation for the No Operation, do nothing node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Read/Write Files from Disk](pages/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) — Documentation for the Read/Write Files from Disk node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Remove Duplicates](pages/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates.md) — Documentation for the Remove Duplicates node in n8n, a workflow automation platform. Includes guidance on usage and links to examples.
- [Templates and examples](pages/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples.md) — Documentation for templates and examples in the Remove Duplicates node in n8n, a workflow automation platform. Includes templates using the node and examples of how to use it.
- [Rename Keys](pages/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys.md) — Documentation for the Rename Keys node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Chat](pages/integrations/builtin/core-nodes/n8n-nodes-langchain.chat.md) — Learn how to use the Chat node in n8n. Follow technical documentation to integrate the Chat node into your workflows.
- [Respond to Webhook](pages/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) — Documentation for the Respond to Webhook node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [RSS Read](pages/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedread.md) — Documentation for the RSS Read node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [RSS Feed Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger.md) — Learn how to use the RSS Feed Trigger node in n8n. Follow technical documentation to integrate RSS Feed Trigger node into your workflows.
- [Schedule Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger.md) — Learn how to use the Schedule Trigger node in n8n. Follow technical documentation to integrate Schedule Trigger node into your workflows.
- [Common issues](pages/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues.md) — Documentation for common issues and questions in the Schedule Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Send Email](pages/integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md) — Documentation for the Send Email node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Sort](pages/integrations/builtin/core-nodes/n8n-nodes-base.sort.md) — Documentation for the Sort node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Split Out](pages/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md) — Documentation for the Split Out node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [SSE Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.ssetrigger.md) — Learn how to use the SSE Trigger node in n8n. Follow technical documentation to integrate SSE Trigger node into your workflows.
- [SSH](pages/integrations/builtin/core-nodes/n8n-nodes-base.ssh.md) — Documentation for the SSH node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Stop And Error](pages/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) — Documentation for the Stop And Error node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Summarize](pages/integrations/builtin/core-nodes/n8n-nodes-base.summarize.md) — Documentation for the Summarize node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Switch](pages/integrations/builtin/core-nodes/n8n-nodes-base.switch.md) — Documentation for the Switch node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [TOTP](pages/integrations/builtin/core-nodes/n8n-nodes-base.totp.md) — Documentation for the TOTP node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Wait](pages/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) — Documentation for the Wait node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
- [Webhook](pages/integrations/builtin/core-nodes/n8n-nodes-base.webhook.md) — Learn how to use the Webhook node in n8n. Follow technical documentation to integrate Webhook node into your workflows.
- [Workflow development](pages/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md) — Learn how to build, test, and use the Webhook node in your workflows in n8n.
- [Common issues](pages/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues.md) — Documentation for common issues and questions in the Webhook node in n8n, a workflow automation platform. Includes details of the issues and suggested solutions.
- [Workflow Trigger](pages/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger.md) — Learn how to use the Workflow Trigger node in n8n. Follow technical documentation to integrate Workflow Trigger node into your workflows.
- [XML](pages/integrations/builtin/core-nodes/n8n-nodes-base.xml.md) — Documentation for the XML node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.

### `builtin/app-nodes.md` (1)

- [App nodes](pages/integrations/builtin/app-nodes.md)

### `builtin/app-nodes` (309)

- [Action Network](pages/integrations/builtin/app-nodes/n8n-nodes-base.actionnetwork.md) — Learn how to use the Action Network node in n8n. Follow technical documentation to integrate Action Network node into your workflows.
- [ActiveCampaign](pages/integrations/builtin/app-nodes/n8n-nodes-base.activecampaign.md) — Learn how to use the ActiveCampaign node in n8n. Follow technical documentation to integrate ActiveCampaign node into your workflows.
- [Adalo](pages/integrations/builtin/app-nodes/n8n-nodes-base.adalo.md) — Learn how to use the Adalo node in n8n. Follow technical documentation to integrate Adalo node into your workflows.
- [Affinity](pages/integrations/builtin/app-nodes/n8n-nodes-base.affinity.md) — Learn how to use the Affinity node in n8n. Follow technical documentation to integrate Affinity node into your workflows.
- [Agile CRM](pages/integrations/builtin/app-nodes/n8n-nodes-base.agilecrm.md) — Learn how to use the Agile CRM node in n8n. Follow technical documentation to integrate Agile CRM node into your workflows.
- [Airtable](pages/integrations/builtin/app-nodes/n8n-nodes-base.airtable.md) — Learn how to use the Airtable node in n8n. Follow technical documentation to integrate Airtable node into your workflows.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues.md) — Documentation for common issues and questions in the Airtable node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Airtop](pages/integrations/builtin/app-nodes/n8n-nodes-base.airtop.md) — Learn how to use the Airtop node in n8n. Follow technical documentation to integrate Airtop node into your workflows.
- [Qwen Cloud](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud.md) — Interact with models available on Qwen Cloud. This page explains how to use the node in n8n workflows to generate text completions, analyze or generate images, and create videos from text
- [AMQP Sender](pages/integrations/builtin/app-nodes/n8n-nodes-base.amqp.md) — Learn how to use the AMQP Sender node in n8n. Follow technical documentation to integrate AMQP Sender node into your workflows.
- [Anthropic](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.anthropic.md) — Learn how to use the Anthropic node in n8n. Follow technical documentation to integrate Anthropic node into your workflows.
- [APITemplate.io](pages/integrations/builtin/app-nodes/n8n-nodes-base.apitemplateio.md) — Learn how to use the APITemplate.io node in n8n. Follow technical documentation to integrate APITemplate.io node into your workflows.
- [Asana](pages/integrations/builtin/app-nodes/n8n-nodes-base.asana.md) — Learn how to use the Asana node in n8n. Follow technical documentation to integrate Asana node into your workflows.
- [Autopilot](pages/integrations/builtin/app-nodes/n8n-nodes-base.autopilot.md) — Learn how to use the Autopilot node in n8n. Follow technical documentation to integrate Autopilot node into your workflows.
- [AWS Certificate Manager](pages/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager.md) — Learn how to use the AWS Certificate Manager node in n8n. Follow technical documentation to integrate AAWS Certificage Manager node into your workflows.
- [AWS Cognito](pages/integrations/builtin/app-nodes/n8n-nodes-base.awscognito.md) — Learn how to use the AWS Cognito node in n8n. Follow technical documentation to integrate AWS Cognito node into your workflows.
- [AWS Comprehend](pages/integrations/builtin/app-nodes/n8n-nodes-base.awscomprehend.md) — Learn how to use the AWS Comprehend node in n8n. Follow technical documentation to integrate AWS Comprehend node into your workflows.
- [AWS DynamoDB](pages/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb.md) — Learn how to use the AWS DynamoDB node in n8n. Follow technical documentation to integrate AWS DynamoDB node into your workflows.
- [AWS Elastic Load Balancing](pages/integrations/builtin/app-nodes/n8n-nodes-base.awselb.md) — Learn how to use the AWS Elastic Load Balancing node in n8n. Follow technical documentation to integrate AWS Elastic Load Balancing node into your workflows.
- [AWS IAM](pages/integrations/builtin/app-nodes/n8n-nodes-base.awsiam.md) — Learn how to use the AWS IAM node in n8n. Follow technical documentation to integrate AWS IAM node into your workflows.
- [AWS Lambda](pages/integrations/builtin/app-nodes/n8n-nodes-base.awslambda.md) — Learn how to use the AWS Lambda node in n8n. Follow technical documentation to integrate AWS Lambda node into your workflows.
- [AWS Rekognition](pages/integrations/builtin/app-nodes/n8n-nodes-base.awsrekognition.md) — Learn how to use the AWS Rekognition node in n8n. Follow technical documentation to integrate AWS Rekognition node into your workflows.
- [AWS S3](pages/integrations/builtin/app-nodes/n8n-nodes-base.awss3.md) — Learn how to use the AWS S3 node in n8n. Follow technical documentation to integrate AWS S3 node into your workflows.
- [AWS SES](pages/integrations/builtin/app-nodes/n8n-nodes-base.awsses.md) — Learn how to use the AWS SES node in n8n. Follow technical documentation to integrate AWS SES node into your workflows.
- [AWS SNS](pages/integrations/builtin/app-nodes/n8n-nodes-base.awssns.md) — Learn how to use the AWS SNS node in n8n. Follow technical documentation to integrate AWS SNS node into your workflows.
- [AWS SQS](pages/integrations/builtin/app-nodes/n8n-nodes-base.awssqs.md) — Learn how to use the AWS SQS node in n8n. Follow technical documentation to integrate AWS SQS node into your workflows.
- [AWS Textract](pages/integrations/builtin/app-nodes/n8n-nodes-base.awstextract.md) — Learn how to use the AWS Textract node in n8n. Follow technical documentation to integrate AWS Textract node into your workflows.
- [AWS Transcribe](pages/integrations/builtin/app-nodes/n8n-nodes-base.awstranscribe.md) — Learn how to use the AWS Transcribe node in n8n. Follow technical documentation to integrate AWS Transcribe node into your workflows.
- [Azure Cosmos DB](pages/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb.md) — Learn how to use the Azure Cosmos DB node in n8n. Follow technical documentation to integrate Azure Cosmos DB node into your workflows.
- [Azure Storage](pages/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage.md) — Learn how to use the Azure Storage node in n8n. Follow technical documentation to integrate Azure Storage node into your workflows.
- [BambooHR](pages/integrations/builtin/app-nodes/n8n-nodes-base.bamboohr.md) — Learn how to use the BambooHR node in n8n. Follow technical documentation to integrate BambooHR node into your workflows.
- [Bannerbear](pages/integrations/builtin/app-nodes/n8n-nodes-base.bannerbear.md) — Learn how to use the Bannerbear node in n8n. Follow technical documentation to integrate Bannerbear node into your workflows.
- [Baserow](pages/integrations/builtin/app-nodes/n8n-nodes-base.baserow.md) — Learn how to use the Baserow node in n8n. Follow technical documentation to integrate Baserow node into your workflows.
- [Beeminder](pages/integrations/builtin/app-nodes/n8n-nodes-base.beeminder.md) — Learn how to use the Beeminder node in n8n. Follow technical documentation to integrate Beeminder node into your workflows.
- [Bitly](pages/integrations/builtin/app-nodes/n8n-nodes-base.bitly.md) — Learn how to use the Bitly node in n8n. Follow technical documentation to integrate Bitly node into your workflows.
- [Bitwarden](pages/integrations/builtin/app-nodes/n8n-nodes-base.bitwarden.md) — Learn how to use the Bitwarden node in n8n. Follow technical documentation to integrate Bitwarden node into your workflows.
- [Box](pages/integrations/builtin/app-nodes/n8n-nodes-base.box.md) — Learn how to use the Box node in n8n. Follow technical documentation to integrate Box node into your workflows.
- [Brandfetch](pages/integrations/builtin/app-nodes/n8n-nodes-base.brandfetch.md) — Learn how to use the Brandfetch node in n8n. Follow technical documentation to integrate Brandfetch node into your workflows.
- [Brevo](pages/integrations/builtin/app-nodes/n8n-nodes-base.brevo.md) — Learn how to use the Brevo node in n8n. Follow technical documentation to integrate Brevo node into your workflows.
- [Bubble](pages/integrations/builtin/app-nodes/n8n-nodes-base.bubble.md) — Learn how to use the Bubble node in n8n. Follow technical documentation to integrate Bubble node into your workflows.
- [Chargebee](pages/integrations/builtin/app-nodes/n8n-nodes-base.chargebee.md) — Learn how to use the Chargebee node in n8n. Follow technical documentation to integrate Chargebee node into your workflows.
- [CircleCI](pages/integrations/builtin/app-nodes/n8n-nodes-base.circleci.md) — Learn how to use the CircleCI node in n8n. Follow technical documentation to integrate CircleCI node into your workflows.
- [Webex by Cisco](pages/integrations/builtin/app-nodes/n8n-nodes-base.ciscowebex.md) — Learn how to use the Webex by Cisco node in n8n. Follow technical documentation to integrate Webex by Cisco node into your workflows.
- [Clearbit](pages/integrations/builtin/app-nodes/n8n-nodes-base.clearbit.md) — Learn how to use the Clearbit node in n8n. Follow technical documentation to integrate Clearbit node into your workflows.
- [ClickUp](pages/integrations/builtin/app-nodes/n8n-nodes-base.clickup.md) — Learn how to use the ClickUp node in n8n. Follow technical documentation to integrate ClickUp node into your workflows.
- [Clockify](pages/integrations/builtin/app-nodes/n8n-nodes-base.clockify.md) — Learn how to use the Clockify node in n8n. Follow technical documentation to integrate Clockify node into your workflows.
- [Cloudflare](pages/integrations/builtin/app-nodes/n8n-nodes-base.cloudflare.md) — Learn how to use the Cloudflare node in n8n. Follow technical documentation to integrate Cloudflare node into your workflows.
- [Cockpit](pages/integrations/builtin/app-nodes/n8n-nodes-base.cockpit.md) — Learn how to use the Cockpit node in n8n. Follow technical documentation to integrate Cockpit node into your workflows.
- [Coda](pages/integrations/builtin/app-nodes/n8n-nodes-base.coda.md) — Learn how to use the Coda node in n8n. Follow technical documentation to integrate Coda node into your workflows.
- [CoinGecko](pages/integrations/builtin/app-nodes/n8n-nodes-base.coingecko.md) — Learn how to use the CoinGecko node in n8n. Follow technical documentation to integrate CoinGecko node into your workflows.
- [Contentful](pages/integrations/builtin/app-nodes/n8n-nodes-base.contentful.md) — Learn how to use the Contentful node in n8n. Follow technical documentation to integrate Contentful node into your workflows.
- [ConvertKit](pages/integrations/builtin/app-nodes/n8n-nodes-base.convertkit.md) — Learn how to use the ConvertKit node in n8n. Follow technical documentation to integrate ConvertKit node into your workflows.
- [Copper](pages/integrations/builtin/app-nodes/n8n-nodes-base.copper.md) — Learn how to use the Copper node in n8n. Follow technical documentation to integrate Copper node into your workflows.
- [Cortex](pages/integrations/builtin/app-nodes/n8n-nodes-base.cortex.md) — Learn how to use the Cortex node in n8n. Follow technical documentation to integrate Cortex node into your workflows.
- [CrateDB](pages/integrations/builtin/app-nodes/n8n-nodes-base.cratedb.md) — Learn how to use the CrateDB node in n8n. Follow technical documentation to integrate CrateDB node into your workflows.
- [Customer.io](pages/integrations/builtin/app-nodes/n8n-nodes-base.customerio.md) — Learn how to use the Customer.io node in n8n. Follow technical documentation to integrate Customer.io node into your workflows.
- [Databricks](pages/integrations/builtin/app-nodes/n8n-nodes-base.databricks.md) — Learn how to use the Databricks node in n8n. Follow technical documentation to integrate Databricks node into your workflows.
- [DeepL](pages/integrations/builtin/app-nodes/n8n-nodes-base.deepl.md) — Learn how to use the DeepL node in n8n. Follow technical documentation to integrate DeepL node into your workflows.
- [Demio](pages/integrations/builtin/app-nodes/n8n-nodes-base.demio.md) — Learn how to use the Demio node in n8n. Follow technical documentation to integrate Demio node into your workflows.
- [DHL](pages/integrations/builtin/app-nodes/n8n-nodes-base.dhl.md) — Learn how to use the DHL node in n8n. Follow technical documentation to integrate DHL node into your workflows.
- [Discord](pages/integrations/builtin/app-nodes/n8n-nodes-base.discord.md) — Learn how to use the Discord node in n8n. Follow technical documentation to integrate Discord node into your workflows.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues.md) — Documentation for common issues and questions in the Discord node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Discourse](pages/integrations/builtin/app-nodes/n8n-nodes-base.discourse.md) — Learn how to use the Discourse node in n8n. Follow technical documentation to integrate Discourse node into your workflows.
- [Disqus](pages/integrations/builtin/app-nodes/n8n-nodes-base.disqus.md) — Learn how to use the Disqus node in n8n. Follow technical documentation to integrate Disqus node into your workflows.
- [Drift](pages/integrations/builtin/app-nodes/n8n-nodes-base.drift.md) — Learn how to use the Drift node in n8n. Follow technical documentation to integrate Drift node into your workflows.
- [Dropbox](pages/integrations/builtin/app-nodes/n8n-nodes-base.dropbox.md) — Learn how to use the Dropbox node in n8n. Follow technical documentation to integrate Dropbox node into your workflows.
- [Dropcontact](pages/integrations/builtin/app-nodes/n8n-nodes-base.dropcontact.md) — Learn how to use the Dropcontact node in n8n. Follow technical documentation to integrate Dropcontact node into your workflows.
- [E-goi](pages/integrations/builtin/app-nodes/n8n-nodes-base.egoi.md) — Learn how to use the E=goi node in n8n. Follow technical documentation to integrate E=goi node into your workflows.
- [Elasticsearch](pages/integrations/builtin/app-nodes/n8n-nodes-base.elasticsearch.md) — Learn how to use the Elasticsearch node in n8n. Follow technical documentation to integrate Elasticsearch node into your workflows.
- [Elastic Security](pages/integrations/builtin/app-nodes/n8n-nodes-base.elasticsecurity.md) — Learn how to use the Elastic Security node in n8n. Follow technical documentation to integrate Elastic Security node into your workflows.
- [Emelia](pages/integrations/builtin/app-nodes/n8n-nodes-base.emelia.md) — Learn how to use the Emelia node in n8n. Follow technical documentation to integrate Emelia node into your workflows.
- [ERPNext](pages/integrations/builtin/app-nodes/n8n-nodes-base.erpnext.md) — Learn how to use the ERPNext node in n8n. Follow technical documentation to integrate ERPNext node into your workflows.
- [Facebook Graph API](pages/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md) — Learn how to use the Facebook Graph API node in n8n. Follow technical documentation to integrate Facebook Graph API node into your workflows.
- [FileMaker](pages/integrations/builtin/app-nodes/n8n-nodes-base.filemaker.md) — Learn how to use the FileMaker node in n8n. Follow technical documentation to integrate FileMaker node into your workflows.
- [Flow](pages/integrations/builtin/app-nodes/n8n-nodes-base.flow.md) — Learn how to use the Flow node in n8n. Follow technical documentation to integrate Flow node into your workflows.
- [Freshdesk](pages/integrations/builtin/app-nodes/n8n-nodes-base.freshdesk.md) — Learn how to use the Freshdesk node in n8n. Follow technical documentation to integrate Freshdesk node into your workflows.
- [Freshservice](pages/integrations/builtin/app-nodes/n8n-nodes-base.freshservice.md) — Learn how to use the Freshservice node in n8n. Follow technical documentation to integrate Freshservice node into your workflows.
- [Freshworks CRM](pages/integrations/builtin/app-nodes/n8n-nodes-base.freshworkscrm.md) — Learn how to use the Freshworks CRM node in n8n. Follow technical documentation to integrate Freshworks CRM node into your workflows.
- [GetResponse](pages/integrations/builtin/app-nodes/n8n-nodes-base.getresponse.md) — Learn how to use the GetResponse node in n8n. Follow technical documentation to integrate GetResponse node into your workflows.
- [Ghost](pages/integrations/builtin/app-nodes/n8n-nodes-base.ghost.md) — Learn how to use the Ghost node in n8n. Follow technical documentation to integrate Ghost node into your workflows.
- [GitHub](pages/integrations/builtin/app-nodes/n8n-nodes-base.github.md) — Learn how to use the GitHub node in n8n. Follow technical documentation to integrate GitHub node into your workflows.
- [GitLab](pages/integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md) — Learn how to use the GitLab node in n8n. Follow technical documentation to integrate GitLab node into your workflows.
- [Gmail](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail.md) — Learn how to use the Gmail node in n8n. Follow technical documentation to integrate Gmail node into your workflows.
- [Draft Operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md) — Learn how to use the Draft Operations of the Gmail node in n8n. Follow technical documentation to integrate Draft Operations into your workflows.
- [Label Operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md) — Learn how to use the Label Operations of the Gmail node in n8n. Follow technical documentation to integrate Label Operations into your workflows.
- [Message Operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md) — Learn how to use the Message Operations of the Gmail node in n8n. Follow technical documentation to integrate Message Operations into your workflows.
- [Thread Operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md) — Learn how to use the Thread Operations of the Gmail node in n8n. Follow technical documentation to integrate Thread Operations into your workflows.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md) — Documentation for common issues and questions in the Gmail node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Gong](pages/integrations/builtin/app-nodes/n8n-nodes-base.gong.md) — Learn how to use the Gong node in n8n. Follow technical documentation to integrate Gong node into your workflows.
- [Google Ads](pages/integrations/builtin/app-nodes/n8n-nodes-base.googleads.md) — Learn how to use the Google Ads node in n8n. Follow technical documentation to integrate Google Ads node into your workflows.
- [Google Analytics](pages/integrations/builtin/app-nodes/n8n-nodes-base.googleanalytics.md) — Learn how to use the Google Analytics node in n8n. Follow technical documentation to integrate Google Analytics node into your workflows.
- [Google BigQuery](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery.md) — Learn how to use the Google BigQuery node in n8n. Follow technical documentation to integrate Google BigQuery node into your workflows.
- [Google Books](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md) — Learn how to use the Google Books node in n8n. Follow technical documentation to integrate Google Books node into your workflows.
- [Google Business Profile](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile.md) — Learn how to use the Google Business Profile node in n8n. Follow technical documentation to integrate Google Business Profile node into your workflows.
- [Google Calendar](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar.md) — Learn how to use the Google Calendar node in n8n. Follow technical documentation to integrate Google Calendar node into your workflows.
- [Calendar operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations.md) — Documentation for the Calendar operations in Google Calendar node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials inform
- [Event operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md) — Documentation for the Event operations in Google Calendar node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials informati
- [Google Chat](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md) — Learn how to use the Google Chat node in n8n. Follow technical documentation to integrate Google Chat node into your workflows.
- [Google Cloud Firestore](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudfirestore.md) — Learn how to use the Google Cloud Firestore node in n8n. Follow technical documentation to integrate Google Cloud Firestore node into your workflows.
- [Google Cloud Natural Language](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudnaturallanguage.md) — Learn how to use the Google Cloud Natural Language node in n8n. Follow technical documentation to integrate Google Cloud Natural Language node into your workflows.
- [Google Cloud Realtime Database](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md) — Learn how to use the Google Cloud Realtime Database node in n8n. Follow technical documentation to integrate Google Cloud Realtime Database node into your workflows.
- [Google Cloud Storage](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage.md) — Learn how to use the Google Cloud Storage node in n8n. Follow technical documentation to integrate Google Cloud Storage node into your workflows.
- [Google Contacts](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlecontacts.md) — Learn how to use the Google Contacts node in n8n. Follow technical documentation to integrate Google Contacts node into your workflows.
- [Google Docs](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledocs.md) — Learn how to use the Google Docs node in n8n. Follow technical documentation to integrate Google Docs node into your workflows.
- [Google Drive](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive.md) — Learn how to use the Google Drive node in n8n. Follow technical documentation to integrate Google Drive node into your workflows.
- [File operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md) — Documentation for the File operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
- [File and Folder operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations.md) — Documentation for the File and Folder operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials in
- [Folder operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md) — Documentation for the Folder operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information
- [Shared Drive operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md) — Documentation for the Shared Drive operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials infor
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues.md) — Documentation for common questions and solutions in the Google Drive node in n8n, a workflow automation platform. Includes details of the issue and suggested resolutions.
- [Google Gemini](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini.md) — Learn how to use the Google Gemini node in n8n. Follow technical documentation to integrate Google Gemini node into your workflows.
- [Google Perspective](pages/integrations/builtin/app-nodes/n8n-nodes-base.googleperspective.md) — Learn how to use the Google Perspective node in n8n. Follow technical documentation to integrate Google Perspective node into your workflows.
- [Google Sheets](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets.md) — Documentation for the Google Sheets node in n8n. Includes details of operations and configuration, and links to examples and credentials information.
- [Document operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md) — Documentation for the Document operations in Google Sheets node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials informat
- [Sheet Within Document operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md) — Documentation for the Sheet operations in Google Sheets node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md) — Documentation for common questions and solutions in the Google Sheets node in n8n, a workflow automation platform. Includes details of the issue and suggested resolutions.
- [Google Slides](pages/integrations/builtin/app-nodes/n8n-nodes-base.googleslides.md) — Learn how to use the Google Slides node in n8n. Follow technical documentation to integrate Google Slides node into your workflows.
- [Google Tasks](pages/integrations/builtin/app-nodes/n8n-nodes-base.googletasks.md) — Learn how to use the Google Tasks node in n8n. Follow technical documentation to integrate Google Tasks node into your workflows.
- [Google Translate](pages/integrations/builtin/app-nodes/n8n-nodes-base.googletranslate.md) — Learn how to use the Google Translate node in n8n. Follow technical documentation to integrate Google Translate node into your workflows.
- [Google Workspace Admin](pages/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin.md) — Learn how to use the Google Workspace Admin node in n8n. Follow technical documentation to integrate Google Workspace Admin node into your workflows.
- [Gotify](pages/integrations/builtin/app-nodes/n8n-nodes-base.gotify.md) — Learn how to use the Gotify node in n8n. Follow technical documentation to integrate Gotify node into your workflows.
- [GoToWebinar](pages/integrations/builtin/app-nodes/n8n-nodes-base.gotowebinar.md) — Learn how to use the GoToWebinar node in n8n. Follow technical documentation to integrate GoToWebinar node into your workflows.
- [Grafana](pages/integrations/builtin/app-nodes/n8n-nodes-base.grafana.md) — Learn how to use the Grafana node in n8n. Follow technical documentation to integrate Grafana node into your workflows.
- [Grist](pages/integrations/builtin/app-nodes/n8n-nodes-base.grist.md) — Learn how to use the Grist node in n8n. Follow technical documentation to integrate Grist node into your workflows.
- [Hacker News](pages/integrations/builtin/app-nodes/n8n-nodes-base.hackernews.md) — Learn how to use the Hacker News node in n8n. Follow technical documentation to integrate Hacker News node into your workflows.
- [HaloPSA](pages/integrations/builtin/app-nodes/n8n-nodes-base.halopsa.md) — Learn how to use the HaloPSA node in n8n. Follow technical documentation to integrate HaloPSA node into your workflows.
- [Harvest](pages/integrations/builtin/app-nodes/n8n-nodes-base.harvest.md) — Learn how to use the Harvest node in n8n. Follow technical documentation to integrate Harvest node into your workflows.
- [Help Scout](pages/integrations/builtin/app-nodes/n8n-nodes-base.helpscout.md) — Learn how to use the Help Scout node in n8n. Follow technical documentation to integrate Help Scout node into your workflows.
- [HighLevel](pages/integrations/builtin/app-nodes/n8n-nodes-base.highlevel.md) — Learn how to use the HighLevel node in n8n. Follow technical documentation to integrate HighLevel node into your workflows.
- [Home Assistant](pages/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant.md) — Learn how to use the Home Assistant node in n8n. Follow technical documentation to integrate Home Assistant node into your workflows.
- [HubSpot](pages/integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md) — Learn how to use the HubSpot node in n8n. Follow technical documentation to integrate HubSpot node into your workflows.
- [Humantic AI](pages/integrations/builtin/app-nodes/n8n-nodes-base.humanticai.md) — Learn how to use the Humantic AI node in n8n. Follow technical documentation to integrate Humantic AI node into your workflows.
- [Hunter](pages/integrations/builtin/app-nodes/n8n-nodes-base.hunter.md) — Learn how to use the Hunter node in n8n. Follow technical documentation to integrate Hunter node into your workflows.
- [Intercom](pages/integrations/builtin/app-nodes/n8n-nodes-base.intercom.md) — Learn how to use the Intercom node in n8n. Follow technical documentation to integrate Intercom node into your workflows.
- [Invoice Ninja](pages/integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja.md) — Learn how to use the Invoice Ninja node in n8n. Follow technical documentation to integrate Invoice Ninja node into your workflows.
- [Iterable](pages/integrations/builtin/app-nodes/n8n-nodes-base.iterable.md) — Learn how to use the Iterable node in n8n. Follow technical documentation to integrate Iterable node into your workflows.
- [Jenkins](pages/integrations/builtin/app-nodes/n8n-nodes-base.jenkins.md) — Learn how to use the Jenkins node in n8n. Follow technical documentation to integrate Jenkins node into your workflows.
- [Jina AI](pages/integrations/builtin/app-nodes/n8n-nodes-base.jinaai.md) — Learn how to use the Jina AI node in n8n. Follow technical documentation to integrate Jina AI node into your workflows.
- [Jira Software](pages/integrations/builtin/app-nodes/n8n-nodes-base.jira.md) — Learn how to use the Jira Software node in n8n. Follow technical documentation to integrate Jira Software node into your workflows.
- [Kafka](pages/integrations/builtin/app-nodes/n8n-nodes-base.kafka.md) — Learn how to use the Kafka node in n8n. Follow technical documentation to integrate Kafka node into your workflows.
- [Keap](pages/integrations/builtin/app-nodes/n8n-nodes-base.keap.md) — Learn how to use the Keap node in n8n. Follow technical documentation to integrate Keap node into your workflows.
- [Kitemaker](pages/integrations/builtin/app-nodes/n8n-nodes-base.kitemaker.md) — Learn how to use the Kitemaker node in n8n. Follow technical documentation to integrate Kitemaker node into your workflows.
- [KoboToolbox](pages/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox.md) — Learn how to use the KoboToolbox node in n8n. Follow technical documentation to integrate KoboToolbox node into your workflows.
- [Lemlist](pages/integrations/builtin/app-nodes/n8n-nodes-base.lemlist.md) — Learn how to use the Lemlist node in n8n. Follow technical documentation to integrate Lemlist node into your workflows.
- [Line](pages/integrations/builtin/app-nodes/n8n-nodes-base.line.md) — Learn how to use the Line node in n8n. Follow technical documentation to integrate Line node into your workflows.
- [Linear](pages/integrations/builtin/app-nodes/n8n-nodes-base.linear.md) — Learn how to use the Linear node in n8n. Follow technical documentation to integrate Linear node into your workflows.
- [LingvaNex](pages/integrations/builtin/app-nodes/n8n-nodes-base.lingvanex.md) — Learn how to use the LingvaNex node in n8n. Follow technical documentation to integrate LingvaNex node into your workflows.
- [LinkedIn](pages/integrations/builtin/app-nodes/n8n-nodes-base.linkedin.md) — Learn how to use the LinkedIn node in n8n. Follow technical documentation to integrate LinkedIn node into your workflows.
- [LoneScale](pages/integrations/builtin/app-nodes/n8n-nodes-base.lonescale.md) — Learn how to use the LoneScale node in n8n. Follow technical documentation to integrate LoneScale node into your workflows.
- [Magento 2](pages/integrations/builtin/app-nodes/n8n-nodes-base.magento2.md) — Learn how to use the Magento 2 node in n8n. Follow technical documentation to integrate Magento 2 node into your workflows.
- [Mailcheck](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailcheck.md) — Learn how to use the Mailcheck node in n8n. Follow technical documentation to integrate Mailcheck node into your workflows.
- [Mailchimp](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp.md) — Learn how to use the Mailchimp node in n8n. Follow technical documentation to integrate Mailchimp node into your workflows.
- [MailerLite](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailerlite.md) — Learn how to use the MailerLite node in n8n. Follow technical documentation to integrate MailerLite node into your workflows.
- [Mailgun](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailgun.md) — Learn how to use the Mailgun node in n8n. Follow technical documentation to integrate Mailgun node into your workflows.
- [Mailjet](pages/integrations/builtin/app-nodes/n8n-nodes-base.mailjet.md) — Learn how to use the Mailjet node in n8n. Follow technical documentation to integrate Mailjet node into your workflows.
- [Mandrill](pages/integrations/builtin/app-nodes/n8n-nodes-base.mandrill.md) — Learn how to use the Mandrill node in n8n. Follow technical documentation to integrate Mandrill node into your workflows.
- [marketstack](pages/integrations/builtin/app-nodes/n8n-nodes-base.marketstack.md) — Learn how to use the marketstack node in n8n. Follow technical documentation to integrate marketstack node into your workflows.
- [Matrix](pages/integrations/builtin/app-nodes/n8n-nodes-base.matrix.md) — Learn how to use the Matrix node in n8n. Follow technical documentation to integrate Matrix node into your workflows.
- [Mattermost](pages/integrations/builtin/app-nodes/n8n-nodes-base.mattermost.md) — Learn how to use the Mattermost node in n8n. Follow technical documentation to integrate Mattermost node into your workflows.
- [Mautic](pages/integrations/builtin/app-nodes/n8n-nodes-base.mautic.md) — Learn how to use the Mautic node in n8n. Follow technical documentation to integrate Mautic node into your workflows.
- [Medium](pages/integrations/builtin/app-nodes/n8n-nodes-base.medium.md) — Learn how to use the Medium node in n8n. Follow technical documentation to integrate Medium node into your workflows.
- [MessageBird](pages/integrations/builtin/app-nodes/n8n-nodes-base.messagebird.md) — Learn how to use the MessageBird node in n8n. Follow technical documentation to integrate MessageBird node into your workflows.
- [Metabase](pages/integrations/builtin/app-nodes/n8n-nodes-base.metabase.md) — Learn how to use the Metabase node in n8n. Follow technical documentation to integrate Metabase node into your workflows.
- [Microsoft Dynamics CRM](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftdynamicscrm.md) — Learn how to use the Microsoft Dynamics CRM node in n8n. Follow technical documentation to integrate Microsoft Dynamics CRM node into your workflows.
- [Microsoft Entra ID](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md) — Learn how to use the Microsoft Entra ID node in n8n. Follow technical documentation to integrate Microsoft Entra ID node into your workflows.
- [Microsoft Excel (OneDrive)](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel.md) — Learn how to use the Microsoft Excel (OneDrive) node in n8n. Follow technical documentation to integrate Microsoft Excel (OneDrive) node into your workflows.
- [Microsoft Excel (SharePoint)](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcelsharepoint.md) — Learn how to use the Microsoft Excel (SharePoint) node in n8n. Follow technical documentation to integrate Microsoft Excel (SharePoint) node into your workflows.
- [Microsoft Graph Security](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity.md) — Learn how to use the Microsoft Graph Security node in n8n. Follow technical documentation to integrate Microsoft Graph Security node into your workflows.
- [Microsoft OneDrive](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive.md) — Learn how to use the Microsoft OneDrive node in n8n. Follow technical documentation to integrate Microsoft OneDrive node into your workflows.
- [Microsoft Outlook](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook.md) — Learn how to use the Microsoft Outlook node in n8n. Follow technical documentation to integrate Microsoft Outlook node into your workflows.
- [Microsoft SharePoint](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint.md) — Learn how to use the Microsoft SharePoint node in n8n. Follow technical documentation to integrate Microsoft SharePoint node into your workflows.
- [Microsoft SQL](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsql.md) — Learn how to use the Microsoft SQL node in n8n. Follow technical documentation to integrate Microsoft SQL node into your workflows.
- [Microsoft Teams](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams.md) — Learn how to use the Microsoft Teams node in n8n. Follow technical documentation to integrate Microsoft Teams node into your workflows.
- [Microsoft To Do](pages/integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo.md) — Learn how to use the Microsoft To Do node in n8n. Follow technical documentation to integrate Microsoft To Do node into your workflows.
- [Mindee](pages/integrations/builtin/app-nodes/n8n-nodes-base.mindee.md) — Learn how to use the Mindee node in n8n. Follow technical documentation to integrate Mindee node into your workflows.
- [MISP](pages/integrations/builtin/app-nodes/n8n-nodes-base.misp.md) — Learn how to use the MISP node in n8n. Follow technical documentation to integrate MISP node into your workflows.
- [Mistral AI](pages/integrations/builtin/app-nodes/n8n-nodes-base.mistralai.md) — Learn how to use the Mistral AI node in n8n. Follow technical documentation to integrate Mistral AI node into your workflows.
- [MiniMax](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.minimax.md) — The MiniMax node lets you interact with MiniMax AI models from n8n. This documentation explains how to integrate MiniMax into your n8n workflows to generate images, produce speech from text, generate
- [Mocean](pages/integrations/builtin/app-nodes/n8n-nodes-base.mocean.md) — Learn how to use the Mocean node in n8n. Follow technical documentation to integrate Mocean node into your workflows.
- [monday.com](pages/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom.md) — Learn how to use the monday.com node in n8n. Follow technical documentation to integrate monday.com node into your workflows.
- [MongoDB](pages/integrations/builtin/app-nodes/n8n-nodes-base.mongodb.md) — Learn how to use the MongoDB node in n8n. Follow technical documentation to integrate MongoDB node into your workflows.
- [Monica CRM](pages/integrations/builtin/app-nodes/n8n-nodes-base.monicacrm.md) — Learn how to use the Monica CRM node in n8n. Follow technical documentation to integrate Monica CRM node into your workflows.
- [Moonshot Kimi](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot.md) — The Moonshot Kimi node lets you interact with Moonshot Kimi AI models from n8n. This documentation explains how to send messages to models, attach images, and analyze images using the node's operation
- [MQTT](pages/integrations/builtin/app-nodes/n8n-nodes-base.mqtt.md) — Learn how to use the MQTT node in n8n. Follow technical documentation to integrate MQTT node into your workflows.
- [MSG91](pages/integrations/builtin/app-nodes/n8n-nodes-base.msg91.md) — Learn how to use the MSG91 node in n8n. Follow technical documentation to integrate MSG91 node into your workflows.
- [MySQL](pages/integrations/builtin/app-nodes/n8n-nodes-base.mysql.md) — Learn how to use the MySQL node in n8n. Follow technical documentation to integrate MySQL node into your workflows.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues.md) — Documentation for common issues and questions in the MySQL node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Customer Datastore (n8n Training)](pages/integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomerdatastore.md) — Learn how to use the Customer Datastore (n8n Training) node in n8n. Follow technical documentation to integrate Customer Datastore (n8n Training) node into your workflows.
- [Customer Messenger (n8n Training)](pages/integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomermessenger.md) — Learn how to use the Customer Messenger (n8n Training) node in n8n. Follow technical documentation to integrate Customer Messenger (n8n Training) node into your workflows.
- [NASA](pages/integrations/builtin/app-nodes/n8n-nodes-base.nasa.md) — Learn how to use the NASA node in n8n. Follow technical documentation to integrate NASA node into your workflows.
- [Netlify](pages/integrations/builtin/app-nodes/n8n-nodes-base.netlify.md) — Learn how to use the Netlify node in n8n. Follow technical documentation to integrate Netlify node into your workflows.
- [Netscaler ADC](pages/integrations/builtin/app-nodes/n8n-nodes-base.netscaleradc.md) — Learn how to use the Netscaler ADC node in n8n. Follow technical documentation to integrate Netscaler ADC node into your workflows.
- [Nextcloud](pages/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud.md) — Learn how to use the Nextcloud node in n8n. Follow technical documentation to integrate Nextcloud node into your workflows.
- [NocoDB](pages/integrations/builtin/app-nodes/n8n-nodes-base.nocodb.md) — Learn how to use the NocoDB node in n8n. Follow technical documentation to integrate NocoDB node into your workflows.
- [Notion](pages/integrations/builtin/app-nodes/n8n-nodes-base.notion.md) — Learn how to use the Notion node in n8n. Follow technical documentation to integrate Notion node into your workflows.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues.md) — Documentation for common issues and questions in the Notion node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [npm](pages/integrations/builtin/app-nodes/n8n-nodes-base.npm.md) — Learn how to use the npm node in n8n. Follow technical documentation to integrate npm node into your workflows.
- [Odoo](pages/integrations/builtin/app-nodes/n8n-nodes-base.odoo.md) — Learn how to use the Odoo node in n8n. Follow technical documentation to integrate Odoo node into your workflows.
- [Okta](pages/integrations/builtin/app-nodes/n8n-nodes-base.okta.md) — Learn how to use the Okta node in n8n. Follow technical documentation to integrate Okta node into your workflows.
- [One Simple API](pages/integrations/builtin/app-nodes/n8n-nodes-base.onesimpleapi.md) — Learn how to use the One Simple API node in n8n. Follow technical documentation to integrate One Simple API node into your workflows.
- [Onfleet](pages/integrations/builtin/app-nodes/n8n-nodes-base.onfleet.md) — Learn how to use the Onfleet node in n8n. Follow technical documentation to integrate Onfleet node into your workflows.
- [OpenAI](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai.md) — Learn how to use the OpenAI node in n8n. Follow technical documentation to integrate OpenAI node into your workflows.
- [Assistant operations](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md) — Documentation for the Assistant operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
- [Audio operations](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md) — Documentation for the Audio operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
- [Conversation operations](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations.md) — Documentation for the Conversation operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information
- [File operations](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md) — Documentation for the File operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
- [Image operations](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md) — Documentation for the Image operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
- [Text operations](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md) — Documentation for the Text operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
- [Video operations](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations.md) — Documentation for the Video operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md) — Documentation for common issues and questions in the OpenAI node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [OpenThesaurus](pages/integrations/builtin/app-nodes/n8n-nodes-base.openthesaurus.md) — Learn how to use the OpenThesaurus node in n8n. Follow technical documentation to integrate OpenThesaurus node into your workflows.
- [OpenWeatherMap](pages/integrations/builtin/app-nodes/n8n-nodes-base.openweathermap.md) — Learn how to use the OpenWeatherMap node in n8n. Follow technical documentation to integrate OpenWeatherMap node into your workflows.
- [Oracle Database](pages/integrations/builtin/app-nodes/n8n-nodes-base.oracledb.md) — Learn how to use the Oracle Database node in n8n. Follow technical documentation to integrate Oracle Database node into your workflows.
- [Oura](pages/integrations/builtin/app-nodes/n8n-nodes-base.oura.md) — Learn how to use the Oura node in n8n. Follow technical documentation to integrate Oura node into your workflows.
- [Paddle](pages/integrations/builtin/app-nodes/n8n-nodes-base.paddle.md) — Learn how to use the Paddle node in n8n. Follow technical documentation to integrate Paddle node into your workflows.
- [PagerDuty](pages/integrations/builtin/app-nodes/n8n-nodes-base.pagerduty.md) — Learn how to use the PagerDuty node in n8n. Follow technical documentation to integrate PagerDuty node into your workflows.
- [PayPal](pages/integrations/builtin/app-nodes/n8n-nodes-base.paypal.md) — Learn how to use the PayPal node in n8n. Follow technical documentation to integrate PayPal node into your workflows.
- [Peekalink](pages/integrations/builtin/app-nodes/n8n-nodes-base.peekalink.md) — Learn how to use the Peekalink node in n8n. Follow technical documentation to integrate Peekalink node into your workflows.
- [Perplexity](pages/integrations/builtin/app-nodes/n8n-nodes-langchain.perplexity.md) — Learn how to use the Perplexity node in n8n. Follow technical documentation to integrate Perplexity node into your workflows.
- [PhantomBuster](pages/integrations/builtin/app-nodes/n8n-nodes-base.phantombuster.md) — Learn how to use the PhantomBuster node in n8n. Follow technical documentation to integrate PhantomBuster node into your workflows.
- [Philips Hue](pages/integrations/builtin/app-nodes/n8n-nodes-base.philipshue.md) — Learn how to use the Philips Hue node in n8n. Follow technical documentation to integrate Philips Hue node into your workflows.
- [Pipedrive](pages/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive.md) — Learn how to use the Pipedrive node in n8n. Follow technical documentation to integrate Pipedrive node into your workflows.
- [Plivo](pages/integrations/builtin/app-nodes/n8n-nodes-base.plivo.md) — Learn how to use the Plivo node in n8n. Follow technical documentation to integrate Plivo node into your workflows.
- [PostBin](pages/integrations/builtin/app-nodes/n8n-nodes-base.postbin.md) — Learn how to use the PostBin node in n8n. Follow technical documentation to integrate PostBin node into your workflows.
- [Postgres](pages/integrations/builtin/app-nodes/n8n-nodes-base.postgres.md) — Learn how to use the Postgres node in n8n. Follow technical documentation to integrate Postgres node into your workflows.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues.md) — Documentation for common issues and questions in the Postgres node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [PostHog](pages/integrations/builtin/app-nodes/n8n-nodes-base.posthog.md) — Learn how to use the PostHog node in n8n. Follow technical documentation to integrate PostHog node into your workflows.
- [ProfitWell](pages/integrations/builtin/app-nodes/n8n-nodes-base.profitwell.md) — Learn how to use the ProfitWell node in n8n. Follow technical documentation to integrate ProfitWell node into your workflows.
- [Pushbullet](pages/integrations/builtin/app-nodes/n8n-nodes-base.pushbullet.md) — Learn how to use the Pushbullet node in n8n. Follow technical documentation to integrate Pushbullet node into your workflows.
- [Pushcut](pages/integrations/builtin/app-nodes/n8n-nodes-base.pushcut.md) — Learn how to use the Pushcut node in n8n. Follow technical documentation to integrate Pushcut node into your workflows.
- [Pushover](pages/integrations/builtin/app-nodes/n8n-nodes-base.pushover.md) — Learn how to use the Pushover node in n8n. Follow technical documentation to integrate Pushover node into your workflows.
- [QuestDB](pages/integrations/builtin/app-nodes/n8n-nodes-base.questdb.md) — Learn how to use the QuestDB node in n8n. Follow technical documentation to integrate QuestDB node into your workflows.
- [Quick Base](pages/integrations/builtin/app-nodes/n8n-nodes-base.quickbase.md) — Learn how to use the Quick Base node in n8n. Follow technical documentation to integrate Quick Base node into your workflows.
- [QuickBooks Online](pages/integrations/builtin/app-nodes/n8n-nodes-base.quickbooks.md) — Learn how to use the QuickBooks Online node in n8n. Follow technical documentation to integrate QuickBooks Online node into your workflows.
- [QuickChart](pages/integrations/builtin/app-nodes/n8n-nodes-base.quickchart.md) — Learn how to use the QuickChart node in n8n. Follow technical documentation to integrate QuickChart node into your workflows.
- [RabbitMQ](pages/integrations/builtin/app-nodes/n8n-nodes-base.rabbitmq.md) — Learn how to use the RabbitMQ node in n8n. Follow technical documentation to integrate RabbitMQ node into your workflows.
- [Raindrop](pages/integrations/builtin/app-nodes/n8n-nodes-base.raindrop.md) — Learn how to use the Raindrop node in n8n. Follow technical documentation to integrate Raindrop node into your workflows.
- [Reddit](pages/integrations/builtin/app-nodes/n8n-nodes-base.reddit.md) — Learn how to use the Reddit node in n8n. Follow technical documentation to integrate Reddit node into your workflows.
- [Redis](pages/integrations/builtin/app-nodes/n8n-nodes-base.redis.md) — Learn how to use the Redis node in n8n. Follow technical documentation to integrate Redis node into your workflows.
- [Rocket.Chat](pages/integrations/builtin/app-nodes/n8n-nodes-base.rocketchat.md) — Learn how to use the Rocket.Chat node in n8n. Follow technical documentation to integrate Rocket.Chat node into your workflows.
- [Rundeck](pages/integrations/builtin/app-nodes/n8n-nodes-base.rundeck.md) — Learn how to use the Rundeck node in n8n. Follow technical documentation to integrate Rundeck node into your workflows.
- [S3](pages/integrations/builtin/app-nodes/n8n-nodes-base.s3.md) — Learn how to use the S3 node in n8n. Follow technical documentation to integrate S3 node into your workflows.
- [Salesforce](pages/integrations/builtin/app-nodes/n8n-nodes-base.salesforce.md) — Learn how to use the Salesforce node in n8n. Follow technical documentation to integrate Salesforce node into your workflows.
- [Salesmate](pages/integrations/builtin/app-nodes/n8n-nodes-base.salesmate.md) — Learn how to use the Salesmate node in n8n. Follow technical documentation to integrate Salesmate node into your workflows.
- [SeaTable](pages/integrations/builtin/app-nodes/n8n-nodes-base.seatable.md) — Learn how to use the SeaTable node in n8n. Follow technical documentation to integrate SeaTable node into your workflows.
- [SecurityScorecard](pages/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard.md) — Learn how to use the SecurityScorecard node in n8n. Follow technical documentation to integrate SecurityScorecard node into your workflows.
- [Segment](pages/integrations/builtin/app-nodes/n8n-nodes-base.segment.md) — Learn how to use the Segment node in n8n. Follow technical documentation to integrate Segment node into your workflows.
- [SendGrid](pages/integrations/builtin/app-nodes/n8n-nodes-base.sendgrid.md) — Learn how to use the SendGrid node in n8n. Follow technical documentation to integrate SendGrid node into your workflows.
- [Sendy](pages/integrations/builtin/app-nodes/n8n-nodes-base.sendy.md) — Learn how to use the Sendy node in n8n. Follow technical documentation to integrate Sendy node into your workflows.
- [Sentry.io](pages/integrations/builtin/app-nodes/n8n-nodes-base.sentryio.md) — Learn how to use the Sentry.io node in n8n. Follow technical documentation to integrate Sentry.io node into your workflows.
- [ServiceNow](pages/integrations/builtin/app-nodes/n8n-nodes-base.servicenow.md) — Learn how to use the ServiceNow node in n8n. Follow technical documentation to integrate ServiceNow node into your workflows.
- [seven](pages/integrations/builtin/app-nodes/n8n-nodes-base.sms77.md) — Learn how to use the seven node in n8n. Follow technical documentation to integrate seven node into your workflows.
- [Shopify](pages/integrations/builtin/app-nodes/n8n-nodes-base.shopify.md) — Learn how to use the Shopify node in n8n. Follow technical documentation to integrate Shopify node into your workflows.
- [SIGNL4](pages/integrations/builtin/app-nodes/n8n-nodes-base.signl4.md) — Learn how to use the SIGNL4 node in n8n. Follow technical documentation to integrate SIGNL4 node into your workflows.
- [Slack](pages/integrations/builtin/app-nodes/n8n-nodes-base.slack.md) — Learn how to use the Slack node in n8n. Follow technical documentation to integrate Slack node into your workflows.
- [Approvals](pages/integrations/builtin/app-nodes/n8n-nodes-base.slack/approvals.md) — Learn how approvers can approve or decline n8n workflow actions directly inside Slack with the Slack node's Send and Wait for Response operation.
- [Snowflake](pages/integrations/builtin/app-nodes/n8n-nodes-base.snowflake.md) — Learn how to use the Snowflake node in n8n. Follow technical documentation to integrate Snowflake node into your workflows.
- [Splunk](pages/integrations/builtin/app-nodes/n8n-nodes-base.splunk.md) — Learn how to use the Splunk node in n8n. Follow technical documentation to integrate Splunk node into your workflows.
- [Spotify](pages/integrations/builtin/app-nodes/n8n-nodes-base.spotify.md) — Learn how to use the Spotify node in n8n. Follow technical documentation to integrate Spotify node into your workflows.
- [Stackby](pages/integrations/builtin/app-nodes/n8n-nodes-base.stackby.md) — Learn how to use the Stackby node in n8n. Follow technical documentation to integrate Stackby node into your workflows.
- [Storyblok](pages/integrations/builtin/app-nodes/n8n-nodes-base.storyblok.md) — Learn how to use the Storyblok node in n8n. Follow technical documentation to integrate Storyblok node into your workflows.
- [Strapi](pages/integrations/builtin/app-nodes/n8n-nodes-base.strapi.md) — Learn how to use the Strapi node in n8n. Follow technical documentation to integrate Strapi node into your workflows.
- [Strava](pages/integrations/builtin/app-nodes/n8n-nodes-base.strava.md) — Learn how to use the Strava node in n8n. Follow technical documentation to integrate Strava node into your workflows.
- [Stripe](pages/integrations/builtin/app-nodes/n8n-nodes-base.stripe.md) — Learn how to use the Stripe node in n8n. Follow technical documentation to integrate Stripe node into your workflows.
- [Supabase](pages/integrations/builtin/app-nodes/n8n-nodes-base.supabase.md) — Learn how to use the Supabase node in n8n. Follow technical documentation to integrate Supabase node into your workflows.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues.md) — Documentation for common issues and questions in the Supabase node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [SyncroMSP](pages/integrations/builtin/app-nodes/n8n-nodes-base.syncromsp.md) — Learn how to use the SyncroMSP node in n8n. Follow technical documentation to integrate SyncroMSP node into your workflows.
- [Taiga](pages/integrations/builtin/app-nodes/n8n-nodes-base.taiga.md) — Learn how to use the Taiga node in n8n. Follow technical documentation to integrate Taiga node into your workflows.
- [Tapfiliate](pages/integrations/builtin/app-nodes/n8n-nodes-base.tapfiliate.md) — Learn how to use the Tapfiliate node in n8n. Follow technical documentation to integrate Tapfiliate node into your workflows.
- [Telegram](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram.md) — Documentation for the Telegram node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
- [Chat operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md) — Documentation for the Chat operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all Chat operations.
- [Callback operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations.md) — Documentation for the Callback operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all Callback operations.
- [File operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md) — Documentation for the File operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all File operations.
- [Message operations](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md) — Documentation for the Message operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all Message operations.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md) — Documentation for common issues and questions in the Telegram node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [TheHive](pages/integrations/builtin/app-nodes/n8n-nodes-base.thehive.md) — Learn how to use the TheHive node in n8n. Follow technical documentation to integrate TheHive node into your workflows.
- [TheHive 5](pages/integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md) — Learn how to use the TheHive 5 node in n8n. Follow technical documentation to integrate TheHive 5 node into your workflows.
- [TimescaleDB](pages/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb.md) — Learn how to use the TimescaleDB node in n8n. Follow technical documentation to integrate TimescaleDB node into your workflows.
- [Todoist](pages/integrations/builtin/app-nodes/n8n-nodes-base.todoist.md) — Learn how to use the Todoist node in n8n. Follow technical documentation to integrate Todoist node into your workflows.
- [Travis CI](pages/integrations/builtin/app-nodes/n8n-nodes-base.travisci.md) — Learn how to use the Travis CI node in n8n. Follow technical documentation to integrate Travis CI node into your workflows.
- [Trello](pages/integrations/builtin/app-nodes/n8n-nodes-base.trello.md) — Learn how to use the Trello node in n8n. Follow technical documentation to integrate Trello node into your workflows.
- [Twake](pages/integrations/builtin/app-nodes/n8n-nodes-base.twake.md) — Learn how to use the Twake node in n8n. Follow technical documentation to integrate Twake node into your workflows.
- [Twilio](pages/integrations/builtin/app-nodes/n8n-nodes-base.twilio.md) — Learn how to use the Twilio node in n8n. Follow technical documentation to integrate Twilio node into your workflows.
- [Twist](pages/integrations/builtin/app-nodes/n8n-nodes-base.twist.md) — Learn how to use the Twist node in n8n. Follow technical documentation to integrate Twist node into your workflows.
- [Unleashed Software](pages/integrations/builtin/app-nodes/n8n-nodes-base.unleashedsoftware.md) — Learn how to use the Unleashed Software node in n8n. Follow technical documentation to integrate Unleashed Software node into your workflows.
- [UpLead](pages/integrations/builtin/app-nodes/n8n-nodes-base.uplead.md) — Learn how to use the UpLead node in n8n. Follow technical documentation to integrate UpLead node into your workflows.
- [uProc](pages/integrations/builtin/app-nodes/n8n-nodes-base.uproc.md) — Learn how to use the uProc node in n8n. Follow technical documentation to integrate uProc node into your workflows.
- [UptimeRobot](pages/integrations/builtin/app-nodes/n8n-nodes-base.uptimerobot.md) — Learn how to use the UptimeRobot node in n8n. Follow technical documentation to integrate UptimeRobot node into your workflows.
- [urlscan.io](pages/integrations/builtin/app-nodes/n8n-nodes-base.urlscanio.md) — Learn how to use the urlscan.io node in n8n. Follow technical documentation to integrate urlscan.io node into your workflows.
- [Venafi TLS Protect Cloud](pages/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud.md) — Learn how to use the Venafi TLS Protect Cloud node in n8n. Follow technical documentation to integrate Venafi TLS Protect Cloud node into your workflows.
- [Venafi TLS Protect Datacenter](pages/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectdatacenter.md) — Learn how to use the Venafi TLS Protect Datacenter node in n8n. Follow technical documentation to integrate Venafi TLS Protect Datacenter node into your workflows.
- [Vero](pages/integrations/builtin/app-nodes/n8n-nodes-base.vero.md) — Learn how to use the Vero node in n8n. Follow technical documentation to integrate Vero node into your workflows.
- [Vonage](pages/integrations/builtin/app-nodes/n8n-nodes-base.vonage.md) — Learn how to use the Vonage node in n8n. Follow technical documentation to integrate Vonage node into your workflows.
- [Webflow](pages/integrations/builtin/app-nodes/n8n-nodes-base.webflow.md) — Learn how to use the Webflow node in n8n. Follow technical documentation to integrate Webflow node into your workflows.
- [Wekan](pages/integrations/builtin/app-nodes/n8n-nodes-base.wekan.md) — Learn how to use the Wekan node in n8n. Follow technical documentation to integrate Wekan node into your workflows.
- [WhatsApp Business Cloud](pages/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp.md) — Learn how to use the WhatsApp Business Cloud node in n8n. Follow technical documentation to integrate WhatsApp Business Cloud node into your workflows.
- [Common issues](pages/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues.md) — Documentation for common issues and questions in the WhatsApp Business Cloud node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Wise](pages/integrations/builtin/app-nodes/n8n-nodes-base.wise.md) — Learn how to use the Wise node in n8n. Follow technical documentation to integrate Wise node into your workflows.
- [WooCommerce](pages/integrations/builtin/app-nodes/n8n-nodes-base.woocommerce.md) — Learn how to use the WooCommerce node in n8n. Follow technical documentation to integrate WooCommerce node into your workflows.
- [WordPress](pages/integrations/builtin/app-nodes/n8n-nodes-base.wordpress.md) — Learn how to use the WordPress node in n8n. Follow technical documentation to integrate WordPress node into your workflows.
- [X (Formerly Twitter)](pages/integrations/builtin/app-nodes/n8n-nodes-base.twitter.md) — Learn how to use the X (Formerly Twitter) node in n8n. Follow technical documentation to integrate X (Formerly Twitter) node into your workflows.
- [Xero](pages/integrations/builtin/app-nodes/n8n-nodes-base.xero.md) — Learn how to use the Xero node in n8n. Follow technical documentation to integrate Xero node into your workflows.
- [Yourls](pages/integrations/builtin/app-nodes/n8n-nodes-base.yourls.md) — Learn how to use the Yourls node in n8n. Follow technical documentation to integrate Yourls node into your workflows.
- [YouTube](pages/integrations/builtin/app-nodes/n8n-nodes-base.youtube.md) — Learn how to use the YouTube node in n8n. Follow technical documentation to integrate YouTube node into your workflows.
- [Zammad](pages/integrations/builtin/app-nodes/n8n-nodes-base.zammad.md) — Learn how to use the Zammad node in n8n. Follow technical documentation to integrate Zammad node into your workflows.
- [Zendesk](pages/integrations/builtin/app-nodes/n8n-nodes-base.zendesk.md) — Learn how to use the Zendesk node in n8n. Follow technical documentation to integrate Zendesk node into your workflows.
- [Zoho CRM](pages/integrations/builtin/app-nodes/n8n-nodes-base.zohocrm.md) — Learn how to use the Zoho CRM node in n8n. Follow technical documentation to integrate Zoho CRM node into your workflows.
- [Zoom](pages/integrations/builtin/app-nodes/n8n-nodes-base.zoom.md) — Learn how to use the Zoom node in n8n. Follow technical documentation to integrate Zoom node into your workflows.
- [Zulip](pages/integrations/builtin/app-nodes/n8n-nodes-base.zulip.md) — Learn how to use the Zulip node in n8n. Follow technical documentation to integrate Zulip node into your workflows.

### `builtin/trigger-nodes.md` (1)

- [Trigger nodes](pages/integrations/builtin/trigger-nodes.md)

### `builtin/trigger-nodes` (105)

- [ActiveCampaign Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.activecampaigntrigger.md) — Learn how to use the ActiveCampaign Trigger node in n8n. Follow technical documentation to integrate ActiveCampaign Trigger node into your workflows.
- [Acuity Scheduling Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.acuityschedulingtrigger.md) — Learn how to use the Acuity Scheduling Trigger node in n8n. Follow technical documentation to integrate Acuity Scheduling Trigger node into your workflows.
- [Affinity Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.affinitytrigger.md) — Learn how to use the Affinity Trigger node in n8n. Follow technical documentation to integrate Affinity Trigger node into your workflows.
- [Airtable Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger.md) — Learn how to use the Airtable Trigger node in n8n. Follow technical documentation to integrate Airtable Trigger node into your workflows.
- [AMQP Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.amqptrigger.md) — Learn how to use the AMQP Trigger node in n8n. Follow technical documentation to integrate AMQP Trigger node into your workflows.
- [Asana Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.asanatrigger.md) — Learn how to use the Asana Trigger node in n8n. Follow technical documentation to integrate Asana Trigger node into your workflows.
- [Autopilot Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.autopilottrigger.md) — Learn how to use the Autopilot Trigger node in n8n. Follow technical documentation to integrate Autopilot Trigger node into your workflows.
- [AWS SNS Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.awssnstrigger.md) — Learn how to use the AWS SNS Trigger node in n8n. Follow technical documentation to integrate AWS SNS Trigger node into your workflows.
- [Bitbucket Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.bitbuckettrigger.md) — Learn how to use the Bitbucket Trigger node in n8n. Follow technical documentation to integrate Bitbucket Trigger node into your workflows.
- [Box Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger.md) — Learn how to use the Box Trigger node in n8n. Follow technical documentation to integrate Box Trigger node into your workflows.
- [Brevo Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.brevotrigger.md) — Learn how to use the Brevo Trigger node in n8n. Follow technical documentation to integrate Brevo Trigger node into your workflows.
- [Calendly Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger.md) — Learn how to use the Calendly Trigger node in n8n. Follow technical documentation to integrate Calendly Trigger node into your workflows.
- [Cal Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger.md) — Learn how to use the Cal Trigger node in n8n. Follow technical documentation to integrate Cal Trigger node into your workflows.
- [Chargebee Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger.md) — Learn how to use the Chargebee Trigger node in n8n. Follow technical documentation to integrate Chargebee Trigger node into your workflows.
- [ClickUp Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger.md) — Learn how to use the ClickUp Trigger node in n8n. Follow technical documentation to integrate ClickUp Trigger node into your workflows.
- [Clockify Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger.md) — Learn how to use the Clockify Trigger node in n8n. Follow technical documentation to integrate Clockify Trigger node into your workflows.
- [ConvertKit Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.convertkittrigger.md) — Learn how to use the ConvertKit Trigger node in n8n. Follow technical documentation to integrate ConvertKit Trigger node into your workflows.
- [Copper Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.coppertrigger.md) — Learn how to use the Copper Trigger node in n8n. Follow technical documentation to integrate Copper Trigger node into your workflows.
- [Customer.io Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger.md) — Learn how to use the Customer.io Trigger node in n8n. Follow technical documentation to integrate Customer.io Trigger node into your workflows.
- [Emelia Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.emeliatrigger.md) — Learn how to use the Emelia Trigger node in n8n. Follow technical documentation to integrate Emelia Trigger node into your workflows.
- [Eventbrite Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.eventbritetrigger.md) — Learn how to use the Eventbrite Trigger node in n8n. Follow technical documentation to integrate Eventbrite Trigger node into your workflows.
- [Facebook Lead Ads Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md) — Learn how to use the Facebook Lead Ads Trigger node in n8n. Follow technical documentation to integrate Facebook Lead Ads Trigger node into your workflows.
- [Facebook Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger.md) — Learn how to use the Facebook Trigger node in n8n. Follow technical documentation to integrate Facebook Trigger node into your workflows.
- [Ad Account](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account.md) — Learn how to use the Ad Account object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Ad Account object into your workflows.
- [Application](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/application.md) — Learn how to use the Application object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Application object into your workflows.
- [Certificate Transparency](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency.md) — Learn how to use the Certificate Transparency object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Certificate Transparency object into y
- [Group](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/group.md) — Learn how to use the Group object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Group object into your workflows.
- [Instagram](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram.md) — Learn how to use the Instagram object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Instagram object into your workflows.
- [Link](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link.md) — Learn how to use the Link object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Link object into your workflows.
- [Page](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page.md) — Learn how to use the Page object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Page object into your workflows.
- [Permissions](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/permissions.md) — Learn how to use the Permissions object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Permissions object into your workflows.
- [User](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/user.md) — Learn how to use the User object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's User object into your workflows.
- [WhatsApp Business Account](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp.md) — Learn how to use the WhatsApp Business Account object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's WhatsApp Business Account object into
- [Workplace Security](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/workplace-security.md) — Learn how to use the Workplace Security object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Workplace Security object into your workflow
- [Figma Trigger (Beta)](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger.md) — Learn how to use the Figma Trigger node in n8n. Follow technical documentation to integrate Figma Trigger node into your workflows.
- [Flow Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.flowtrigger.md) — Learn how to use the Flow Trigger node in n8n. Follow technical documentation to integrate Flow Trigger node into your workflows.
- [Form.io Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.formiotrigger.md) — Learn how to use the Form.io Trigger node in n8n. Follow technical documentation to integrate Form.io Trigger node into your workflows.
- [Formstack Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.formstacktrigger.md) — Learn how to use the Formstack Trigger node in n8n. Follow technical documentation to integrate Formstack Trigger node into your workflows.
- [GetResponse Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.getresponsetrigger.md) — Learn how to use the GetResponse Trigger node in n8n. Follow technical documentation to integrate GetResponse Trigger node into your workflows.
- [GitHub Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger.md) — Learn how to use the GitHub Trigger node in n8n. Follow technical documentation to integrate GitHub Trigger node into your workflows.
- [GitLab Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger.md) — Learn how to use the GitLab Trigger node in n8n. Follow technical documentation to integrate GitLab Trigger node into your workflows.
- [Gmail Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger.md) — Learn how to use the Gmail Trigger node in n8n. Follow technical documentation to integrate Gmail Trigger node into your workflows.
- [Poll mode options](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/poll-mode-options.md) — Learn about the poll mode options available to the Gmail Trigger node in n8n and how to configure them.
- [Common issues](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/common-issues.md) — Documentation for common issues and questions in the Gmail Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Google Calendar Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googlecalendartrigger.md) — Learn how to use the Google Calendar Trigger node in n8n. Follow technical documentation to integrate Google Calendar Trigger node into your workflows.
- [Google Drive Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger.md) — Learn how to use the Google Drive Trigger node in n8n. Follow technical documentation to integrate Google Drive Trigger node into your workflows.
- [Common issues](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues.md) — Documentation for common issues and questions in the Google Drive Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Google Business Profile Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googlebusinessprofiletrigger.md) — Learn how to use the Google Business Profile Trigger node in n8n. Follow technical documentation to integrate Google Business Profile Trigger node into your workflows.
- [Google Sheets Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger.md) — Learn how to use the Google Sheets Trigger node in n8n. Follow technical documentation to integrate Google Sheets Trigger node into your workflows.
- [Common issues](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/common-issues.md) — Documentation for common issues and questions in the Google Sheets Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Gumroad Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.gumroadtrigger.md) — Learn how to use the Gumroad Trigger node in n8n. Follow technical documentation to integrate Gumroad Trigger node into your workflows.
- [Help Scout Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.helpscouttrigger.md) — Learn how to use the Help Scout Trigger node in n8n. Follow technical documentation to integrate Help Scout Trigger node into your workflows.
- [HubSpot Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md) — Learn how to use the HubSpot Trigger node in n8n. Follow technical documentation to integrate HubSpot Trigger node into your workflows.
- [Invoice Ninja Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.invoiceninjatrigger.md) — Learn how to use the Invoice Ninja Trigger node in n8n. Follow technical documentation to integrate Invoice Ninja Trigger node into your workflows.
- [Jira Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.jiratrigger.md) — Learn how to use the Jira Trigger node in n8n. Follow technical documentation to integrate Jira Trigger node into your workflows.
- [Jotform Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.jotformtrigger.md) — Learn how to use the Jotform Trigger node in n8n. Follow technical documentation to integrate Jotform Trigger node into your workflows.
- [Kafka Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger.md) — Learn how to use the Kafka Trigger node in n8n. Follow technical documentation to integrate Kafka Trigger node into your workflows.
- [Keap Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.keaptrigger.md) — Learn how to use the Keap Trigger node in n8n. Follow technical documentation to integrate Keap Trigger node into your workflows.
- [KoboToolbox Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger.md) — Learn how to use the KoboToolbox Trigger node in n8n. Follow technical documentation to integrate KoboToolbox Trigger node into your workflows.
- [Lemlist Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.lemlisttrigger.md) — Learn how to use the Lemlist Trigger node in n8n. Follow technical documentation to integrate Lemlist Trigger node into your workflows.
- [Linear Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger.md) — Learn how to use the Linear Trigger node in n8n. Follow technical documentation to integrate Linear Trigger node into your workflows.
- [LoneScale Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.lonescaletrigger.md) — Learn how to use the LoneScale Trigger node in n8n. Follow technical documentation to integrate LoneScale Trigger node into your workflows.
- [Mailchimp Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mailchimptrigger.md) — Learn how to use the Mailchimp Trigger node in n8n. Follow technical documentation to integrate Mailchimp Trigger node into your workflows.
- [MailerLite Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mailerlitetrigger.md) — Learn how to use the MailerLite Trigger node in n8n. Follow technical documentation to integrate MailerLite Trigger node into your workflows.
- [Mailjet Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mailjettrigger.md) — Learn how to use the Mailjet Trigger node in n8n. Follow technical documentation to integrate Mailjet Trigger node into your workflows.
- [Mautic Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mautictrigger.md) — Learn how to use the Mautic Trigger node in n8n. Follow technical documentation to integrate Mautic Trigger node into your workflows.
- [Microsoft OneDrive Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger.md) — Learn how to use the Microsoft OneDrive Trigger node in n8n. Follow technical documentation to integrate Microsoft OneDrive Trigger node into your workflows.
- [Microsoft Outlook Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md) — Learn how to use the Microsoft Outlook Trigger node in n8n. Follow technical documentation to integrate Microsoft Outlook Trigger node into your workflows.
- [Microsoft Teams Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md) — Learn how to use the Microsoft Teams Trigger node in n8n. Follow technical documentation to integrate Microsoft Teams Trigger node into your workflows.
- [MQTT Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.mqtttrigger.md) — Learn how to use the MQTT Trigger node in n8n. Follow technical documentation to integrate MQTT Trigger node into your workflows.
- [Netlify Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.netlifytrigger.md) — Learn how to use the Netlify Trigger node in n8n. Follow technical documentation to integrate Netlify Trigger node into your workflows.
- [Notion Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.notiontrigger.md) — Learn how to use the Notion Trigger node in n8n. Follow technical documentation to integrate Notion Trigger node into your workflows.
- [Onfleet Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.onfleettrigger.md) — Learn how to use the Onfleet Trigger node in n8n. Follow technical documentation to integrate Onfleet Trigger node into your workflows.
- [PayPal Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.paypaltrigger.md) — Learn how to use the PayPal Trigger node in n8n. Follow technical documentation to integrate PayPal Trigger node into your workflows.
- [Pipedrive Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.pipedrivetrigger.md) — Learn how to use the Pipedrive Trigger node in n8n. Follow technical documentation to integrate Pipedrive Trigger node into your workflows.
- [Postgres Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger.md) — Learn how to use the Postgres Trigger node in n8n. Follow technical documentation to integrate Postgres Trigger node into your workflows.
- [Postmark Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.postmarktrigger.md) — Learn how to use the Postmark Trigger node in n8n. Follow technical documentation to integrate Postmark Trigger node into your workflows.
- [Pushcut Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger.md) — Learn how to use the Pushcut Trigger node in n8n. Follow technical documentation to integrate Pushcut Trigger node into your workflows.
- [RabbitMQ Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.rabbitmqtrigger.md) — Learn how to use the RabbitMQ Trigger node in n8n. Follow technical documentation to integrate RabbitMQ Trigger node into your workflows.
- [Redis Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.redistrigger.md) — Learn how to use the Redis Trigger node in n8n. Follow technical documentation to integrate Redis Trigger node into your workflows.
- [Salesforce Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger.md) — Learn how to use the Salesforce Trigger node in n8n. Follow technical documentation to integrate Salesforce Trigger node into your workflows.
- [SeaTable Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.seatabletrigger.md) — Learn how to use the SeaTable Trigger node in n8n. Follow technical documentation to integrate SeaTable Trigger node into your workflows.
- [Shopify Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.shopifytrigger.md) — Learn how to use the Shopify Trigger node in n8n. Follow technical documentation to integrate Shopify Trigger node into your workflows.
- [Slack Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md) — Learn how to use the Slack Trigger node in n8n. Follow technical documentation to integrate Slack Trigger node into your workflows.
- [Strava Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.stravatrigger.md) — Learn how to use the Strava Trigger node in n8n. Follow technical documentation to integrate Strava Trigger node into your workflows.
- [Stripe Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger.md) — Learn how to use the Stripe Trigger node in n8n. Follow technical documentation to integrate Stripe Trigger node into your workflows.
- [SurveyMonkey Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.surveymonkeytrigger.md) — Learn how to use the SurveyMonkey Trigger node in n8n. Follow technical documentation to integrate SurveyMonkey Trigger node into your workflows.
- [Taiga Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.taigatrigger.md) — Learn how to use the Taiga Trigger node in n8n. Follow technical documentation to integrate Taiga Trigger node into your workflows.
- [Telegram Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger.md) — Learn how to use the Telegram Trigger node in n8n. Follow technical documentation to integrate Telegram Trigger node into your workflows.
- [Common issues](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues.md) — Documentation for common issues and questions in the Telegram Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [TheHive 5 Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger.md) — Learn how to use the TheHive 5 Trigger node in n8n. Follow technical documentation to integrate TheHive 5 Trigger node into your workflows.
- [TheHive Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger.md) — Learn how to use the TheHive Trigger node in n8n. Follow technical documentation to integrate TheHive Trigger node into your workflows.
- [Toggl Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.toggltrigger.md) — Learn how to use the Toggl Trigger node in n8n. Follow technical documentation to integrate Toggl Trigger node into your workflows.
- [Trello Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger.md) — Learn how to use the Trello Trigger node in n8n. Follow technical documentation to integrate Trello Trigger node into your workflows.
- [Twilio Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger.md) — Learn how to use the Twilio Trigger node in n8n. Follow technical documentation to integrate Twilio Trigger node into your workflows.
- [Typeform Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.typeformtrigger.md) — Learn how to use the Typeform Trigger node in n8n. Follow technical documentation to integrate Typeform Trigger node into your workflows.
- [Venafi TLS Protect Cloud Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md) — Learn how to use the Venafi TLS Protect Cloud Trigger node in n8n. Follow technical documentation to integrate Venafi TLS Protect Cloud Trigger node into your workflows.
- [Webex by Cisco Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.ciscowebextrigger.md) — Learn how to use the Webex by Cisco Trigger node in n8n. Follow technical documentation to integrate Webex by Cisco Trigger node into your workflows.
- [Webflow Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.webflowtrigger.md) — Learn how to use the Webflow Trigger node in n8n. Follow technical documentation to integrate Webflow Trigger node into your workflows.
- [WhatsApp Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md) — Learn how to use the WhatsApp Trigger node in n8n. Follow technical documentation to integrate WhatsApp Trigger node into your workflows.
- [Wise Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.wisetrigger.md) — Learn how to use the Wise Trigger node in n8n. Follow technical documentation to integrate Wise Trigger node into your workflows.
- [WooCommerce Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.woocommercetrigger.md) — Learn how to use the WooCommerce Trigger node in n8n. Follow technical documentation to integrate WooCommerce Trigger node into your workflows.
- [Workable Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.workabletrigger.md) — Learn how to use the Workable Trigger node in n8n. Follow technical documentation to integrate Workable Trigger node into your workflows.
- [Wufoo Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.wufootrigger.md) — Learn how to use the Wufoo Trigger node in n8n. Follow technical documentation to integrate Wufoo Trigger node into your workflows.
- [Zendesk Trigger](pages/integrations/builtin/trigger-nodes/n8n-nodes-base.zendesktrigger.md) — Learn how to use the Zendesk Trigger node in n8n. Follow technical documentation to integrate Zendesk Trigger node into your workflows.

### `builtin/cluster-nodes.md` (1)

- [Cluster nodes](pages/integrations/builtin/cluster-nodes.md) — Understand cluster nodes in n8n, and browse the cluster nodes library.

### `builtin/cluster-nodes` (105)

- [Root nodes](pages/integrations/builtin/cluster-nodes/root-nodes.md) — Understand root nodes in n8n, and browse the root nodes library.
- [AI Agent](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent.md) — Learn how to use the AI Agent node in n8n. Follow technical documentation to integrate AI Agent node into your workflows.
- [Conversational Agent](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent.md) — Learn how to use the Conversational Agent of the AI Agent node in n8n. Follow technical documentation to integrate the Conversational Agent into your workflows.
- [OpenAI Functions Agent](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent.md) — Learn how to use the OpenAI Functions Agent of the AI Agent node in n8n. Follow technical documentation to integrate the OpenAI Functions Agent into your workflows.
- [Plan and Execute Agent](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent.md) — Learn how to use the Plan and Execute Agent of the AI Agent node in n8n. Follow technical documentation to integrate the Plan and Execute Agent into your workflows.
- [ReAct Agent](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent.md) — Learn how to use the ReAct Agent of the AI Agent node in n8n. Follow technical documentation to integrate the ReAct Agent into your workflows.
- [SQL Agent](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/sql-agent.md) — Learn how to use the SQL Agent of the AI Agent node in n8n. Follow technical documentation to integrate the SQL Agent into your workflows.
- [Tools Agent](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md) — Learn how to use the Tools Agent of the AI Agent node in n8n. Follow technical documentation to integrate the Tools Agent into your workflows.
- [Common issues](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md) — Documentation for common issues and questions in the AI Agent node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Basic LLM Chain](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md) — Learn how to use the Basic LLM Chain node in n8n. Follow technical documentation to integrate Basic LLM Chain node into your workflows.
- [Question and Answer Chain](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa.md) — Learn how to use the Question and Answer Chain node in n8n. Follow technical documentation to integrate Question and Answer Chain node into your workflows.
- [Common issues](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues.md) — Documentation for common issues and questions in the Question and Answer Chain node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Summarization Chain](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md) — Learn how to use the Summarize Chain node in n8n. Follow technical documentation to integrate Summarize Chain node into your workflows.
- [Information Extractor](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor.md) — Learn how to use the Information Extractor node in n8n. Follow technical documentation to integrate Information Extractor node into your workflows.
- [Text Classifier](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md) — Learn how to use the Text Classifier node in n8n. Follow technical documentation to integrate Text Classifier node into your workflows.
- [Sentiment Analysis](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis.md) — Learn how to use the Sentiment Analysis node in n8n. Follow technical documentation to integrate Sentiment Analysis node into your workflows.
- [LangChain Code](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md) — Learn how to use the LangChain Code node in n8n. Follow technical documentation to integrate LangChain Code node into your workflows.
- [Microsoft Agent 365 Trigger](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger.md) — Learn how to use the Microsoft Agent 365 Trigger node in n8n. Follow technical documentation to integrate Microsoft Agent 365 Trigger node into your workflows.
- [Azure AI Search Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch.md) — Learn how to use the Azure AI Search Vector Store node in n8n. Follow technical documentation to integrate Azure AI Search Vector Store node into your workflows.
- [Simple Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md) — Learn how to use the Simple Vector Store node in n8n. Follow technical documentation to integrate Simple Vector Store node into your workflows.
- [Milvus Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus.md) — Learn how to use the Milvus Vector Store node in n8n. Follow technical documentation to integrate Milvus Vector Store node into your workflows.
- [MongoDB Atlas Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md) — Learn how to use the MongoDB Atlas Vector Store node in n8n. Follow technical documentation to integrate MongoDB Atlas Vector Store node into your workflows.
- [PGVector Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md) — Learn how to use the PGVector Vector Store node in n8n. Follow technical documentation to integrate PGVector Vector Store node into your workflows.
- [Oracle Database Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreoracledb.md) — Learn how to use the Oracle Database Vector Store node in n8n. Follow technical documentation to integrate Oracle Database Vector Store node into your workflows.
- [Chroma Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma.md) — Learn how to use the Chroma Vector Store node in n8n. Follow technical documentation to integrate Chroma Vector Store node into your workflows.
- [Pinecone Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md) — Learn how to use the Pinecone Vector Store node in n8n. Follow technical documentation to integrate Pinecone Vector Store node into your workflows.
- [Qdrant Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md) — Learn how to use the Qdrant Vector Store node in n8n. Follow technical documentation to integrate Qdrant Vector Store node into your workflows.
- [Redis Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis.md) — Learn how to use the Redis Vector Store node in n8n. Follow technical documentation to integrate Redis Vector Store node into your workflows.
- [Supabase Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md) — Learn how to use the Supabase Vector Store node in n8n. Follow technical documentation to integrate Supabase Vector Store node into your workflows.
- [Weaviate Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate.md) — Learn how to use the Weaviate Vector Store node in n8n. Follow technical documentation to integrate Weaviate Vector Store node into your workflows.
- [Zep Vector Store](pages/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep.md) — Learn how to use the Zep Vector Store node in n8n. Follow technical documentation to integrate Zep Vector Store node into your workflows.
- [Sub-nodes](pages/integrations/builtin/cluster-nodes/sub-nodes.md) — Understand sub-nodes in n8n, and browse the sub-nodes library.
- [Default Data Loader](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md) — Learn how to use the Default Data Loader node in n8n. Follow technical documentation to integrate Default Data Loader node into your workflows.
- [GitHub Document Loader](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md) — Learn how to use the GitHub Document Loader node in n8n. Follow technical documentation to integrate GitHub Document Loader node into your workflows.
- [Embeddings AWS Bedrock](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md) — Learn how to use the Embeddings AWS Bedrock node in n8n. Follow technical documentation to integrate Embeddings AWS Bedrock node into your workflows.
- [Embeddings Azure OpenAI](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md) — Learn how to use the Embeddings Azure OpenAI node in n8n. Follow technical documentation to integrate Embeddings Azure OpenAI node into your workflows.
- [Embeddings Cohere](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md) — Learn how to use the Embeddings Cohere node in n8n. Follow technical documentation to integrate Embeddings Cohere node into your workflows.
- [Embeddings Google Gemini](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md) — Learn how to use the Embeddings Google Gemini node in n8n. Follow technical documentation to integrate Embeddings Google Gemini node into your workflows.
- [Embeddings Google PaLM](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md) — Learn how to use the Embeddings Google PaLM node in n8n. Follow technical documentation to integrate Embeddings Google PaLM node into your workflows.
- [Embeddings Google Vertex](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglevertex.md) — Learn how to use the Embeddings Google Vertex node in n8n. Follow technical documentation to integrate Embeddings Google Gemini node into your workflows.
- [Embeddings HuggingFace Inference](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md) — Learn how to use the Embeddings HuggingFace Inference node in n8n. Follow technical documentation to integrate Embeddings HuggingFace Inference node into your workflows.
- [Embeddings Lemonade](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade.md) — Learn how to use the Embeddings Lemonade node in n8n. Follow technical documentation to integrate Embeddings Lemonade node into your workflows.
- [Embeddings Mistral Cloud](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md) — Learn how to use the Embeddings Mistral Cloud node in n8n. Follow technical documentation to integrate Embeddings Mistral Cloud node into your workflows.
- [Embeddings Ollama](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama.md) — Learn how to use the Embeddings Ollama node in n8n. Follow technical documentation to integrate Embeddings Ollama node into your workflows.
- [Embeddings OpenAI](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md) — Learn how to use the Embeddings OpenAI node in n8n. Follow technical documentation to integrate Embeddings OpenAI node into your workflows.
- [Embeddings Oracle Database](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsoracledb.md) — Learn how to use the Embeddings Oracle Database node in n8n. Follow technical documentation to integrate Embeddings Oracle Database node into your workflows.
- [Qwen Cloud Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud.md) — The Qwen Cloud Chat Model node sends prompts to conversational models available on Qwen Cloud (for advanced AI chains). This page explains how to configure the node in n8n workflows and covers common
- [Anthropic Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md) — Learn how to use the Anthropic Chat Model node in n8n. Follow technical documentation to integrate Anthropic Chat Model node into your workflows.
- [AWS Bedrock Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md) — Learn how to use the AWS Bedrock Chat Model node in n8n. Follow technical documentation to integrate AWS Bedrock Chat Model node into your workflows.
- [Azure OpenAI Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md) — Learn how to use the Azure OpenAI Chat Model node in n8n. Follow technical documentation to integrate Azure OpenAI Chat Model node into your workflows.
- [Cohere Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere.md) — Learn how to use the Cohere Chat Model node in n8n. Follow technical documentation to integrate Cohere Chat Model node into your workflows.
- [DeepSeek Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek.md) — Learn how to use the DeepSeek Chat Model node in n8n. Follow technical documentation to integrate DeepSeek Chat Model node into your workflows.
- [Google Gemini Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md) — Learn how to use the Google Gemini Chat Model node in n8n. Follow technical documentation to integrate Google Gemini Chat Model node into your workflows.
- [Google Vertex Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md) — Learn how to use the Google Vertex Chat Model node in n8n. Follow technical documentation to integrate Google Vertex Chat Model node into your workflows.
- [Groq Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md) — Learn how to use the Groq Chat Model node in n8n. Follow technical documentation to integrate Groq Chat Model node into your workflows.
- [Lemonade Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade.md) — Learn how to use the Lemonade Chat Model node in n8n. Follow technical documentation to integrate Lemonade Chat Model node into your workflows.
- [MiniMax Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax.md) — Learn how to use the MiniMax Chat Model node in n8n. Follow technical documentation to integrate MiniMax Chat Model node into your workflows.
- [Mistral Cloud Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md) — Learn how to use the Mistral Cloud Chat Model node in n8n. Follow technical documentation to integrate Mistral Cloud Chat Model node into your workflows.
- [Moonshot Kimi Chat Model node](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot.md) — Integrate the Moonshot Kimi Chat Model into n8n workflows to generate chat responses for AI chains. Common uses include generating conversational replies, integrating with LangChain-style workflows, a
- [NVIDIA Nemotron Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia.md) — Learn how to use the NVIDIA Nemotron Chat Model node in n8n. Follow technical documentation to integrate NVIDIA Nemotron Chat Model node into your workflows.
- [Ollama Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama.md) — Learn how to use the Ollama Chat Model node in n8n. Follow technical documentation to integrate Ollama Chat Model node into your workflows.
- [Common issues](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md) — Documentation for common issues and questions in the Ollama Chat Model node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [OpenAI Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai.md) — Learn how to use the OpenAI Chat Model node in n8n. Follow technical documentation to integrate OpenAI Chat Model node into your workflows.
- [Common issues](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues.md) — Documentation for common issues and questions in the OpenAI Chat Model node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [OpenRouter Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter.md) — Learn how to use the OpenRouter Chat Model node in n8n. Follow technical documentation to integrate OpenRouter Chat Model node into your workflows.
- [Vercel AI Gateway Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatvercel.md) — Learn how to use the Vercel AI Gateway Chat Model node in n8n. Follow technical documentation to integrate Vercel AI Gateway Chat Model node into your workflows.
- [xAI Grok Chat Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok.md) — Learn how to use the xAI Grok Chat Model node in n8n. Follow technical documentation to integrate xAI Grok Chat Model node into your workflows.
- [Cohere Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md) — Learn how to use the Cohere Model node in n8n. Follow technical documentation to integrate Cohere Model node into your workflows.
- [Lemonade Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade.md) — Learn how to use the Lemonade Model node in n8n. Follow technical documentation to integrate Lemonade Model node into your workflows.
- [Ollama Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama.md) — Learn how to use the Ollama Model node in n8n. Follow technical documentation to integrate Ollama Model node into your workflows.
- [Common issues](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/common-issues.md) — Documentation for common issues and questions in the Ollama Model node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Hugging Face Inference Model](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md) — Learn how to use the Hugging Face Inference Model node in n8n. Follow technical documentation to integrate Hugging Face Inference Model node into your workflows.
- [Chat Memory Manager](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md) — Learn how to use the Chat Memory Manager node in n8n. Follow technical documentation to integrate Chat Memory Manager node into your workflows.
- [Simple Memory](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow.md) — Learn how to use the Simple Memory node in n8n. Follow technical documentation to integrate Simple Memory node into your workflows.
- [Common issues](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues.md) — Documentation for common issues and questions in the Simple Memory node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Motorhead](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md) — Learn how to use the Motorhead node in n8n. Follow technical documentation to integrate Motorhead node into your workflows.
- [MongoDB Chat Memory](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat.md) — Learn how to use the MongoDB Chat Memory node in n8n. Follow technical documentation to integrate MongoDB Chat Memory node into your workflows.
- [Redis Chat Memory](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md) — Learn how to use the Redis Chat Memory node in n8n. Follow technical documentation to integrate Redis Chat Memory node into your workflows.
- [Postgres Chat Memory](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md) — Learn how to use the Postgres Chat Memory node in n8n. Follow technical documentation to integrate Postgres Chat Memory node into your workflows.
- [Xata](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md) — Learn how to use the Xata node in n8n. Follow technical documentation to integrate Xata node into your workflows.
- [Zep](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md) — Learn how to use the Zep node in n8n. Follow technical documentation to integrate Zep node into your workflows.
- [Auto-fixing Output Parser](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing.md) — Learn how to use the Auto-fixing Output Parser node in n8n. Follow technical documentation to integrate Auto-fixing Output Parser node into your workflows.
- [Item List Output Parser](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist.md) — Learn how to use the Item List Output Parser node in n8n. Follow technical documentation to integrate Item List Output Parser node into your workflows.
- [Structured Output Parser](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured.md) — Learn how to use the Structured Output Parser node in n8n. Follow technical documentation to integrate Structured Output Parser node into your workflows.
- [Common issues](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues.md) — Documentation for common issues and questions in the Structured Output Parser node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
- [Contextual Compression Retriever](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression.md) — Learn how to use the Contextual Compression Retriever node in n8n. Follow technical documentation to integrate Contextual Compression Retriever node into your workflows.
- [MultiQuery Retriever](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery.md) — Learn how to use the MultiQuery Retriever node in n8n. Follow technical documentation to integrate MultiQuery Retriever node into your workflows.
- [Vector Store Retriever](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) — Learn how to use the Vector Store Retriever node in n8n. Follow technical documentation to integrate Vector Store Retriever node into your workflows.
- [Workflow Retriever](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow.md) — Learn how to use the Workflow Retriever node in n8n. Follow technical documentation to integrate Workflow Retriever node into your workflows.
- [Character Text Splitter](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter.md) — Learn how to use the Character Text Splitter node in n8n. Follow technical documentation to integrate Character Text Splitter node into your workflows.
- [Recursive Character Text Splitter](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md) — Learn how to use the Recursive Character Text Splitter node in n8n. Follow technical documentation to integrate Recursive Character Text Splitter node into your workflows.
- [Token Splitter](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter.md) — Learn how to use the Token Splitter node in n8n. Follow technical documentation to integrate Token Splitter node into your workflows.
- [AI Agent Tool](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent.md) — Learn how to use the AI Agent Tool node in n8n. Follow technical documentation to integrate the AI Agent Tool node into your workflows.
- [Calculator](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcalculator.md) — Learn how to use the Calculator node in n8n. Follow technical documentation to integrate Calculator node into your workflows.
- [Custom Code Tool](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md) — Learn how to use the Custom Code Tool node in n8n. Follow technical documentation to integrate Custom Code Tool node into your workflows.
- [MCP Client Tool](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md) — Learn how to use the MCP Client Tool node in n8n. Follow technical documentation to integrate MCP Client Tool node into your workflows.
- [SearXNG Tool](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng.md) — Learn how to use the SearXNG Tool node in n8n. Follow technical documentation to integrate SearXNG Tool node into your workflows.
- [SerpApi (Google Search)](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md) — Learn how to use the SerpApi (Google Search) node in n8n. Follow technical documentation to integrate SerpApi (Google Search) node into your workflows.
- [Think Tool](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink.md) — Learn how to use the Think Tool node in n8n. Follow technical documentation to integrate the Tool Think node into your workflows.
- [Vector Store Question Answer Tool](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) — Learn how to use the Vector Store Question Answer Tool node in n8n. Follow technical documentation to integrate Vector Store Question Answer Tool node into your workflows.
- [Wikipedia](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia.md) — Learn how to use the Wikipedia node in n8n. Follow technical documentation to integrate Wikipedia node into your workflows.
- [Wolfram|Alpha tool](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md) — Learn how to use the Wolfram|Alpha tool node in n8n. Follow technical documentation to integrate Wolfram|Alpha tool node into your workflows.
- [Call n8n Workflow Tool](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) — Learn how to use the Call n8n Workflow Tool node in n8n. Follow technical documentation to integrate Call n8n Workflow Tool node into your workflows.
- [Reranker Cohere](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere.md) — Learn how to use the Reranker Cohere node in n8n. Follow technical documentation to integrate Cohere reranking into your workflows.
- [Model Selector](pages/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector.md) — Learn how to use the Model Selector node in n8n. Follow technical documentation to integrate Model Selector node into your workflows.

### `builtin/credentials.md` (1)

- [Credentials](pages/integrations/builtin/credentials.md)

### `builtin/credentials` (326)

- [Action Network credentials](pages/integrations/builtin/credentials/actionnetwork.md) — Documentation for Action Network credentials. Use these credentials to authenticate Action Network in n8n, a workflow automation platform.
- [ActiveCampaign credentials](pages/integrations/builtin/credentials/activecampaign.md) — Documentation for ActiveCampaign credentials. Use these credentials to authenticate ActiveCampaign in n8n, a workflow automation platform.
- [Acuity Scheduling credentials](pages/integrations/builtin/credentials/acuityscheduling.md) — Documentation for Acuity Scheduling credentials. Use these credentials to authenticate Acuity Scheduling in n8n, a workflow automation platform.
- [Adalo credentials](pages/integrations/builtin/credentials/adalo.md) — Documentation for Adalo credentials. Use these credentials to authenticate Adalo in n8n, a workflow automation platform.
- [Affinity credentials](pages/integrations/builtin/credentials/affinity.md) — Documentation for the Affinity credentials. Use these credentials to authenticate Affinity in n8n, a workflow automation platform.
- [Agile CRM credentials](pages/integrations/builtin/credentials/agilecrm.md) — Documentation for Agile CRM credentials. Use these credentials to authenticate Agile CRM in n8n, a workflow automation platform.
- [Airtable credentials](pages/integrations/builtin/credentials/airtable.md) — Documentation for Airtable credentials. Use these credentials to authenticate Airtable in n8n, a workflow automation platform.
- [Airtop credentials](pages/integrations/builtin/credentials/airtop.md) — Documentation for the Airtop credentials. Use these credentials to authenticate Airtop in n8n, a workflow automation platform.
- [Qwen Cloud credentials](pages/integrations/builtin/credentials/alibaba.md) — Documentation for Qwen Cloud credentials. Use these credentials to authenticate Qwen Cloud in n8n, a workflow automation platform.
- [AlienVault credentials](pages/integrations/builtin/credentials/alienvault.md) — Documentation for the AlienVault credentials. Use these credentials to authenticate AlienVault in n8n, a workflow automation platform.
- [AMQP credentials](pages/integrations/builtin/credentials/amqp.md) — Documentation for AMQP credentials. Use these credentials to authenticate AMQP in n8n, a workflow automation platform.
- [Anthropic credentials](pages/integrations/builtin/credentials/anthropic.md) — Documentation for the Anthropic credentials. Use these credentials to authenticate Anthropic in n8n, a workflow automation platform.
- [APITemplate.io credentials](pages/integrations/builtin/credentials/apitemplateio.md) — Documentation for APITemplate.io credentials. Use these credentials to authenticate APITemplate.io in n8n, a workflow automation platform.
- [Asana credentials](pages/integrations/builtin/credentials/asana.md) — Documentation for Asana credentials. Use these credentials to authenticate Asana in n8n, a workflow automation platform.
- [Auth0 Management credentials](pages/integrations/builtin/credentials/auth0management.md) — Documentation for the Auth0 Management credentials. Use these credentials to authenticate Auth0 Management in n8n, a workflow automation platform.
- [Autopilot credentials](pages/integrations/builtin/credentials/autopilot.md) — Documentation for Autopilot credentials. Use these credentials to authenticate Autopilot in n8n, a workflow automation platform.
- [AWS credentials](pages/integrations/builtin/credentials/aws.md) — Documentation for AWS credentials. Use these credentials to authenticate AWS in n8n, a workflow automation platform.
- [Azure OpenAI credentials](pages/integrations/builtin/credentials/azureopenai.md) — Documentation for Azure OpenAI credentials. Use these credentials to authenticate OpenAI in n8n, a workflow automation platform.
- [Azure Cosmos DB credentials](pages/integrations/builtin/credentials/azurecosmosdb.md) — Documentation for the Azure Cosmos DB credentials. Use these credentials to authenticate Azure Cosmos DB in n8n, a workflow automation platform.
- [Azure AI Search credentials](pages/integrations/builtin/credentials/azureaisearch.md) — Documentation for Azure AI Search credentials. Use these credentials to authenticate Azure AI Search in n8n, a workflow automation platform.
- [Azure Storage credentials](pages/integrations/builtin/credentials/azurestorage.md) — Documentation for the Azure Storage credentials. Use these credentials to authenticate Azure Storage in n8n, a workflow automation platform.
- [BambooHR credentials](pages/integrations/builtin/credentials/bamboohr.md) — Documentation for BambooHR credentials. Use these credentials to authenticate BambooHR in n8n, a workflow automation platform.
- [Bannerbear credentials](pages/integrations/builtin/credentials/bannerbear.md) — Documentation for Bannerbear credentials. Use these credentials to authenticate Bannerbear in n8n, a workflow automation platform.
- [Baserow credentials](pages/integrations/builtin/credentials/baserow.md) — Documentation for Baserow credentials. Use these credentials to authenticate Baserow in n8n, a workflow automation platform.
- [Beeminder credentials](pages/integrations/builtin/credentials/beeminder.md) — Documentation for Beeminder credentials. Use these credentials to authenticate Beeminder in n8n, a workflow automation platform.
- [Bitbucket credentials](pages/integrations/builtin/credentials/bitbucket.md) — Documentation for Bitbucket credentials. Use these credentials to authenticate Bitbucket in n8n, a workflow automation platform.
- [Bitly credentials](pages/integrations/builtin/credentials/bitly.md) — Documentation for Bitly credentials. Use these credentials to authenticate Bitly in n8n, a workflow automation platform.
- [Bitwarden credentials](pages/integrations/builtin/credentials/bitwarden.md) — Documentation for Bitwarden credentials. Use these credentials to authenticate Bitwarden in n8n, a workflow automation platform.
- [Box credentials](pages/integrations/builtin/credentials/box.md) — Documentation for Box credentials. Use these credentials to authenticate Box in n8n, a workflow automation platform.
- [Brandfetch credentials](pages/integrations/builtin/credentials/brandfetch.md) — Documentation for Brandfetch credentials. Use these credentials to authenticate Brandfetch in n8n, a workflow automation platform.
- [Brave Search credentials](pages/integrations/builtin/credentials/bravesearch.md) — Documentation for the Brave Search credentials. Use these credentials to authenticate Brave Search in n8n, a workflow automation platform.
- [Brevo credentials](pages/integrations/builtin/credentials/brevo.md) — Documentation for Brevo credentials. Use these credentials to authenticate Brevo in n8n, a workflow automation platform.
- [Bubble credentials](pages/integrations/builtin/credentials/bubble.md) — Documentation for Bubble credentials. Use these credentials to authenticate Bubble in n8n, a workflow automation platform.
- [Cal.com credentials](pages/integrations/builtin/credentials/cal.md) — Documentation for Cal.com credentials. Use these credentials to authenticate Cal.com in n8n, a workflow automation platform.
- [Calendly credentials](pages/integrations/builtin/credentials/calendly.md) — Documentation for Calendly credentials. Use these credentials to authenticate Calendly in n8n, a workflow automation platform.
- [Carbon Black credentials](pages/integrations/builtin/credentials/carbonblack.md) — Documentation for the Carbon Black credentials. Use these credentials to authenticate Carbon Black in n8n, a workflow automation platform.
- [Chargebee credentials](pages/integrations/builtin/credentials/chargebee.md) — Documentation for Chargebee credentials. Use these credentials to authenticate Chargebee in n8n, a workflow automation platform.
- [CircleCI credentials](pages/integrations/builtin/credentials/circleci.md) — Documentation for CircleCI credentials. Use these credentials to authenticate CircleCI in n8n, a workflow automation platform.
- [Cisco Meraki credentials](pages/integrations/builtin/credentials/ciscomeraki.md) — Documentation for the Cisco Meraki credentials. Use these credentials to authenticate Cisco Meraki in n8n, a workflow automation platform.
- [Cisco Secure Endpoint credentials](pages/integrations/builtin/credentials/ciscosecureendpoint.md) — Documentation for the Cisco Secure Endpoint credentials. Use these credentials to authenticate Cisco Secure Endpoint in n8n, a workflow automation platform.
- [Cisco Umbrella credentials](pages/integrations/builtin/credentials/ciscoumbrella.md) — Documentation for the Cisco Umbrella credentials. Use these credentials to authenticate Cisco Umbrella in n8n, a workflow automation platform.
- [Clearbit credentials](pages/integrations/builtin/credentials/clearbit.md) — Documentation for Clearbit credentials. Use these credentials to authenticate Clearbit in n8n, a workflow automation platform.
- [ClickUp credentials](pages/integrations/builtin/credentials/clickup.md) — Documentation for ClickUp credentials. Use these credentials to authenticate ClickUp in n8n, a workflow automation platform.
- [Clockify credentials](pages/integrations/builtin/credentials/clockify.md) — Documentation for Clockify credentials. Use these credentials to authenticate Clockify in n8n, a workflow automation platform.
- [Cloudflare credentials](pages/integrations/builtin/credentials/cloudflare.md) — Documentation for Cloudflare credentials. Use these credentials to authenticate Cloudflare in n8n, a workflow automation platform.
- [Cockpit credentials](pages/integrations/builtin/credentials/cockpit.md) — Documentation for Cockpit credentials. Use these credentials to authenticate Cockpit in n8n, a workflow automation platform.
- [Coda credentials](pages/integrations/builtin/credentials/coda.md) — Documentation for Coda credentials. Use these credentials to authenticate Coda in n8n, a workflow automation platform.
- [Cohere credentials](pages/integrations/builtin/credentials/cohere.md) — Documentation for the Cohere credentials. Use these credentials to authenticate Cohere in n8n, a workflow automation platform.
- [Contentful credentials](pages/integrations/builtin/credentials/contentful.md) — Documentation for Contentful credentials. Use these credentials to authenticate Contentful in n8n, a workflow automation platform.
- [ConvertAPI credentials](pages/integrations/builtin/credentials/convertapi.md) — Documentation for the ConvertAPI credentials. Use these credentials to authenticate ConvertAPI in n8n, a workflow automation platform.
- [ConvertKit credentials](pages/integrations/builtin/credentials/convertkit.md) — Documentation for ConvertKit credentials. Use these credentials to authenticate ConvertKit in n8n, a workflow automation platform.
- [Copper credentials](pages/integrations/builtin/credentials/copper.md) — Documentation for Copper credentials. Use these credentials to authenticate Copper in n8n, a workflow automation platform.
- [Cortex credentials](pages/integrations/builtin/credentials/cortex.md) — Documentation for the Cortex credentials. Use these credentials to authenticate Cortex in n8n, a workflow automation platform.
- [CrateDB credentials](pages/integrations/builtin/credentials/cratedb.md) — Documentation for CrateDB credentials. Use these credentials to authenticate CrateDB in n8n, a workflow automation platform.
- [CrowdStrike credentials](pages/integrations/builtin/credentials/crowdstrike.md) — Documentation for the CrowdStrike credentials. Use these credentials to authenticate CrowdStrike in n8n, a workflow automation platform.
- [Crypto credentials](pages/integrations/builtin/credentials/crypto.md) — Documentation for the Crypto credentials. Use these credentials to authenticate the Crypto node in n8n, a workflow automation platform.
- [Customer.io credentials](pages/integrations/builtin/credentials/customerio.md) — Documentation for Customer.io credentials. Use these credentials to authenticate Customer.io in n8n, a workflow automation platform.
- [Databricks credentials](pages/integrations/builtin/credentials/databricks.md) — Documentation for Databricks credentials. Use these credentials to authenticate Databricks in n8n, a workflow automation platform.
- [Datadog credentials](pages/integrations/builtin/credentials/datadog.md) — Documentation for the Datadog credentials. Use these credentials to authenticate Datadog in n8n, a workflow automation platform.
- [Daytona credentials](pages/integrations/builtin/credentials/daytona.md) — Documentation for the Daytona credentials. Use these credentials to authenticate Daytona in n8n, a workflow automation platform.
- [DeepL credentials](pages/integrations/builtin/credentials/deepl.md) — Documentation for DeepL credentials. Use these credentials to authenticate DeepL in n8n, a workflow automation platform.
- [DeepSeek credentials](pages/integrations/builtin/credentials/deepseek.md) — Documentation for DeepSeek credentials. Use these credentials to authenticate Deepseek in n8n, a workflow automation platform.
- [Demio credentials](pages/integrations/builtin/credentials/demio.md) — Documentation for Demio credentials. Use these credentials to authenticate Demio in n8n, a workflow automation platform.
- [DFIR-IRIS credentials](pages/integrations/builtin/credentials/dfiriris.md) — Documentation for the DFIR-IRIS credentials. Use these credentials to authenticate DFIR-IRIS in n8n, a workflow automation platform.
- [DHL credentials](pages/integrations/builtin/credentials/dhl.md) — Documentation for DHL credentials. Use these credentials to authenticate DHL in n8n, a workflow automation platform.
- [Discord credentials](pages/integrations/builtin/credentials/discord.md) — Documentation for Discord credentials. Use these credentials to authenticate Discord in n8n, a workflow automation platform.
- [Discourse credentials](pages/integrations/builtin/credentials/discourse.md) — Documentation for Discourse credentials. Use these credentials to authenticate Discourse in n8n, a workflow automation platform.
- [Disqus credentials](pages/integrations/builtin/credentials/disqus.md) — Documentation for Disqus credentials. Use these credentials to authenticate Disqus in n8n, a workflow automation platform.
- [Drift credentials](pages/integrations/builtin/credentials/drift.md) — Documentation for Drift credentials. Use these credentials to authenticate Drift in n8n, a workflow automation platform.
- [Dropbox credentials](pages/integrations/builtin/credentials/dropbox.md) — Documentation for Dropbox credentials. Use these credentials to authenticate Dropbox in n8n, a workflow automation platform.
- [Dropcontact credentials](pages/integrations/builtin/credentials/dropcontact.md) — Documentation for Dropcontact credentials. Use these credentials to authenticate Dropcontact in n8n, a workflow automation platform.
- [Dynatrace credentials](pages/integrations/builtin/credentials/dynatrace.md) — Documentation for the Dynatrace credentials. Use these credentials to authenticate Dynatrace in n8n, a workflow automation platform.
- [E-goi credentials](pages/integrations/builtin/credentials/egoi.md) — Documentation for E-goi credentials. Use these credentials to authenticate E-goi in n8n, a workflow automation platform.
- [Elasticsearch credentials](pages/integrations/builtin/credentials/elasticsearch.md) — Documentation for Elasticsearch credentials. Use these credentials to authenticate Elasticsearch in n8n, a workflow automation platform.
- [Elastic Security credentials](pages/integrations/builtin/credentials/elasticsecurity.md) — Documentation for Elastic Security credentials. Use these credentials to authenticate Elastic Security in n8n, a workflow automation platform.
- [Emelia credentials](pages/integrations/builtin/credentials/emelia.md) — Documentation for Emelia credentials. Use these credentials to authenticate Emelia in n8n, a workflow automation platform.
- [ERPNext credentials](pages/integrations/builtin/credentials/erpnext.md) — Documentation for ERPNext credentials. Use these credentials to authenticate ERPNext in n8n, a workflow automation platform.
- [Eventbrite credentials](pages/integrations/builtin/credentials/eventbrite.md) — Documentation for Eventbrite credentials. Use these credentials to authenticate Eventbrite in n8n, a workflow automation platform.
- [F5 Big-IP credentials](pages/integrations/builtin/credentials/f5bigip.md) — Documentation for the F5 Big-IP credentials. Use these credentials to authenticate F5 Big-IP in n8n, a workflow automation platform.
- [Facebook App credentials](pages/integrations/builtin/credentials/facebookapp.md) — Documentation for Facebook App credentials. Use these credentials to authenticate Facebook App in n8n, a workflow automation platform.
- [Facebook Graph API credentials](pages/integrations/builtin/credentials/facebookgraph.md) — Documentation for Facebook Graph API credentials. Use these credentials to authenticate Facebook Graph API in n8n, a workflow automation platform.
- [Facebook Lead Ads credentials](pages/integrations/builtin/credentials/facebookleadads.md) — Documentation for the Facebook Lead Ads credentials. Use these credentials to authenticate Facebook Lead Ads in n8n, a workflow automation platform.
- [Figma credentials](pages/integrations/builtin/credentials/figma.md) — Documentation for Figma credentials. Use these credentials to authenticate Figma in n8n, a workflow automation platform.
- [FileMaker credentials](pages/integrations/builtin/credentials/filemaker.md) — Documentation for FileMaker credentials. Use these credentials to authenticate FileMaker in n8n, a workflow automation platform.
- [Filescan credentials](pages/integrations/builtin/credentials/filescan.md) — Documentation for the Filescan credentials. Use these credentials to authenticate Filescan in n8n, a workflow automation platform.
- [Flow credentials](pages/integrations/builtin/credentials/flow.md) — Documentation for Flow credentials. Use these credentials to authenticate Flow in n8n, a workflow automation platform.
- [Form.io Trigger credentials](pages/integrations/builtin/credentials/formiotrigger.md) — Documentation for Form.io Trigger credentials. Use these credentials to authenticate Form.io Trigger in n8n, a workflow automation platform.
- [Formstack Trigger credentials](pages/integrations/builtin/credentials/formstacktrigger.md) — Documentation for Formstack Trigger credentials. Use these credentials to authenticate Formstack Trigger in n8n, a workflow automation platform.
- [Fortinet FortiGate credentials](pages/integrations/builtin/credentials/fortigate.md) — Documentation for the Fortinet FortiGate credentials. Use these credentials to authenticate Fortinet FortiGate in n8n, a workflow automation platform.
- [Freshdesk credentials](pages/integrations/builtin/credentials/freshdesk.md) — Documentation for Freshdesk credentials. Use these credentials to authenticate Freshdesk in n8n, a workflow automation platform.
- [Freshservice credentials](pages/integrations/builtin/credentials/freshservice.md) — Documentation for Freshservice credentials. Use these credentials to authenticate Freshservice in n8n, a workflow automation platform.
- [Freshworks CRM credentials](pages/integrations/builtin/credentials/freshworkscrm.md) — Documentation for Freshworks CRM credentials. Use these credentials to authenticate Freshworks CRM in n8n, a workflow automation platform.
- [FTP credentials](pages/integrations/builtin/credentials/ftp.md) — Documentation for FTP credentials. Use these credentials to authenticate FTP in n8n, a workflow automation platform.
- [GetResponse credentials](pages/integrations/builtin/credentials/getresponse.md) — Documentation for GetResponse credentials. Use these credentials to authenticate GetResponse in n8n, a workflow automation platform.
- [Ghost credentials](pages/integrations/builtin/credentials/ghost.md) — Documentation for Ghost credentials. Use these credentials to authenticate Ghost in n8n, a workflow automation platform.
- [Git credentials](pages/integrations/builtin/credentials/git.md) — Documentation for Git credentials. Use these credentials to authenticate Git in n8n, a workflow automation platform.
- [GitHub credentials](pages/integrations/builtin/credentials/github.md) — Documentation for GitHub credentials. Use these credentials to authenticate GitHub in n8n, a workflow automation platform.
- [GitLab credentials](pages/integrations/builtin/credentials/gitlab.md) — Documentation for GitLab credentials. Use these credentials to authenticate GitLab in n8n, a workflow automation platform.
- [Gong credentials](pages/integrations/builtin/credentials/gong.md) — Documentation for the Gong credentials. Use these credentials to authenticate Gong in n8n, a workflow automation platform.
- [Google](pages/integrations/builtin/credentials/google.md) — Documentation for Google credentials. Use these credentials to authenticate with Google in n8n.
- [Google OAuth2 single service](pages/integrations/builtin/credentials/google/oauth-single-service.md) — Documentation for single service OAuth2 Google credentials. Use these credentials to authenticate with Google in n8n.
- [Google OAuth2 generic](pages/integrations/builtin/credentials/google/oauth-generic.md) — Documentation for generic OAuth2 Google credentials. Use these credentials to authenticate Google services in n8n, a workflow automation platform.
- [Google Service Account](pages/integrations/builtin/credentials/google/service-account.md) — Documentation for service account Google credentials. Use these credentials to authenticate Google in n8n, a workflow automation platform.
- [Google Gemini(PaLM) credentials](pages/integrations/builtin/credentials/googleai.md) — Documentation for the Google Gemini(PaLM) credentials. Use these credentials to authenticate Google Gemini and Google PaLM AI nodes in n8n, a workflow automation platform.
- [Gotify credentials](pages/integrations/builtin/credentials/gotify.md) — Documentation for Gotify credentials. Use these credentials to authenticate Gotify in n8n, a workflow automation platform.
- [GoToWebinar credentials](pages/integrations/builtin/credentials/gotowebinar.md) — Documentation for GoToWebinar credentials. Use these credentials to authenticate GoToWebinar in n8n, a workflow automation platform.
- [Grafana credentials](pages/integrations/builtin/credentials/grafana.md) — Documentation for Grafana credentials. Use these credentials to authenticate Grafana in n8n, a workflow automation platform.
- [Grist credentials](pages/integrations/builtin/credentials/grist.md) — Documentation for Grist credentials. Use these credentials to authenticate Grist in n8n, a workflow automation platform.
- [Groq credentials](pages/integrations/builtin/credentials/groq.md) — Documentation for the Groq credentials. Use these credentials to authenticate Groq in n8n, a workflow automation platform.
- [Gumroad credentials](pages/integrations/builtin/credentials/gumroad.md) — Documentation for Gumroad credentials. Use these credentials to authenticate Gumroad in n8n, a workflow automation platform.
- [HaloPSA credentials](pages/integrations/builtin/credentials/halopsa.md) — Documentation for HaloPSA credentials. Use these credentials to authenticate HaloPSA in n8n, a workflow automation platform.
- [Harvest credentials](pages/integrations/builtin/credentials/harvest.md) — Documentation for Harvest credentials. Use these credentials to authenticate Harvest in n8n, a workflow automation platform.
- [Help Scout credentials](pages/integrations/builtin/credentials/helpscout.md) — Documentation for Help Scout credentials. Use these credentials to authenticate Help Scout in n8n, a workflow automation platform.
- [HighLevel credentials](pages/integrations/builtin/credentials/highlevel.md) — Documentation for HighLevel credentials. Use these credentials to authenticate HighLevel in n8n, a workflow automation platform.
- [Home Assistant credentials](pages/integrations/builtin/credentials/homeassistant.md) — Documentation for Home Assistant credentials. Use these credentials to authenticate Home Assistant in n8n, a workflow automation platform.
- [HTTP Request credentials](pages/integrations/builtin/credentials/httprequest.md) — Documentation for HTTP Request credentials. Use these credentials to authenticate the HTTP Request node in n8n.
- [HubSpot credentials](pages/integrations/builtin/credentials/hubspot.md) — Documentation for HubSpot credentials. Use these credentials to authenticate HubSpot in n8n, a workflow automation platform.
- [Hugging Face credentials](pages/integrations/builtin/credentials/huggingface.md) — Documentation for the Hugging Face credentials. Use these credentials to authenticate Hugging Face in n8n, a workflow automation platform.
- [Humantic AI credentials](pages/integrations/builtin/credentials/humanticai.md) — Documentation for Humantic AI credentials. Use these credentials to authenticate Humantic AI in n8n, a workflow automation platform.
- [Hunter credentials](pages/integrations/builtin/credentials/hunter.md) — Documentation for Hunter credentials. Use these credentials to authenticate Hunter in n8n, a workflow automation platform.
- [Hybrid Analysis credentials](pages/integrations/builtin/credentials/hybridanalysis.md) — Documentation for the Hybrid Analysis credentials. Use these credentials to authenticate Hybrid Analysis in n8n, a workflow automation platform.
- [IMAP](pages/integrations/builtin/credentials/imap.md) — Documentation for IMAP credentials. Use these credentials to authenticate IMAP in n8n, a workflow automation platform.
- [Gmail](pages/integrations/builtin/credentials/imap/gmail.md) — Documentation for Gmail IMAP credentials. Use these credentials to authenticate Gmail IMAP in n8n, a workflow automation platform.
- [Outlook.com](pages/integrations/builtin/credentials/imap/outlook.md) — Documentation for Outlook.com IMAP credentials. Use these credentials to authenticate Outlook.com IMAP in n8n, a workflow automation platform.
- [Yahoo](pages/integrations/builtin/credentials/imap/yahoo.md) — Documentation for Yahoo IMAP credentials. Use these credentials to authenticate Yahoo IMAP in n8n, a workflow automation platform.
- [Imperva WAF credentials](pages/integrations/builtin/credentials/impervawaf.md) — Documentation for the Imperva WAF credentials. Use these credentials to authenticate Imperva WAF in n8n, a workflow automation platform.
- [Intercom credentials](pages/integrations/builtin/credentials/intercom.md) — Documentation for Intercom credentials. Use these credentials to authenticate Intercom in n8n, a workflow automation platform.
- [Invoice Ninja credentials](pages/integrations/builtin/credentials/invoiceninja.md) — Documentation for Invoice Ninja credentials. Use these credentials to authenticate Invoice Ninja in n8n, a workflow automation platform.
- [Iterable credentials](pages/integrations/builtin/credentials/iterable.md) — Documentation for Iterable credentials. Use these credentials to authenticate Iterable in n8n, a workflow automation platform.
- [Jenkins credentials](pages/integrations/builtin/credentials/jenkins.md) — Documentation for Jenkins credentials. Use these credentials to authenticate Jenkins in n8n, a workflow automation platform.
- [Jina AI credentials](pages/integrations/builtin/credentials/jinaai.md) — Documentation for the Jina AI credentials. Use these credentials to authenticate Jina AI in n8n, a workflow automation platform.
- [Jira credentials](pages/integrations/builtin/credentials/jira.md) — Documentation for Jira credentials. Use these credentials to authenticate Jira in n8n, a workflow automation platform.
- [Jotform credentials](pages/integrations/builtin/credentials/jotform.md) — Documentation for Jotform credentials. Use these credentials to authenticate Jotform in n8n, a workflow automation platform.
- [JWT credentials](pages/integrations/builtin/credentials/jwt.md) — Documentation for the JWT credentials. Use these credentials to authenticate JWT in n8n, a workflow automation platform.
- [Kafka credentials](pages/integrations/builtin/credentials/kafka.md) — Documentation for Kafka credentials. Use these credentials to authenticate Kafka in n8n, a workflow automation platform.
- [Keap credentials](pages/integrations/builtin/credentials/keap.md) — Documentation for Keap credentials. Use these credentials to authenticate Keap in n8n, a workflow automation platform.
- [Kibana credentials](pages/integrations/builtin/credentials/kibana.md) — Documentation for the Kibana credentials. Use these credentials to authenticate Kibana in n8n, a workflow automation platform.
- [Kitemaker credentials](pages/integrations/builtin/credentials/kitemaker.md) — Documentation for Kitemaker credentials. Use these credentials to authenticate Kitemaker in n8n, a workflow automation platform.
- [KoboToolbox credentials](pages/integrations/builtin/credentials/kobotoolbox.md) — Documentation for KoboToolbox credentials. Use these credentials to authenticate KoboToolbox in n8n, a workflow automation platform.
- [LDAP credentials](pages/integrations/builtin/credentials/ldap.md) — Documentation for the LDAP credentials. Use these credentials to authenticate LDAP in n8n, a workflow automation platform.
- [Lemlist credentials](pages/integrations/builtin/credentials/lemlist.md) — Documentation for Lemlist credentials. Use these credentials to authenticate Lemlist in n8n, a workflow automation platform.
- [Lemonade credentials](pages/integrations/builtin/credentials/lemonade.md) — Documentation for Lemonade credentials. Use these credentials to authenticate Lemonade in n8n, a workflow automation platform.
- [Line credentials](pages/integrations/builtin/credentials/line.md) — Documentation for Line credentials. Use these credentials to authenticate the Line node in n8n, a workflow automation platform.
- [Linear credentials](pages/integrations/builtin/credentials/linear.md) — Documentation for Linear credentials. Use these credentials to authenticate Linear in n8n, a workflow automation platform.
- [LingvaNex credentials](pages/integrations/builtin/credentials/lingvanex.md) — Documentation for LingvaNex credentials. Use these credentials to authenticate LingvaNex in n8n, a workflow automation platform.
- [LinkedIn credentials](pages/integrations/builtin/credentials/linkedin.md) — Documentation for LinkedIn credentials. Use these credentials to authenticate LinkedIn in n8n, a workflow automation platform.
- [LoneScale credentials](pages/integrations/builtin/credentials/lonescale.md) — Documentation for LoneScale credentials. Use these credentials to authenticate LoneScale in n8n, a workflow automation platform.
- [Magento 2 credentials](pages/integrations/builtin/credentials/magento2.md) — Documentation for Magento 2 credentials. Use these credentials to authenticate Magento 2 in n8n, a workflow automation platform.
- [Mailcheck credentials](pages/integrations/builtin/credentials/mailcheck.md) — Documentation for Mailcheck credentials. Use these credentials to authenticate Mailcheck in n8n, a workflow automation platform.
- [Mailchimp credentials](pages/integrations/builtin/credentials/mailchimp.md) — Documentation for Mailchimp credentials. Use these credentials to authenticate Mailchimp in n8n, a workflow automation platform.
- [MailerLite credentials](pages/integrations/builtin/credentials/mailerlite.md) — Documentation for MailerLite credentials. Use these credentials to authenticate MailerLite in n8n, a workflow automation platform.
- [Mailgun credentials](pages/integrations/builtin/credentials/mailgun.md) — Documentation for Mailgun credentials. Use these credentials to authenticate Mailgun in n8n, a workflow automation platform.
- [Mailjet credentials](pages/integrations/builtin/credentials/mailjet.md) — Documentation for Mailjet credentials. Use these credentials to authenticate Mailjet in n8n, a workflow automation platform.
- [Malcore credentials](pages/integrations/builtin/credentials/malcore.md) — Documentation for the Malcore credentials. Use these credentials to authenticate Malcore in n8n, a workflow automation platform.
- [Mandrill credentials](pages/integrations/builtin/credentials/mandrill.md) — Documentation for Mandrill credentials. Use these credentials to authenticate Mandrill in n8n, a workflow automation platform.
- [Marketstack credentials](pages/integrations/builtin/credentials/marketstack.md) — Documentation for Marketstack credentials. Use these credentials to authenticate Marketstack in n8n, a workflow automation platform.
- [Matrix credentials](pages/integrations/builtin/credentials/matrix.md) — Documentation for Matrix credentials. Use these credentials to authenticate Matrix in n8n, a workflow automation platform.
- [Mattermost credentials](pages/integrations/builtin/credentials/mattermost.md) — Documentation for Mattermost credentials. Use these credentials to authenticate Mattermost in n8n, a workflow automation platform.
- [Mautic credentials](pages/integrations/builtin/credentials/mautic.md) — Documentation for Mautic credentials. Use these credentials to authenticate Mautic in n8n, a workflow automation platform.
- [MCP credentials](pages/integrations/builtin/credentials/mcp.md) — Documentation for MCP credentials. Use these credentials to authenticate MCP servers in n8n, a workflow automation platform.
- [Medium credentials](pages/integrations/builtin/credentials/medium.md) — Documentation for Medium credentials. Use these credentials to authenticate Medium in n8n, a workflow automation platform.
- [MessageBird credentials](pages/integrations/builtin/credentials/messagebird.md) — Documentation for MessageBird credentials. Use these credentials to authenticate MessageBird in n8n, a workflow automation platform.
- [Metabase credentials](pages/integrations/builtin/credentials/metabase.md) — Documentation for Metabase credentials. Use these credentials to authenticate Metabase in n8n, a workflow automation platform.
- [Microsoft credentials](pages/integrations/builtin/credentials/microsoft.md) — Documentation for Microsoft credentials. Use these credentials to authenticate with Microsoft in n8n.
- [Microsoft Azure Monitor credentials](pages/integrations/builtin/credentials/microsoftazuremonitor.md) — Documentation for the Microsoft Azure Monitor credentials. Use these credentials to authenticate Microsoft Azure Monitor in n8n, a workflow automation platform.
- [Microsoft Entra ID credentials](pages/integrations/builtin/credentials/microsoftentra.md) — Documentation for the Microsoft Entra ID credentials. Use these credentials to authenticate Microsoft Entra ID in n8n, a workflow automation platform.
- [Microsoft Entra Service Principal credentials](pages/integrations/builtin/credentials/microsoftentraserviceprincipal.md) — Documentation for the Microsoft Entra Service Principal credentials. Use these credentials to authenticate Microsoft services in n8n, a workflow automation platform.
- [Microsoft SQL credentials](pages/integrations/builtin/credentials/microsoftsql.md) — Documentation for Microsoft SQL credentials. Use these credentials to authenticate Microsoft SQL in n8n, a workflow automation platform.
- [Microsoft Agent 365 credentials](pages/integrations/builtin/credentials/microsoftagent365.md) — Documentation for Microsoft Agent 365 credentials. Use these credentials to authenticate Microsoft Agent 365 in n8n, a workflow automation platform.
- [Milvus credentials](pages/integrations/builtin/credentials/milvus.md) — Documentation for the Milvus credentials. Use these credentials to authenticate Milvus in n8n, a workflow automation platform.
- [Mindee credentials](pages/integrations/builtin/credentials/mindee.md) — Documentation for Mindee credentials. Use these credentials to authenticate Mindee in n8n, a workflow automation platform.
- [Miro credentials](pages/integrations/builtin/credentials/miro.md) — Documentation for the Miro credentials. Use these credentials to authenticate Miro in n8n, a workflow automation platform.
- [MISP credentials](pages/integrations/builtin/credentials/misp.md) — Documentation for MISP credentials. Use these credentials to authenticate MISP in n8n, a workflow automation platform.
- [Mist credentials](pages/integrations/builtin/credentials/mist.md) — Documentation for the Mist credentials. Use these credentials to authenticate Mist in n8n, a workflow automation platform.
- [MiniMax credentials](pages/integrations/builtin/credentials/minimax.md) — Documentation for MiniMax credentials. Use these credentials to authenticate MiniMax in n8n, a workflow automation platform.
- [Mistral Cloud credentials](pages/integrations/builtin/credentials/mistral.md) — Documentation for the Mistral Cloud credentials. Use these credentials to authenticate Mistral Cloud in n8n, a workflow automation platform.
- [Mocean credentials](pages/integrations/builtin/credentials/mocean.md) — Documentation for Mocean credentials. Use these credentials to authenticate Mocean in n8n, a workflow automation platform.
- [monday.com credentials](pages/integrations/builtin/credentials/mondaycom.md) — Documentation for monday.com credentials. Use these credentials to authenticate monday.com in n8n, a workflow automation platform.
- [MongoDB credentials](pages/integrations/builtin/credentials/mongodb.md) — Documentation for MongoDB credentials. Use these credentials to authenticate MongoDB in n8n, a workflow automation platform.
- [Monica CRM credentials](pages/integrations/builtin/credentials/monicacrm.md) — Documentation for Monica CRM credentials. Use these credentials to authenticate Monica CRM in n8n, a workflow automation platform.
- [Moonshot credentials](pages/integrations/builtin/credentials/moonshot.md) — Documentation for Moonshot credentials. Use these credentials to authenticate Moonshot in n8n, a workflow automation platform.
- [Motorhead credentials](pages/integrations/builtin/credentials/motorhead.md) — Documentation for the Motorhead credentials. Use these credentials to authenticate Motorhead in n8n, a workflow automation platform.
- [MQTT credentials](pages/integrations/builtin/credentials/mqtt.md) — Documentation for MQTT credentials. Use these credentials to authenticate MQTT in n8n, a workflow automation platform.
- [MSG91 credentials](pages/integrations/builtin/credentials/msg91.md) — Documentation for MSG91 credentials. Use these credentials to authenticate MSG91 in n8n, a workflow automation platform.
- [MySQL credentials](pages/integrations/builtin/credentials/mysql.md) — Documentation for MySQL credentials. Use these credentials to authenticate MySQL in n8n, a workflow automation platform.
- [NASA credentials](pages/integrations/builtin/credentials/nasa.md) — Documentation for NASA credentials. Use these credentials to authenticate NASA in n8n, a workflow automation platform.
- [Netlify credentials](pages/integrations/builtin/credentials/netlify.md) — Documentation for Netlify credentials. Use these credentials to authenticate Netlify in n8n, a workflow automation platform.
- [Netscaler ADC credentials](pages/integrations/builtin/credentials/netscaleradc.md) — Documentation for Netscaler ADC credentials. Use these credentials to authenticate Netscaler ADC in n8n, a workflow automation platform.
- [Nextcloud credentials](pages/integrations/builtin/credentials/nextcloud.md) — Documentation for Nextcloud credentials. Use these credentials to authenticate Nextcloud in n8n, a workflow automation platform.
- [NocoDB credentials](pages/integrations/builtin/credentials/nocodb.md) — Documentation for NocoDB credentials. Use these credentials to authenticate NocoDB in n8n, a workflow automation platform.
- [Notion credentials](pages/integrations/builtin/credentials/notion.md) — Documentation for Notion credentials. Use these credentials to authenticate Notion in n8n, a workflow automation platform.
- [npm credentials](pages/integrations/builtin/credentials/npm.md) — Documentation for the npm credentials. Use these credentials to authenticate npm in n8n, a workflow automation platform.
- [NVIDIA Nemotron credentials](pages/integrations/builtin/credentials/nvidia.md) — Documentation for NVIDIA Nemotron credentials. Use these credentials to authenticate NVIDIA Nemotron in n8n, a workflow automation platform.
- [Odoo credentials](pages/integrations/builtin/credentials/odoo.md) — Documentation for Odoo credentials. Use these credentials to authenticate Odoo in n8n, a workflow automation platform.
- [Okta credentials](pages/integrations/builtin/credentials/okta.md) — Documentation for the Okta credentials. Use these credentials to authenticate Okta in n8n, a workflow automation platform.
- [Ollama credentials](pages/integrations/builtin/credentials/ollama.md) — Documentation for the Ollama credentials. Use these credentials to authenticate Ollama in n8n, a workflow automation platform.
- [One Simple API credentials](pages/integrations/builtin/credentials/onesimpleapi.md) — Documentation for One Simple API credentials. Use these credentials to authenticate One Simple API in n8n, a workflow automation platform.
- [Onfleet credentials](pages/integrations/builtin/credentials/onfleet.md) — Documentation for Onfleet credentials. Use these credentials to authenticate Onfleet in n8n, a workflow automation platform.
- [OpenAI credentials](pages/integrations/builtin/credentials/openai.md) — Documentation for OpenAI credentials. Use these credentials to authenticate with OpenAI in n8n.
- [OpenCTI credentials](pages/integrations/builtin/credentials/opencti.md) — Documentation for the OpenCTI credentials. Use these credentials to authenticate OpenCTI in n8n, a workflow automation platform.
- [OpenRouter credentials](pages/integrations/builtin/credentials/openrouter.md) — Documentation for OpenRouter credentials. Use these credentials to authenticate OpenRouter in n8n, a workflow automation platform.
- [OpenWeatherMap credentials](pages/integrations/builtin/credentials/openweathermap.md) — Documentation for OpenWeatherMap credentials. Use these credentials to authenticate OpenWeatherMap in n8n, a workflow automation platform.
- [Oracle Database credentials](pages/integrations/builtin/credentials/oracledb.md) — Documentation for Oracle Database credentials. Use these credentials to authenticate Oracle Database in n8n, a workflow automation platform.
- [Oura credentials](pages/integrations/builtin/credentials/oura.md) — Documentation for Oura credentials. Use these credentials to authenticate Oura in n8n, a workflow automation platform.
- [Paddle credentials](pages/integrations/builtin/credentials/paddle.md) — Documentation for Paddle credentials. Use these credentials to authenticate Paddle in n8n, a workflow automation platform.
- [PagerDuty credentials](pages/integrations/builtin/credentials/pagerduty.md) — Documentation for PagerDuty credentials. Use these credentials to authenticate PagerDuty in n8n, a workflow automation platform.
- [PayPal credentials](pages/integrations/builtin/credentials/paypal.md) — Documentation for PayPal credentials. Use these credentials to authenticate PayPal in n8n, a workflow automation platform.
- [Peekalink credentials](pages/integrations/builtin/credentials/peekalink.md) — Documentation for Peekalink credentials. Use these credentials to authenticate Peekalink in n8n, a workflow automation platform.
- [Perplexity credentials](pages/integrations/builtin/credentials/perplexity.md) — Documentation for the Perplexity credentials. Use these credentials to authenticate Perplexity in n8n, a workflow automation platform.
- [PhantomBuster credentials](pages/integrations/builtin/credentials/phantombuster.md) — Documentation for PhantomBuster credentials. Use these credentials to authenticate PhantomBuster in n8n, a workflow automation platform.
- [Philips Hue credentials](pages/integrations/builtin/credentials/philipshue.md) — Documentation for Philips Hue credentials. Use these credentials to authenticate Philips Hue in n8n, a workflow automation platform.
- [Chroma credentials](pages/integrations/builtin/credentials/chroma.md) — Documentation for the Chroma credentials. Use these credentials to authenticate Chroma in n8n, a workflow automation platform.
- [Pinecone credentials](pages/integrations/builtin/credentials/pinecone.md) — Documentation for the Pinecone credentials. Use these credentials to authenticate Pinecone in n8n, a workflow automation platform.
- [Pipedrive credentials](pages/integrations/builtin/credentials/pipedrive.md) — Documentation for Pipedrive credentials. Use these credentials to authenticate Pipedrive in n8n, a workflow automation platform.
- [Plivo credentials](pages/integrations/builtin/credentials/plivo.md) — Documentation for Plivo credentials. Use these credentials to authenticate Plivo in n8n, a workflow automation platform.
- [Postgres credentials](pages/integrations/builtin/credentials/postgres.md) — Documentation for Postgres credentials. Use these credentials to authenticate Postgres in n8n, a workflow automation platform.
- [PostHog credentials](pages/integrations/builtin/credentials/posthog.md) — Documentation for PostHog credentials. Use these credentials to authenticate PostHog in n8n, a workflow automation platform.
- [Postmark credentials](pages/integrations/builtin/credentials/postmark.md) — Documentation for Postmark credentials. Use these credentials to authenticate Postmark in n8n, a workflow automation platform.
- [ProfitWell credentials](pages/integrations/builtin/credentials/profitwell.md) — Documentation for ProfitWell credentials. Use these credentials to authenticate ProfitWell in n8n, a workflow automation platform.
- [Pushbullet credentials](pages/integrations/builtin/credentials/pushbullet.md) — Documentation for Pushbullet credentials. Use these credentials to authenticate Pushbullet in n8n, a workflow automation platform.
- [Pushcut credentials](pages/integrations/builtin/credentials/pushcut.md) — Documentation for Pushcut credentials. Use these credentials to authenticate Pushcut in n8n, a workflow automation platform.
- [Pushover credentials](pages/integrations/builtin/credentials/pushover.md) — Documentation for Pushover credentials. Use these credentials to authenticate Pushover in n8n, a workflow automation platform.
- [QRadar credentials](pages/integrations/builtin/credentials/qradar.md) — Documentation for the QRadar credentials. Use these credentials to authenticate QRadar in n8n, a workflow automation platform.
- [Qdrant credentials](pages/integrations/builtin/credentials/qdrant.md) — Documentation for the Qdrant credentials. Use these credentials to authenticate Qdrant in n8n, a workflow automation platform.
- [Qualys credentials](pages/integrations/builtin/credentials/qualys.md) — Documentation for the Qualys credentials. Use these credentials to authenticate Qualys in n8n, a workflow automation platform.
- [QuestDB credentials](pages/integrations/builtin/credentials/questdb.md) — Documentation for QuestDB credentials. Use these credentials to authenticate QuestDB in n8n, a workflow automation platform.
- [Quick Base credentials](pages/integrations/builtin/credentials/quickbase.md) — Documentation for Quick Base credentials. Use these credentials to authenticate Quick Base in n8n, a workflow automation platform.
- [QuickBooks credentials](pages/integrations/builtin/credentials/quickbooks.md) — Documentation for QuickBooks credentials. Use these credentials to authenticate QuickBooks in n8n, a workflow automation platform.
- [RabbitMQ credentials](pages/integrations/builtin/credentials/rabbitmq.md) — Documentation for RabbitMQ credentials. Use these credentials to authenticate RabbitMQ in n8n, a workflow automation platform.
- [Raindrop credentials](pages/integrations/builtin/credentials/raindrop.md) — Documentation for Raindrop credentials. Use these credentials to authenticate Raindrop in n8n, a workflow automation platform.
- [Rapid7 InsightVM credentials](pages/integrations/builtin/credentials/rapid7insightvm.md) — Documentation for the Rapid7 InsightVM credentials. Use these credentials to authenticate Rapid7 InsightVm in n8n, a workflow automation platform.
- [Recorded Future credentials](pages/integrations/builtin/credentials/recordedfuture.md) — Documentation for the Recorded Future credentials. Use these credentials to authenticate Recorded Future in n8n, a workflow automation platform.
- [Reddit credentials](pages/integrations/builtin/credentials/reddit.md) — Documentation for Reddit credentials. Use these credentials to authenticate Reddit in n8n, a workflow automation platform.
- [Redis credentials](pages/integrations/builtin/credentials/redis.md) — Documentation for Redis credentials. Use these credentials to authenticate Redis in n8n, a workflow automation platform.
- [Rocket.Chat credentials](pages/integrations/builtin/credentials/rocketchat.md) — Documentation for Rocket.Chat credentials. Use these credentials to authenticate Rocket.Chat in n8n, a workflow automation platform.
- [Rundeck credentials](pages/integrations/builtin/credentials/rundeck.md) — Documentation for Rundeck credentials. Use these credentials to authenticate Rundeck in n8n, a workflow automation platform.
- [S3 credentials](pages/integrations/builtin/credentials/s3.md) — Documentation for S3 credentials. Use these credentials to authenticate S3 in n8n, a workflow automation platform.
- [Salesforce credentials](pages/integrations/builtin/credentials/salesforce.md) — Documentation for Salesforce credentials. Use these credentials to authenticate Salesforce in n8n, a workflow automation platform.
- [Salesmate credentials](pages/integrations/builtin/credentials/salesmate.md) — Documentation for Salesmate credentials. Use these credentials to authenticate Salesmate in n8n, a workflow automation platform.
- [Schema Registry credentials](pages/integrations/builtin/credentials/schemaregistry.md) — Documentation for Schema Registry credentials. Use these credentials to authenticate Schema Registry in n8n, a workflow automation platform.
- [SearXNG credentials](pages/integrations/builtin/credentials/searxng.md) — Documentation for the SearXNG credentials. Use these credentials to authenticate SearXNG in n8n, a workflow automation platform.
- [SeaTable credentials](pages/integrations/builtin/credentials/seatable.md) — Documentation for SeaTable credentials. Use these credentials to authenticate SeaTable in n8n, a workflow automation platform.
- [SecurityScorecard credentials](pages/integrations/builtin/credentials/securityscorecard.md) — Documentation for SecurityScorecard credentials. Use these credentials to authenticate SecurityScorecard in n8n, a workflow automation platform.
- [Segment credentials](pages/integrations/builtin/credentials/segment.md) — Documentation for Segment credentials. Use these credentials to authenticate Segment in n8n, a workflow automation platform.
- [Sekoia credentials](pages/integrations/builtin/credentials/sekoia.md) — Documentation for the Sekoia credentials. Use these credentials to authenticate Sekoia in n8n, a workflow automation platform.
- [Send Email](pages/integrations/builtin/credentials/send-email.md) — Documentation for Send Email credentials. Use these credentials to authenticate Send Email in n8n, a workflow automation platform.
- [Gmail](pages/integrations/builtin/credentials/send-email/gmail.md) — Documentation for Gmail Send Email credentials. Use these credentials to authenticate Send Email with Gmail in n8n, a workflow automation platform.
- [Outlook.com](pages/integrations/builtin/credentials/send-email/outlook.md) — Documentation for Outlook.com Send Email credentials. Use these credentials to authenticate Send Email with Outlook.com in n8n, a workflow automation platform.
- [Yahoo](pages/integrations/builtin/credentials/send-email/yahoo.md) — Documentation for Yahoo Send Email credentials. Use these credentials to authenticate Send Email with Yahoo in n8n, a workflow automation platform.
- [SendGrid credentials](pages/integrations/builtin/credentials/sendgrid.md) — Documentation for SendGrid credentials. Use these credentials to authenticate SendGrid in n8n, a workflow automation platform.
- [Sendy credentials](pages/integrations/builtin/credentials/sendy.md) — Documentation for Sendy credentials. Use these credentials to authenticate Sendy in n8n, a workflow automation platform.
- [Sentry.io credentials](pages/integrations/builtin/credentials/sentryio.md) — Documentation for Sentry.io credentials. Use these credentials to authenticate Sentry.io in n8n, a workflow automation platform.
- [Serp credentials](pages/integrations/builtin/credentials/serp.md) — Documentation for the Serp credentials. Use these credentials to authenticate Serp in n8n, a workflow automation platform.
- [ServiceNow credentials](pages/integrations/builtin/credentials/servicenow.md) — Documentation for ServiceNow credentials. Use these credentials to authenticate ServiceNow in n8n, a workflow automation platform.
- [seven credentials](pages/integrations/builtin/credentials/sms77.md) — Documentation for seven credentials. Use these credentials to authenticate seven in n8n, a workflow automation platform.
- [Shopify credentials](pages/integrations/builtin/credentials/shopify.md) — Documentation for Shopify credentials. Use these credentials to authenticate Shopify in n8n, a workflow automation platform.
- [Shuffler credentials](pages/integrations/builtin/credentials/shuffler.md) — Documentation for the Shuffler credentials. Use these credentials to authenticate Shuffle in n8n, a workflow automation platform.
- [SIGNL4 credentials](pages/integrations/builtin/credentials/signl4.md) — Documentation for SIGNL4 credentials. Use these credentials to authenticate SIGNL4 in n8n, a workflow automation platform.
- [Slack credentials](pages/integrations/builtin/credentials/slack.md) — Documentation for Slack credentials. Use these credentials to authenticate Slack in n8n, a workflow automation platform.
- [Snowflake credentials](pages/integrations/builtin/credentials/snowflake.md) — Documentation for Snowflake credentials. Use these credentials to authenticate Snowflake in n8n, a workflow automation platform.
- [SolarWinds IPAM credentials](pages/integrations/builtin/credentials/solarwindsipam.md) — Documentation for the SolarWinds IPAM credentials. Use these credentials to authenticate SolarWinds IPAM in n8n, a workflow automation platform.
- [SolarWinds Observability SaaS credentials](pages/integrations/builtin/credentials/solarwindsobservability.md) — Documentation for the SolarWinds Observability SaaS credential, Use these credentials to authenticate SolarWinds Observability SaaS in n8n, a workflow automation platform
- [Splunk credentials](pages/integrations/builtin/credentials/splunk.md) — Documentation for Splunk credentials. Use these credentials to authenticate Splunk in n8n, a workflow automation platform.
- [Spotify credentials](pages/integrations/builtin/credentials/spotify.md) — Documentation for Spotify credentials. Use these credentials to authenticate Spotify in n8n, a workflow automation platform.
- [SSH credentials](pages/integrations/builtin/credentials/ssh.md) — Documentation for SSH credentials. Use these credentials to authenticate SSH in n8n, a workflow automation platform.
- [Stackby credentials](pages/integrations/builtin/credentials/stackby.md) — Documentation for Stackby credentials. Use these credentials to authenticate Stackby in n8n, a workflow automation platform.
- [Storyblok credentials](pages/integrations/builtin/credentials/storyblok.md) — Documentation for Storyblok credentials. Use these credentials to authenticate Storyblok in n8n, a workflow automation platform.
- [Strapi credentials](pages/integrations/builtin/credentials/strapi.md) — Documentation for Strapi credentials. Use these credentials to authenticate Strapi in n8n, a workflow automation platform.
- [Strava credentials](pages/integrations/builtin/credentials/strava.md) — Documentation for Strava credentials. Use these credentials to authenticate Strava in n8n, a workflow automation platform.
- [Stripe credentials](pages/integrations/builtin/credentials/stripe.md) — Documentation for Stripe credentials. Use these credentials to authenticate Stripe in n8n, a workflow automation platform.
- [Supabase credentials](pages/integrations/builtin/credentials/supabase.md) — Documentation for Supabase credentials. Use these credentials to authenticate Supabase in n8n, a workflow automation platform.
- [SurveyMonkey credentials](pages/integrations/builtin/credentials/surveymonkey.md) — Documentation for SurveyMonkey credentials. Use these credentials to authenticate SurveyMonkey in n8n, a workflow automation platform.
- [SyncroMSP credentials](pages/integrations/builtin/credentials/syncromsp.md) — Documentation for SyncroMSP credentials. Use these credentials to authenticate SyncroMSP in n8n, a workflow automation platform.
- [Sysdig credentials](pages/integrations/builtin/credentials/sysdig.md) — Documentation for the Sysdig credentials. Use these credentials to authenticate Sysdig in n8n, a workflow automation platform.
- [Taiga credentials](pages/integrations/builtin/credentials/taiga.md) — Documentation for Taiga credentials. Use these credentials to authenticate Taiga in n8n, a workflow automation platform.
- [Tapfiliate credentials](pages/integrations/builtin/credentials/tapfiliate.md) — Documentation for Tapfiliate credentials. Use these credentials to authenticate Tapfiliate in n8n, a workflow automation platform.
- [Telegram credentials](pages/integrations/builtin/credentials/telegram.md) — Documentation for Telegram credentials. Use these credentials to authenticate with Telegram in n8n.
- [TheHive credentials](pages/integrations/builtin/credentials/thehive.md) — Documentation for TheHive credentials. Use these credentials to authenticate TheHive in n8n, a workflow automation platform.
- [TheHive 5 credentials](pages/integrations/builtin/credentials/thehive5.md) — Documentation for TheHive 5 credentials. Use these credentials to authenticate TheHive in n8n, a workflow automation platform.
- [TimescaleDB credentials](pages/integrations/builtin/credentials/timescaledb.md) — Documentation for TimescaleDB credentials. Use these credentials to authenticate TimescaleDB in n8n, a workflow automation platform.
- [Todoist credentials](pages/integrations/builtin/credentials/todoist.md) — Documentation for Todoist credentials. Use these credentials to authenticate Todoist in n8n, a workflow automation platform.
- [Toggl credentials](pages/integrations/builtin/credentials/toggl.md) — Documentation for Toggl credentials. Use these credentials to authenticate Toggl in n8n, a workflow automation platform.
- [TOTP credentials](pages/integrations/builtin/credentials/totp.md) — Documentation for TOTP credentials. Use these credentials to authenticate TOTP in n8n, a workflow automation platform.
- [Travis CI credentials](pages/integrations/builtin/credentials/travisci.md) — Documentation for Travis CI credentials. Use these credentials to authenticate Travis CI in n8n, a workflow automation platform.
- [Trellix ePO credentials](pages/integrations/builtin/credentials/trellixepo.md) — Documentation for the Trellix ePO credentials. Use these credentials to authenticate Trellix ePO in n8n, a workflow automation platform.
- [Trello credentials](pages/integrations/builtin/credentials/trello.md) — Documentation for Trello credentials. Use these credentials to authenticate Trello in n8n, a workflow automation platform.
- [Twake credentials](pages/integrations/builtin/credentials/twake.md) — Documentation for Twake credentials. Use these credentials to authenticate Twake in n8n, a workflow automation platform.
- [Twilio credentials](pages/integrations/builtin/credentials/twilio.md) — Documentation for Twilio credentials. Use these credentials to authenticate Twilio in n8n, a workflow automation platform.
- [Twist credentials](pages/integrations/builtin/credentials/twist.md) — Documentation for Twist credentials. Use these credentials to authenticate Twist in n8n, a workflow automation platform.
- [Typeform credentials](pages/integrations/builtin/credentials/typeform.md) — Documentation for Typeform credentials. Use these credentials to authenticate Typeform in n8n, a workflow automation platform.
- [Unleashed Software credentials](pages/integrations/builtin/credentials/unleashedsoftware.md) — Documentation for Unleashed Software credentials. Use these credentials to authenticate Unleashed Software in n8n, a workflow automation platform.
- [UpLead credentials](pages/integrations/builtin/credentials/uplead.md) — Documentation for UpLead credentials. Use these credentials to authenticate UpLead in n8n, a workflow automation platform.
- [uProc credentials](pages/integrations/builtin/credentials/uproc.md) — Documentation for uProc credentials. Use these credentials to authenticate uProc in n8n, a workflow automation platform.
- [UptimeRobot credentials](pages/integrations/builtin/credentials/uptimerobot.md) — Documentation for UptimeRobot credentials. Use these credentials to authenticate UptimeRobot in n8n, a workflow automation platform.
- [urlscan.io credentials](pages/integrations/builtin/credentials/urlscanio.md) — Documentation for urlscan.io credentials. Use these credentials to authenticate urlscan.io in n8n, a workflow automation platform.
- [Venafi TLS Protect Cloud credentials](pages/integrations/builtin/credentials/venafitlsprotectcloud.md) — Documentation for Venafi TLS Protect Cloud credentials. Use these credentials to authenticate Venafi TLS Protect Cloud in n8n, a workflow automation platform.
- [Venafi TLS Protect Datacenter credentials](pages/integrations/builtin/credentials/venafitlsprotectdatacenter.md) — Documentation for Venafi TLS Protect Datacenter credentials. Use these credentials to authenticate Venafi TLS Protect Datacenter in n8n, a workflow automation platform.
- [Vercel AI Gateway credentials](pages/integrations/builtin/credentials/vercel.md) — Documentation for the Vercel AI Gateway credentials. Use these credentials to authenticate the Vercel AI Gateway in n8n, a workflow automation platform.
- [Vero credentials](pages/integrations/builtin/credentials/vero.md) — Documentation for Vero credentials. Use these credentials to authenticate Vero in n8n, a workflow automation platform.
- [VirusTotal credentials](pages/integrations/builtin/credentials/virustotal.md) — Documentation for the VirusTotal credentials. Use these credentials to authenticate VirusTotal in n8n, a workflow automation platform.
- [Vonage credentials](pages/integrations/builtin/credentials/vonage.md) — Documentation for Vonage credentials. Use these credentials to authenticate Vonage in n8n, a workflow automation platform.
- [Weaviate credentials](pages/integrations/builtin/credentials/weaviate.md) — Documentation for Weaviate credentials. Use these credentials to authenticate Weaviate in n8n, a workflow automation platform.
- [Webex by Cisco credentials](pages/integrations/builtin/credentials/ciscowebex.md) — Documentation for Webex by Cisco credentials. Use these credentials to authenticate Webex by Cisco in n8n, a workflow automation platform.
- [Webflow credentials](pages/integrations/builtin/credentials/webflow.md) — Documentation for Webflow credentials. Use these credentials to authenticate Webflow in n8n, a workflow automation platform.
- [Webhook credentials](pages/integrations/builtin/credentials/webhook.md) — Documentation for Webhook credentials. Use these credentials to authenticate Webhook in n8n, a workflow automation platform.
- [Wekan credentials](pages/integrations/builtin/credentials/wekan.md) — Documentation for Wekan credentials. Use these credentials to authenticate Wekan in n8n, a workflow automation platform.
- [WhatsApp Business Cloud credentials](pages/integrations/builtin/credentials/whatsapp.md) — Documentation for WhatsApp Business Cloud credentials. Use these credentials to authenticate with WhatsApp Business Cloud in n8n.
- [Wise credentials](pages/integrations/builtin/credentials/wise.md) — Documentation for Wise credentials. Use these credentials to authenticate Wise in n8n, a workflow automation platform.
- [Wolfram|Alpha credentials](pages/integrations/builtin/credentials/wolframalpha.md) — Documentation for the Wolfram|Alpha credentials. Use these credentials to authenticate Wolfram|Alpha in n8n, a workflow automation platform.
- [WooCommerce credentials](pages/integrations/builtin/credentials/woocommerce.md) — Documentation for WooCommerce credentials. Use these credentials to authenticate WooCommerce in n8n, a workflow automation platform.
- [WordPress credentials](pages/integrations/builtin/credentials/wordpress.md) — Documentation for WordPress credentials. Use these credentials to authenticate WordPress in n8n, a workflow automation platform.
- [Workable credentials](pages/integrations/builtin/credentials/workable.md) — Documentation for Workable credentials. Use these credentials to authenticate Workable in n8n, a workflow automation platform.
- [Wufoo credentials](pages/integrations/builtin/credentials/wufoo.md) — Documentation for Wufoo credentials. Use these credentials to authenticate Wufoo in n8n, a workflow automation platform.
- [X (formerly Twitter) credentials](pages/integrations/builtin/credentials/twitter.md) — Documentation for X credentials. Use these credentials to authenticate X in n8n, a workflow automation platform.
- [xAI credentials](pages/integrations/builtin/credentials/xai.md) — Documentation for xAI credentials. Use these credentials to authenticate xAI in n8n, a workflow automation platform.
- [Xata credentials](pages/integrations/builtin/credentials/xata.md) — Documentation for the Xata credentials. Use these credentials to authenticate Xata in n8n, a workflow automation platform.
- [Xero credentials](pages/integrations/builtin/credentials/xero.md) — Documentation for Xero credentials. Use these credentials to authenticate Xero in n8n, a workflow automation platform.
- [Yourls credentials](pages/integrations/builtin/credentials/yourls.md) — Documentation for Yourls credentials. Use these credentials to authenticate Yourls in n8n, a workflow automation platform.
- [Zabbix credentials](pages/integrations/builtin/credentials/zabbix.md) — Documentation for the Zabbix credentials. Use these credentials to authenticate Zabbix in n8n, a workflow automation platform.
- [Zammad credentials](pages/integrations/builtin/credentials/zammad.md) — Documentation for Zammad credentials. Use these credentials to authenticate Zammad in n8n, a workflow automation platform.
- [Zendesk credentials](pages/integrations/builtin/credentials/zendesk.md) — Documentation for Zendesk credentials. Use these credentials to authenticate Zendesk in n8n, a workflow automation platform.
- [Zep credentials](pages/integrations/builtin/credentials/zep.md) — Documentation for the Zep credentials. Use these credentials to authenticate Zep in n8n, a workflow automation platform.
- [Zoho credentials](pages/integrations/builtin/credentials/zoho.md) — Documentation for Zoho credentials. Use these credentials to authenticate Zoho in n8n, a workflow automation platform.
- [Zoom credentials](pages/integrations/builtin/credentials/zoom.md) — Documentation for Zoom credentials. Use these credentials to authenticate Zoom in n8n, a workflow automation platform.
- [Zscaler ZIA credentials](pages/integrations/builtin/credentials/zscalerzia.md) — Documentation for the Zscaler ZIA credentials. Use these credentials to authenticate Zscaler ZIA in n8n, a workflow automation platform.
- [Zulip credentials](pages/integrations/builtin/credentials/zulip.md) — Documentation for Zulip credentials. Use these credentials to authenticate Zulip in n8n, a workflow automation platform.

### `builtin/custom-api-actions-for-existing-nodes.md` (1)

- [Custom API actions for existing nodes](pages/integrations/builtin/custom-api-actions-for-existing-nodes.md)

### `builtin/handle-rate-limits.md` (1)

- [Handle rate limits](pages/integrations/builtin/handle-rate-limits.md) — How to handle API rate limits when using n8n integrations.

### `builtin/deprecated-nodes.md` (1)

- [Deprecated nodes](pages/integrations/builtin/deprecated-nodes.md)

### `community-nodes/installation-and-management.md` (1)

- [Installation and management](pages/integrations/community-nodes/installation-and-management.md)

### `community-nodes/installation-and-management` (4)

- [Install verified community nodes](pages/integrations/community-nodes/installation-and-management/install-verified-community-nodes.md)
- [GUI installation](pages/integrations/community-nodes/installation-and-management/gui-installation.md)
- [Manual installation](pages/integrations/community-nodes/installation-and-management/manual-installation.md)
- [Environment variable installation](pages/integrations/community-nodes/installation-and-management/environment-variable-installation.md)

### `community-nodes/risks.md` (1)

- [Risks](pages/integrations/community-nodes/risks.md)

### `community-nodes/blocklist.md` (1)

- [Blocklist](pages/integrations/community-nodes/blocklist.md)

### `community-nodes/using-community-nodes.md` (1)

- [Using community nodes](pages/integrations/community-nodes/using-community-nodes.md)

### `community-nodes/troubleshooting.md` (1)

- [Troubleshooting](pages/integrations/community-nodes/troubleshooting.md)

### `community-nodes/building-community-nodes.md` (1)

- [Building community nodes](pages/integrations/community-nodes/building-community-nodes.md)

---


## Source and attribution

Local copies in this folder come from n8n’s public documentation and public OpenAPI endpoints. They are a **working snapshot for project documentation**, not an official n8n publication.

### Official documentation

- Site: https://docs.n8n.io/
- Connect / API: https://docs.n8n.io/connect/n8n-api/
- Markdown per page: append `.md` to any docs URL
- Index: https://docs.n8n.io/sitemap.md
- AI index: https://docs.n8n.io/llms.txt
- This snapshot: **1,343** pages under `pages/` (full sitemap), plus OpenAPI from RaceCS and n8n Cloud
- This file is the compiled runbook.

n8n remains the source of truth. Paths, request bodies, and schemas can change between instance versions.

### OpenAPI

| File | Fetched from |
| --- | --- |
| `openapi/n8n.racecs.com-openapi.yml` | https://n8n.racecs.com/api/v1/openapi.yml |
| `openapi/n8n.racecs.com-docs.html` | https://n8n.racecs.com/api/v1/docs/ |
| `openapi/internal.users.n8n.cloud-openapi.yml` | https://internal.users.n8n.cloud/api/v1/openapi.yml |
| `openapi/n8n-github-openapi.yml` | https://raw.githubusercontent.com/n8n-io/n8n/master/packages/cli/src/public-api/v1/openapi.yml (split `$ref` spec; not a full standalone document) |

`openapi/endpoints.json` is generated from those YAML files.

### License notes

- n8n Public API OpenAPI `info.license`: [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)
- Terms: https://n8n.io/legal/#terms
- Contact listed in the spec: hello@n8n.io

Do not treat this tree as redistributable n8n documentation. Keep it as internal project reference unless n8n’s license and terms allow otherwise.

---
