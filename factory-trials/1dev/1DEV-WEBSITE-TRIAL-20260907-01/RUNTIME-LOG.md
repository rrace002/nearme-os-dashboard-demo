# Runtime log — 1DEV-WEBSITE-TRIAL-20260907-01

Working artifact only. Not a durable Airtable receipt. Append-only for this VM folder.

| when (UTC) | actor (actual) | role (registry) | action | input → output | result | missing |
|---|---|---|---|---|---|---|
| 2026-09-08T03:44:21Z | Cursor Cloud bc-585598ce-ea56-4ca9-aa5f-11f100143409 · grok-4.6-high | 04 Theme holder=Script (not this actor) | Start whole-website trial | assignment 1DEV-WEBSITE-TRIAL-20260907-01 · project rec2TGgh9WIfpeL1i | OK | — |
| 2026-09-08T03:44:21Z–2026-09-08T03:54:00Z | Cursor | (read-only) | Read Orchestrator + Control + Page Slots schema/rows | bases appc0ux4lMLH2R6PR, appaqwW9su2kPHw8W, appzSnVLfWHvKwtiV → live IDs | OK | Stage.Role empty on 1Dev |
| 2026-09-08T03:44:21Z–2026-09-08T03:54:00Z | Cursor | (read-only) | Enumerate Site Pages | Project.Site Pages 121 IDs in 3 batches; table total 186 | OK | no url_path field |
| 2026-09-08T03:44:21Z–2026-09-08T03:54:00Z | Cursor | (read-only) | Instructions/Sections/Blocks/Tokens/File Registry | 17 / 7 / 25 / 53 | OK | INS md files on C:\ |
| 2026-09-08T03:54:00Z | Cursor | (local files only) | Write labelled drafts + inventory + report | /workspace/factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01 | OK | factory output adapter |
| 2026-09-08T03:54:00Z | Cursor | (local tests) | Parse HTML, inventory counts, no placeholder tel | VERIFICATION.md | OK if 0 FAIL | Browser MCP unavailable |
| 2026-09-08T03:54:00Z | Cursor | C2 Scribe holder=Claude (interim) | Airtable Action Log write | would log this trial | **BLOCKED** | assignment forbids Airtable writes |
| 2026-09-08T03:56:00Z | Cursor Cloud bc-585598ce-ea56-4ca9-aa5f-11f100143409 · grok-4.6-high | 04 Theme holder=Script (actual=Cursor) | Build private runnable preview from existing inventory.csv | 121 pages + preview index + demo-url-map + localhost:8768 | OK | approved url_path; GHL; INS md |
| 2026-09-08T03:58:00Z | Cursor | local tests | Static link/H1/viewport/form + HTTP 200 on all 121 + nav markers | test_preview.py + curl 127.0.0.1:8768 | OK | Browser MCP / JS click-path not run |
| 2026-09-08T03:58:00Z | Cursor | C2 Scribe | Airtable Action Log write for demo build | this preview | **BLOCKED** | assignment forbids Airtable writes |
| 2026-09-08T04:19:00Z | Cursor | file handoff | Package portable site ZIP (HTML/CSS/JS + README only) | 130 entries · 358709 bytes · copies in trial folder + `/opt/cursor/artifacts/` | OK on disk | Artifacts **panel** visibility is a platform UI fact, not proven from this VM |
| 2026-09-08T04:38:00Z–2026-09-08T04:41:00Z | Cursor | local visual tests | Chrome CDP on `127.0.0.1:8768` (Browser MCP unavailable) | index + svc-cat01-hub + svc-cat01-01 + contact; empty `checkValidity=false`; filled submit shows DEMO ONLY and Network POST count 0 | OK PNGs in artifacts + `preview-screenshots/` | native empty-submit tooltip not in PNG; no Cursor Web browser click-through |
| 2026-09-08T04:41:00Z | Cursor | private preview branch | Distinguish server vs platform vs client | Server `127.0.0.1:8768` HTTP 200 localhost-only; client `net::ERR_BLOCKED_BY_CLIENT` left as client policy; no public bind, no protection disable | ZIP is authorized handoff | live private-preview URL still blocked on Rich’s browser until that client allowlists the host |
| 2026-09-08T04:41:00Z | Cursor | C2 Scribe | Airtable Action Log write for this handoff | this correction | **BLOCKED** | assignment forbids Airtable writes |

| 2026-09-08T04:46:00Z | Cursor | artifact UX | Codex: ZIP listed but “Preview not available for .zip”; PNG thumbnail only | Cursor Web Artifacts pane + forum 166771 + API download docs | **Web UI download NOT verified** | ZIP/HTML have no Web preview/download control; API download needs owner key (not present here) |
| 2026-09-08T04:46:00Z | Cursor | file handoff | Refresh ZIP README bind | `python3 -m http.server 8768 --bind 127.0.0.1`; double-click index.html first; 130 entries · 358770 bytes | ZIP on disk refreshed | Web UI still cannot download it |
| 2026-09-08T04:46:00Z | Cursor | tests | No Chrome this turn (bound: skip hang risk) | — | skipped | — |
| 2026-09-08T05:15:16Z–2026-09-08T05:20:45Z | Cursor Cloud bc-585598ce-ea56-4ca9-aa5f-11f100143409 · grok-4.6-high | 04 Theme holder=Script (actual=Cursor) | **PRESENTATION-01** gutters + visitor/audit split | input ZIP `artifacts/1DEV-WEBSITE-TRIAL-20260907-01-preview.zip` 358770 B / 130 entries (Codex API-read). Output: `preview/css/site.css`; 121 `preview/pages/*.html`; `preview/index.html`; `_build_preview.py`; refreshed ZIP 358738 B / 130 entries / 122 HTML | OK in VM | not 145 Any Drain visual match; Web UI still has no ZIP download |

**phase/stage:** 04 Theme / Designer `recuiaLZsSpx2VBvP` Doing.  
**cost_usd:** unknown (not measured). **started_at/ended_at (Airtable):** not written. **task_id:** 1DEV-WEBSITE-TRIAL-20260907-01.

**VM-local (not a human download):** preview server on `127.0.0.1:8768`; `factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01/preview/`; this RUNTIME-LOG.

**Cursor Web Artifacts pane:** listing verified by Codex; **download/open control not present** for ZIP; PNG thumbnail only. That is the precise platform limitation of the Web UI.

**Supported download (not the Web pane):** `GET https://api.cursor.com/v1/agents/bc-585598ce-ea56-4ca9-aa5f-11f100143409/artifacts/download?path=artifacts/1DEV-WEBSITE-TRIAL-20260907-01-preview.zip` with the owner’s API key. This VM did not execute it.

**PRESENTATION-01 tests:** `test_preview.py` fails=0 (121 pages + preview index; 1 H1; relative file/hash links; no tel:; review-notes collapsed; visitor banner; `--grid-gutter` via `padding-inline`; form `preventDefault`). Chrome CDP (bound 45s) hub/child/contact at 375 and 1280: computed padding-left/right **24px** (`--grid-gutter`); `scrollWidth === clientWidth` (no overflow); review notes `open=false` until opened; filled submit DEMO ONLY text; Network POST **0**. Screenshots: `preview-screenshots/p01-*.png` and `/opt/cursor/artifacts/screenshots/p01-*.png`. Browser MCP unavailable. No private-preview-host retry.

**PRESENTATION-01 remaining limits:** 145 Any Drain hub was not available in this VM — no visual-equivalence claim. Cursor Web Artifacts listing is still not a human download (ZIP: no preview/download control). Authenticated API download remains the supported retrieval path. `cost_usd` unknown. Airtable not written.

**Read-back:** this file exists at `factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01/RUNTIME-LOG.md`.
