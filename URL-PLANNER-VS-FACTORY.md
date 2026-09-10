# url_planner.py vs NearMe OS factory (this dashboard)

Comparison of the **site-spec URL planner** (`url_planner.py` from `site_spec_base_template`) with the **site configuration / factory agent** in this dashboard (`index.html`).

They solve the same job at a high level — turn business + services into a page list with URLs — but they sit at different layers of NearMe OS.

| | `url_planner.py` | Dashboard factory (`index.html`) |
| --- | --- | --- |
| **Role** | Spec-layer URL grammar. Writes a planned sitemap CSV. | Demo/runtime factory. Plans inventory, then renders HTML. |
| **Language** | Python CLI | In-browser JavaScript; optional Python engine over HTTP |
| **Python file** | `url_planner.py` (this file) | Referenced as `python engine/build_server.py` — **not in this repo** |
| **Primary function** | `main(folder)` | `runFactoryBuild` → `planInventory` → `buildSiteHtml` or `POST /build` |
| **Output** | `06_url_structure.csv` | In-memory `site.inventory` + HTML pages (or engine preview URLs) |
| **Stops at** | Planned rows + production checkboxes | Render + word-band QA + (demo) GHL wiring |

---

## 1. What each one is

### `url_planner.py`

A **deterministic CSV expander**. An operator fills four intake sheets; this script expands them into one row per planned URL. It does not pick a trade pack, does not render pages, and does not invent keywords.

Reads:

1. `01_business_profile.csv` — domain
2. `02_locations.csv` — city / state / `city_label` (empty file = single-location)
3. `03_service_categories.csv` — category hubs
4. `04_keywords.csv` — keyword children, joined by `category_index`

Writes `06_url_structure.csv` with `status=planned` and all done-flags `N`.

### Dashboard factory agent

A **vertical-pack factory** inside the cockpit. Site config (Live → Site config) only displays name / code / domain / GHL. The real planner is the factory build:

- UI sequence: S1 → S8
- URL planner step: **S4 · Plan URLs + inventory** (`planInventory`)
- Then it keeps going: TEMPLATE copy, HTML emit, link + word-band QA

If `http://127.0.0.1:8765/health` is up, S8 is supposed to POST `exportSiteForEngine(site)` to the Python bridge. If the bridge is down, the browser fallback runs the same inventory + HTML in JS.

---

## 2. Sequence comparison

### url_planner.py — internal process

```
folder arg
  → load 01 (fail if empty) → domain
  → load 02, 03, 04 (fail if 03 or 04 empty)
  → emit HOME  https://{domain}/
  → if 02 empty: one fake location with blank city/state
  → for each category:
       for each location:
         emit CATEGORY  /{category_slug}[-{city_label}]/
         for each keyword where category_index matches:
           emit SERVICE or LOCATION-VARIANT
             /{category}/{keyword}[-{city_label}]/
             parent_url = category slug
  → write 06_url_structure.csv
  → print counts
```

URL grammar:

- Single-site: `/{category_slug}/` then `/{category_slug}/{keyword_slug}/`
- Multi-city: `/{category_slug}-{city_label}/` then `/{category_slug}-{city_label}/{keyword_slug}-{city_label}/`

Page types: `home` | `category` | `service` | `location-variant`.

### Dashboard factory — internal process

**Cockpit “Generating site” (5 UI steps):**

1. Parse brief → questionnaire (FACT pass-through)
2. Plan URLs + inventory
3. Compose TEMPLATE packs (AI off)
4. Render + validate
5. Wire forms → GHL (demo)

**Factory overlay (S1–S8), what actually runs:**

| Step | Label | What the JS really does |
| --- | --- | --- |
| S1 | Parse questionnaire → facts | Reads `site.intake` (NAP, services, towns, hours). No CSV. |
| S2 | Keyword / intent seeds | UI only. No keyword API. |
| S3 | Instantiate page types | `resolveVertical(site)` picks Electrician / Plumber / HVAC / Handyman / Cleaning from the services string. |
| S4 | Plan URLs + inventory | **`planInventory(site)`** — this is the counterpart to `url_planner.py`. |
| S5/S6 | Compose TEMPLATE packs | FACT/AUTO/LIBRARY strings in `renderFactoryPage` (AI off). |
| S7 | Emit inventory rows | `site.inventory[]` with codes `EES-01`, target keywords from title + area. |
| S8 | Render + validate | Engine POST `/build`, else `buildSiteHtml` + `runClientValidation`. |

`planInventory` URL grammar (always single-area, nested hubs):

```
/                                      HOME
/{hub.slug}/                           SVC-HUB      (category)
/{hub.slug}/{child-slug}/              SVC-CHILD    (service)
/about/                                COMP-HUB
/about/why-choose-us/                  COMP-CHILD
/about/best-company/                   COMP-BEST
/contact/                              COMP-CONTACT
/{form.slug}/                          FORM-PRICING | FORM-SERVICE-REQ
```

Vertical packs are **hardcoded** (`VERTICAL_PACKS`), not read from `03`/`04`.

---

## 3. Data mapping

| Planner concept | `url_planner.py` | Dashboard factory |
| --- | --- | --- |
| Domain | `01.domain` | `site.domain` (often `draft.demo` until publish) |
| Locations | `02_locations.csv` rows | One `site.area` string. **No city replication.** |
| Categories | `03.category_slug` + name | `VERTICAL_PACKS[vertical].hubs[].slug` |
| Keywords / children | `04.keywords` filtered by `category_index` | Hub `children[]` titles, slugified |
| Home | Always one row | HOME `/` |
| Category page | `page_type=category` | `SVC-HUB` |
| Service page | `service` or `location-variant` | `SVC-CHILD` |
| Company / forms | **Not generated** | About, Why Choose, Best Company, Contact, 2 forms |
| Parent | `parent_url` on every non-home row | `hub` + `parentTitle` on children only |
| Priority | From `04.priority` (default 3) | Not stored. Plan page caps instead. |
| Production flags | p1–p9, h1_meta, internal_links, glossary, qa | Separate QA table (word-band / no-IT / broken links) |
| Target keyword | Implicit in `04.keyword` | `slugify(title) + " " + slugify(area)` |

---

## 4. Side-by-side internals

### Inputs

`url_planner.py` is **sheet-driven**. Wrong or empty CSVs fail fast. Keyword set is whatever the operator typed.

The factory is **pack-driven**. Intake facts (name, phone, city, towns, hours, notes) fill copy. The tree of URLs comes from the vertical pack, not from a keyword worksheet. `resolveVertical` is a regex on the services string; `"Other local service"` aliases to Cleaning.

Site config UI does **not** feed the planner. Saving config is a demo toast.

### Python file

| | Planner | Dashboard |
| --- | --- | --- |
| File | `url_planner.py` | `engine/build_server.py` (referenced, not shipped here) |
| Job | Expand CSVs → `06` | HTTP `/health` + `/build`; dashboard still calls `planInventory` locally even on engine success |
| Payload to engine | n/a | `{ id, name, code, vertical, area, phone, ghl, intake }` — **no URL list, no 01–04 CSVs** |

So even the “Python engine” path does not run `url_planner.py`. The engine is a renderer/validator. The URL tree is still the JS pack.

### Sequence overlap (the real equivalent)

The **only** step that matches `url_planner.py` is factory **S4 / `planInventory`**.

Both:

- Always emit a home page
- Nest service URLs under a category/hub slug
- Use trailing slashes
- Are deterministic (no LLM)

They diverge immediately after that:

- Planner stops at CSV + checkboxes
- Factory continues into HTML, nav, FAQ, forms, QA, publish, GHL

### Internal processes `url_planner.py` has that the factory does not

- Multi-location cartesian product (category × city, keyword × city)
- `city_label` baked into the slug (`panel-upgrades-elizabeth-nj`)
- Explicit `location-variant` vs `service`
- Join key `category_index` between categories and keywords
- Full `06` production columns (assignee, due_date, wp_post_id, p1–p9, WP/glossary flags)
- Operator-authored keyword list (04) as the source of truth

### Internal processes the factory has that `url_planner.py` does not

- Vertical pack library (5 trades)
- Company pages + lead forms
- Nested `/hub/child/` without city suffix
- TEMPLATE HTML render (AI off)
- Client validation (word bands per role, no-IT lexicon, `data-nm-path` link check)
- Optional engine bridge + browser fallback
- Plan limits (pages / sites / revisions)
- Demo publish URLs (`*.demo.nearmeos.com`)
- Keyword → landing → organic map lives in **PPC**, not in URL planning

---

## 5. What would have to change to make them the same process

To drive the dashboard from `url_planner.py` (or the same 01–04 sheets):

1. Load 01–04 (or equivalent JSON) instead of `VERTICAL_PACKS`.
2. Use planner URL grammar, including `city_label` and location-variants.
3. Map `category` → `SVC-HUB`, `service`/`location-variant` → `SVC-CHILD`.
4. Keep factory-only extras (COMP + FORM) as a second pass **after** 06, or add them to the planner.
5. Point S8 at `06_url_structure.csv` rows rather than inventing `site.inventory`.
6. Keep p1–p9 on the 06 file; map factory QA into `qa_passed`.

To make `url_planner.py` cover what the factory emits today:

1. Add rows for `/about/`, `/contact/`, and form slugs.
2. Optionally skip 02 when `city_label` is unused (factory’s single-area mode).
3. Still would not render HTML — that stays factory/engine.

---

## 6. Short verdict

`url_planner.py` is the **spec compiler**: 01+02+03+04 → 06. It is the URL source of truth for the spreadsheet / WordPress production pipeline.

This dashboard’s site-config agent is a **demo factory**. `planInventory` is a simplified, pack-based cousin of `url_planner.py` (home + hubs + children, no locations sheet, no 04 keywords). Everything around it (S1 facts, S5–S8 templates, QA, GHL, publish) is extra and does not exist in the planner.

They are not the same Python file and they do not share a sequence except the “emit nested service URLs” idea. Wiring them together means making S4 consume 06 (or the same CSVs), instead of `VERTICAL_PACKS`.
