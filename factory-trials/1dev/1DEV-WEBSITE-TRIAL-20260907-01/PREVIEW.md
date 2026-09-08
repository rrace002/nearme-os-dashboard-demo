# Private preview — how to run

Trial: `1DEV-WEBSITE-TRIAL-20260907-01`

Human download (do not use a bare `PREVIEW.md` at repo root):

- [OPEN-HERE.md](OPEN-HERE.md)
- [1DEV-WEBSITE-TRIAL-20260907-01-preview.zip](1DEV-WEBSITE-TRIAL-20260907-01-preview.zip)

Repo-root path for chat: `factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01/`

This is a **PRIVATE DEMO**. It is not a public deployment. `index.html` is a **preview-only navigation index**, not Home, and not a Site Pages row.

## Start command

```bash
cd /workspace/factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01/preview
python3 -m http.server 8768 --bind 127.0.0.1
```

## Open

- Preview index (not Home): http://127.0.0.1:8768/
- First hub: http://127.0.0.1:8768/pages/svc-cat01-hub.html
- First child: http://127.0.0.1:8768/pages/svc-cat01-01.html
- Contact form: http://127.0.0.1:8768/pages/com-cat01-form01.html

On this VM a server is already bound to `127.0.0.1:8768` (tmux session `1dev-preview`). Bind is localhost only.

The optional README command is `python3 -m http.server 8768 --bind 127.0.0.1`. Double-click `index.html` is the simplest open once the folder is on a laptop.

Cursor Web Artifacts listing is **not** a download. See [DOWNLOAD-LIMITATION.md](DOWNLOAD-LIMITATION.md).

Preview routes are `pages/{slot_id}.html`. Approved `url_slug` values are **leaf slugs**, not paths. See `preview/demo-url-map.json` (explicitly **not** the approved URL manifest).

Dashboard `index.html` at repo root was not modified.
