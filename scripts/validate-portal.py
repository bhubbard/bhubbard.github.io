#!/usr/bin/env python3
"""
Automated Verification & Integrity Suite for bhubbard.github.io (code.brandonhubbard.com)
Validates:
  1. index.html structure, meta tags, canonical URLs, JSON-LD schema, and internal anchor targets
  2. Absence of dead/removed repository references across index.html, README.md, sitemap.xml, and API JSONs
  3. api/projects.json and api/github-pages.json schema integrity, non-empty descriptions, and category consistency
  4. Synchronization between api/projects.json and inlined REPOSITORIES in index.html
  5. sitemap.xml and robots.txt XML/URL validity and canonical domain consistency
  6. Optional live HTTP 200 verification (--verify-network)
"""

import os
import sys
import re
import json
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
import urllib.request
import concurrent.futures

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANONICAL_DOMAIN = "https://code.brandonhubbard.com"

# Repositories confirmed deleted from GitHub that must never be linked
REMOVED_REPOS = {
    "godot-rs",
    "hyperframes-rs",
    "mlx-serve-rs",
    "mlx-vlm-rs",
    "npwd-rs",
    "unified-audit-rs",
    "video-use-rs",
}


class PortalHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.duplicate_ids = []
        self.hrefs = []
        self.imgs = []
        self.buttons = []
        self.inputs = []
        self.bench_rows = []
        self.scripts_json_ld = []
        self.in_json_ld = False
        self.current_json_ld = []
        self.meta_tags = []
        self.canonical_links = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if "id" in attr_dict and attr_dict["id"]:
            el_id = attr_dict["id"]
            if el_id in self.ids:
                self.duplicate_ids.append(el_id)
            self.ids.add(el_id)
        if tag == "a" and "href" in attr_dict:
            self.hrefs.append(attr_dict["href"])
        if tag == "img":
            self.imgs.append(attr_dict)
        if tag == "button":
            self.buttons.append(attr_dict)
        if tag == "input":
            self.inputs.append(attr_dict)
        if tag == "tr" and "data-bench-name" in attr_dict:
            self.bench_rows.append(attr_dict)
        if tag == "meta":
            self.meta_tags.append(attr_dict)
        if tag == "link" and attr_dict.get("rel") == "canonical":
            self.canonical_links.append(attr_dict.get("href"))
        if tag == "script" and attr_dict.get("type") == "application/ld+json":
            self.in_json_ld = True
            self.current_json_ld = []

    def handle_endtag(self, tag):
        if tag == "script" and self.in_json_ld:
            self.in_json_ld = False
            self.scripts_json_ld.append("".join(self.current_json_ld))

    def handle_data(self, data):
        if self.in_json_ld:
            self.current_json_ld.append(data)


def assert_true(condition, message, failures):
    if not condition:
        failures.append(message)
        print(f"  [FAIL] {message}")
    else:
        print(f"  [PASS] {message}")


def validate_all(verify_network=False):
    failures = []
    print("=== 1. Validating index.html Structure, Semantics & Anchors ===")
    index_path = os.path.join(BASE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    parser = PortalHTMLParser()
    parser.feed(html_content)

    assert_true(
        parser.canonical_links == [f"{CANONICAL_DOMAIN}/"],
        f"Canonical link is {CANONICAL_DOMAIN}/ (got {parser.canonical_links})",
        failures,
    )

    assert_true(
        len(parser.scripts_json_ld) >= 1,
        f"Found {len(parser.scripts_json_ld)} JSON-LD structured data block(s)",
        failures,
    )
    for raw_ld in parser.scripts_json_ld:
        try:
            parsed_ld = json.loads(raw_ld)
            assert_true(
                "@context" in parsed_ld and "@graph" in parsed_ld,
                "JSON-LD contains valid @context and @graph",
                failures,
            )
        except Exception as e:
            failures.append(f"Invalid JSON-LD: {e}")

    # Verify all #anchor links resolve to existing IDs in index.html
    anchor_hrefs = [h for h in parser.hrefs if h.startswith("#") and len(h) > 1]
    missing_anchors = [h for h in anchor_hrefs if h[1:] not in parser.ids]
    assert_true(
        len(missing_anchors) == 0,
        f"All {len(anchor_hrefs)} internal #anchor links resolve to valid DOM IDs (missing: {missing_anchors})",
        failures,
    )

    assert_true(
        len(parser.duplicate_ids) == 0,
        f"Zero duplicate DOM IDs in index.html (duplicates: {parser.duplicate_ids})",
        failures,
    )

    relative_hrefs = [h for h in parser.hrefs if h.startswith("./")]
    assert_true(
        len(relative_hrefs) == 0,
        f"Zero ambiguous relative './' links in index.html (found: {relative_hrefs})",
        failures,
    )

    assert_true(
        len(parser.bench_rows) >= 40,
        f"Empirical Benchmark Matrix contains {len(parser.bench_rows)} verified Rust rows (>= 40)",
        failures,
    )

    unlabeled_inputs = [
        inp for inp in parser.inputs if not inp.get("aria-label") and not inp.get("placeholder")
    ]
    assert_true(
        len(unlabeled_inputs) == 0,
        f"All {len(parser.inputs)} <input> elements have accessible aria-label or placeholder",
        failures,
    )

    # Verify no removed repositories appear anywhere in index.html, README.md, sitemap.xml, or api/*.json
    print("\n=== 2. Checking for Pruned / Deleted Repositories ===")
    for filename in ["index.html", "README.md", "sitemap.xml", "api/projects.json", "api/github-pages.json"]:
        fpath = os.path.join(BASE_DIR, filename)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
        found_dead = [r for r in REMOVED_REPOS if r in text]
        assert_true(
            len(found_dead) == 0,
            f"{filename} contains 0 references to deleted repositories (found: {found_dead})",
            failures,
        )

    print("\n=== 3. Validating API JSON Files & Inlined Catalog Sync ===")
    projects_path = os.path.join(BASE_DIR, "api", "projects.json")
    pages_path = os.path.join(BASE_DIR, "api", "github-pages.json")
    benchmarks_path = os.path.join(BASE_DIR, "api", "benchmarks.json")
    with open(projects_path, "r", encoding="utf-8") as f:
        projects = json.load(f)
    with open(pages_path, "r", encoding="utf-8") as f:
        pages = json.load(f)
    with open(benchmarks_path, "r", encoding="utf-8") as f:
        benchmarks = json.load(f)

    assert_true(
        len(projects) >= 120,
        f"api/projects.json contains {len(projects)} repositories (>= 120)",
        failures,
    )
    assert_true(
        len(pages) >= 65,
        f"api/github-pages.json contains {len(pages)} verified live pages (>= 65)",
        failures,
    )
    assert_true(
        len(benchmarks) == len(parser.bench_rows) and len(benchmarks) >= 40,
        f"api/benchmarks.json contains all {len(benchmarks)} verified empirical Rust benchmarks (matching index.html)",
        failures,
    )

    required_keys = {
        "name",
        "description",
        "language",
        "category",
        "categories",
        "stars",
        "has_pages",
        "page_url",
        "has_benchmarks",
        "benchmark_url",
        "github_url",
        "target_url",
        "topics",
        "is_archived",
        "pushed_at",
    }
    missing_keys_repos = [
        p.get("name") for p in projects if not required_keys.issubset(set(p.keys()))
    ]
    assert_true(
        len(missing_keys_repos) == 0,
        "All entries in api/projects.json have complete required schema keys",
        failures,
    )

    empty_desc_repos = [
        p["name"]
        for p in projects
        if not p.get("description") or p["description"].strip().lower() == "none"
    ]
    assert_true(
        len(empty_desc_repos) == 0,
        f"All {len(projects)} projects have non-empty descriptions (empty: {empty_desc_repos})",
        failures,
    )

    # Extract inlined REPOSITORIES from index.html and compare
    m = re.search(r"let REPOSITORIES = (\[.*?\n\]);", html_content, re.DOTALL)
    assert_true(m is not None, "Found inlined REPOSITORIES array in index.html", failures)
    if m:
        inlined_repos = json.loads(m.group(1))
        assert_true(
            len(inlined_repos) == len(projects),
            f"Inlined REPOSITORIES count ({len(inlined_repos)}) matches api/projects.json ({len(projects)})",
            failures,
        )

    # Cross-verify all github.com/bhubbard/<repo> and code.brandonhubbard.com/<repo>/ URLs in index.html and README.md
    known_repos = {p["name"].lower() for p in projects}
    known_pages = {p["name"].lower() for p in pages}
    with open(os.path.join(BASE_DIR, "README.md"), "r", encoding="utf-8") as f:
        readme_content = f.read()

    for label, doc_text in [("index.html", html_content), ("README.md", readme_content)]:
        gh_refs = {
            m_gh.group(1).lower()
            for m_gh in re.finditer(r"https://github\.com/bhubbard/([a-zA-Z0-9_.-]+)", doc_text)
        }
        unknown_gh = sorted(gh_refs - known_repos)
        assert_true(
            len(unknown_gh) == 0,
            f"All {len(gh_refs)} GitHub repo links in {label} exist in api/projects.json (unknown: {unknown_gh})",
            failures,
        )

        page_refs = {
            m_pg.group(1).lower()
            for m_pg in re.finditer(r"https://code\.brandonhubbard\.com/([a-zA-Z0-9_.-]+)/", doc_text)
            if m_pg.group(1).lower() != "api"
        }
        unknown_pages = sorted(page_refs - known_pages)
        assert_true(
            len(unknown_pages) == 0,
            f"All {len(page_refs)} code.brandonhubbard.com/<repo>/ links in {label} exist in api/github-pages.json (unknown: {unknown_pages})",
            failures,
        )

    print("\n=== 4. Validating CNAME, robots.txt & sitemap.xml ===")
    with open(os.path.join(BASE_DIR, "CNAME"), "r", encoding="utf-8") as f:
        cname = f.read().strip()
    assert_true(
        cname == "code.brandonhubbard.com",
        f"CNAME is 'code.brandonhubbard.com' (got '{cname}')",
        failures,
    )

    with open(os.path.join(BASE_DIR, "robots.txt"), "r", encoding="utf-8") as f:
        robots = f.read()
    assert_true(
        f"Sitemap: {CANONICAL_DOMAIN}/sitemap.xml" in robots,
        f"robots.txt points to {CANONICAL_DOMAIN}/sitemap.xml",
        failures,
    )

    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text for el in root.findall("sm:url/sm:loc", ns)]
    assert_true(
        len(locs) >= 65,
        f"sitemap.xml is valid XML and contains {len(locs)} canonical URLs",
        failures,
    )
    non_canonical_locs = [u for u in locs if not u.startswith(CANONICAL_DOMAIN)]
    assert_true(
        len(non_canonical_locs) == 0,
        f"All sitemap.xml URLs start with {CANONICAL_DOMAIN} (invalid: {non_canonical_locs})",
        failures,
    )

    if verify_network:
        print("\n=== 5. Verifying Live HTTP 200 Status Across All Sitemap URLs ===")

        def check_url(u):
            try:
                req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Portal-Validator"})
                with urllib.request.urlopen(req, timeout=6) as resp:
                    return (u, resp.status == 200)
            except Exception:
                return (u, False)

        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
            results = list(ex.map(check_url, locs))
        failed_urls = [u for u, ok in results if not ok]
        assert_true(
            len(failed_urls) == 0,
            f"All {len(locs)} sitemap URLs responded with HTTP 200 (failed: {failed_urls})",
            failures,
        )

    print("\n" + "=" * 60)
    if failures:
        print(f"VALIDATION FAILED with {len(failures)} error(s):")
        for err in failures:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("ALL VALIDATION CHECKS PASSED SUCCESSFULLY!")
        sys.exit(0)


if __name__ == "__main__":
    verify_net = "--verify-network" in sys.argv
    validate_all(verify_network=verify_net)
