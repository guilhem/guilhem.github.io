#!/usr/bin/env python3
"""Check built HTML, local links, feeds, and draft isolation with the stdlib."""

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links = set(), []
        self.h1 = 0
        self.language = self.canonical = None
        self.redirect = False
        self.draft = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "draft-notice" in attrs.get("class", "").split():
            self.draft = True
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "h1":
            self.h1 += 1
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.redirect = True
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])

def check(root, drafts):
    origin = "https://guilhem.github.io/"
    pages = {p.relative_to(root).as_posix(): Page(p.read_text()) for p in root.rglob("*.html")}
    assert pages, "No HTML generated"
    for required in ("index.html", "about/index.html", "posts/index.html", "tags/index.html", "search/index.html", "404.html"):
        assert required in pages, f"Missing page: {required}"

    for path, page in pages.items():
        # Hugo's pagination aliases are redirect documents, not content pages.
        if not page.redirect:
            assert page.language == "fr", f"Wrong document language: {path}"
            assert page.h1 == 1, f"Expected one h1: {path}"
        assert page.canonical and page.canonical.startswith(origin), f"Wrong canonical URL: {path}"
        for link in page.links:
            url = urlsplit(urljoin(origin + path, link))
            if url.netloc != "guilhem.github.io" or url.scheme not in ("http", "https"):
                continue
            target = unquote(url.path).lstrip("/")
            if not target or target.endswith("/"):
                target += "index.html"
            elif (root / target).is_dir():
                target += "/index.html"
            assert (root / target).is_file(), f"Broken link in {path}: {link}"
            if url.fragment and target in pages:
                assert unquote(url.fragment) in pages[target].ids, f"Broken anchor in {path}: {link}"

    search = json.loads((root / "index.json").read_text())
    assert isinstance(search, list), "Search index must be an array, including when empty"
    feed = ET.parse(root / "index.xml")
    ET.parse(root / "sitemap.xml")
    if not drafts:
        assert not any(page.draft for page in pages.values()), "A draft was included in the production build"
    indexed_urls = [item["permalink"] for item in search]
    indexed_urls += [item.findtext("link") for item in feed.findall("./channel/item")]
    for url in indexed_urls:
        path = unquote(urlsplit(url).path).lstrip("/").rstrip("/") + "/index.html"
        assert path in pages, f"Search/RSS references a missing page: {url}"
        assert drafts or not pages[path].draft, f"Draft leaked into search/RSS: {url}"
    print(f"OK: {len(pages)} HTML pages, local links/anchors, RSS, sitemap, search; drafts={drafts}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--drafts", action="store_true")
    args = parser.parse_args()
    check(args.directory, args.drafts)
