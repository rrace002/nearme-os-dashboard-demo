# Command cheat sheet

Commands extracted from official docs. Prefer the source page when flags change.

## One-line setup

Source: [`deploy/host-n8n/install-options/one-line-setup.md`](../pages/deploy/host-n8n/install-options/one-line-setup.md)

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

## Install with Docker

Source: [`deploy/host-n8n/install-options/install-with-docker.md`](../pages/deploy/host-n8n/install-options/install-with-docker.md)

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
# Pull latest (stable) version 
docker pull n8nio/n8n

# Pull specific version 
docker pull n8nio/n8n:1.81.0

# Pull next (unstable) version 
docker pull n8nio/n8n:next
```

```
# Find your container ID 
docker ps -a

# Stop the container with the `<container_id>` 
docker stop <container_id>

# Remove the container with the `<container_id>` 
docker rm <container_id>

# Start the container 
docker run --name=<container_name> [options] -d n8nio/n8n
```

```
# Navigate to the directory containing your docker compose file 
cd </path/to/your/compose/file/directory>

# Pull latest version 
docker compose pull

# Stop and remove older version 
docker compose down

# Start the container 
docker compose up -d
```

```
pnpm stack --tunnel
```

```
# Terminal 1: Start the cloudflared tunnel service 
pnpm --filter n8n-containers services --services cloudflared

# Terminal 2: Start n8n locally 
pnpm dev
```

```
pnpm --filter n8n-containers services:clean
```

## Use the command line

Source: [`deploy/host-n8n/configure-n8n/use-the-command-line.md`](../pages/deploy/host-n8n/configure-n8n/use-the-command-line.md)

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

## n8n CLI

Source: [`connect/n8n-cli.md`](../pages/connect/n8n-cli.md)

```
# Use directly with npx (zero install) 
npx @n8n/cli workflow list

# Or install globally 
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

## Authentication

Source: [`connect/n8n-api/authentication.md`](../pages/connect/n8n-api/authentication.md)

```
# For a self-hosted n8n instance 
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'

# For n8n Cloud 
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'
```

## Pagination

Source: [`connect/n8n-api/pagination.md`](../pages/connect/n8n-api/pagination.md)

```
# For a self-hosted n8n instance 
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'

# For n8n Cloud 
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'
```

```
Then to request the next page:
```

## Connect to the n8n docs MCP server

Source: [`connect/connect-to-n8n-docs-mcp-server.md`](../pages/connect/connect-to-n8n-docs-mcp-server.md)

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

## MCP client connection examples

Source: [`connect/connect-to-n8n-mcp-server/mcp-client-examples.md`](../pages/connect/connect-to-n8n-mcp-server/mcp-client-examples.md)

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

## Connecting Gemini CLI to n8n MCP server 

Use the following CLI command:
```

```
Or add the following entry to your `~/.gemini/settings.json` file:
```

```
Here, replace:

* `<your-n8n-domain>`: Your n8n domain, for example `https://your-instance.app.n8n.cloud`, found in n8n under **Settings** > **Instance-level MCP > Connect a client > Server URL**.

Run `/mcp` in Gemini CLI and select **n8n** to complete the OAuth authorization.

## Connecting Cursor to n8n MCP server 

In the **Connect a client** dialog, select **Cursor** from **Your client**, then select **One-click setup** to open Cursor and add the n8n server automatically. Approve access when Cursor redirects you back to n8n.

Or add the following entry to your `~/.cursor/mcp.json` file (or the project's `.cursor/mcp.json`):
```

```
Here, replace:

* `<your-n8n-domain>`: Your n8n domain, for example `https://your-instance.app.n8n.cloud`, found in n8n under **Settings** > **Instance-level MCP > Connect a client > Server URL**.

## Connecting VS Code to n8n MCP server 

In the **Connect a client** dialog, select **VS Code** from **Your client**, then select **One-click setup** to open VS Code and add the n8n server automatically. Approve access when VS Code redirects you back to n8n.

Or add the following entry to your workspace's `.vscode/mcp.json` file:
```

```
Here, replace:

* `<your-n8n-domain>`: Your n8n domain, for example `https://your-instance.app.n8n.cloud`, found in n8n under **Settings** > **Instance-level MCP > Connect a client > Server URL**.

## Connecting Windsurf to n8n MCP server 

Add the following entry to your `~/.codeium/windsurf/mcp_config.json` file:
```
