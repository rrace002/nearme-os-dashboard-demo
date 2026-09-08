# Downstream correction list — 1DEV-WEBSITE-TRIAL-20260907-01

Compact handoff. Not a new tracker. Demo can run while publication stays blocked.

| page_key / record ID | section_key | issue | evidence | exact fix | role / holder | needs_Rich |
|---|---|---|---|---|---|---|
| all pages · Profile `recWYYESWPIB316ao` | INS-HEADER / S0.B3a / A1 | Placeholder phone; `tel:` omitted in demo | Profile.phone `123-456-7890` | Replace with real number **or** formally omit NAP phone forever | Intake · Rich | **true** — business FACT |
| all pages | S0.B4 | No hero/owned images | Profile.hero_image unmapped; INS-THEME owned-files-only | Collapse (done in demo) or supply owned files at `sites/1dev-ai-coding-services/img/` | Theme Script / Rich for photos | true only to supply photos |
| all chrome | INS-CONTACT / INS-FOOTER | No email | Profile.email blank | Provide or keep omitted | Intake · Rich | **true** for an inbox |
| `1dev-ai-coding-services/com-cat01-form01` `rec9q8rrROQPi8qT4` | A1 | Form not connected | GHL skipped; no endpoint | Keep DEMO ONLY until webhook URL exists | Intake · Rich | true to enable posting; not required for demo |
| (no row) Privacy | null | No privacy page; consent cannot link | INS-PRIVACY To do; no Site Page | Author page + instruction if forms need it | Instruction unassigned; legal copy | **true** for legal text |
| (no row) HOME | null | No `/` page | INS-HOME Done; no Site Page; preview index is **not** Home | Stamp HOME only if 1Dev needs it | Architect Script; IA decision | **true** to decide IA |
| all SVC-CHILD `…/svc-catNN-NN` | null | No child Sections/Blocks | tblstEhFHsgkXLMa7 has 7 hub-only rows | Author child section contracts; do not reuse hub keys | Instruction Engineer **unassigned** (not a Roles row) | false |
| all SVC-HUB e.g. `…/svc-cat01-hub` `rec7fyDPxevfUjMak` | INS-SVC-HUB vs S0–S7 | Summary lists stat tiles / how-it-works / single Book-a-Call; Sections differ; S6 withheld | Instruction `recDWTfnWhujzjw8P` vs 7 Section rows | Resolve in Airtable; do not treat demo layout as the spec | Instruction unassigned | false |
| all SVC-HUB S0.B1 | S0.B1 | H1 TIGHT (18 / measured 44) | Blocks row `recrXok5bFfqqso4B` | Writer fit to budget or change contract | Writer Claude (interim) | false |
| all SVC-CHILD | null | FAQ 4–5 vs INS-FAQ floor 6 | `recpWWV3GQJmXeep5` vs `recSa9sAuVQDhvSgI` | Resolve count; demo uses 4 labelled non-FACT Qs | Instruction / Writer | false |
| all tiles S2 | S2.B2 | Titles exceed 28-char tile cap | Site Pages `page_title`; Pages.tile_label unmapped | Add tile_label field or shorten **labels only** (do not rename page_key) | Architect / Writer | false |
| Content.* / FAQ.q/a / Pages.tile_label | S0.B2 S1 S4 S7 S2 | src_fields have no tables | Orchestrator schema | Map or null+review (demo used null+provisional copy) | Instruction / Architect | false |
| `…/com-cat01-hub` `recdf8kRNn7HcEDLb` | null | INS-COMP-HUB not in Instructions; INS-ABOUT To do | Instructions table | Author About instruction + sections | Instruction unassigned | false |
| `…/com-cat01-form01` | null | FORM vs INS-CONTACT-PAGE vs INS-FORMS | instruction_ref INS-COMP-CONTACT is Page Slots choice only | Do not coerce types; demo is generic contact only | Architect | false |
| `…/ind-*` | null | INS-IND-* not in Instructions | 7 industry rows | Author or accept provisional | Instruction unassigned | false |
| URL manifest | null | No approved hierarchical path | Site Pages has url_slug only; File Registry inventory is 145anydrain | Provide 1Dev path artifact; do not promote `pages/{slot_id}.html` | Keyword / Architect | **true** to approve live paths |
| INS-TRACKING | null | Blocked | Needs Stape + GTM | Supply IDs when in scope | Rich | **true** |
| Operator LLC | INS-FOOTER | Unconfirmed | Profile.operator_model | Confirm or keep omitted (demo omitted) | Rich | **true** |
| Output adapter | 06 Builder | Production path is framework `/sites/{project_tag}/` | This repo is dashboard demo | Copy preview to factory repo when mounted | Builder Script | false |
| C2 log | INS-LOGGING | Airtable Action Log not written | This assignment forbids writes | C2 persist later | C2 Claude (interim) | false |

**Go-live blockers (publication):** B phone, email/privacy/legal, GHL if forms must post, tracking, owned images, url_path approval, factory INS files + Builder output, Rich gates 07/08.

**Cosmetic / content refinements (demo already runs):** tile 28-char labels, H1 TIGHT, FAQ count, hub summary vs 7 sections, child section rows, Content.* unmapped, About/IND instruction prose, 1devai.io DNS.

**Deferred (not in 121-row manifest):** HOME, Privacy, Glossary page, estimate / book-a-call / emergency form variants. Do not claim the site is complete.
