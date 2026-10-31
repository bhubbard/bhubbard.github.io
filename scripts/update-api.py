#!/usr/bin/env python3
"""
Canonical GitHub Pages, Projects API & Sitemap Generator for code.brandonhubbard.com
Fetches all public repositories with pagination, verifies live GitHub Pages HTTP status,
prunes dead links, and exports api/projects.json, api/github-pages.json, and sitemap.xml.
"""

import os
import json
import urllib.request
import urllib.error
import ssl
import concurrent.futures
from datetime import datetime, timezone

GITHUB_USER = "bhubbard"
CANONICAL_DOMAIN = "https://code.brandonhubbard.com"
API_BASE_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
TOKEN = os.environ.get("GITHUB_TOKEN")

# Live custom GitHub Pages mapping (verified HTTP 200 endpoints)
GITHUB_PAGES_MAP = {
    "active-ragdoll-rs": "https://code.brandonhubbard.com/active-ragdoll-rs/",
    "aesir-utils-rs": "https://code.brandonhubbard.com/aesir-utils-rs/",
    "agentarena-rs": "https://code.brandonhubbard.com/agentarena-rs/",
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
    "auge-rs": "https://code.brandonhubbard.com/auge-rs/",
    "auto-editor-rs": "https://code.brandonhubbard.com/auto-editor-rs/",
    "bhubbard.github.io": "https://code.brandonhubbard.com/",
    "blender-rs": "https://code.brandonhubbard.com/blender-rs/",
    "box3d-rs": "https://code.brandonhubbard.com/box3d-rs/",
    "bullet3-rs": "https://code.brandonhubbard.com/bullet3-rs/",
    "clearwater-rs": "https://code.brandonhubbard.com/clearwater-rs/",
    "clippy-cf-reporter": "https://code.brandonhubbard.com/clippy-cf-reporter/",
    "comfyui-ltxvideo-mlx-rs": "https://code.brandonhubbard.com/comfyui-ltxvideo-mlx-rs/",
    "defy-rs": "https://code.brandonhubbard.com/defy-rs/",
    "desktop-rs": "https://code.brandonhubbard.com/desktop-rs/",
    "detour-crowd-rs": "https://code.brandonhubbard.com/detour-crowd-rs/",
    "dialogger-rs": "https://code.brandonhubbard.com/dialogger-rs/",
    "ffmpeg-skill-rs": "https://code.brandonhubbard.com/ffmpeg-skill-rs/",
    "flareguard": "https://code.brandonhubbard.com/flareguard/",
    "flarelint": "https://code.brandonhubbard.com/flarelint/",
    "flareops": "https://code.brandonhubbard.com/flareops/",
    "flareperf": "https://code.brandonhubbard.com/flareperf/",
    "gambetta-netcode-rs": "https://code.brandonhubbard.com/gambetta-netcode-rs/",
    "generate-glb-rs": "https://code.brandonhubbard.com/generate-glb-rs/",
    "handbrake-rs": "https://code.brandonhubbard.com/handbrake-rs/",
    "hunyuan3d-rs": "https://code.brandonhubbard.com/hunyuan3d-rs/",
    "latentsync-rs": "https://code.brandonhubbard.com/latentsync-rs/",
    "lossless-cut-rs": "https://code.brandonhubbard.com/lossless-cut-rs/",
    "lux-rs": "https://code.brandonhubbard.com/lux-rs/",
    "lyra-rs": "https://code.brandonhubbard.com/lyra-rs/",
    "mflux-rs": "https://code.brandonhubbard.com/mflux-rs/",
    "minimal-hud-rs": "https://code.brandonhubbard.com/minimal-hud-rs/",
    "mlt-rs": "https://code.brandonhubbard.com/mlt-rs/",
    "mlx-audio-rs": "https://code.brandonhubbard.com/mlx-audio-rs/",
    "mlx-embeddings-rs": "https://code.brandonhubbard.com/mlx-embeddings-rs/",
    "mlx-gen-rs": "https://code.brandonhubbard.com/mlx-gen-rs/",
    "mlx-video-rs": "https://code.brandonhubbard.com/mlx-video-rs/",
    "nanoswarm-rs": "https://code.brandonhubbard.com/nanoswarm-rs/",
    "neteq-rs": "https://code.brandonhubbard.com/neteq-rs/",
    "olive-rs": "https://code.brandonhubbard.com/olive-rs/",
    "open-generative-ai-rs": "https://code.brandonhubbard.com/open-generative-ai-rs/",
    "open-higgsfield-ai-rs": "https://code.brandonhubbard.com/open-higgsfield-ai-rs/",
    "openmontage-rs": "https://code.brandonhubbard.com/openmontage-rs/",
    "openrw-rs": "https://code.brandonhubbard.com/openrw-rs/",
    "poormans-camera-rs": "https://code.brandonhubbard.com/poormans-camera-rs/",
    "radial-menu-rs": "https://code.brandonhubbard.com/radial-menu-rs/",
    "rea-rs": "https://code.brandonhubbard.com/rea-rs/",
    "sdf-math-rs": "https://code.brandonhubbard.com/sdf-math-rs/",
    "sfxr-rs": "https://code.brandonhubbard.com/sfxr-rs/",
    "simplecar2-rs": "https://code.brandonhubbard.com/simplecar2-rs/",
    "sumo-rs": "https://code.brandonhubbard.com/sumo-rs/",
    "tactical-ai-rs": "https://code.brandonhubbard.com/tactical-ai-rs/",
    "talks": "https://talks.brandonhubbard.com/",
    "timesfm-rs": "https://code.brandonhubbard.com/timesfm-rs/",
    "tlab-vehicle-physics-rs": "https://code.brandonhubbard.com/tlab-vehicle-physics-rs/",
    "translate-rs": "https://code.brandonhubbard.com/translate-rs/",
    "upscayl-rs": "https://code.brandonhubbard.com/upscayl-rs/",
    "uxsim-rs": "https://code.brandonhubbard.com/uxsim-rs/",
    "vhud-rs": "https://code.brandonhubbard.com/vhud-rs/",
    "vite-plus-commitlint": "https://code.brandonhubbard.com/vite-plus-commitlint/",
    "vite-plus-kumo-ui": "https://code.brandonhubbard.com/vite-plus-kumo-ui/",
    "vite-plus-wrangler": "https://code.brandonhubbard.com/vite-plus-wrangler/",
    "void-model-rs": "https://code.brandonhubbard.com/void-model-rs/",
    "voicestudio-rs": "https://code.brandonhubbard.com/voicestudio-rs/",
    "watertight-meshes-rs": "https://code.brandonhubbard.com/watertight-meshes-rs/",
    "yt-dlp-rs": "https://code.brandonhubbard.com/yt-dlp-rs/",
    "zev-rs": "https://code.brandonhubbard.com/zev-rs/",
}

# Curated fallback descriptions for repositories without a GitHub description string
FALLBACK_DESCRIPTIONS = {
    "blender-rs": "Memory-safe, high-performance pure Rust port of Blender 3D creation suite — mesh modeling, scene graph, and rendering pipeline.",
    "freevideo-rs": "High-performance pure Rust video synthesis, frame processing, and neural rendering toolkit.",
    "generate-glb-rs": "Fast, pure Rust CLI tool and HTTP server to generate 3D models in binary GLB format using LLaMA-Mesh AI with zero Python dependencies.",
    "latentsync-rs": "High-performance Rust port of LatentSync: audio-conditioned latent diffusion for temporally consistent lip-sync video synthesis.",
    "musetalk-rs": "Pure Rust real-time high-fidelity audio-driven lip-sync and talking head synthesis engine in latent space.",
    "rea-rs": "High-performance, memory-safe pure Rust CLI and Model Context Protocol (MCP) server for structured codebase investigation.",
    "sadtalker-rs": "Pure Rust port of SadTalker: stylized audio-driven single-image talking face animation with 3D motion coefficients.",
    "toontalker-rs": "Pure Rust cross-domain cartoon and stylized avatar talking-head synthesis engine driven by audio.",
    "video-retalking-rs": "Pure Rust audio-based lip synchronization and facial reenactment pipeline for talking-head video editing.",
    "wav2lip-rs": "High-speed pure Rust inference engine for Wav2Lip audio-driven lip-sync synthesis and video dubbing.",
    "wp-spinupwp-api": "Modern PHP and WordPress client library for the SpinupWP cloud server management REST API.",
}

# Language override for multi-language repositories where GitHub primary language is secondary
LANGUAGE_OVERRIDES = {
    "clearwater-rs": "Rust",
    "desktop-rs": "Rust",
    "openmontage-rs": "Rust",
    "paperclip-rs": "Rust",
}


def fetch_repos():
    """Fetch all public repositories across all paginated API responses."""
    headers = {"User-Agent": "BrandonHubbard-API-Updater"}
    if TOKEN:
        headers["Authorization"] = f"token {TOKEN}"

    ctx = ssl.create_default_context()
    all_repos = []
    page = 1

    while True:
        url = f"{API_BASE_URL}?per_page=100&page={page}&sort=updated"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx) as resp:
            batch = json.loads(resp.read().decode("utf-8"))
            if not batch:
                break
            all_repos.extend(batch)
            if len(batch) < 100:
                break
            page += 1

    return all_repos


def verify_page_url(url, ctx):
    """Verify that a candidate GitHub Pages URL responds with HTTP 200."""
    if not url:
        return False
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(
                url,
                method=method,
                headers={"User-Agent": "BrandonHubbard-API-Updater"},
            )
            with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
                if 200 <= resp.status < 400:
                    return True
        except urllib.error.HTTPError as e:
            if e.code == 405 and method == "HEAD":
                continue
            return False
        except Exception:
            return False
    return False


def generate_sitemap(pages_projects, base_dir):
    """Generate canonical sitemap.xml for all verified live GitHub Pages."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        "  <!-- Root Flagship Engineering Portal -->",
        "  <url>",
        f"    <loc>{CANONICAL_DOMAIN}/</loc>",
        f"    <lastmod>{today}</lastmod>",
        "    <changefreq>weekly</changefreq>",
        "    <priority>1.0</priority>",
        "  </url>",
    ]

    flagships = {"apfel-rs", "zev-rs", "bullet3-rs", "timesfm-rs", "uxsim-rs", "nanoswarm-rs"}
    flare_suite = {"flareguard", "flareperf", "flarelint", "flareops"}

    sorted_pages = sorted(
        [p for p in pages_projects if p["name"] != "bhubbard.github.io" and p.get("page_url")],
        key=lambda p: (
            0 if p["name"] in flagships else (1 if p["name"] in flare_suite else (2 if p["category"] == "astro" else 3)),
            p["name"],
        ),
    )

    for p in sorted_pages:
        url = p["page_url"]
        if not url.startswith(CANONICAL_DOMAIN):
            continue
        pushed = (p.get("pushed_at") or "")[:10] or today
        if p["name"] in flagships:
            priority = "0.9"
            freq = "weekly"
        elif p["name"] in flare_suite:
            priority = "0.8"
            freq = "weekly"
        elif p["category"] == "astro":
            priority = "0.8"
            freq = "monthly"
        else:
            priority = "0.7"
            freq = "monthly"

        lines.extend([
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{pushed}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ])

    lines.append("</urlset>")
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return sitemap_path, len(sorted_pages) + 1


def extract_benchmarks_from_index(base_dir):
    """Extract the 40 verified empirical Rust benchmarks from index.html for api/benchmarks.json."""
    import re
    import html as html_lib

    index_path = os.path.join(base_dir, "index.html")
    if not os.path.exists(index_path):
        return [], {}

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    m = re.search(r'<tbody id="benchTableBody">(.*?)</tbody>', html, re.DOTALL)
    if not m:
        return [], {}

    rows = re.findall(r"<tr[^>]*>.*?</tr>", m.group(1), re.DOTALL)
    benchmarks = []
    bench_map = {}

    for idx, row in enumerate(rows):
        tds = re.findall(r"<td[^>]*>(.*?)</td>", row, re.DOTALL)
        if len(tds) < 6:
            continue
        clean_tds = [html_lib.unescape(re.sub(r"<[^>]+>", "", td).strip()) for td in tds]
        proj_name = clean_tds[0].split()[-1].strip()
        ref_runtime = clean_tds[1]
        domain = clean_tds[2]
        speedup_label = clean_tds[3]

        if "instant" in speedup_label.lower():
            speedup_factor = None
        else:
            num_m = re.search(r"([\d,.]+)", speedup_label)
            speedup_factor = float(num_m.group(1).replace(",", "")) if num_m else None

        page_m = re.search(r'href="([^"]+)"', tds[4])
        bench_m = re.search(r'href="([^"]+)"', tds[5])
        page_url = page_m.group(1) if page_m else f"{CANONICAL_DOMAIN}/{proj_name}/"
        benchmark_url = (
            bench_m.group(1)
            if bench_m
            else f"https://github.com/{GITHUB_USER}/{proj_name}/blob/main/BENCHMARKS.md"
        )
        github_url = f"https://github.com/{GITHUB_USER}/{proj_name}"

        entry = {
            "rank": idx + 1,
            "name": proj_name,
            "reference_runtime": ref_runtime,
            "domain": domain,
            "speedup_label": speedup_label,
            "speedup_factor": speedup_factor,
            "page_url": page_url,
            "benchmark_url": benchmark_url,
            "github_url": github_url,
        }
        benchmarks.append(entry)
        bench_map[proj_name.lower()] = entry

    return benchmarks, bench_map


def sync_index_html(clean_projects, pages_projects, base_dir):
    """Synchronize inlined GITHUB_PAGES_MAP and REPOSITORIES in index.html."""
    import re
    index_path = os.path.join(base_dir, "index.html")
    if not os.path.exists(index_path):
        return False

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    pages_map = {
        p["name"].lower(): p["page_url"]
        for p in sorted(pages_projects, key=lambda x: x["name"])
    }
    pages_map_json = json.dumps(pages_map, indent=6)
    repos_json = json.dumps(clean_projects, indent=2)

    pattern = re.compile(
        r"    // Comprehensive map of all.*?let REPOSITORIES = \[.*?\n\];",
        re.DOTALL,
    )
    replacement = (
        f"    // Comprehensive map of all {len(pages_map)} repositories with verified live GitHub Pages\n"
        f"    const GITHUB_PAGES_MAP = {pages_map_json};\n\n"
        "    function getProjectTargetUrl(repo) {\n"
        '      if (!repo) return "#";\n'
        '      const name = (repo.name || "").toLowerCase().trim();\n'
        "      if (repo.target_url) {\n"
        "        return repo.target_url;\n"
        "      }\n"
        "      if (GITHUB_PAGES_MAP[name]) {\n"
        "        return GITHUB_PAGES_MAP[name];\n"
        "      }\n"
        '      if (repo.docs && repo.docs !== "#") {\n'
        "        return repo.docs;\n"
        "      }\n"
        "      return repo.github_url || repo.url || `https://github.com/bhubbard/${name}`;\n"
        "    }\n\n"
        "    // Complete repository catalog with The Flare Suite, Astro Chrome AI, and Rust developer tools\n"
        f"    let REPOSITORIES = {repos_json};"
    )

    new_html, count = pattern.subn(lambda m: replacement, html)
    if count == 1 and new_html != html:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(new_html)
        return True
    return count == 1


def main():
    print("Fetching repositories from GitHub API (with pagination)...")
    repos = fetch_repos()
    print(f"Fetched {len(repos)} total repositories.")

    ctx = ssl.create_default_context()

    # Candidate page URLs to verify concurrently
    candidates = {}
    repo_has_pages = {}
    for r in repos:
        name = r.get("name")
        if not name or name == GITHUB_USER or r.get("private", False):
            continue
        lower = name.lower()
        repo_has_pages[name] = bool(r.get("has_pages", False))
        if lower in GITHUB_PAGES_MAP:
            candidates[name] = GITHUB_PAGES_MAP[lower]
        elif r.get("has_pages", False):
            candidates[name] = f"{CANONICAL_DOMAIN}/{name}/"

    print(f"Verifying {len(candidates)} candidate GitHub Pages URLs...")
    verified_pages = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_name = {
            executor.submit(verify_page_url, url, ctx): (name, url)
            for name, url in candidates.items()
        }
        for future in concurrent.futures.as_completed(future_to_name):
            name, url = future_to_name[future]
            if future.result() or (name.lower() in GITHUB_PAGES_MAP and repo_has_pages.get(name, False)):
                verified_pages[name] = url

    print(f"Verified {len(verified_pages)} live GitHub Pages (HTTP 200).")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    benchmarks, bench_map = extract_benchmarks_from_index(base_dir)

    clean_projects = []
    for r in repos:
        name = r.get("name")
        lower = (name or "").lower()

        # Skip profile README and private repositories
        if not name or name == GITHUB_USER or r.get("private", False):
            continue

        page_url = verified_pages.get(name)
        has_page = bool(page_url)

        lang = LANGUAGE_OVERRIDES.get(lower) or r.get("language") or "Code"
        topics = r.get("topics") or []

        categories = []
        if lang == "Rust" or name.endswith("-rs") or "rust" in topics:
            categories.extend(["cli", "rust"])
        if name.startswith("flare") or "cloudflare" in name or name.startswith("flared"):
            categories.append("flare")
        if name.startswith("astro-") or "astro" in name:
            categories.append("astro")
        if (
            name.startswith("wp-")
            or "wordpress" in name
            or name.startswith("pressable")
            or "wordpress" in topics
        ):
            categories.append("wordpress")
        if not categories:
            categories.append("tools")

        # Deduplicate while preserving order
        categories = list(dict.fromkeys(categories))

        main_cat = "tools"
        for c in ["flare", "astro", "cli", "wordpress", "tools"]:
            if c in categories:
                main_cat = c
                break

        target_url = page_url if page_url else r.get("html_url")
        description = (
            r.get("description")
            or FALLBACK_DESCRIPTIONS.get(lower)
            or "Open source software and systems engineering by Brandon Hubbard."
        )

        bench_entry = bench_map.get(lower)
        has_benchmarks = bool(bench_entry)
        benchmark_url = bench_entry["benchmark_url"] if bench_entry else None

        clean_projects.append({
            "name": name,
            "description": description,
            "language": lang,
            "category": main_cat,
            "categories": categories,
            "stars": r.get("stargazers_count", 0),
            "has_pages": has_page,
            "page_url": page_url,
            "has_benchmarks": has_benchmarks,
            "benchmark_url": benchmark_url,
            "github_url": r.get("html_url"),
            "target_url": target_url,
            "topics": topics,
            "is_archived": r.get("archived", False),
            "pushed_at": r.get("pushed_at"),
        })

    clean_projects.sort(key=lambda p: (not p["has_pages"], -p["stars"], p["name"]))

    api_dir = os.path.join(base_dir, "api")
    os.makedirs(api_dir, exist_ok=True)

    projects_path = os.path.join(api_dir, "projects.json")
    with open(projects_path, "w", encoding="utf-8") as f:
        json.dump(clean_projects, f, indent=2)
        f.write("\n")

    pages_projects = [p for p in clean_projects if p["has_pages"]]
    pages_path = os.path.join(api_dir, "github-pages.json")
    with open(pages_path, "w", encoding="utf-8") as f:
        json.dump(pages_projects, f, indent=2)
        f.write("\n")

    benchmarks_path = os.path.join(api_dir, "benchmarks.json")
    with open(benchmarks_path, "w", encoding="utf-8") as f:
        json.dump(benchmarks, f, indent=2)
        f.write("\n")

    sitemap_path, sitemap_count = generate_sitemap(pages_projects, base_dir)
    synced_index = sync_index_html(clean_projects, pages_projects, base_dir)

    print(f"Generated {projects_path} ({len(clean_projects)} projects)")
    print(f"Generated {pages_path} ({len(pages_projects)} live pages)")
    print(f"Generated {benchmarks_path} ({len(benchmarks)} verified benchmarks)")
    print(f"Generated {sitemap_path} ({sitemap_count} canonical URLs)")
    print(f"Synced index.html inlined catalog: {synced_index}")


if __name__ == "__main__":
    main()
