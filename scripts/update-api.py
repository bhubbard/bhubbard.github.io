#!/usr/bin/env python3
"""
Canonical GitHub Pages & Projects API Generator for code.brandonhubbard.com
Fetches public repositories, verifies live pages, prunes dead links,
and exports api/projects.json and api/github-pages.json.
"""

import os
import json
import urllib.request
import urllib.error
import ssl

GITHUB_USER = "bhubbard"
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100&sort=updated"
TOKEN = os.environ.get("GITHUB_TOKEN")

# Live custom GitHub Pages mapping
GITHUB_PAGES_MAP = {
    "active-ragdoll-rs": "https://code.brandonhubbard.com/active-ragdoll-rs/",
    "aesir-utils-rs": "https://code.brandonhubbard.com/aesir-utils-rs/",
    "apfel-rs": "https://code.brandonhubbard.com/apfel-rs/",
    "astro-client-directive-ai": "https://code.brandonhubbard.com/astro-client-directive-ai/",
    "astro-dev-audit-nano": "https://code.brandonhubbard.com/astro-dev-audit-nano/",
    "astro-dev-broken-anchor-healer": "https://code.brandonhubbard.com/astro-dev-broken-anchor-healer/",
    "astro-dev-content-linter": "https://code.brandonhubbard.com/astro-dev-content-linter/",
    "astro-dev-copy-optimizer": "https://code.brandonhubbard.com/astro-dev-copy-optimizer/",
    "astro-dev-i18n-coverage": "https://code.brandonhubbard.com/astro-dev-i18n-coverage/",
    "astro-dev-island-hydration-advisor": "https://code.brandonhubbard.com/astro-dev-island-hydration-advisor/",
    "astro-dev-mock-generator": "https://code.brandonhubbard.com/astro-dev-mock-generator/",
    "astro-dev-schema-scaffolder": "https://code.brandonhubbard.com/astro-dev-schema-scaffolder/",
    "astro-og-smart-crop": "https://code.brandonhubbard.com/astro-og-smart-crop/",
    "astro-prefetch-ai-brief": "https://code.brandonhubbard.com/astro-prefetch-ai-brief/",
    "astro-rehype-nano-code": "https://code.brandonhubbard.com/astro-rehype-nano-code/",
    "astro-schema-ld-verifier": "https://code.brandonhubbard.com/astro-schema-ld-verifier/",
    "bhubbard.github.io": "https://code.brandonhubbard.com/",
    "bullet3-rs": "https://code.brandonhubbard.com/bullet3-rs/",
    "clippy-cf-reporter": "https://code.brandonhubbard.com/clippy-cf-reporter/",
    "defy-rs": "https://code.brandonhubbard.com/defy-rs/",
    "detour-crowd-rs": "https://code.brandonhubbard.com/detour-crowd-rs/",
    "dialogger-rs": "https://code.brandonhubbard.com/dialogger-rs/",
    "flareguard": "https://code.brandonhubbard.com/flareguard/",
    "flarelint": "https://code.brandonhubbard.com/flarelint/",
    "flareops": "https://code.brandonhubbard.com/flareops/",
    "flareperf": "https://code.brandonhubbard.com/flareperf/",
    "gambetta-netcode-rs": "https://code.brandonhubbard.com/gambetta-netcode-rs/",
    "godot-rs": "https://code.brandonhubbard.com/godot-rs/",
    "hyperframes-rs": "https://code.brandonhubbard.com/hyperframes-rs/",
    "minimal-hud-rs": "https://code.brandonhubbard.com/minimal-hud-rs/",
    "npwd-rs": "https://code.brandonhubbard.com/npwd-rs/",
    "openrw-rs": "https://code.brandonhubbard.com/openrw-rs/",
    "poormans-camera-rs": "https://code.brandonhubbard.com/poormans-camera-rs/",
    "radial-menu-rs": "https://code.brandonhubbard.com/radial-menu-rs/",
    "sdf-math-rs": "https://code.brandonhubbard.com/sdf-math-rs/",
    "sfxr-rs": "https://code.brandonhubbard.com/sfxr-rs/",
    "simplecar2-rs": "https://code.brandonhubbard.com/simplecar2-rs/",
    "sumo-rs": "https://code.brandonhubbard.com/sumo-rs/",
    "tactical-ai-rs": "https://code.brandonhubbard.com/tactical-ai-rs/",
    "talks": "https://talks.brandonhubbard.com/",
    "tlab-vehicle-physics-rs": "https://code.brandonhubbard.com/tlab-vehicle-physics-rs/",
    "uxsim-rs": "https://code.brandonhubbard.com/uxsim-rs/",
    "vhud-rs": "https://code.brandonhubbard.com/vhud-rs/",
    "video-use-rs": "https://code.brandonhubbard.com/video-use-rs/",
    "vite-plus-commitlint": "https://code.brandonhubbard.com/vite-plus-commitlint/",
    "vite-plus-kumo-ui": "https://code.brandonhubbard.com/vite-plus-kumo-ui/",
    "vite-plus-wrangler": "https://code.brandonhubbard.com/vite-plus-wrangler/",
    "zev-rs": "https://code.brandonhubbard.com/zev-rs/"
}

def fetch_repos():
    headers = {"User-Agent": "BrandonHubbard-API-Updater"}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"

    req = urllib.request.Request(API_URL, headers=headers)
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    print("Fetching repositories from GitHub API...")
    repos = fetch_repos()
    print(f"Fetched {len(repos)} repositories.")

    clean_projects = []
    for r in repos:
        name = r.get("name")
        lower = name.lower()

        # Skip profile README and private
        if name == GITHUB_USER or r.get("private", False):
            continue

        has_page = lower in GITHUB_PAGES_MAP or r.get("has_pages", False)
        page_url = GITHUB_PAGES_MAP.get(lower)
        if not page_url and r.get("has_pages", False):
            page_url = f"https://code.brandonhubbard.com/{name}/"

        lang = r.get("language") or "Code"
        categories = []
        if lang == "Rust" or name.endswith("-rs"):
            categories.extend(["cli", "rust"])
        if name.startswith("flare") or "cloudflare" in name or name.startswith("flared"):
            categories.append("flare")
        if name.startswith("astro-") or "astro" in name:
            categories.append("astro")
        if name.startswith("wp-") or "wordpress" in name or name.startswith("pressable"):
            categories.append("wordpress")
        if not categories:
            categories.append("tools")

        main_cat = "tools"
        for c in ["flare", "astro", "cli", "wordpress", "tools"]:
            if c in categories:
                main_cat = c
                break

        target_url = page_url if page_url else r.get("html_url")
        topics = r.get("topics") or []

        clean_projects.append({
            "name": name,
            "description": r.get("description") or "Open source software and systems engineering by Brandon Hubbard.",
            "language": lang,
            "category": main_cat,
            "categories": categories,
            "stars": r.get("stargazers_count", 0),
            "has_pages": bool(page_url),
            "page_url": page_url,
            "github_url": r.get("html_url"),
            "target_url": target_url,
            "topics": topics,
            "is_archived": r.get("archived", False),
            "pushed_at": r.get("pushed_at")
        })

    clean_projects.sort(key=lambda p: (not p["has_pages"], -p["stars"], p["name"]))

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    api_dir = os.path.join(base_dir, "api")
    os.makedirs(api_dir, exist_ok=True)

    projects_path = os.path.join(api_dir, "projects.json")
    with open(projects_path, "w", encoding="utf-8") as f:
        json.dump(clean_projects, f, indent=2)

    pages_path = os.path.join(api_dir, "github-pages.json")
    with open(pages_path, "w", encoding="utf-8") as f:
        json.dump([p for p in clean_projects if p["has_pages"]], f, indent=2)

    print(f"Generated {projects_path} ({len(clean_projects)} projects)")
    print(f"Generated {pages_path} ({sum(1 for p in clean_projects if p['has_pages'])} pages)")

if __name__ == "__main__":
    main()
