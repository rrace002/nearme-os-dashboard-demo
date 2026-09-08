PRIVATE 1Dev demo — open this on your computer
Trial: 1DEV-WEBSITE-TRIAL-20260907-01
This ZIP is the human handoff. It is not a live website and not a public deploy.

How to open (no internet required)
1. Unzip this archive.
2. Double-click index.html
   That is the simplest option.
3. Optional local server (localhost only; not all interfaces):
   python3 -m http.server 8768 --bind 127.0.0.1
   then open http://127.0.0.1:8768/
4. Use Preview index → a Service hub → a child page → Contact.

What this is
- 121 inventory pages plus a preview-only index (that index is NOT Home).
- Links are relative: pages/{slot_id}.html
- Those paths are NOT the approved public URL manifest (url_slug is a leaf only).
- Forms say DEMO ONLY / NOT CONNECTED. They validate on the page and do not send data.

Omitted on purpose
- No telephone link (placeholder number is not published)
- No pricing, ratings, or client photos

Do not upload this folder to a public host as the live 1devai.io site.
The optional server must stay on 127.0.0.1 only.
