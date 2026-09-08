#!/usr/bin/env python3
"""Working-artifact builder for trial 1DEV-WEBSITE-TRIAL-20260907-01. Not a factory runner."""
from __future__ import annotations

import csv
import html
import json
import os
import re
from collections import Counter
from html.parser import HTMLParser

OUT = "/workspace/factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01"
DRAFTS = os.path.join(OUT, "drafts")
os.makedirs(DRAFTS, exist_ok=True)

START = "2026-09-08T03:44:21Z"
END = "2026-09-08T03:54:00Z"
TRIAL = "1DEV-WEBSITE-TRIAL-20260907-01"
PROJECT = "rec2TGgh9WIfpeL1i"
PROFILE = "recWYYESWPIB316ao"
HUB_REC = "rec7fyDPxevfUjMak"
CHILD_REC = "reccOWSGW38ZxJ9Ya"
CONTACT_REC = "rec9q8rrROQPi8qT4"

F = {
    "page_key": "fldSkPP87mEiTpwCn",
    "page_title": "fld0g2Iufve5hp1Re",
    "url_slug": "fld90aMO13Uf7k30L",
    "instruction_ref": "fldFlCcpe0HC242l1",
    "page_type": "fldMR1ZuG67bgSqG3",
    "target_keyword": "fldRUxBtK83XkyhQb",
    "slot_id": "fldVYBrDgYiobhpny",
    "approval": "fldXGyrnRnW9t78dV",
    "family": "fldhJebV5QtYBsEc5",
    "content": "fldioVUBquCY9Oh8d",
    "sort": "fldvwQV4gGHTs9j2T",
}

INS_IN_TABLE = {
    "INS-THEME",
    "INS-ABOUT",
    "INS-CONTACT-PAGE",
    "INS-FOOTER",
    "INS-SVC-HUB",
    "INS-KEYWORDS",
    "INS-FAQ",
    "INS-LOGGING",
    "INS-HEADER",
    "INS-TRACKING",
    "INS-PRIVACY",
    "INS-SVC-CHILD",
    "INS-HOME",
    "INS-FORMS",
    "INS-GLOSSARY",
    "INS-CONTACT",
    "INS-MENU",
}

UNKNOWN_INS = {
    "INS-COMP-HUB",
    "INS-COMP-CHILD",
    "INS-COMP-CONTACT",
    "INS-IND-HUB",
    "INS-IND-CHILD",
}

BATCH3 = [
    ("recOghkSR7dcq13BN", "1dev-ai-coding-services/svc-cat10-01", "svc-cat10-01", "svc", "SVC-CHILD", 1001, "ai pair programming sessions", "AI Pair Programming Sessions", "ai-pair-programming-sessions", "approved", "todo", "INS-SVC-CHILD"),
    ("recpjCsezMIsomwvn", "1dev-ai-coding-services/svc-cat10-02", "svc-cat10-02", "svc", "SVC-CHILD", 1002, "cursor and copilot workflow training", "Cursor and Copilot Workflow Training", "cursor-and-copilot-workflow-training", "approved", "todo", "INS-SVC-CHILD"),
    ("recGPSTDMt1w7BDVG", "1dev-ai-coding-services/svc-cat10-03", "svc-cat10-03", "svc", "SVC-CHILD", 1003, "team ai coding playbooks", "Team AI Coding Playbooks", "team-ai-coding-playbooks", "approved", "todo", "INS-SVC-CHILD"),
    ("recWDT038MLT1LjVY", "1dev-ai-coding-services/svc-cat10-04", "svc-cat10-04", "svc", "SVC-CHILD", 1004, "prompt engineering for developers", "Prompt Engineering for Developers", "prompt-engineering-for-developers", "approved", "todo", "INS-SVC-CHILD"),
    ("rech0mCCUv9odH8bl", "1dev-ai-coding-services/svc-cat10-05", "svc-cat10-05", "svc", "SVC-CHILD", 1005, "codebase onboarding with ai", "Codebase Onboarding with AI", "codebase-onboarding-with-ai", "approved", "todo", "INS-SVC-CHILD"),
    ("recxP0XNjwevA0DnB", "1dev-ai-coding-services/svc-cat10-06", "svc-cat10-06", "svc", "SVC-CHILD", 1006, "ai-assisted test writing training", "AI-Assisted Test Writing Training", "ai-assisted-test-writing-training", "approved", "todo", "INS-SVC-CHILD"),
    ("recr1Xu6UgN6U1WLC", "1dev-ai-coding-services/svc-cat10-07", "svc-cat10-07", "svc", "SVC-CHILD", 1007, "ai code review coaching", "AI Code Review Coaching", "ai-code-review-coaching", "approved", "todo", "INS-SVC-CHILD"),
    ("rec2QSS2UpOxyY7HX", "1dev-ai-coding-services/svc-cat10-08", "svc-cat10-08", "svc", "SVC-CHILD", 1008, "staff-augmented ai coding sprints", "Staff-Augmented AI Coding Sprints", "staff-augmented-ai-coding-sprints", "approved", "todo", "INS-SVC-CHILD"),
    ("recBOTXW7HqFawaD1", "1dev-ai-coding-services/svc-cat10-09", "svc-cat10-09", "svc", "SVC-CHILD", 1009, "engineering manager ai briefings", "Engineering Manager AI Briefings", "engineering-manager-ai-briefings", "approved", "todo", "INS-SVC-CHILD"),
    ("rec5mmkvHIJgEriO4", "1dev-ai-coding-services/svc-cat10-10", "svc-cat10-10", "svc", "SVC-CHILD", 1010, "safe ai coding policy workshops", "Safe AI Coding Policy Workshops", "safe-ai-coding-policy-workshops", "approved", "todo", "INS-SVC-CHILD"),
    ("recdf8kRNn7HcEDLb", "1dev-ai-coding-services/com-cat01-hub", "com-cat01-hub", "com", "COMP-HUB", 1300, "about 1dev ai coding services", "About 1Dev Ai Coding Services", "about-1dev", "approved", "todo", "INS-COMP-HUB"),
    ("recF9SF6rwziE71P7", "1dev-ai-coding-services/com-cat01-01", "com-cat01-01", "com", "COMP-CHILD", 1301, "why choose 1dev ai coding", "Why Choose 1Dev", "why-choose-us", "approved", "todo", "INS-COMP-CHILD"),
    ("recpP3q6HnAd5gFeT", "1dev-ai-coding-services/com-cat01-02", "com-cat01-02", "com", "COMP-CHILD", 1302, "1dev coding service areas", "Service Areas", "service-areas", "approved", "todo", "INS-COMP-CHILD"),
    ("rec9q8rrROQPi8qT4", "1dev-ai-coding-services/com-cat01-form01", "com-cat01-form01", "com", "FORM", 1390, "contact 1dev ai coding", "Contact 1Dev", "contact", "approved", "todo", "INS-COMP-CONTACT"),
    ("rec3h9LRTRcaK6bYD", "1dev-ai-coding-services/ind-cat01-hub", "ind-cat01-hub", "ind", "IND-HUB", 1400, "ai development by industry", "Industries", "industries", "approved", "todo", "INS-IND-HUB"),
    ("recWZMyNugP4vLVgN", "1dev-ai-coding-services/ind-cat01-01", "ind-cat01-01", "ind", "IND-CHILD", 1401, "ai development for healthcare", "Healthcare", "healthcare", "approved", "todo", "INS-IND-CHILD"),
    ("recFBdFmH8adNdn19", "1dev-ai-coding-services/ind-cat01-02", "ind-cat01-02", "ind", "IND-CHILD", 1402, "ai development for logistics", "Logistics", "logistics", "approved", "todo", "INS-IND-CHILD"),
    ("rec12Ac1T2Mufhf5B", "1dev-ai-coding-services/ind-cat01-03", "ind-cat01-03", "ind", "IND-CHILD", 1403, "ai development for professional services", "Professional Services", "professional-services", "approved", "todo", "INS-IND-CHILD"),
    ("recwmIKtrKg3n8bBs", "1dev-ai-coding-services/ind-cat01-04", "ind-cat01-04", "ind", "IND-CHILD", 1404, "ai development for ecommerce", "Ecommerce", "ecommerce", "approved", "todo", "INS-IND-CHILD"),
    ("rec51pWvIT4tiSdI6", "1dev-ai-coding-services/ind-cat01-05", "ind-cat01-05", "ind", "IND-CHILD", 1405, "ai development for property management", "Property Management", "property-management", "approved", "todo", "INS-IND-CHILD"),
    ("recHVHxzELZRa9FvL", "1dev-ai-coding-services/ind-cat01-06", "ind-cat01-06", "ind", "IND-CHILD", 1406, "ai development for manufacturing", "Manufacturing", "manufacturing", "approved", "todo", "INS-IND-CHILD"),
]


def cell(r, k):
    v = r["cellValuesByFieldId"].get(F[k])
    if isinstance(v, dict):
        return v.get("name")
    return v


def load_pages():
    rows = []
    for path in [
        "/home/ubuntu/.cursor/projects/workspace/agent-tools/07196f33-d017-497e-b27b-a83abb600053.txt",
        "/home/ubuntu/.cursor/projects/workspace/agent-tools/078a8a0f-bb83-40b9-af1a-c6503a195e27.txt",
    ]:
        for rec in json.load(open(path))["records"]:
            rows.append(
                {
                    "record_id": rec["id"],
                    "page_key": cell(rec, "page_key"),
                    "slot_id": cell(rec, "slot_id"),
                    "family": cell(rec, "family"),
                    "page_type": cell(rec, "page_type"),
                    "sort_order": cell(rec, "sort"),
                    "target_keyword": cell(rec, "target_keyword"),
                    "page_title": cell(rec, "page_title"),
                    "url_slug": cell(rec, "url_slug"),
                    "approval_status": cell(rec, "approval"),
                    "content_status": cell(rec, "content"),
                    "instruction_ref": cell(rec, "instruction_ref"),
                }
            )
    keys = {r["page_key"] for r in rows}
    for t in BATCH3:
        rec = {
            "record_id": t[0],
            "page_key": t[1],
            "slot_id": t[2],
            "family": t[3],
            "page_type": t[4],
            "sort_order": t[5],
            "target_keyword": t[6],
            "page_title": t[7],
            "url_slug": t[8],
            "approval_status": t[9],
            "content_status": t[10],
            "instruction_ref": t[11],
        }
        if rec["page_key"] not in keys:
            rows.append(rec)
    rows.sort(key=lambda r: (r["sort_order"] or 0, r["slot_id"]))
    return rows


def classify(row):
    ins = row["instruction_ref"]
    ptype = row["page_type"]
    flags = []
    if ins in UNKNOWN_INS:
        flags.append("instruction_ref_not_in_Instructions_table")
    if ptype in {"IND-HUB", "COMP-HUB"} and ins not in INS_IN_TABLE:
        flags.append("page_type_vocab_from_Page_Slots_not_Instructions")
    if ptype == "FORM" and ins == "INS-COMP-CONTACT":
        flags.append("FORM_is_not_INS-FORMS_and_not_INS-CONTACT-PAGE")
    if not row["url_slug"]:
        flags.append("missing_url_slug")
    # hierarchical path not present
    flags.append("url_slug_is_leaf_not_path")
    parent = None
    m = re.match(r"(svc-cat\d+|com-cat\d+|ind-cat\d+)-(hub|\d+|form\d+)$", row["slot_id"])
    if m:
        parent = f"{m.group(1)}-hub" if m.group(2) != "hub" else ""
        flags.append("parent_inferred_from_slot_id_only")
    coverage = "blocked"
    if ptype == "SVC-HUB":
        coverage = "summary_plus_airtable_sections_labelled_draft"
    elif ptype == "SVC-CHILD":
        coverage = "summary_based_draft_full_compliance_unverified"
    elif ptype == "FORM":
        coverage = "nap_shell_only_phone_omitted"
    else:
        coverage = "blocked_missing_instruction_and_sections"
    return parent, flags, coverage


def write_inventory(rows):
    path = os.path.join(OUT, "inventory.csv")
    fields = [
        "record_id",
        "page_key",
        "slot_id",
        "family",
        "page_type",
        "sort_order",
        "target_keyword",
        "page_title",
        "url_slug",
        "approval_status",
        "content_status",
        "instruction_ref",
        "instruction_in_control_table",
        "inferred_parent_slot",
        "coverage_class",
        "flags",
    ]
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            parent, flags, coverage = classify(r)
            w.writerow(
                {
                    **{k: r[k] for k in [
                        "record_id",
                        "page_key",
                        "slot_id",
                        "family",
                        "page_type",
                        "sort_order",
                        "target_keyword",
                        "page_title",
                        "url_slug",
                        "approval_status",
                        "content_status",
                        "instruction_ref",
                    ]},
                    "instruction_in_control_table": "yes" if r["instruction_ref"] in INS_IN_TABLE else "no",
                    "inferred_parent_slot": parent or "",
                    "coverage_class": coverage,
                    "flags": "|".join(flags),
                }
            )
    return path


TOKENS = {
    "--content-col": "1248px",
    "--page-max": "1440px",
    "--hero-min-h": "480px",
    "--block-pad": "var(--space-7)",
    "--space-7": "64px",
    "--space-5": "32px",
    "--space-4": "24px",
    "--space-3": "16px",
    "--space-2": "8px",
    "--grid-gutter": "24px",
    "--gutter-side": "96px",
    "--radius": "14px",
    "--color-bg": "#ffffff",
    "--color-surface": "#f6f7f9",
    "--color-text": "#161616",
    "--color-divider": "#d7dce2",
    "--color-accent": "#e0241c",
    "--color-accent-ink": "#ffffff",
    "--font-heading": "system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
    "--type-display-l": "42px",
    "--type-display-m": "30px",
    "--type-heading-m": "20px",
    "--type-body-m": "16px",
    "--type-body-s": "14px",
    "--type-label-caps": "12px",
    "--measure-prose": "68ch",
    "--input-h": "48px",
    "--hit-min": "44px",
    "--tile-min-h": "96px",
    "--cta-min-h": "168px",
    "--faq-row-min-h": "72px",
    "--nav-h": "84px",
}


def write_css():
    path = os.path.join(OUT, "tokens-soft.css")
    lines = [
        "/* WORKING ARTIFACT — Tokens.soft_value from appaqwW9su2kPHw8W / tblUwtDpXvcHpIy3M",
        "   NOT generated by theme.py (file not in this VM). Decision E default, not Profile.accent_color.",
        "   --color-accent-ink is a draft alias (not in Tokens table) for contrast on accent fill.",
        ":root {",
    ]
    for k, v in TOKENS.items():
        lines.append(f"  {k}: {v};")
    lines.append("}")
    lines.append(
        """
* { box-sizing: border-box; }
body { margin:0; font-family: var(--font-heading); color: var(--color-text); background: var(--color-bg); font-size: var(--type-body-m); line-height: 1.55; }
.page { max-width: var(--page-max); margin: 0 auto; }
.wrap { max-width: var(--content-col); margin: 0 auto; padding: 0 var(--grid-gutter); }
.draft-banner { background:#111; color:#fff; padding:10px 16px; font-size:13px; }
.draft-banner strong { color:#ffd54a; }
.gap { outline: 2px dashed #e0241c; padding: 8px; }
.muted { color: #5c5c5c; }
.hero { min-height: var(--hero-min-h); display:flex; align-items:center; padding: var(--space-7) 0; }
.hero h1 { font-family: var(--font-heading); font-size: var(--type-display-l); line-height: 1.15; margin:0 0 12px; max-width: var(--measure-prose); }
.kicker { font-size: var(--type-label-caps); letter-spacing:.08em; text-transform:uppercase; color:#5c5c5c; }
.section { padding: var(--space-7) 0; border-top: 1px solid var(--color-divider); }
.section h2 { font-size: var(--type-display-m); margin:0 0 16px; }
.tiles { display:grid; grid-template-columns: repeat(auto-fill, minmax(220px,1fr)); gap: var(--space-5); }
.tile { background: var(--color-surface); border:1px solid var(--color-divider); border-radius: var(--radius); padding:16px; min-height: var(--tile-min-h); text-decoration:none; color:inherit; display:block; }
.cta { background: var(--color-accent); color: var(--color-accent-ink); display:inline-block; padding:12px 20px; min-height: var(--hit-min); border-radius: var(--radius); text-decoration:none; }
.cta[aria-disabled] { opacity:.45; pointer-events:none; }
.faq dt { font-weight:600; margin-top:12px; }
.faq dd { margin:4px 0 0; max-width: var(--measure-prose); }
.omit { background:#fafafa; color: #5c5c5c; font-style:italic; }
.label { font-size:11px; background:#eee; padding:2px 6px; border-radius:4px; margin-right:6px; }
button[disabled] { min-height: var(--input-h); }
"""
    )
    open(path, "w").write("\n".join(lines))
    return path


def esc(s):
    return html.escape(s)


def write_hub(rows):
    children = [r for r in rows if r["slot_id"].startswith("svc-cat01-") and r["page_type"] == "SVC-CHILD"]
    hub = next(r for r in rows if r["record_id"] == HUB_REC)
    h1 = f"{hub['target_keyword']} in Elizabeth, NJ"
    tiles = "\n".join(
        f'    <a class="tile" href="#{esc(c["url_slug"])}" data-url-status="leaf-slug-only"><strong>{esc(c["page_title"])}</strong><div class="muted">{esc(c["target_keyword"])}</div></a>'
        for c in children
    )
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DRAFT (summary + Airtable hub sections) — {esc(hub['page_title'])} | 1Dev Ai Coding Services</title>
<meta name="description" content="Labelled working draft. Not a factory-compliant build. Not for publication.">
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="../tokens-soft.css">
</head>
<body>
<div class="draft-banner">
  <strong>WORKING DRAFT — NOT FACTORY-COMPLIANT.</strong>
  Trial {TRIAL} · page_key {esc(hub['page_key'])} · {HUB_REC} · INS-SVC-HUB recDWTfnWhujzjw8P.
  Source: Airtable Sections/Blocks/Tokens + instruction summary. Full INS-SVC-HUB.md not in this VM.
  CONFLICT (unresolved): INS-SVC-HUB summary H1 = category keyword + location; INS-SVC-CHILD summary uses “Count on {{business}}…”. This hub uses the hub summary, not the child formula.
  S0.B1 fit is TIGHT (budget_min 18 / measured_capacity 44). Phone omitted (placeholder). Hero image collapsed. S6 withheld. Canonical URL path unknown.
</div>
<div class="page">
<header class="wrap" style="padding:16px 24px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--color-divider);min-height:var(--nav-h)">
  <div><strong>1Dev Ai Coding Services</strong><div class="muted">12 Sayre St, Elizabeth, NJ 07208 · 1devai.io (DNS unresolved from this VM)</div></div>
  <nav class="muted">Home / nav: DRAFT-GAP (no HOME Site Page row; url_slug is not a path)</nav>
</header>

<section class="hero wrap" id="S0" data-section="INS-SVC-HUB.S0">
  <div>
    <span class="label">S0.B1 H1</span><span class="label">budget_min 18 · measured_capacity 44 · TIGHT</span>
    <p class="kicker">Service hub · {esc(hub['target_keyword'])}</p>
    <h1>{esc(h1)}</h1>
    <p class="gap">S0.B2 Deck src_field Content.deck → null + review (no Content table in orchestrator). Keywords.primary semantically ≈ Site Pages.target_keyword.</p>
    <p class="gap">S0.B4 Hero image: Profile.hero_image unmapped — on_empty collapse_to_single_column. No owned asset. Do not invent a team/equipment photo.</p>
    <p class="gap">S0.B3a primary action: tel: omitted (placeholder phone). Book-a-call form URL unknown (no form02 row). Secondary optional omitted.</p>
  </div>
</section>

<section class="section wrap" id="S1" data-section="INS-SVC-HUB.S1">
  <span class="label">S1.B1 Prose</span><span class="label">budget 180–520 · measured 340 · TIGHT</span>
  <p>This hub is for custom software development: scoped application work such as business apps, internal tools, and rebuilds. It is written for operators who want a consultative build rather than a generic AI consulting engagement or an offshore staffing bench. Exact deliverables belong in a written scope.</p>
  <p class="gap">Content.intro unmapped → the paragraph above is labelled draft, not a FACT package list. S1 instructions: no heading, no bullets, one paragraph. This draft keeps a single paragraph.</p>
</section>

<section class="section wrap" id="S2" data-section="INS-SVC-HUB.S2">
  <span class="label">S2 Tile grid</span><span class="label">cardinality 6–16 · 10 children</span>
  <h2>Child services</h2>
  <p class="muted">Tiles use live Site Pages titles for this hub. href is the leaf url_slug only — not a hierarchical route. Pages.tile_label unmapped (null + review). Label cap 28 characters is load-bearing; several titles exceed it and are flagged, not renamed.</p>
  <div class="tiles">
{tiles}
  </div>
</section>

<section class="section wrap" id="S4" data-section="INS-SVC-HUB.S4" style="min-height:var(--cta-min-h)">
  <span class="label">S4 CTA band</span>
  <h2>Talk through a scoped build</h2>
  <p class="gap">Content.cta_head / Content.cta_label unmapped. Profile.phone omitted. No tel: link. GHL calendar skipped.</p>
  <a class="cta" href="#contact-form-shell" aria-disabled="true">Contact form (non-posting shell)</a>
</section>

<section class="section wrap omit" id="S6" data-section="INS-SVC-HUB.S6">
  <span class="label">S6 WITHHELD</span>
  Stat row omitted: Sections.S6 / Profile.proof_1..4 unverified and field missing. No verified stats.
</section>

<section class="section wrap" id="A1" data-section="INS-SVC-HUB.A1">
  <span class="label">A1 / INS-CONTACT shell</span>
  <h2>On-page contact (staging shell)</h2>
  <p>GHL webhook skipped per Intake notes — do not POST. Phone field required by INS-CONTACT is omitted here because Profile.phone is a placeholder, not a verified FACT.</p>
  <form id="contact-form-shell" onsubmit="return false;">
    <p><label>Name <input required name="name"></label></p>
    <p><label>Email <input type="email" required name="email"></label></p>
    <p><label>How can we help? <select name="service"><option>Custom software development</option></select></label></p>
    <p><label>Details <textarea name="message" required></textarea></label></p>
    <p class="gap">Consent + privacy link: INS-PRIVACY is To do; no Privacy Site Page.</p>
    <p><button type="submit" disabled>Submit disabled on this draft</button></p>
  </form>
  <p class="muted">Address FACT: 12 Sayre St, Elizabeth, NJ 07208. Hours: 9 AM – 5 PM. Email: blank (do not invent). Phone: omitted.</p>
</section>

<section class="section wrap" id="S7" data-section="INS-SVC-HUB.S7">
  <span class="label">S7 FAQ</span>
  <h2>Custom software development questions we hear a lot</h2>
  <p class="gap">FAQ.q / FAQ.a unmapped. INS-FAQ asks 2+2+2 (floor 6); hub S7 is 4–8; child summary says 4–5. Unresolved. Below is trade-neutral structure copy — not a FACT FAQ set and not PAA-sourced.</p>
  <dl class="faq">
    <dt>What does custom software development usually include?</dt>
    <dd>Scoped application work such as business apps, internal tools, and rebuilds. Exact deliverables belong in a written scope.</dd>
    <dt>Is this a local Elizabeth, NJ service?</dt>
    <dd>Profile lists an Elizabeth, NJ hub with North Jersey hybrid and remote US case by case. This site must not add location doorway pages.</dd>
    <dt>Do you publish pricing here?</dt>
    <dd>Omit pricing unless a verified FACT exists. None is on the Profile.</dd>
    <dt>How do I start?</dt>
    <dd>Use the on-page form shell. Live webhook and calendar were skipped in Stage 01 notes.</dd>
  </dl>
</section>

<footer class="section wrap muted">
  <p>INS-FOOTER requires privacy + terms links — INS-PRIVACY is To do; no Privacy Site Page. Operator “Race Computer Services, LLC” is marked unconfirmed on the Profile — not published as FACT here.</p>
  <p>Schema (Service + ItemList + FAQPage + BreadcrumbList) not emitted: phone/NAP incomplete; no canonical path; not for index.</p>
  <p>© draft only · 1Dev Ai Coding Services · {TRIAL} · do not deploy</p>
</footer>
</div>
</body>
</html>
"""
    path = os.path.join(DRAFTS, "svc-cat01-hub.html")
    open(path, "w").write(html_doc)
    return path, h1, children


def write_child(rows):
    child = next(r for r in rows if r["record_id"] == CHILD_REC)
    area = "Elizabeth, NJ and North Jersey (remote US case by case)"
    h1 = f"Count on 1Dev Ai Coding Services for professional {child['target_keyword']} in {area}."
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DRAFT (INS-SVC-CHILD summary ONLY) — {esc(child['page_title'])} | 1Dev Ai Coding Services</title>
<meta name="description" content="Summary-based labelled draft. No Airtable Sections/Blocks for SVC-CHILD. Not factory-compliant.">
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="../tokens-soft.css">
</head>
<body>
<div class="draft-banner">
  <strong>SUMMARY-BASED DRAFT — FULL COMPLIANCE UNVERIFIED.</strong>
  {CHILD_REC} · {esc(child['page_key'])} · INS-SVC-CHILD recpWWV3GQJmXeep5.
  No Sections/Blocks rows for child pages in tblstEhFHsgkXLMa7. Numeric child budgets = null.
  Do not treat this as satisfying missing full INS-SVC-CHILD.md prose.
  CONFLICT: child summary asks 4–5 FAQs; INS-FAQ floor is 6 (2+2+2). Not silently resolved.
</div>
<div class="page wrap">
<p class="kicker">SVC-CHILD · parent hub slot svc-cat01-hub (inferred from slot_id only; url_slug is not a path)</p>
<h1>{esc(h1)}</h1>
<p class="gap">P1 hero+intro: Content.intro unmapped. Hero image: none. Phone CTA omitted. H1 length exceeds hub S0.B1 measured_capacity 44 (child has no own budget row).</p>
<h2>Gains (structure only — 6–10 bullets required by summary; facts not invented)</h2>
<ul>
  <li>DRAFT-GAP: gain 1 — no verified offer list on Profile</li>
  <li>DRAFT-GAP: gain 2</li>
  <li>DRAFT-GAP: gain 3</li>
  <li>DRAFT-GAP: gain 4</li>
  <li>DRAFT-GAP: gain 5</li>
  <li>DRAFT-GAP: gain 6</li>
</ul>
<h2>Tailor-fit</h2>
<p>Profile unique claims (verbatim): “1Dev Ai is a consultative application development service. Why rely on a full team, when 1 dev is all you need?” Do not add invented differentiators.</p>
<h2>Problems (4 cards) — structure only</h2>
<p class="gap">No problem-card FACT source. Cards not fabricated.</p>
<h2>Solo vs company</h2>
<p>Argument exists in the instruction summary only (red/green comparison). Comparison table not filled with invented competitor claims. No competitors field on Profiles.</p>
<h2>How it works</h2>
<p class="gap">No verified process steps in Profile.</p>
<h2>Best-provider + pricing</h2>
<p class="omit">Pricing omitted — no FACT. Credentials/ratings omitted.</p>
<p>Glossary subset: DRAFT-GAP (no 1Dev glossary page; glossary-map.csv is 145 Any Drain terms on a Windows path).</p>
<p>Why-us tiles: DRAFT-GAP Profile.proof_1..4 unmapped.</p>
<p>On-page contact: non-posting shell; phone omitted; GHL skipped.</p>
<p>FAQs: required by summary; FAQ.q/a unmapped — not invented as FACT. Recurring CTA bands min 4: not rendered as live tel/calendar CTAs.</p>
<p>Schema Service+LocalBusiness+FAQPage+BreadcrumbList: not emitted (incomplete NAP / no canonical path).</p>
</div>
</body>
</html>
"""
    path = os.path.join(DRAFTS, "svc-cat01-01.html")
    open(path, "w").write(html_doc)
    return path, child, h1


def write_contact():
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DRAFT (NAP shell) — Contact 1Dev | 1Dev Ai Coding Services</title>
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="../tokens-soft.css">
</head>
<body>
<div class="draft-banner">
  <strong>NAP SHELL — NOT INS-CONTACT-PAGE and NOT INS-FORMS.</strong>
  {CONTACT_REC} · 1dev-ai-coding-services/com-cat01-form01 · page_type FORM · instruction_ref INS-COMP-CONTACT (not in Instructions table; is a Page Slots choice).
  Dedicated INS-CONTACT-PAGE is To do. INS-FORMS describes estimate/book-a-call/emergency — not this row. Do not coerce.
</div>
<div class="page wrap">
<h1>Contact 1Dev</h1>
<p>Address (Profile FACT): 12 Sayre St, Elizabeth, NJ 07208</p>
<p>Hours (Profile): 9 AM – 5 PM</p>
<p class="gap">Phone: omitted. Profile.phone is 123-456-7890 (placeholder). No tel: link.</p>
<p class="gap">Email: blank. Do not invent an inbox at 1devai.io.</p>
<p>Domain recorded on Profile notes: 1devai.io. This VM could not resolve the hostname (not an HTTP 500 in this run).</p>
<form onsubmit="return false;">
  <p><label>Name <input required name="name"></label></p>
  <p><label>Email <input type="email" required name="email"></label></p>
  <p><label>Details <textarea name="message"></textarea></label></p>
  <p><button disabled>Submit disabled — GHL skipped</button></p>
</form>
</div>
</body>
</html>
"""
    path = os.path.join(DRAFTS, "com-cat01-form01.html")
    open(path, "w").write(html_doc)
    return path


class H1Counter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.text = []
        self._in_h1 = False

    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            self.h1 += 1
            self._in_h1 = True

    def handle_endtag(self, tag):
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data):
        if self._in_h1:
            self.text.append(data)


def verify(rows):
    results = []

    def check(name, ok, detail):
        results.append((name, "PASS" if ok else "FAIL", detail))

    check("inventory_count_121", len(rows) == 121, str(len(rows)))
    check("all_approved", all(r["approval_status"] == "approved" for r in rows), str(Counter(r["approval_status"] for r in rows)))
    check("all_content_todo", all(r["content_status"] == "todo" for r in rows), str(Counter(r["content_status"] for r in rows)))
    check("unique_page_key", len({r["page_key"] for r in rows}) == 121, "")
    check("unique_url_slug", len({r["url_slug"] for r in rows}) == 121, str(Counter(r["url_slug"] for r in rows).most_common(3)))
    types = Counter(r["page_type"] for r in rows)
    check(
        "type_counts",
        types == Counter({"SVC-HUB": 10, "SVC-CHILD": 100, "COMP-HUB": 1, "COMP-CHILD": 2, "FORM": 1, "IND-HUB": 1, "IND-CHILD": 6}),
        str(dict(types)),
    )
    check("no_home_row", not any(r["page_type"] == "HOME" or r["slot_id"] == "home" for r in rows), "")
    check("no_privacy_row", not any("privacy" in (r["url_slug"] or "") for r in rows), "")

    for fname in ["svc-cat01-hub.html", "svc-cat01-01.html", "com-cat01-form01.html"]:
        path = os.path.join(DRAFTS, fname)
        text = open(path).read()
        p = H1Counter()
        p.feed(text)
        check(f"{fname}_one_h1", p.h1 == 1, str(p.h1))
        check(f"{fname}_no_placeholder_tel", "tel:123" not in text and "tel:123-456-7890" not in text, "")
        check(f"{fname}_draft_banner", "DRAFT" in text, "")
        check(f"{fname}_noindex", "noindex" in text, "")
    hub = open(os.path.join(DRAFTS, "svc-cat01-hub.html")).read()
    check("hub_live_record_id", HUB_REC in hub, "")
    check("hub_not_stale_child_titles", "Custom Web App Development" not in hub, "")
    check("hub_live_child_title", "Custom Business Applications" in hub, "")
    check("hub_s6_withheld", "S6 WITHHELD" in hub, "")
    check("hub_h1_not_child_formula", "Count on 1Dev" not in re.search(r"<h1>(.*?)</h1>", hub, re.S).group(1), "")
    child = open(os.path.join(DRAFTS, "svc-cat01-01.html")).read()
    check("child_live_record_id", CHILD_REC in child, "")
    check("child_live_title", "Custom Business Applications" in child, "")

    path = os.path.join(OUT, "VERIFICATION.md")
    lines = ["# Verification — executed locally in this VM", "", "Proposed browser/CDP pass: **not run** (Browser MCP tools unavailable).", ""]
    fails = 0
    for name, status, detail in results:
        if status != "PASS":
            fails += 1
        lines.append(f"- `{name}`: **{status}** {detail}".rstrip())
    lines.append("")
    lines.append(f"Executed checks: {len(results)}. Failures: {fails}.")
    open(path, "w").write("\n".join(lines) + "\n")
    return results, fails


def write_report(rows, verify_fails):
    types = Counter(r["page_type"] for r in rows)
    ins = Counter(r["instruction_ref"] for r in rows)
    path = os.path.join(OUT, "REPORT.md")
    open(path, "w").write(f"""# 1Dev whole-website trial — {TRIAL}

**Result:** A factory-compliant production site **cannot** run from this cloud session. What **can** run now is a labelled, non-compliant working draft for service hubs (Airtable section/block/token contracts + INS-SVC-HUB summary) and a summary-only child outline. This run produced those drafts plus a 121-row inventory and this report under `/workspace/factory-trials/1dev/{TRIAL}/`.

**Decisive remaining dependency:** replace or formally omit Profile.phone `123-456-7890` (business FACT; blocks INS-HEADER `tel:` on every page). In parallel, the local framework instruction files (`INS-SVC-HUB.md` and the rest) are not mounted here, so full numeric section contracts cannot be satisfied.

This assignment **did not** commit, push, write Airtable, flip stages, dispatch Dart/n8n, or deploy.

---

## 1. Environment / access evidence and Stage snapshot

| Item | Evidence |
|---|---|
| Runtime | Cursor Cloud Linux VM (`uname` Linux cursor 6.12.94+ x86_64). Not Windows. |
| Run | [bc-585598ce-ea56-4ca9-aa5f-11f100143409](https://cursor.com/agents/bc-585598ce-ea56-4ca9-aa5f-11f100143409) · model `grok-4.6-high` (not switched) · owner rrace002@gmail.com |
| Repo | `github.com/rrace002/nearme-os-dashboard-demo` @ `/workspace` · branch `main` · `f76a5baedffcfbfd1535f905b1f18718d25ddd6a` · `## main...origin/main` |
| Workspace files | `index.html`, `README.md`, `netlify.toml`, `robots.txt`, `.gitignore`. **Not** the Website factory framework. |
| C:/ and E:/ | Not mounted. Not retried as if they were. |
| Dashboard `index.html` | Unrelated NearMe OS demo cockpit. **Not** used as a factory template. |
| Permitted output | `{OUT}` (untracked; `.gitignore` does not mention it). **No git commit authorized.** |
| Airtable | Orchestrator [appc0ux4lMLH2R6PR](https://airtable.com/appc0ux4lMLH2R6PR) · Control [appaqwW9su2kPHw8W](https://airtable.com/appaqwW9su2kPHw8W) · Page Slots template [appzSnVLfWHvKwtiV](https://airtable.com/appzSnVLfWHvKwtiV) readable |

**Project** [`rec2TGgh9WIfpeL1i`](https://airtable.com/appc0ux4lMLH2R6PR/tbls2Yd480KVT1KiT/rec2TGgh9WIfpeL1i) Name `1Dev Ai Coding Services` · `project_tag` formula `1dev-ai-coding-services` · Status **In progress** · Current stage **04 Theme** (kanban; treat as possibly stale).

**Profile** [`recWYYESWPIB316ao`](https://airtable.com/appc0ux4lMLH2R6PR/tblL8JoM2oeH0jDpH/recWYYESWPIB316ao) Project link **is** `rec2TGgh9WIfpeL1i`. Status Complete does **not** validate every field.

**Stages** (workflow record; `started_at`/`ended_at` blank; `days_open` ≈ 8 is age-since-row-creation, **not** time-in-stage; **1Dev Stage.Role `fldT1a6R7NriHn7ho` empty**):

| Seq | Stage rec | Status | Stage.Owner field | Registry holder (Roles) | Actual 1Dev Action Log actor |
|---|---|---|---|---|---|
| 01 | recMg0nv7mhJPhyhz | Done | Rich | Rich | mixed (intake) |
| 02 | recyv3ptYck9e9SIm | Done (gate) | Rich | Rich | Rich (approval) |
| 03 | recwj3zH9MrBMIDUJ | Done | (blank) | Script | stamp actions |
| 04 | recuiaLZsSpx2VBvP | **Doing (frontier)** | (blank) | Script | **Cursor** (holder-of-record ≠ actor) |
| 05–08 | rec4zVONnoy8iRbm9 … recSkqy0IaMPMNXIK | Not started | 07 Owner=Rich; others blank | 05 Claude (interim); 06/08 Script/Developer | none for 1Dev |

Last 1Dev Action Log: [`recHVwkyXLqLY3dZH`](https://airtable.com/appc0ux4lMLH2R6PR/tblvXqdcAg2YMPkXn/recHVwkyXLqLY3dZH) When `2026-08-31T04:47:00Z` · Actor Cursor · Role 04 Theme · Result OK · “Check Airtable for updated template instruction set”. Theme-proof HTML lives on local Windows; **not artifact-verified here**. Staleness of last **substantive** (non-monitor) progress: that 2026-08-31 theme/instruction check. Time-in-stage **unknown**.

**Known limitation (A) confirmed:** full INS prose is repo-only on `C:\\Users\\Rich\\Documents\\Website factory framework 08-27-26\\`. File Registry paths point there. Absent access is disclosed; Airtable summaries/sections were still read.

**1devai.io:** this VM `Could not resolve host: 1devai.io` (not HTTP 500). Prior snapshot of HTTP 500 is **not reproduced** here; DNS failure is the live observation.

---

## 2. Page inventory / instruction coverage

**Counts (live, paginated via Project.Site Pages IDs; filter-by-Project `hasAnyOf` previously 400'd):** **121** 1Dev pages. Site Pages table total across projects: **186**. Check figures match. Historic 173/181 **not** imposed. Page Slots template describes “1 hub + 10 items + 2 forms” per category; **1Dev does not follow that form count**.

All 121: `approval_status=approved`, `content_status=todo`. No excluded/blocked rows. Unapproved: **0**.

| page_type | n | instruction_ref | In Instructions table? | Sections rows | Coverage class |
|---|---|---|---|---|---|
| SVC-HUB | {types['SVC-HUB']} | INS-SVC-HUB | Yes (Done) | 7 (S0,S1,S2,S4,A1,S6,S7) | Labelled hub draft possible; full INS.md unverified |
| SVC-CHILD | {types['SVC-CHILD']} | INS-SVC-CHILD | Yes (Done) | **0** | Summary-based draft only |
| COMP-HUB | {types['COMP-HUB']} | INS-COMP-HUB | **No** (INS-ABOUT = To do) | 0 | Blocked |
| COMP-CHILD | {types['COMP-CHILD']} | INS-COMP-CHILD | **No** | 0 | Blocked |
| FORM | {types['FORM']} | INS-COMP-CONTACT | **No** (Page Slots choice; INS-CONTACT-PAGE To do; INS-CONTACT is a **block**; INS-FORMS is estimate/book/emergency) | 0 | NAP shell only |
| IND-HUB | {types['IND-HUB']} | INS-IND-HUB | **No** | 0 | Blocked |
| IND-CHILD | {types['IND-CHILD']} | INS-IND-CHILD | **No** | 0 | Blocked |
| HOME | 0 | INS-HOME Done as instruction | 0 | Inventory gap (Page Slots page_type enum also has **no HOME**) |
| Privacy | 0 | INS-PRIVACY To do | 0 | Missing; project-specific if required |
| Glossary page | 0 | INS-GLOSSARY Done as **block** | 0 | Optional; not in 1Dev inventory |
| plat family | 0 | INS-PLAT-* in Page Slots only | 0 | Not in 1Dev inventory |

`instruction_ref` frequencies: {dict(ins)}

**Instructions live (17):** 13 Done; 3 To do (**INS-ABOUT, INS-CONTACT-PAGE, INS-PRIVACY**); 1 Blocked (**INS-TRACKING** — Stape/GTM from Rich). Matches Claude snapshot D.

**INS-SVC-CHILD** [`recpWWV3GQJmXeep5`](https://airtable.com/appaqwW9su2kPHw8W/tblPva1eNRowILnYT/recpWWV3GQJmXeep5) actual wording:

> Child service page (/{{category}}/{{service}}/). One H1: 'Count on {{business}} for professional {{keyword}} in {{service_area}}'. P1–P6 argument: hero+intro, gains (6–10 bullets), tailor-fit, problems (4 cards), solo-vs-company comparison (red/green), how-it-works steps, best-provider + pricing (omit if no FACT). Plus glossary subset, why-us tiles (late), on-page contact form, 4–5 keyword FAQs, recurring CTA bands (min 4: hero Book-a-Call, Emergency, Estimate, closing all three). Schema: Service + LocalBusiness + FAQPage + BreadcrumbList. Owned images; trade-neutral; no invented facts.

Sufficient to assess specified shape and produce a labelled summary draft. **Not** proof that missing full prose and numeric section contracts were satisfied.

**INS-SVC-HUB** summary (different from child; **do not merge**): One H1 = category keyword + location. Sections listed: hero (single Book a Call), stat tiles, category overview card, 6 primary + 4 more services, how-it-works, FAQ 5–6, glossary subset, contact form, closing CTA, areas, footer. Schema Service + ItemList + BreadcrumbList + FAQPage.

**Unresolved conflict with the 7 Section rows:** Airtable sections are S0 Hero (primary **plus optional secondary**, not “single Book a Call”), S1 intro (no heading), S2 tiles 6–16, S4 one CTA band, A1 component, **S6 withheld**, S7 FAQ 4–8. Hub summary still mentions stat tiles and how-it-works that have **no Section row**. Not silently resolved.

**src_fields → null + review (no coerce):** `Content.intro`, `Content.deck`, `Content.cta_head`, `Content.cta_label`, `FAQ.q`, `FAQ.a`, `Pages.tile_label`, `Profile.hero_image`, `Profile.proof_1..4`, `Profile.accent_color`. Semantic only: `Keywords.primary` ≈ `Site Pages.target_keyword`; `Profile.phone` exists but is placeholder.

**Blocks:** 25, all linked to those hub sections. S0.B1 H1 **TIGHT** (min 18 / measured 44). S1.B1 TIGHT. S7.B2e2 TIGHT.

**Tokens:** 53 rows. `soft_value` = Decision E. `--content-col` 1248px, `--page-max` 1440px, `--hero-min-h` 480px, `--radius` 14px, `--color-accent` `#e0241c`. `theme.py` / `tokens.css` not in this workspace.

**URLs:** `url_slug` is a leaf. Site Pages has **no** `url_path`. File Registry `url-structure-inventory.csv` is **145anydrain**, not 1Dev. Parent/child inferred from `slot_id` pattern only — flagged, not fabricated as routes. No slug collisions inside the 121. `page_key` = `{{project_tag}}/{{slot_id}}` preserved.

**New vs prior snapshot:** cat01 children are **not** “Custom Web App Development / Internal Tools and Dashboards / …”. Live cat01-01 is **Custom Business Applications** (`custom-business-applications`), then Desktop Application Development, Internal Tools and Admin Panels, SaaS Product Development, Legacy System Replacement, etc. Prior draft titles were stale and were corrected.

**Keyword/title:** present on all 121; generally aligned to slug. Tile labels >28 chars exist (S2 hard cap) — flagged, not renamed.

---

## 3. Completed artifacts and verification

Produced (working artifacts, not durable factory receipts):

| Path | What |
|---|---|
| `{OUT}/REPORT.md` | This assessment |
| `{OUT}/RUNTIME-LOG.md` | Per-task log |
| `{OUT}/inventory.csv` | All 121 pages |
| `{OUT}/tokens-soft.css` | Tokens.soft_value subset; not theme.py output |
| `{OUT}/drafts/svc-cat01-hub.html` | Labelled hub draft S0/S1/S2/S4/S6-omit/A1/S7 |
| `{OUT}/drafts/svc-cat01-01.html` | Child summary-only skeleton |
| `{OUT}/drafts/com-cat01-form01.html` | Contact NAP shell; phone omitted |
| `{OUT}/VERIFICATION.md` | Executed local checks |

**Not claimed:** factory-compliant build, publication, schema emission, GHL POST, theme lock, or Stage 04 Done.

**Tests:** HTML parse / one H1 / no placeholder `tel:` / live record IDs / live child titles / S6 withheld — see VERIFICATION.md. Failures in that file: {verify_fails}. Browser/CDP: **not executed**.

---

## 4. Consolidated blockers

| ID | Page/task | Stage | Evidence | Holder (registry) / actual | Remedy | needs_Rich |
|---|---|---|---|---|---|---|
| B1 | Every page NAP `tel:` | 01 facts still affect 04+ | Profile.phone `123-456-7890`; INS-HEADER requires character-exact FACT | Intake holder Rich | Replace with real number **or** formally omit phone from chrome | **true** — business FACT |
| B2 | Full INS prose / theme.py | 04 Theme | File Registry Windows paths; not mounted | C3 Infrastructure (Developer) can place files; Rich owns the PC | Provide `INS-SVC-HUB.md`, `INS-SVC-CHILD.md`, `INS-HOME.md`, `INS-HEADER.md`, `INS-FOOTER.md`, `INS-MENU.md`, `INS-CONTACT.md`, `INS-FAQ.md`, `theme.py` from `C:\\Users\\Rich\\Documents\\Website factory framework 08-27-26\\` | true only if a human must copy from the PC; implementation is not automatically Rich |
| B3 | SVC-CHILD / HOME / FORM / COMP / IND sections | 04–05 | Exactly 7 Sections, all `page_type=INS-SVC-HUB` | **Instruction Engineer is not a Roles row** (unassigned) | Author Section/Block rows per page type; do not reuse hub keys | false |
| B4 | INS-COMP-HUB vs INS-ABOUT | 03/05 | Inventory `INS-COMP-HUB`; Instructions has INS-ABOUT To do | Architect Script / Writer | Map or author; do not guess | false |
| B5 | HOME missing | 03 Architect notes stale vs later stamps | INS-HOME Done; no Site Page; Page Slots has no HOME type | Architect | If 1Dev needs `/`, stamp a HOME row after Rich confirms it is in scope | **true** if deciding the IA; false to investigate |
| B6 | Dedicated Contact vs FORM | 03 | FORM `contact` + INS-COMP-CONTACT vs INS-CONTACT-PAGE To do | Architect / Instruction | Do not treat them as the same page type | false |
| B7 | Privacy | — | INS-PRIVACY To do; no row | — | Author only if 1Dev requires it (forms/consent) | **true** for legal copy |
| B8 | INS-TRACKING | later | Blocked; needs Stape + GTM | Rich | Supply IDs when tracking is in scope | **true** |
| B9 | GHL forms | 01 skipped | Delivery notes: webhook/calendar skipped | Rich | Optional; shells stay non-posting until then | true to enable posting; not blocking labelled drafts |
| B10 | Email / operator LLC | 01 | Email blank; operator unconfirmed | Rich | Provide or keep omitted | **true** for those fields |
| B11 | Owned images | 04 | No Profile.hero_image; INS-THEME owned-files-only | Theme Script / Rich for photos | Collapse empty slots; do not hotlink | true for supplying photos |
| B12 | Output adapter `/sites/{{project_tag}}/` | 06 | Builder target is framework-local, not this dashboard repo | Builder Script | Do not write production into this repo | false |
| B13 | Canonical URL map | 02/03 | No 1Dev url-structure-inventory in File Registry | Keyword/Architect | Provide approved path artifact; do not invent `/${{hub}}/{{child}}` from slugs | false to hunt; **true** to approve paths |
| B14 | Gate/publication | 02 already Done; 07/08 not started | This trial must not clear gates | Rich for gates | Do not flip Status | n/a |
| B15 | 1Dev Stage.Role empty | routing | `fldT1a6R7NriHn7ho` blank on all 8 | Dispatcher | Join missing; this trial does not appoint holders | false |
| B16 | Hub summary vs 7 sections | 04 | Stat tiles / how-it-works in summary; S6 withheld in Sections | Instruction | Resolve conflict in Airtable; do not pick silently | false |
| B17 | H1 budget TIGHT vs child formula | 04/05 | S0.B1 measured 44 vs long child H1 | Writer | Do not claim fit | false |
| B18 | Airtable Action Log write | logging | INS-LOGGING requires cloud log; this assignment forbids writes | C2 Scribe (Claude interim) | Parent may persist later | false for this agent |

Business questionnaire: Intake notes say Profile drafted from **old questionnaire**. Profiles table **is** the currently authorized store (questionnaire answers). It is **not** silently promoted to a future master store. No 15-question definition found. Delivery notes are the owner FACT dump dated 2026-08-30. Competitors/partners/offers/social/ratings: **absent**. Unknown remains unknown.

---

## 5. Runtime log and persistence status

See `{OUT}/RUNTIME-LOG.md`.

| Persistence | Status |
|---|---|
| Working log saved + read-back | **Yes** — `{OUT}/RUNTIME-LOG.md` |
| Durable Airtable Action Log / C2 receipt | **Pending** — writes unauthorized. No new `rec*` for this trial. |
| Git commit / PR | **Not performed** (assignment forbids) |
| Factory run fully logged? | **No.** Chat + VM files only until C2/parent persists. |

Actor of this run: Cursor Cloud agent `bc-585598ce-ea56-4ca9-aa5f-11f100143409`. Registry Theme holder: **Script**. cost_usd: **null**. runtime_sec: **unknown**.

---

## 6. Highest-priority next action

**Owner: Rich.** Replace or formally omit Profile.phone `123-456-7890` on [`recWYYESWPIB316ao`](https://airtable.com/appc0ux4lMLH2R6PR/tblL8JoM2oeH0jDpH/recWYYESWPIB316ao).

**Why first:** it is a business FACT already on the authorized Profile; INS-HEADER/FOOTER/CONTACT require character-exact NAP; a placeholder must not be published; every page’s chrome is blocked until this is decided. File/row investigation and labelled drafts were done in this run and do not wait on him.

After that (not Rich unless he is the only person with the PC): mount or copy the File Registry instruction files into a reachable workspace so Stage 04/05 can leave summary-based drafts.
""")
    return path


def write_log(rows):
    path = os.path.join(OUT, "RUNTIME-LOG.md")
    open(path, "w").write(f"""# Runtime log — {TRIAL}

Working artifact only. Not a durable Airtable receipt. Append-only for this VM folder.

| when (UTC) | actor (actual) | role (registry) | action | input → output | result | missing |
|---|---|---|---|---|---|---|
| {START} | Cursor Cloud bc-585598ce-ea56-4ca9-aa5f-11f100143409 · grok-4.6-high | 04 Theme holder=Script (not this actor) | Start whole-website trial | assignment {TRIAL} · project {PROJECT} | OK | — |
| {START}–{END} | Cursor | (read-only) | Read Orchestrator + Control + Page Slots schema/rows | bases appc0ux4lMLH2R6PR, appaqwW9su2kPHw8W, appzSnVLfWHvKwtiV → live IDs | OK | Stage.Role empty on 1Dev |
| {START}–{END} | Cursor | (read-only) | Enumerate Site Pages | Project.Site Pages 121 IDs in 3 batches; table total 186 | OK | no url_path field |
| {START}–{END} | Cursor | (read-only) | Instructions/Sections/Blocks/Tokens/File Registry | 17 / 7 / 25 / 53 | OK | INS md files on C:\\ |
| {END} | Cursor | (local files only) | Write labelled drafts + inventory + report | {OUT} | OK | factory output adapter |
| {END} | Cursor | (local tests) | Parse HTML, inventory counts, no placeholder tel | VERIFICATION.md | OK if 0 FAIL | Browser MCP unavailable |
| {END} | Cursor | C2 Scribe holder=Claude (interim) | Airtable Action Log write | would log this trial | **BLOCKED** | assignment forbids Airtable writes |

**phase/stage:** 04 Theme / Designer `recuiaLZsSpx2VBvP` Doing.  
**cost_usd:** null. **started_at/ended_at (Airtable):** not written. **task_id:** {TRIAL}.  
**tests actually run:** local HTML/inventory assertions. **tests proposed not run:** browser visual, theme.py, factory linter, GHL POST.

**Read-back:** this file exists at `{path}`.
""")
    return path


def main():
    rows = load_pages()
    assert len(rows) == 121, len(rows)
    inv = write_inventory(rows)
    css = write_css()
    hub_path, h1, children = write_hub(rows)
    child_path, child, ch1 = write_child(rows)
    contact = write_contact()
    results, fails = verify(rows)
    report = write_report(rows, fails)
    log = write_log(rows)
    print("rows", len(rows))
    print("hub h1", h1, "chars", len(h1))
    print("child", child["page_title"], child["record_id"])
    print("children", len(children))
    print("verify fails", fails)
    for name, status, detail in results:
        if status != "PASS":
            print("FAIL", name, detail)
    print("wrote", inv, css, hub_path, child_path, contact, report, log)


if __name__ == "__main__":
    main()
