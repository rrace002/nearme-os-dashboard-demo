# Source and attribution

Local copies in this folder come from n8n’s public documentation and public OpenAPI endpoints. They are a **working snapshot for project documentation**, not an official n8n publication.

## Official documentation

- Site: https://docs.n8n.io/
- Connect / API: https://docs.n8n.io/connect/n8n-api/
- Markdown per page: append `.md` to any docs URL
- Index: https://docs.n8n.io/sitemap.md
- AI index: https://docs.n8n.io/llms.txt

n8n remains the source of truth. Paths, request bodies, and schemas can change between instance versions.

## OpenAPI

| File | Fetched from |
| --- | --- |
| `openapi/n8n.racecs.com-openapi.yml` | https://n8n.racecs.com/api/v1/openapi.yml |
| `openapi/n8n.racecs.com-docs.html` | https://n8n.racecs.com/api/v1/docs/ |
| `openapi/internal.users.n8n.cloud-openapi.yml` | https://internal.users.n8n.cloud/api/v1/openapi.yml |
| `openapi/n8n-github-openapi.yml` | https://raw.githubusercontent.com/n8n-io/n8n/master/packages/cli/src/public-api/v1/openapi.yml (split `$ref` spec; not a full standalone document) |

`ENDPOINTS.md` and `openapi/endpoints.json` are generated from those YAML files.

## License notes

- n8n Public API OpenAPI `info.license`: [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)
- Terms: https://n8n.io/legal/#terms
- Contact listed in the spec: hello@n8n.io

Do not treat this tree as redistributable n8n documentation. Keep it as internal project reference unless n8n’s license and terms allow otherwise.
