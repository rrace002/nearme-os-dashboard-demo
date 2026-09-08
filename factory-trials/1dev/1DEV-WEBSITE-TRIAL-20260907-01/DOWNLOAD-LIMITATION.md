# Cursor Web artifact download — exact limitation

Trial: `1DEV-WEBSITE-TRIAL-20260907-01`  
Observed by Codex on Cursor Web (this run): the Artifacts tree **lists** the ZIP and `screenshots/01-preview-index.png`. Clicking the ZIP shows **“Preview not available for .zip”** with **no download control**. Clicking the PNG shows a **tiny thumbnail** with **no full-size control**. Listing is not a human download.

## What the Web UI actually supports (this product)

- **ZIP:** no in-UI preview and no in-UI download. Cursor staff (Colin, 2026-07-27, forum topic “Unable to download artifacts that do not have a preview in Cursor Web”) stated the download control was **removed for security** and restoring it is on a to-do list. https://forum.cursor.com/t/unable-to-download-artifacts-that-do-not-have-a-preview-in-cursor-web/166771
- **PNG:** thumbnail preview only, as observed. Full-size / download was **not** observed.
- **HTML artifacts:** not a rendered site. HTML artifact rendering is an open feature request (June 2026). https://forum.cursor.com/t/html-artifact-rendering/163242

This trial will **not** scrape blob/S3 URLs from DevTools, mint a public URL, email the file through another transport, bind the demo on all interfaces, or disable client protection.

## Supported download that is not the Web Artifacts pane

Authenticated **Cloud Agent API** (requires the owner’s Cursor API key; 15-minute URL):

```bash
curl --request GET \
  --url 'https://api.cursor.com/v1/agents/bc-585598ce-ea56-4ca9-aa5f-11f100143409/artifacts' \
  -u "$CURSOR_API_KEY:"

curl --request GET \
  --url 'https://api.cursor.com/v1/agents/bc-585598ce-ea56-4ca9-aa5f-11f100143409/artifacts/download?path=artifacts/1DEV-WEBSITE-TRIAL-20260907-01-preview.zip' \
  -u "$CURSOR_API_KEY:"
```

Docs: https://cursor.com/docs/cloud-agent/api/endpoints  
That returns `{ "url", "expiresAt" }`. Then unzip and **double-click `index.html`**.

This agent cannot complete that call: it has no user API key here, and it will not substitute an unauthenticated public link.

## After you have the folder

Simplest: double-click `index.html`.  
Optional: `python3 -m http.server 8768 --bind 127.0.0.1` (localhost only).
