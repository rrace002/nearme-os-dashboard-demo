#!/usr/bin/env python3
"""Build the private 1Dev preview from inventory.csv. Not a factory runner."""
from __future__ import annotations

import csv
import html
import json
import os
from collections import defaultdict

ROOT = "/workspace/factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01"
INV = os.path.join(ROOT, "inventory.csv")
PREVIEW = os.path.join(ROOT, "preview")
PAGES = os.path.join(PREVIEW, "pages")
os.makedirs(PAGES, exist_ok=True)

BUSINESS = "1Dev Ai Coding Services"
ADDRESS = "12 Sayre St, Elizabeth, NJ 07208"
HOURS = "9 AM – 5 PM"
AREA = "Elizabeth, NJ"
AREA_LONG = "Elizabeth NJ hub; North Jersey hybrid; remote US — cities listed case by case. No LOC doorway pages."
CLAIMS = "1Dev Ai is a consultative application development service. Why rely on a full team, when 1 dev is all you need?"
NOT_FIT = "Not generic AI consulting or offshore body-shop staffing. No location doorway pages. No invented testimonials."
TRADE = "AI-assisted software development / coding services"

DEMO_NOTE = (
    "PRIVATE DEMO — not for publication. Preview routes use slot_id filenames. "
    "That mapping is NOT the approved site URL manifest (url_slug is a leaf only; no url_path)."
)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def load_rows():
    with open(INV, newline="") as fh:
        return list(csv.DictReader(fh))


def by_slot(rows):
    return {r["slot_id"]: r for r in rows}


def children_of(rows, hub_slot):
    return [r for r in rows if r["inferred_parent_slot"] == hub_slot]


def href(slot: str) -> str:
    return f"{slot}.html"


def chrome_nav(rows, current: str | None) -> str:
    hubs = [r for r in rows if r["page_type"] == "SVC-HUB"]
    hub_links = "\n".join(
        f'        <a href="{href(r["slot_id"])}">{esc(r["page_title"])}</a>' for r in hubs
    )
    return f"""<header class="site-header">
  <div class="inner">
    <a class="brand" href="../index.html">
      <strong>{esc(BUSINESS)}</strong>
      <span class="nap">{esc(ADDRESS)} · {esc(HOURS)} · phone omitted (placeholder)</span>
    </a>
    <nav class="primary" aria-label="Preview navigation">
      <a href="../index.html">Preview index</a>
      <details>
        <summary>Services</summary>
        <div>
{hub_links}
        </div>
      </details>
      <a href="{href("com-cat01-hub")}">About</a>
      <a href="{href("ind-cat01-hub")}">Industries</a>
      <a href="{href("com-cat01-form01")}">Contact</a>
    </nav>
  </div>
</header>"""


def visitor_banner() -> str:
    return """<div class="demo-banner" role="status">
  <strong>PRIVATE DEMO / PROVISIONAL / NOT FOR PUBLICATION.</strong>
  Not factory-compliant. Do not deploy.
</div>"""


def review_notes(row: dict, items: list[str]) -> str:
    lis = "\n".join(f"    <li>{item}</li>" for item in items)
    return f"""<details class="review-notes">
  <summary>Review notes (audit evidence — not visitor copy)</summary>
  <div class="review-notes-body">
    <p><strong>Identifiers.</strong> page_key <code>{esc(row["page_key"])}</code> · record {esc(row["record_id"])} · {esc(row["page_type"])} · {esc(row["instruction_ref"])} · approved slug <code>{esc(row["url_slug"])}</code> (leaf, not a path). Preview routes use slot_id filenames and are not the approved URL manifest.</p>
    <ul>
{lis}
    </ul>
  </div>
</details>"""


def banner(row: dict, extra: str) -> str:
    items = [esc(extra)] if extra else []
    return visitor_banner() + "\n" + review_notes(row, items)


def crumbs(row: dict, slots: dict) -> str:
    parts = [f'<a href="../index.html">Preview index</a>']
    parent = row.get("inferred_parent_slot")
    if parent and parent in slots:
        p = slots[parent]
        parts.append(f'<a href="{href(parent)}">{esc(p["page_title"])}</a>')
    parts.append(esc(row["page_title"]))
    return f'<p class="crumbs wrap">{" / ".join(parts)}</p>'


def form_html(default_service: str, hub_titles: list[str]) -> str:
    opts = "\n".join(
        f'      <option{" selected" if t == default_service else ""}>{esc(t)}</option>'
        for t in hub_titles
    )
    return f"""<form class="demo-form" data-demo-form novalidate>
  <p class="form-note"><strong>DEMO ONLY / NOT CONNECTED.</strong> No approved submission endpoint. Phone field omitted (Profile.phone is placeholder 123-456-7890). Privacy page not in inventory — consent is demo-only.</p>
  <label>Name <input name="name" required autocomplete="name"></label>
  <label>Email <input type="email" name="email" required autocomplete="email"></label>
  <label>How can we help?
    <select name="service" required>
{opts}
    </select>
  </label>
  <label>Details <textarea name="details" required minlength="8"></textarea></label>
  <label class="form-note"><input type="checkbox" name="demo_ack" required> I understand this form does not send a message.</label>
  <button class="cta" type="submit">Validate demo form</button>
  <p class="form-ok" data-demo-result hidden></p>
</form>"""


def footer() -> str:
    return f"""<footer class="site-footer">
  <div class="wrap">
    <p>{esc(BUSINESS)} · {esc(ADDRESS)} · {esc(HOURS)}</p>
    <p>Phone omitted. Email not provided.</p>
  </div>
</footer>
<script src="../js/demo-form.js"></script>"""


def page_shell(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | {esc(BUSINESS)} (private demo)</title>
<meta name="description" content="Private labelled demo. Not a factory-compliant build. Not for publication.">
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="../css/site.css">
</head>
<body>
{body}
</body>
</html>
"""


def hub_page(row, rows, slots, hub_titles):
    kids = children_of(rows, row["slot_id"])
    tiles = "\n".join(
        f'    <a class="tile" href="{href(k["slot_id"])}"><strong>{esc(k["page_title"])}</strong><div class="nap">{esc(k["target_keyword"])}</div></a>'
        for k in kids
    )
    kw = row["target_keyword"]
    extra = (
        "Provisional hub from Airtable INS-SVC-HUB sections S0/S1/S2/S4/S6-omit/S7. "
        "Full INS-SVC-HUB.md not in this VM. Hero image collapsed. No tel:."
    )
    notes = [
        esc(extra),
        '<span data-section="INS-SVC-HUB.S0">S0.B1 H1 TIGHT 18/44 (contract vs measured). S0.B2 Content.deck unmapped. S0.B4 Profile.hero_image unmapped — collapsed. Primary tel omitted.</span>',
        '<span data-section="INS-SVC-HUB.S1">S1 Content.intro unmapped. Visitor paragraph is provisional demo copy, not a FACT package list. Writer.</span>',
        '<span data-section="INS-SVC-HUB.S2">S2 Pages.tile_label unmapped. Tiles use preview <code>slot_id</code> filenames, not approved hierarchical paths.</span>',
        '<span data-section="INS-SVC-HUB.S4">S4 Content.cta_head unmapped. No tel:. No book-a-call row in this project’s inventory.</span>',
        '<span data-section="INS-SVC-HUB.S6">S6 omitted from visitor view: Profile.proof_1..4 unmapped. No verified stats. Empty diagnostic-only stat row removed.</span>',
        '<span data-section="INS-SVC-HUB.S7">S7 FAQ.q / FAQ.a unmapped. Not PAA-sourced. Not a FACT FAQ set. Writer.</span>',
        "Privacy / terms pages are not in the 1Dev Site Pages manifest. Operator LLC on Profile is unconfirmed and is not published. Form remains DEMO ONLY / NOT CONNECTED on the page.",
    ]
    body = f"""{visitor_banner()}
{review_notes(row, notes)}
{chrome_nav(rows, row["slot_id"])}
{crumbs(row, slots)}
<main>
<section class="hero wrap" id="S0" data-section="INS-SVC-HUB.S0">
  <div>
    <p class="kicker">Service hub · {esc(kw)}</p>
    <h1>{esc(kw)} in {esc(AREA)}</h1>
    <p><a class="cta" href="#contact-form">Talk through a scoped build</a>
       <a class="cta secondary" href="{href("com-cat01-form01")}">Contact page</a></p>
  </div>
</section>
<section class="section wrap" id="S1" data-section="INS-SVC-HUB.S1">
  <p>This hub is for {esc(kw)}: scoped application work. It is for operators who want a consultative build rather than generic AI consulting or an offshore staffing bench. Exact deliverables belong in a written scope.</p>
</section>
<section class="section wrap" id="S2" data-section="INS-SVC-HUB.S2">
  <h2>Child services</h2>
  <div class="tiles">
{tiles}
  </div>
</section>
<section class="section wrap" id="S4" data-section="INS-SVC-HUB.S4" style="min-height:var(--cta-min-h)">
  <h2>Talk through a scoped build</h2>
  <a class="cta" href="#contact-form">Open demo form</a>
</section>
<section class="section wrap" id="S7" data-section="INS-SVC-HUB.S7">
  <h2>{esc(kw)} questions we hear a lot</h2>
  <dl class="faq">
    <dt>What does {esc(kw)} usually include?</dt>
    <dd>Scoped application work named on this hub and its child pages. Exact deliverables belong in a written scope.</dd>
    <dt>Is this a local Elizabeth, NJ service?</dt>
    <dd>{esc(AREA_LONG)}</dd>
    <dt>Do you publish pricing here?</dt>
    <dd>No. Pricing is omitted because no FACT exists on the Profile.</dd>
    <dt>How do I start?</dt>
    <dd>Use the demo form. It does not send. Live webhook and calendar were skipped at Intake.</dd>
  </dl>
</section>
<section class="section wrap" id="contact-form" data-section="INS-SVC-HUB.A1">
  <h2>On-page contact</h2>
  {form_html(row["page_title"], hub_titles)}
</section>
</main>
{footer()}"""
    return page_shell(row["page_title"], body)


def child_page(row, rows, slots, hub_titles):
    parent = slots.get(row["inferred_parent_slot"])
    kw = row["target_keyword"]
    extra = (
        "Provisional child from INS-SVC-CHILD summary only. No Airtable Sections/Blocks for SVC-CHILD. "
        "Gains/problem cards are argument structure, not FACT offers. FAQ count conflict (summary 4–5 vs INS-FAQ floor 6) unresolved."
    )
    notes = [
        esc(extra),
        "Content.intro unmapped. Hero image none. Phone CTA omitted.",
        "How it works omitted from visitor view: no verified process steps on Profile. section_key null (no child Sections).",
        "Pricing / credentials / ratings omitted from visitor view — no FACT. Writer.",
        "Privacy / terms pages are not in the 1Dev Site Pages manifest. Operator LLC on Profile is unconfirmed and is not published. Form remains DEMO ONLY / NOT CONNECTED on the page.",
    ]
    parent_link = (
        f'<a href="{href(parent["slot_id"])}">{esc(parent["page_title"])}</a>'
        if parent
        else "parent hub"
    )
    body = f"""{visitor_banner()}
{review_notes(row, notes)}
{chrome_nav(rows, row["slot_id"])}
{crumbs(row, slots)}
<main class="prose-page wrap">
<h1>Count on {esc(BUSINESS)} for professional {esc(kw)} in {esc(AREA)}.</h1>
<p>This page is about {esc(kw)}. {esc(CLAIMS)} {esc(NOT_FIT)} Exact deliverables belong in a written scope.</p>
<h2>Gains</h2>
<ul>
  <li>Scope is written before build work starts.</li>
  <li>Consultative application work, not a generic AI-consulting engagement.</li>
  <li>Named topic: {esc(kw)} — not a location doorway page.</li>
  <li>One builder instead of a full-team bench when that is the fit ({esc(CLAIMS)}).</li>
  <li>Remote US only case by case, per Profile service area.</li>
  <li>Not offshore body-shop staffing (Profile not-a-fit).</li>
</ul>
<h2>Problems</h2>
<div class="cards">
  <div class="card"><strong>Unwritten scope</strong><p>Work starts without a written definition of {esc(kw)}.</p></div>
  <div class="card"><strong>Team overhead</strong><p>A full team is retained when one consultative builder would do.</p></div>
  <div class="card"><strong>Fit to operations</strong><p>Software that does not match how the operation actually runs.</p></div>
  <div class="card"><strong>Disconnected systems</strong><p>Tools that do not connect, with no integration plan in the scope.</p></div>
</div>
<h2>Solo vs company</h2>
<p>{esc(CLAIMS)} Competitor names are not on the Profile and are not invented here.</p>
<h2>Questions</h2>
<dl class="faq">
  <dt>What is this page for?</dt>
  <dd>{esc(kw)} as an approved child keyword under {parent_link}.</dd>
  <dt>Will you invent testimonials or ratings?</dt>
  <dd>No. {esc(NOT_FIT)}</dd>
  <dt>Is pricing listed?</dt>
  <dd>No FACT pricing on the Profile.</dd>
  <dt>How do I contact you?</dt>
  <dd>Use the demo form. It does not send. Phone is omitted.</dd>
</dl>
<section class="section" id="contact-form">
  <h2>On-page contact</h2>
  {form_html(parent["page_title"] if parent else row["page_title"], hub_titles)}
</section>
</main>
{footer()}"""
    return page_shell(row["page_title"], body)


def about_page(row, rows, slots, hub_titles):
    extra = "Provisional COMP-HUB. INS-COMP-HUB is not in Instructions; INS-ABOUT is To do. No Sections rows. Uses Profile FACT only."
    notes = [
        esc(extra),
        "Founding story, licensing, insurance, team photos: not on Profile. Not invented. INS-ABOUT not written.",
        "Privacy / terms pages are not in the 1Dev Site Pages manifest. Operator LLC on Profile is unconfirmed and is not published.",
    ]
    kids = children_of(rows, row["slot_id"])
    tiles = "\n".join(
        f'    <a class="tile" href="{href(k["slot_id"])}">{esc(k["page_title"])}</a>' for k in kids
    )
    hubs = [r for r in rows if r["page_type"] == "SVC-HUB"]
    hub_tiles = "\n".join(
        f'    <a class="tile" href="{href(h["slot_id"])}">{esc(h["page_title"])}</a>' for h in hubs
    )
    body = f"""{visitor_banner()}
{review_notes(row, notes)}
{chrome_nav(rows, row["slot_id"])}
{crumbs(row, slots)}
<main class="prose-page wrap">
<h1>About {esc(BUSINESS)}</h1>
<p>{esc(CLAIMS)}</p>
<p>Trade on Profile: {esc(TRADE)}</p>
<p>{esc(AREA_LONG)}</p>
<p>{esc(NOT_FIT)}</p>
<p>Address: {esc(ADDRESS)} · Hours: {esc(HOURS)} · Phone omitted · Email not provided.</p>
<h2>Company pages in this preview</h2>
<div class="tiles">{tiles}
    <a class="tile" href="{href("com-cat01-form01")}">Contact 1Dev</a>
</div>
<h2>Service hubs</h2>
<div class="tiles">{hub_tiles}</div>
</main>
{footer()}"""
    return page_shell(row["page_title"], body)


def why_page(row, rows, slots, hub_titles):
    extra = "Provisional COMP-CHILD. INS-COMP-CHILD not in Instructions. Unique claims only."
    notes = [
        esc(extra),
        "Proof tiles, ratings, years, warranty: not on Profile. Profile.proof_1..4 unmapped. Empty diagnostic-only proof section not shown.",
    ]
    body = f"""{visitor_banner()}
{review_notes(row, notes)}
{chrome_nav(rows, row["slot_id"])}
{crumbs(row, slots)}
<main class="prose-page wrap">
<h1>Why choose 1Dev</h1>
<p>{esc(CLAIMS)}</p>
<p>{esc(NOT_FIT)}</p>
<p><a class="cta" href="{href("com-cat01-form01")}">Contact (demo form)</a></p>
</main>
{footer()}"""
    return page_shell(row["page_title"], body)


def areas_page(row, rows, slots, hub_titles):
    extra = "Provisional COMP-CHILD service-areas. Must not add city doorway pages."
    notes = [
        esc(extra),
        "No city list beyond Profile. Do not stamp LOC doorway pages. Diagnostic-only city-list section not shown.",
    ]
    body = f"""{visitor_banner()}
{review_notes(row, notes)}
{chrome_nav(rows, row["slot_id"])}
{crumbs(row, slots)}
<main class="prose-page wrap">
<h1>Service areas</h1>
<p>{esc(AREA_LONG)}</p>
<p>Address: {esc(ADDRESS)}</p>
</main>
{footer()}"""
    return page_shell(row["page_title"], body)


def contact_page(row, rows, slots, hub_titles):
    extra = (
        "FORM row INS-COMP-CONTACT (Page Slots choice, not in Instructions). "
        "Not INS-CONTACT-PAGE (To do) and not INS-FORMS estimate/book/emergency."
    )
    notes = [
        esc(extra),
        "Phone omitted (Profile.phone is placeholder). No tel: link. Email blank — not invented. Privacy page not in inventory.",
        "DEMO ONLY / NOT CONNECTED form warning remains visible on the visitor form. No approved submission endpoint.",
    ]
    body = f"""{visitor_banner()}
{review_notes(row, notes)}
{chrome_nav(rows, row["slot_id"])}
{crumbs(row, slots)}
<main class="prose-page wrap">
<h1>Contact 1Dev</h1>
<p>Address: {esc(ADDRESS)}</p>
<p>Hours: {esc(HOURS)}</p>
<p>Phone omitted. Email not provided.</p>
{form_html("Custom Software Development", hub_titles)}
</main>
{footer()}"""
    return page_shell(row["page_title"], body)


def ind_hub(row, rows, slots, hub_titles):
    kids = children_of(rows, row["slot_id"])
    tiles = "\n".join(
        f'    <a class="tile" href="{href(k["slot_id"])}"><strong>{esc(k["page_title"])}</strong><div class="nap">{esc(k["target_keyword"])}</div></a>'
        for k in kids
    )
    extra = "Provisional IND-HUB. INS-IND-HUB not in Instructions. No Sections."
    notes = [
        esc(extra),
        "No industry credentials invented. Copy is limited to page title/keyword plus Profile not-a-fit.",
    ]
    body = f"""{visitor_banner()}
{review_notes(row, notes)}
{chrome_nav(rows, row["slot_id"])}
{crumbs(row, slots)}
<main class="prose-page wrap">
<h1>Industries</h1>
<p>Approved industry verticals for this project. Copy is limited to the page title/keyword plus Profile not-a-fit. No industry credentials invented.</p>
<div class="tiles">{tiles}</div>
</main>
{footer()}"""
    return page_shell(row["page_title"], body)


def ind_child(row, rows, slots, hub_titles):
    extra = "Provisional IND-CHILD. INS-IND-CHILD not in Instructions. No vertical credentials on Profile."
    notes = [
        esc(extra),
        "No industry-specific credentials, case studies, or compliance claims are on the Profile, so none are stated on the visitor page.",
    ]
    body = f"""{visitor_banner()}
{review_notes(row, notes)}
{chrome_nav(rows, row["slot_id"])}
{crumbs(row, slots)}
<main class="prose-page wrap">
<h1>{esc(row["page_title"])}</h1>
<p>This preview page exists because the inventory includes the keyword “{esc(row["target_keyword"])}”. {esc(CLAIMS)} No {esc(row["page_title"]).lower()}-specific credentials, case studies, or compliance claims are on the Profile, so none are stated here.</p>
<p><a class="cta" href="{href("com-cat01-form01")}">Contact (demo form)</a>
   <a class="cta secondary" href="{href("ind-cat01-hub")}">All industries</a></p>
</main>
{footer()}"""
    return page_shell(row["page_title"], body)


def index_html(rows, status):
    hubs = [r for r in rows if r["page_type"] == "SVC-HUB"]
    hub_tiles = "\n".join(
        f'    <a class="tile" href="pages/{href(h["slot_id"])}">{esc(h["page_title"])}</a>' for h in hubs
    )
    def rows_html(kind):
        out = []
        for r in rows:
            if status[r["slot_id"]]["preview_class"] != kind:
                continue
            out.append(
                f"<tr><td><a href=\"pages/{href(r['slot_id'])}\">{esc(r['slot_id'])}</a></td>"
                f"<td>{esc(r['page_title'])}</td><td>{esc(r['page_type'])}</td>"
                f"<td>{esc(r['url_slug'])}</td><td>{esc(status[r['slot_id']]['preview_class'])}</td></tr>"
            )
        return "\n".join(out)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PRIVATE PREVIEW INDEX — {esc(BUSINESS)}</title>
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
{visitor_banner()}
<details class="review-notes">
  <summary>Review notes (audit evidence — not visitor copy)</summary>
  <div class="review-notes-body">
    <p><strong>This index is not Home</strong> and is not in the approved Site Pages manifest. There is no HOME row for 1Dev. Internal links use <code>pages/{{slot_id}}.html</code>. Approved <code>url_slug</code> values are leaf slugs only. Trial 1DEV-WEBSITE-TRIAL-20260907-01.</p>
    <p>Deferred (not in manifest): HOME, Privacy, Glossary page, estimate/book-a-call/emergency forms.</p>
  </div>
</details>
<header class="site-header">
  <div class="inner">
    <div class="brand"><strong>{esc(BUSINESS)}</strong><span class="nap">{esc(ADDRESS)} · phone omitted</span></div>
    <nav class="primary">
      <a href="pages/{href("svc-cat01-hub")}">First hub</a>
      <a href="pages/{href("svc-cat01-01")}">First child</a>
      <a href="pages/{href("com-cat01-form01")}">Contact</a>
    </nav>
  </div>
</header>
<main class="wrap prose-page">
<h1>Private website demo</h1>
<p>Runnable preview of the approved 121-page inventory. Start at a hub, follow child tiles, use the contact form (validation only).</p>
<p><span class="badge hub">demo-hub 10</span> <span class="badge child">demo-child-summary 100</span> <span class="badge prov">provisional 11</span></p>
<h2>Service hubs</h2>
<div class="tiles">{hub_tiles}</div>
<h2>Company / industry / contact</h2>
<div class="tiles">
  <a class="tile" href="pages/{href("com-cat01-hub")}">About</a>
  <a class="tile" href="pages/{href("com-cat01-01")}">Why choose 1Dev</a>
  <a class="tile" href="pages/{href("com-cat01-02")}">Service areas</a>
  <a class="tile" href="pages/{href("com-cat01-form01")}">Contact</a>
  <a class="tile" href="pages/{href("ind-cat01-hub")}">Industries</a>
</div>
<details class="review-notes">
  <summary>Preview manifest (121) — audit</summary>
  <div class="review-notes-body">
<table class="status-table">
<thead><tr><th>preview file (slot_id)</th><th>title</th><th>type</th><th>approved url_slug (leaf)</th><th>class</th></tr></thead>
<tbody>
{rows_html("demo-hub")}
{rows_html("demo-child-summary")}
{rows_html("provisional")}
</tbody>
</table>
  </div>
</details>
</main>
<footer class="site-footer"><div class="wrap"><p>Open <a href="demo-url-map.json">demo-url-map.json</a> for preview path vs approved slug.</p></div></footer>
</body>
</html>
"""


def classify(row):
    t = row["page_type"]
    if t == "SVC-HUB":
        return "demo-hub"
    if t == "SVC-CHILD":
        return "demo-child-summary"
    return "provisional"


def main():
    rows = load_rows()
    slots = by_slot(rows)
    hub_titles = [r["page_title"] for r in rows if r["page_type"] == "SVC-HUB"]
    builders = {
        "SVC-HUB": hub_page,
        "SVC-CHILD": child_page,
        "COMP-HUB": about_page,
        "FORM": contact_page,
        "IND-HUB": ind_hub,
        "IND-CHILD": ind_child,
    }
    special = {"com-cat01-01": why_page, "com-cat01-02": areas_page}
    status = {}
    url_map = []
    for r in rows:
        cls = classify(r)
        fn = special.get(r["slot_id"]) or builders[r["page_type"]]
        html_doc = fn(r, rows, slots, hub_titles)
        path = os.path.join(PAGES, f"{r['slot_id']}.html")
        open(path, "w").write(html_doc)
        preview_path = f"pages/{r['slot_id']}.html"
        status[r["slot_id"]] = {
            "preview_class": cls,
            "record_id": r["record_id"],
            "page_key": r["page_key"],
            "page_type": r["page_type"],
            "instruction_ref": r["instruction_ref"],
        }
        url_map.append(
            {
                "page_key": r["page_key"],
                "record_id": r["record_id"],
                "slot_id": r["slot_id"],
                "approved_url_slug_leaf": r["url_slug"],
                "approved_url_path": None,
                "preview_path": preview_path,
                "preview_only": True,
                "note": "preview_path is NOT an approved hierarchical URL",
            }
        )
    open(os.path.join(PREVIEW, "index.html"), "w").write(index_html(rows, status))
    open(os.path.join(PREVIEW, "demo-url-map.json"), "w").write(
        json.dumps(
            {
                "warning": "This file is a preview-only route map. It is not the approved site URL manifest.",
                "approved_url_path_field": None,
                "preview_index": "index.html (NOT HOME; HOME is not in Site Pages)",
                "routes": url_map,
            },
            indent=2,
        )
        + "\n"
    )
    counts = defaultdict(int)
    for v in status.values():
        counts[v["preview_class"]] += 1
    open(os.path.join(PREVIEW, "STATUS.json"), "w").write(
        json.dumps(
            {
                "included_in_preview": 121,
                "by_class": dict(counts),
                "deferred_not_in_manifest": [
                    "HOME /",
                    "INS-PRIVACY /privacy/",
                    "glossary page",
                    "INS-FORMS estimate / book-a-call / emergency",
                ],
                "go_live_blocked": [
                    "placeholder phone",
                    "no GHL endpoint",
                    "no owned images",
                    "INS-TRACKING",
                    "no Privacy page",
                    "no approved url_path",
                    "full INS md not mounted",
                    "this dashboard repo is not production destination",
                ],
            },
            indent=2,
        )
        + "\n"
    )
    print("wrote", len(rows), "pages", dict(counts))


if __name__ == "__main__":
    main()
