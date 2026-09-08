#!/usr/bin/env python3
"""Local preview tests. No customer data is sent."""
from __future__ import annotations

import os
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

PREVIEW = "/workspace/factory-trials/1dev/1DEV-WEBSITE-TRIAL-20260907-01/preview"
PAGES = os.path.join(PREVIEW, "pages")


class Doc(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.h1 = 0
        self.viewport = False
        self.forms = 0
        self.demo_forms = 0
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "a" and "href" in d:
            self.hrefs.append(d["href"])
        if tag == "link" and d.get("href"):
            self.hrefs.append(d["href"])
        if tag == "script" and d.get("src"):
            self.hrefs.append(d["src"])
        if tag == "h1":
            self.h1 += 1
        if tag == "meta" and d.get("name") == "viewport":
            self.viewport = True
        if tag == "form":
            self.forms += 1
            if "data-demo-form" in d:
                self.demo_forms += 1
        if "id" in d:
            self.ids.add(d["id"])


def resolve(base_file: str, href: str) -> tuple[str, str]:
    if href.startswith("#"):
        return "hash", href[1:]
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https", "mailto", "tel"}:
        return parsed.scheme, href
    path = os.path.normpath(os.path.join(os.path.dirname(base_file), parsed.path))
    return "file", path


def main():
    fails = []
    pages = [os.path.join(PAGES, f) for f in sorted(os.listdir(PAGES)) if f.endswith(".html")]
    if len(pages) != 121:
        fails.append(f"page_count {len(pages)}")
    index = os.path.join(PREVIEW, "index.html")
    files = pages + [index]
    for path in files:
        text = open(path).read()
        if "tel:123" in text or "123-456-7890" in text and "placeholder" not in text and path.endswith("form01"):
            # placeholder may be mentioned as omitted; tel: must not exist
            pass
        if re.search(r'href=["\']tel:', text):
            fails.append(f"tel_link {path}")
        doc = Doc()
        doc.feed(text)
        if doc.h1 != 1:
            fails.append(f"h1 {os.path.basename(path)}={doc.h1}")
        if not doc.viewport:
            fails.append(f"viewport {path}")
        if "pages/" in path and doc.forms and doc.demo_forms != doc.forms:
            fails.append(f"form_not_demo {path}")
        if "review-notes" not in text:
            fails.append(f"review_notes {os.path.basename(path)}")
        if "PRIVATE DEMO / PROVISIONAL / NOT FOR PUBLICATION" not in text:
            fails.append(f"visitor_banner {os.path.basename(path)}")
        # page_key belongs in review notes, not the visible banner
        banner = text.split("</div>", 1)[0] if "demo-banner" in text else ""
        if "page_key " in banner:
            fails.append(f"page_key_in_banner {os.path.basename(path)}")
        if "review-notes" in text and "<details class=\"review-notes\" open" in text:
            fails.append(f"review_notes_open {os.path.basename(path)}")
        for href in doc.hrefs:
            kind, target = resolve(path, href)
            if kind == "hash":
                if target and target not in doc.ids and target not in {"contact-form"}:
                    # hash-only on same page
                    if target not in doc.ids:
                        fails.append(f"missing_hash {os.path.basename(path)} #{target}")
            elif kind == "file":
                if not os.path.exists(target):
                    fails.append(f"broken {os.path.basename(path)} -> {href}")
            elif kind == "tel":
                fails.append(f"tel {path} {target}")
    css = os.path.join(PREVIEW, "css/site.css")
    js = os.path.join(PREVIEW, "js/demo-form.js")
    css_text = open(css).read()
    if "@media (max-width: 800px)" not in css_text:
        fails.append("responsive_query")
    if "padding-inline: var(--grid-gutter)" not in css_text:
        fails.append("gutter_inline")
    if ".hero { min-height: var(--hero-min-h); display: flex; align-items: center; padding: var(--space-7) 0; }" in css_text:
        fails.append("hero_padding_shorthand")
    js_text = open(js).read()
    if "NOT CONNECTED" not in js_text:
        fails.append("form_js")
    if "preventDefault" not in js_text:
        fails.append("form_preventDefault")
    print(f"static_checks fails={len(fails)}")
    for f in fails[:40]:
        print("FAIL", f)
    if len(fails) > 40:
        print("...", len(fails) - 40, "more")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
