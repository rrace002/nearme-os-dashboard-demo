#!/usr/bin/env python3
"""Convert a live design source (URL or HTML file) into a factory instruction set.

NearMe OS factory builds are driven by named instruction sets (PROD-SDTS-V1,
MASTER-IT-V1, Standard). This script is the source → instructions pass:

  1. Fetch / read the design source HTML
  2. Extract NAP-like facts, chrome tokens, nav, headings, forms
  3. Emit JSON (machine) + Markdown (agent / factory brief)

Usage:
  python3 scripts/design_source_to_instructions.py https://example.com --id MY-SET-V1
  python3 scripts/design_source_to_instructions.py ./snapshot.html --id MY-SET-V1 --out docs/instructions
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs" / "instructions"

PHONE_RE = re.compile(
    r"(?:\+1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}"
)
EMAIL_RE = re.compile(r"[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}", re.I)
HEX_RE = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b")
SKIP_HREF = re.compile(
    r"^(#|javascript:|mailto:|tel:|sms:)", re.I
)
SKIP_LABEL = re.compile(
    r"^(home|search|find now|submit|learn more|read more|click here|"
    r"facebook-?f?|twitter|youtube|linkedin|telegram|whatsapp|instagram|"
    r"thank you for your inquiry!?)$",
    re.I,
)
NOISE_HEX = {
    "#fff", "#ffffff", "#000", "#000000", "#eee", "#eeeeee",
    "#ccc", "#cccccc", "#ddd", "#dddddd", "#333", "#333333",
    "#111", "#111111", "#222", "#222222", "#444", "#444444",
    "#f3f2f2", "#201e1d",
}


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return slug or "item"


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def expand_hex(value: str) -> str:
    raw = value.lower()
    if len(raw) == 4:
        return "#" + "".join(ch * 2 for ch in raw[1:])
    return raw


class SourceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._skip = False
        self._tag_stack: list[str] = []
        self._capture_title = False
        self._capture_heading = False
        self._heading_buf: list[str] = []
        self._link_href: str | None = None
        self._link_buf: list[str] = []
        self.title = ""
        self.meta_description = ""
        self.headings: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.texts: list[str] = []
        self.form_fields: list[str] = []
        self.select_options: list[str] = []
        self.styles: list[str] = []
        self.inline_styles: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k.lower(): (v or "") for k, v in attrs}
        self._tag_stack.append(tag)
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip = True
        if tag == "style":
            self._skip = False  # capture CSS text, skip later via _in_style
        if tag == "meta":
            name = (ad.get("name") or ad.get("property") or "").lower()
            if name in {"description", "og:description"} and not self.meta_description:
                self.meta_description = collapse(ad.get("content", ""))
        if tag == "title":
            self._capture_title = True
        if tag in {"h1", "h2", "h3"}:
            self._capture_heading = True
            self._heading_buf = []
        if tag == "a":
            self._link_href = ad.get("href") or ""
            self._link_buf = []
        if tag in {"input", "textarea", "select"}:
            label = ad.get("name") or ad.get("placeholder") or ad.get("aria-label") or ad.get("id")
            if label:
                self.form_fields.append(collapse(label))
        if tag == "option" and ad.get("value"):
            self.select_options.append(collapse(ad.get("value") or ""))
        if ad.get("style"):
            self.inline_styles.append(ad["style"])

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip = False
        if tag == "title":
            self._capture_title = False
        if tag in {"h1", "h2", "h3"}:
            heading = collapse("".join(self._heading_buf))
            if heading:
                self.headings.append(heading)
            self._capture_heading = False
            self._heading_buf = []
        if tag == "a":
            label = collapse("".join(self._link_buf))
            href = self._link_href or ""
            if label and href and not SKIP_HREF.match(href) and not SKIP_LABEL.match(label):
                self.links.append((label, href))
            self._link_href = None
            self._link_buf = []
        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()
        elif tag in self._tag_stack:
            self._tag_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._tag_stack and self._tag_stack[-1] == "style":
            self.styles.append(data)
            return
        if self._skip:
            return
        text = collapse(data)
        if not text:
            return
        if self._capture_title:
            self.title = collapse((self.title + " " + text).strip())
        if self._capture_heading:
            self._heading_buf.append(text)
        if self._link_href is not None:
            self._link_buf.append(text)
        if len(text) > 2:
            self.texts.append(text)


def fetch_html(source: str, timeout: int = 25) -> tuple[str, str]:
    path = Path(source)
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace"), source
    url = source if "://" in source else "https://" + source
    req = Request(url, headers={"User-Agent": "NearMeOS-instruction-extractor/1.0"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            html = resp.read().decode(charset, errors="replace")
            final = resp.geturl() or url
            return html, final
    except (HTTPError, URLError, TimeoutError) as exc:
        raise SystemExit(f"Failed to fetch {url}: {exc}") from exc


def extract_phones(text: str) -> list[str]:
    found = []
    for match in PHONE_RE.findall(text):
        cleaned = collapse(match)
        if cleaned not in found and not cleaned.startswith("20"):
            found.append(cleaned)
    return found[:6]


def extract_emails(text: str) -> list[str]:
    found = []
    for match in EMAIL_RE.findall(text):
        low = match.lower()
        if low.endswith((".png", ".jpg", ".gif", ".webp", ".svg")):
            continue
        if low not in found:
            found.append(low)
    return found[:6]


def extract_colors(parser: SourceParser) -> list[str]:
    blob = "\n".join(parser.styles + parser.inline_styles)
    counts: Counter[str] = Counter()
    for raw in HEX_RE.findall(blob):
        hexv = expand_hex(raw)
        if hexv in NOISE_HEX:
            continue
        counts[hexv] += 1
    return [color for color, _ in counts.most_common(8)]


def unique_keep_order(items: list[str], limit: int | None = None) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        key = collapse(item)
        low = key.lower()
        if not key or low in seen or SKIP_LABEL.match(key):
            continue
        seen.add(low)
        out.append(key)
        if limit and len(out) >= limit:
            break
    return out


def cluster_hubs(labels: list[str], children_hint: list[str]) -> list[dict[str, Any]]:
    hubs: list[dict[str, Any]] = []
    used_children: set[str] = set()
    for label in labels[:10]:
        slug = slugify(label)
        kids = []
        for child in children_hint:
            if child.lower() == label.lower() or child.lower() in used_children:
                continue
            if label.lower().split()[0] in child.lower() or len(kids) < 3:
                if len(kids) >= 10:
                    break
                # Prefer children that share a token with the hub, else fill later.
                hub_tokens = set(re.findall(r"[a-z]{4,}", label.lower()))
                child_tokens = set(re.findall(r"[a-z]{4,}", child.lower()))
                if hub_tokens & child_tokens or not kids:
                    kids.append(child)
                    used_children.add(child.lower())
        while len(kids) < 3:
            filler = f"{label} — option {len(kids) + 1}"
            kids.append(filler)
        hubs.append({
            "title": label,
            "slug": slug,
            "blurb": f"Service family taken from the design source nav/headings ({label}).",
            "children": kids[:10],
        })
    return hubs


def default_chrome(colors: list[str]) -> dict[str, str]:
    navy = colors[0] if colors else "#12314e"
    gold = colors[1] if len(colors) > 1 else "#f5a800"
    link = colors[2] if len(colors) > 2 else "#0b5394"
    return {
        "ink": "#1c2733",
        "navy": navy,
        "navyDeep": "#0b2338",
        "gold": gold,
        "goldSoft": "#ffd35c",
        "link": link,
        "tint": "#f4f7fa",
        "fontBody": "Georgia, 'Times New Roman', serif",
        "fontUi": "'Segoe UI', Arial, Helvetica, sans-serif",
    }


def looks_like_it(text: str) -> bool:
    return bool(re.search(
        r"\b(managed it|cybersecurity|msp|vcio|microsoft 365|office 365|cloud services|it support)\b",
        text,
        re.I,
    ))


def instruction_id_for(source_url: str, explicit: str | None) -> str:
    if explicit:
        return explicit.strip().upper().replace(" ", "-")
    host = urlparse(source_url).netloc.replace("www.", "")
    if "san-diegotechsupport" in host or "sandiegotechsupport" in host:
        return "PROD-SDTS-V1"
    if "elizabethelectrical" in host:
        return "PROD-EES-V1"
    if "cryptocurrencyconsulting" in host:
        return "PROD-CRYPTO-V1"
    slug = slugify(host.split(".")[0] or "source")
    return f"SRC-{slug.upper()}-V1"


def build_instruction(html: str, source_url: str, set_id: str) -> dict[str, Any]:
    parser = SourceParser()
    parser.feed(html)
    blob = " ".join(parser.texts)
    phones = extract_phones(blob + " " + html)
    emails = extract_emails(html)
    colors = extract_colors(parser)
    nav_labels = unique_keep_order(
        [label for label, href in parser.links if not re.search(r"facebook|twitter|youtube|linkedin|instagram|whatsapp|telegram", href, re.I)],
        24,
    )
    headings = unique_keep_order(parser.headings, 20)
    form_options = unique_keep_order(
        [opt for opt in parser.select_options if len(opt) > 2 and opt.lower() not in {"select", "select a service"}],
        20,
    )
    service_labels = unique_keep_order(form_options + headings + nav_labels, 16)
    hubs = cluster_hubs(service_labels[:10] or ["Services"], service_labels[10:] or service_labels)
    allow_it = looks_like_it(blob + " " + parser.title)
    title = parser.title or urlparse(source_url).netloc or set_id
    name_guess = re.split(r"[|–—-]", title)[0].strip() or title
    chrome = default_chrome(colors)
    demo_hubs = []
    for hub in hubs[:3]:
        demo_hubs.append({
            "title": hub["title"],
            "slug": hub["slug"],
            "children": hub["children"][:3],
        })
    forms = [
        {"title": "Request a Quote", "slug": "request-a-quote", "role": "FORM-PRICING"},
        {"title": "Request a Consultation", "slug": "request-a-consultation", "role": "FORM-SERVICE-REQ"},
    ]
    return {
        "id": set_id,
        "name": set_id,
        "source": {
            "url": source_url,
            "fetched": date.today().isoformat(),
            "kind": "live-site" if source_url.startswith("http") else "html-file",
            "title": title,
            "description": parser.meta_description,
        },
        "vertical": "IT / MSP" if allow_it else "Local services",
        "allowIt": allow_it,
        "noun": "IT support partner" if allow_it else "local service company",
        "businessName": name_guess,
        "nap": {
            "name": name_guess,
            "phone": phones[0] if phones else "",
            "email": emails[0] if emails else "",
            "address": "",
            "city": "",
            "confirm": True,
        },
        "valueProposition": parser.meta_description or (headings[1] if len(headings) > 1 else headings[0] if headings else ""),
        "chrome": chrome,
        "extractedColors": colors,
        "nav": nav_labels[:16],
        "headings": headings[:16],
        "formFields": unique_keep_order(parser.form_fields, 12),
        "serviceHints": service_labels,
        "forms": forms,
        "gate1": {"hubs": 10, "childrenPerHub": 10, "targetPages": 117},
        "hubs": hubs,
        "demoHubs": demo_hubs,
        "rules": [
            "Treat extracted NAP, testimonials, and prices as [confirm] until an owner verifies them.",
            "Do not copy competitor body copy verbatim — rebuild from FACTS + TEMPLATE packs.",
            "Preserve information architecture (hubs, children, forms, company pages) from this instruction set.",
            "Staging builds get a STAGING PREVIEW banner and noindex.",
            "Factory TEMPLATE pass is AI-off; owner review replaces placeholder copy at rollout.",
            "Skip the no-IT validator when allowIt is true.",
        ],
    }


def render_markdown(instr: dict[str, Any]) -> str:
    src = instr["source"]
    nap = instr["nap"]
    chrome = instr["chrome"]
    hubs = instr.get("hubs") or []
    demo = instr.get("demoHubs") or []
    lines = [
        f"# {instr['id']} — factory instruction set",
        "",
        "Generated by `scripts/design_source_to_instructions.py`.",
        "",
        "## Source",
        "",
        f"- **URL:** {src.get('url', '')}",
        f"- **Fetched:** {src.get('fetched', '')}",
        f"- **Kind:** {src.get('kind', '')}",
        f"- **Page title:** {src.get('title', '')}",
        "",
        "## Use this set when",
        "",
        f"Rebuilding a site that should inherit the **{instr.get('vertical', 'local services')}** "
        f"information architecture and chrome of the design source — not a pixel clone of the live copy.",
        "",
        "## Facts (NAP / identity)",
        "",
        "| Field | Value | Notes |",
        "|---|---|---|",
        f"| business_name | {nap.get('name', '')} | from title |",
        f"| phone | {nap.get('phone', '') or '—'} | {'[confirm]' if nap.get('confirm') else 'source'} |",
        f"| email | {nap.get('email', '') or '—'} | {'[confirm]' if nap.get('confirm') else 'source'} |",
        f"| vertical | {instr.get('vertical', '')} | |",
        f"| allow IT language | {instr.get('allowIt')} | factory no-IT gate |",
        "",
        f"**Value proposition:** {instr.get('valueProposition') or '—'}",
        "",
        "## Chrome tokens",
        "",
        "| Token | Value |",
        "|---|---|",
    ]
    for key, val in chrome.items():
        lines.append(f"| {key} | `{val}` |")
    if instr.get("extractedColors"):
        lines += ["", "Extracted hex (most frequent, non-gray): " + ", ".join(f"`{c}`" for c in instr["extractedColors"])]
    lines += [
        "",
        "## Gate 1 inventory",
        "",
        f"Target **{instr['gate1']['hubs']} × {instr['gate1']['childrenPerHub']}** "
        f"SVC-CHILD pages (~{instr['gate1']['targetPages']} with chrome).",
        "",
        "### Hubs from source",
        "",
    ]
    for hub in hubs:
        kids = ", ".join(hub.get("children") or [])
        lines.append(f"- **{hub['title']}** (`/{hub['slug']}/`) — {kids}")
    lines += [
        "",
        "### In-browser demo pack (3 × 3)",
        "",
        "Used by the dashboard factory fallback so a demo stays reviewable.",
        "",
    ]
    for hub in demo:
        kids = ", ".join(hub.get("children") or [])
        lines.append(f"- **{hub['title']}** — {kids}")
    lines += ["", "## Forms", ""]
    for form in instr.get("forms") or []:
        lines.append(f"- `{form['role']}` `{form['slug']}` — {form['title']}")
    nav = instr.get("nav") or []
    if nav:
        lines += ["", "## Nav labels captured", "", ", ".join(nav)]
    lines += ["", "## Factory rules", ""]
    for rule in instr.get("rules") or []:
        lines.append(f"- {rule}")
    lines += [
        "",
        "## Agent brief",
        "",
        "Rebuild the site with NearMe OS factory chrome (utility bar, wordmark + phone CTA, ",
        "navy nav with dropdowns, gold CTAs, FAQ + Independent Operator VS blocks, conversion trio forms). ",
        "Map every hub/child in this file. Mark unverified NAP and credentials `[confirm]`. ",
        "Do not scrape or republish the source site's body copy.",
        "",
    ]
    return "\n".join(lines)


def write_instruction(instr: dict[str, Any], out_dir: Path) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = instr["id"]
    json_path = out_dir / f"{stem}.json"
    md_path = out_dir / f"{stem}.md"
    json_path.write_text(json.dumps(instr, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(instr), encoding="utf-8")
    return json_path, md_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Live URL or path to an HTML snapshot")
    parser.add_argument("--id", dest="set_id", help="Instruction set id (e.g. PROD-SDTS-V1)")
    parser.add_argument("--out", dest="out_dir", default=str(DEFAULT_OUT), help="Output directory")
    parser.add_argument("--stdout-json", action="store_true", help="Print JSON to stdout instead of writing files")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    html, final_url = fetch_html(args.source)
    set_id = instruction_id_for(final_url, args.set_id)
    instr = build_instruction(html, final_url, set_id)
    if args.stdout_json:
        json.dump(instr, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0
    json_path, md_path = write_instruction(instr, Path(args.out_dir))
    print(f"Wrote {json_path.relative_to(ROOT)}")
    print(f"Wrote {md_path.relative_to(ROOT)}")
    print(f"Set {instr['id']} · vertical={instr['vertical']} · hubs={len(instr['hubs'])} · allowIt={instr['allowIt']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
