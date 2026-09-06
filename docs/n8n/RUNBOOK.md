# n8n operations runbook

Full operational runbook compiled from **1,343** official n8n documentation pages (https://docs.n8n.io/sitemap.md), plus live OpenAPI from our RaceCS instance and n8n Cloud.

n8n remains the source of truth. This runbook is the **how we run it** overlay: procedures first, then pointers into the local page copies.

| Asset | Path |
| --- | --- |
| This runbook | [RUNBOOK.md](RUNBOOK.md) |
| Every official page (local) | [pages/](pages/) |
| Complete page index | [runbook/PAGE-INDEX.md](runbook/PAGE-INDEX.md) |
| Nodes / credentials catalog (945 pages) | [runbook/NODES.md](runbook/NODES.md) |
| Command cheat sheet | [runbook/CHEATSHEET.md](runbook/CHEATSHEET.md) |
| Environment variables | [runbook/ENV-VARS.md](runbook/ENV-VARS.md) |
| Public API endpoint catalog | [ENDPOINTS.md](ENDPOINTS.md) |
| Similar-link list (Connect/API) | [LINKS.md](LINKS.md) |
| Attribution | [SOURCE.md](SOURCE.md) |

**RaceCS instance**

- Editor / API host: `https://n8n.racecs.com`
- Swagger: https://n8n.racecs.com/api/v1/docs/
- OpenAPI: https://n8n.racecs.com/api/v1/openapi.yml
- Auth header: `X-N8N-API-KEY`

---

## 0. How to use this runbook

1. Follow the numbered procedures in this file for day-to-day ops.
2. Open the linked `pages/...` file when you need the full official steps, flags, or screenshots.
3. For “is there a node for X?”, search [runbook/NODES.md](runbook/NODES.md).
4. For HTTP against `/api/v1`, use [ENDPOINTS.md](ENDPOINTS.md).
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

Source section: [runbook/PAGE-INDEX.md](runbook/PAGE-INDEX.md) → Deploy (123 pages). Overview: [pages/deploy/readme.md](pages/deploy/readme.md).

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
Catalog: [runbook/ENV-VARS.md](runbook/ENV-VARS.md)

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

The same page covers license, user management, community packages, LDAP reset, and more. Search headings in [use-the-command-line.md](pages/deploy/host-n8n/configure-n8n/use-the-command-line.md) or [runbook/CHEATSHEET.md](runbook/CHEATSHEET.md).

---

## 5. Public API (programmatic ops)

Sources: [pages/connect/n8n-api.md](pages/connect/n8n-api.md), [pages/connect/n8n-api/authentication.md](pages/connect/n8n-api/authentication.md), [pages/connect/n8n-api/pagination.md](pages/connect/n8n-api/pagination.md), [ENDPOINTS.md](ENDPOINTS.md)

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

Full tables: [ENDPOINTS.md](ENDPOINTS.md). Resource docs: `pages/connect/n8n-api/<resource>.md`.

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

137 pages under Build: [runbook/PAGE-INDEX.md](runbook/PAGE-INDEX.md) (Build section). Start: [pages/build/](pages/build/) via sitemap entries.

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

945 pages: [runbook/NODES.md](runbook/NODES.md)

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

Every official URL → local file: **[runbook/PAGE-INDEX.md](runbook/PAGE-INDEX.md)**

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
