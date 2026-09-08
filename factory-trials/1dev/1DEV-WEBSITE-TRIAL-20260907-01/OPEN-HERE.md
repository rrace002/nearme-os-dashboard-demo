# Open the 1Dev private demo here

Trial: `1DEV-WEBSITE-TRIAL-20260907-01`

Chat and Files-tree links must be **repo-root scoped**. A bare `PREVIEW.md` at the repository root does not exist.

## Human download is not the Artifacts listing

Codex verified on Cursor Web: Artifacts **lists** the ZIP, but clicking it shows **“Preview not available for .zip”** with **no download control**. The PNG listing shows a thumbnail only. **Presence is not a download.**

The Web Artifacts pane has no supported ZIP download/open control. Cursor staff removed the download UX for non-previewable artifacts (forum, 2026-07-27). HTML artifact rendering is also not a product feature.

This trial will not scrape blob URLs, publish the site, or disable client protection.

The **supported** download that exists outside that pane is the authenticated Cloud Agent API (owner API key, 15-minute URL). Exact commands: [DOWNLOAD-LIMITATION.md](DOWNLOAD-LIMITATION.md). This agent cannot run that call (no user API key here).

## After you have the unzipped folder

Simplest: **double-click `index.html`**.

Optional localhost-only server: `python3 -m http.server 8768 --bind 127.0.0.1`

## Files-tree paths (source, not a rendered site)

- `factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01/1DEV-WEBSITE-TRIAL-20260907-01-preview.zip`
- [preview/index.html](preview/index.html) — preview index, **not** Home
- [preview/pages/svc-cat01-hub.html](preview/pages/svc-cat01-hub.html)
- [preview/pages/svc-cat01-01.html](preview/pages/svc-cat01-01.html)
- [preview/pages/com-cat01-form01.html](preview/pages/com-cat01-form01.html)

## Localhost URL (this VM only)

`http://127.0.0.1:8768/` is HTTP 200 **inside this VM**. It is not a laptop URL. `net::ERR_BLOCKED_BY_CLIENT` remains a client-side block and is not bypassed.
