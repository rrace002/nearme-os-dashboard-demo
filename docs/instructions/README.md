# Factory instruction sets

NearMe OS builds are driven by **instruction sets**, not by cloning a live page.

```
design source (URL or HTML)
        │
        ▼
scripts/design_source_to_instructions.py
        │
        ▼
JSON (machine) + Markdown (agent brief)
        │
        ▼
factory / dashboard Generate  →  TEMPLATE pack + chrome remap
```

## Catalog

| Id | Source | Vertical | Notes |
|---|---|---|---|
| [Standard](Standard.md) | factory default | Electrician (or other trade via vertical pack) | Demo-sized 3×3 |
| [PROD-SDTS-V1](PROD-SDTS-V1.md) | [san-diegotechsupport.com](https://san-diegotechsupport.com/) | IT / MSP | Curated Gate 1 10×10. Raw extractor dump in [samples/](samples/PROD-SDTS-V1-EXTRACT.md) |
| [MASTER-IT-V1](MASTER-IT-V1.md) | SDTS IA, factory navy/gold chrome | IT / MSP | Replica template without SDTS NAP |
| [PROD-EES-V1](PROD-EES-V1.md) | [EES staging](https://elizabeth-electrical-services.netlify.app/) | Electrician | 10 service families from the factory home |

`catalog.js` is loaded by the dashboard so Generate / Instructions can apply these sets in the browser.

## Derive a new set

```bash
python3 scripts/design_source_to_instructions.py https://example.com --id SRC-EXAMPLE-V1
```

Or pass a local HTML snapshot:

```bash
python3 scripts/design_source_to_instructions.py ./snapshot.html --id SRC-EXAMPLE-V1
```

The extractor is a first pass. Curate hubs/children and `[confirm]` NAP before using the set on a real factory run.

## Rules every set must carry

- Rebuild from FACTS + TEMPLATE packs — do not republish source body copy.
- Staging banner + `noindex` until go-live.
- `allowIt: true` turns off the factory no-IT validator (required for MSP replicas).
- In-browser demo uses `demoHubs` (3×3). Gate 1 uses full `hubs` (10×10).
