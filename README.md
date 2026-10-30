# bhubbard.github.io

[![Live Demo](https://img.shields.io/badge/Live%20Demo-code.brandonhubbard.com-brightgreen?logo=github)](https://code.brandonhubbard.com/)

Official open source software portal and flagship engineering hub for **Brandon Hubbard** ([brandonhubbard.com](https://brandonhubbard.com)).

Built in accordance with strict **Swiss Modernist Grid Design Standards** (dark mode `#0a0a0a`, 0px border-radius, `Plus Jakarta Sans` & `JetBrains Mono` typography).

> 🎮 **Live Interactive Visualizer & Demo:** [bhubbard.github.io on code.brandonhubbard.com](https://code.brandonhubbard.com/)

---

## 🛡️ The Flare Suite (Cloudflare Developer Ecosystem)

A unified suite of high-throughput compiled Rust binaries engineered for Cloudflare Workers, Pages, and edge architectures:

1. 🛡️ **[`flareguard`](https://code.brandonhubbard.com/flareguard/)** ([GitHub](https://github.com/bhubbard/flareguard)) — Cloudflare Security, Secret Leaks, Binding Validation, Zone Posture, Origin IP Hunting.
   ```bash
   cargo install flareguard
   ```
2. ⚡ **[`flareperf`](https://code.brandonhubbard.com/flareperf/)** ([GitHub](https://github.com/bhubbard/flareperf)) — Edge Performance, Bundle Budgets, V8 Isolate Cold-Start, 50-Subrequest Limits, D1 Batching.
   ```bash
   cargo install flareperf
   ```
3. 🔍 **[`flarelint`](https://code.brandonhubbard.com/flarelint/)** ([GitHub](https://github.com/bhubbard/flarelint)) — OXC-Powered AST Static Analysis, Node.js Compatibility, ctx.waitUntil Linter, Durable Objects Safety.
   ```bash
   cargo install flarelint
   ```
4. 🔄 **[`flareops`](https://code.brandonhubbard.com/flareops/)** ([GitHub](https://github.com/bhubbard/flareops)) — DevEx, Wrangler Binding Sync, .dev.vars Migrations, _routes.json Optimizer.
   ```bash
   cargo install flareops
   ```

---

## 🤖 Astro Chrome Built-in AI Suite (13 Packages)

Zero-cost, zero-latency developer tooling powered directly by on-device **Gemini Nano**:

- **[`astro-client-directive-ai`](https://code.brandonhubbard.com/astro-client-directive-ai/)** ([GitHub](https://github.com/bhubbard/astro-client-directive-ai)) — Custom hydration directive (`client:ai-ready`) for Gemini Nano.
- **[`astro-rehype-nano-code`](https://code.brandonhubbard.com/astro-rehype-nano-code/)** ([GitHub](https://github.com/bhubbard/astro-rehype-nano-code)) — Zero-JS interactive code explainer and annotations.
- **[`astro-prefetch-ai-brief`](https://code.brandonhubbard.com/astro-prefetch-ai-brief/)** ([GitHub](https://github.com/bhubbard/astro-prefetch-ai-brief)) — 15-word AI link hover summaries via Chrome Summarizer API.
- **[`astro-dev-audit-nano`](https://code.brandonhubbard.com/astro-dev-audit-nano/)** ([GitHub](https://github.com/bhubbard/astro-dev-audit-nano)) — Dev Toolbar WCAG a11y, heading hierarchy, & SEO live auditor.
- **[`astro-dev-copy-optimizer`](https://code.brandonhubbard.com/astro-dev-copy-optimizer/)** ([GitHub](https://github.com/bhubbard/astro-dev-copy-optimizer)) — In-browser copy tuner & tone rewriter with 1-click clipboard copy.
- **[`astro-og-smart-crop`](https://code.brandonhubbard.com/astro-og-smart-crop/)** ([GitHub](https://github.com/bhubbard/astro-og-smart-crop)) — Dynamic social card previews & character-budgeted headline optimizer.
- **[`astro-schema-ld-verifier`](https://code.brandonhubbard.com/astro-schema-ld-verifier/)** ([GitHub](https://github.com/bhubbard/astro-schema-ld-verifier)) — JSON-LD semantics & microdata auditor against rendered DOM.
- **[`astro-dev-i18n-coverage`](https://code.brandonhubbard.com/astro-dev-i18n-coverage/)** ([GitHub](https://github.com/bhubbard/astro-dev-i18n-coverage)) — Dev-time missing translation finder with contextual locale export.
- **[`astro-dev-content-linter`](https://code.brandonhubbard.com/astro-dev-content-linter/)** ([GitHub](https://github.com/bhubbard/astro-dev-content-linter)) — Style guide, tone, jargon, & reading level linter.
- **[`astro-dev-schema-scaffolder`](https://code.brandonhubbard.com/astro-dev-schema-scaffolder/)** ([GitHub](https://github.com/bhubbard/astro-dev-schema-scaffolder)) — Instant Schema.org JSON-LD microdata generator.
- **[`astro-dev-mock-generator`](https://code.brandonhubbard.com/astro-dev-mock-generator/)** ([GitHub](https://github.com/bhubbard/astro-dev-mock-generator)) — Synthetic mock data generator for Content Collections Zod schemas.
- **[`astro-dev-broken-anchor-healer`](https://code.brandonhubbard.com/astro-dev-broken-anchor-healer/)** ([GitHub](https://github.com/bhubbard/astro-dev-broken-anchor-healer)) — Smart anchor link validator & semantic heading matcher.
- **[`astro-dev-island-hydration-advisor`](https://code.brandonhubbard.com/astro-dev-island-hydration-advisor/)** ([GitHub](https://github.com/bhubbard/astro-dev-island-hydration-advisor)) — Island hydration inspector & below-the-fold advisor.

---

## 🦀 High-Throughput Rust Ports & Verified Benchmark Suite (40 Verified Benchmarks)

Native, compiled, SIMD-accelerated Rust ports engineered to replace heavy Python, C++, and Electron runtimes with sub-millisecond execution and fractional memory footprints. Every project below features an empirical `BENCHMARKS.md` report comparing it directly to the original reference implementation:

| Project | Original Reference | Domain / Purpose | Speedup Factor | Live Demo / Docs | Benchmarks |
| :--- | :--- | :--- | :---: | :---: | :---: |
| ⚡ **`zev-rs`** | LLM Routers | Zero-token mathematical router | **Instant (5.8 µs)** | [Live Site](https://code.brandonhubbard.com/zev-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/zev-rs/blob/main/BENCHMARKS.md) |
| 🍏 **`apfel-rs`** | PyTorch / HF | Apple Silicon FoundationModels | **11.4× faster** | [Live Site](https://code.brandonhubbard.com/apfel-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/apfel-rs/blob/main/BENCHMARKS.md) |
| 🎯 **`bullet3-rs`** | Bullet3 (C++) | 3D Rigid/Soft-body Physics Engine | **4.2× faster** | [Live Site](https://code.brandonhubbard.com/bullet3-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/bullet3-rs/blob/main/BENCHMARKS.md) |
| 🚦 **`uxsim-rs`** | UXsim (Python) | Macroscopic City-Wide Traffic Simulator | **1,620× faster** | [Live Site](https://code.brandonhubbard.com/uxsim-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/uxsim-rs/blob/main/BENCHMARKS.md) |
| 📈 **`timesfm-rs`** | Google TimesFM (JAX) | Zero-Shot Time-Series Forecasting | **13.4× faster** | [Live Site](https://code.brandonhubbard.com/timesfm-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/timesfm-rs/blob/main/BENCHMARKS.md) |
| 🎬 **`comfyui-ltxvideo-mlx-rs`** | ComfyUI LTX (PyTorch) | Cinematic DiT Video Generation | **4.8× faster** | [Live Site](https://code.brandonhubbard.com/comfyui-ltxvideo-mlx-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/comfyui-ltxvideo-mlx-rs/blob/main/BENCHMARKS.md) |
| 💬 **`mlx-gen-rs`** | mlx-lm (Python) | High-Throughput LLM Text Generation | **1.37× faster** | [Live Site](https://code.brandonhubbard.com/mlx-gen-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlx-gen-rs/blob/main/BENCHMARKS.md) |
| 🌍 **`translate-rs`** | LibreTranslate (Python) | Offline Neural Machine Translation | **11.1× faster** | [Live Site](https://code.brandonhubbard.com/translate-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/translate-rs/blob/main/BENCHMARKS.md) |
| 👁️ **`auge-rs`** | GazeTracking (Python) | 3,200 FPS Eye & Gaze Estimation | **47.4× faster** | [Live Site](https://code.brandonhubbard.com/auge-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/auge-rs/blob/main/BENCHMARKS.md) |
| 📹 **`yt-dlp-rs`** | yt-dlp (Python) | Zero-Python Video Metadata Extractor | **23.3× faster** | [Live Site](https://code.brandonhubbard.com/yt-dlp-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/yt-dlp-rs/blob/main/BENCHMARKS.md) |
| ✂️ **`lossless-cut-rs`** | LosslessCut (Electron) | Zero-Loss Keyframe Video Trimmer | **154× faster** | [Live Site](https://code.brandonhubbard.com/lossless-cut-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/lossless-cut-rs/blob/main/BENCHMARKS.md) |
| 🎞️ **`handbrake-rs`** | HandBrake CLI (C) | Hardware Video Transcode Orchestration | **44.0× faster** | [Live Site](https://code.brandonhubbard.com/handbrake-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/handbrake-rs/blob/main/BENCHMARKS.md) |
| 🫒 **`olive-rs`** | Olive (C++) | Non-Linear Node Compositing Engine | **7.2× faster** | [Live Site](https://code.brandonhubbard.com/olive-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/olive-rs/blob/main/BENCHMARKS.md) |
| 📽️ **`mlt-rs`** | MLT Framework (C) | Real-Time Video Filter Graph Engine | **3.7× faster** | [Live Site](https://code.brandonhubbard.com/mlt-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlt-rs/blob/main/BENCHMARKS.md) |
| 🎨 **`mflux-rs`** | mflux (Python MLX) | Flux.1-schnell Image Generation | **1.89× faster** | [Live Site](https://code.brandonhubbard.com/mflux-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mflux-rs/blob/main/BENCHMARKS.md) |
| 🎙️ **`mlx-audio-rs`** | mlx-audio (Python) | Speech-to-Text & Audio Synthesis | **2.3× faster** | [Live Site](https://code.brandonhubbard.com/mlx-audio-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlx-audio-rs/blob/main/BENCHMARKS.md) |
| 🔍 **`mlx-embeddings-rs`** | sentence-transformers | Vector Embeddings & Similarity | **5.4× faster** | [Live Site](https://code.brandonhubbard.com/mlx-embeddings-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlx-embeddings-rs/blob/main/BENCHMARKS.md) |
| 💡 **`lux-rs`** | Lux (Python / Elixir) | Volumetric Lighting & Tensor Dispatch | **132× faster** | [Live Site](https://code.brandonhubbard.com/lux-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/lux-rs/blob/main/BENCHMARKS.md) |
| 🧠 **`open-generative-ai-rs`** | Python GenAI Pipelines | Generative AI Orchestration Runtime | **60.7× faster** | [Live Site](https://code.brandonhubbard.com/open-generative-ai-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/open-generative-ai-rs/blob/main/BENCHMARKS.md) |
| 🎥 **`open-higgsfield-ai-rs`** | Higgsfield (Python) | Camera Motion & Neural Video Synthesis | **46.3× faster** | [Live Site](https://code.brandonhubbard.com/open-higgsfield-ai-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/open-higgsfield-ai-rs/blob/main/BENCHMARKS.md) |
| 🩺 **`clippy-cf-reporter`** | Node.js Action Runner | Clippy SARIF & PR Annotation Reporter | **181× faster** | [Live Site](https://code.brandonhubbard.com/clippy-cf-reporter/) | [`BENCHMARKS.md`](https://github.com/bhubbard/clippy-cf-reporter/blob/main/BENCHMARKS.md) |
| ⚡ **`vite-plus-commitlint`** | @commitlint/cli (Node) | Native Git Commit Hook Linter | **525× faster** | [Live Site](https://code.brandonhubbard.com/vite-plus-commitlint/) | [`BENCHMARKS.md`](https://github.com/bhubbard/vite-plus-commitlint/blob/main/BENCHMARKS.md) |
| 🧩 **`vite-plus-kumo-ui`** | Storybook / Vite (Node) | Kumo UI Spec & Token Bundler | **180× faster** | [Live Site](https://code.brandonhubbard.com/vite-plus-kumo-ui/) | [`BENCHMARKS.md`](https://github.com/bhubbard/vite-plus-kumo-ui/blob/main/BENCHMARKS.md) |
| 🏎️ **`tlab-vehicle-physics-rs`**| Vehicle Physics (C#) | Pacejka Magic Formula Vehicle Dynamics | **8.4× faster** | [Live Site](https://code.brandonhubbard.com/tlab-vehicle-physics-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/tlab-vehicle-physics-rs/blob/main/BENCHMARKS.md) |
| 🚗 **`simplecar2-rs`** | SimpleCar2 (GDScript) | Arcade Simulation Vehicle Physics | **6.8× faster** | [Live Site](https://code.brandonhubbard.com/simplecar2-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/simplecar2-rs/blob/main/BENCHMARKS.md) |
| 🚦 **`sumo-rs`** | Eclipse SUMO (C++) | Microscopic Urban Mobility Simulator | **12.1× faster** | [Live Site](https://code.brandonhubbard.com/sumo-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/sumo-rs/blob/main/BENCHMARKS.md) |
| 🚶 **`detour-crowd-rs`** | Recast/Detour (C++) | Navmesh Crowd & Agent Navigation | **5.6× faster** | [Live Site](https://code.brandonhubbard.com/detour-crowd-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/detour-crowd-rs/blob/main/BENCHMARKS.md) |
| 🦹 **`openrw-rs`** | OpenRW (C++) | GTA III Re-implementation Components | **4.1× faster** | [Live Site](https://code.brandonhubbard.com/openrw-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/openrw-rs/blob/main/BENCHMARKS.md) |
| 📡 **`gambetta-netcode-rs`** | Gambetta Netcode (JS) | Client-side Prediction & Reconciliation | **14.2× faster** | [Live Site](https://code.brandonhubbard.com/gambetta-netcode-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/gambetta-netcode-rs/blob/main/BENCHMARKS.md) |
| 🔊 **`sfxr-rs`** | sfxr (C / SDL) | 8-bit Procedural Sound Synthesizer | **18.0× faster** | [Live Site](https://code.brandonhubbard.com/sfxr-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/sfxr-rs/blob/main/BENCHMARKS.md) |
| 📐 **`sdf-math-rs`** | Inigo Quilez (GLSL) | 2D & 3D Signed Distance Functions | **24.5× faster** | [Live Site](https://code.brandonhubbard.com/sdf-math-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/sdf-math-rs/blob/main/BENCHMARKS.md) |
| 🎯 **`tactical-ai-rs`** | Game AI Pro (C#) | Tactical Cover & Flanking Behavior Trees | **9.2× faster** | [Live Site](https://code.brandonhubbard.com/tactical-ai-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/tactical-ai-rs/blob/main/BENCHMARKS.md) |
| 💬 **`dialogger-rs`** | Dialogger (C#) | Nonlinear Dialogue Graph Traversal | **16.5× faster** | [Live Site](https://code.brandonhubbard.com/dialogger-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/dialogger-rs/blob/main/BENCHMARKS.md) |
| ⭕ **`radial-menu-rs`** | RadialMenu (Lua/CEF) | 60 FPS Pie & Radial Navigation | **28.0× faster** | [Live Site](https://code.brandonhubbard.com/radial-menu-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/radial-menu-rs/blob/main/BENCHMARKS.md) |
| 🧭 **`minimal-hud-rs`** | Minimal-HUD (Lua) | Low-Latency In-Game HUD Elements | **42.0× faster** | [Live Site](https://code.brandonhubbard.com/minimal-hud-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/minimal-hud-rs/blob/main/BENCHMARKS.md) |
| 🗺️ **`vhud-rs`** | V-HUD (Lua) | Mini-Map Radar & Vector Navigation | **35.0× faster** | [Live Site](https://code.brandonhubbard.com/vhud-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/vhud-rs/blob/main/BENCHMARKS.md) |
| 🤸 **`active-ragdoll-rs`** | Active Ragdoll (Unity) | Physics-Driven Character Ragdolls | **7.8× faster** | [Live Site](https://code.brandonhubbard.com/active-ragdoll-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/active-ragdoll-rs/blob/main/BENCHMARKS.md) |
| 🎥 **`poormans-camera-rs`** | Poor Man's Camera (C#) | 3D Cinematic Camera Rigs | **18.5× faster** | [Live Site](https://code.brandonhubbard.com/poormans-camera-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/poormans-camera-rs/blob/main/BENCHMARKS.md) |
| 🛡️ **`defy-rs`** | PoliceTools / Defy | Entity Dispatch & Tracking Logic | **22.0× faster** | [Live Site](https://code.brandonhubbard.com/defy-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/defy-rs/blob/main/BENCHMARKS.md) |
| ⚙️ **`aesir-utils-rs`** | AesirUtils (FiveM) | Memory Buffer & Safezone Utilities | **45.0× faster** | [Live Site](https://code.brandonhubbard.com/aesir-utils-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/aesir-utils-rs/blob/main/BENCHMARKS.md) |

---

## 🐝 Autonomous AI Swarms, 3D Generative Engines & Media Systems in Rust

- 🐝 **[`nanoswarm-rs`](https://code.brandonhubbard.com/nanoswarm-rs/)** ([GitHub](https://github.com/bhubbard/nanoswarm-rs)) — 100% on-device autonomous AI agent swarm in native Rust (`<30MB` RAM, `5.8µs` SIMD routing).
- 🧊 **[`watertight-meshes-rs`](https://code.brandonhubbard.com/watertight-meshes-rs/)** ([GitHub](https://github.com/bhubbard/watertight-meshes-rs)) — High-performance Rust engine and CLI for generating, validating, voxelizing, and repairing 100% watertight 3D AI meshes.
- 🌌 **[`lyra-rs`](https://code.brandonhubbard.com/lyra-rs/)** ([GitHub](https://github.com/bhubbard/lyra-rs)) — Pure Rust fork and high-performance engine for NVIDIA Project Lyra: Open Generative 3D World Models and Gaussian Splatting.
- 🎨 **[`hunyuan3d-rs`](https://code.brandonhubbard.com/hunyuan3d-rs/)** ([GitHub](https://github.com/bhubbard/hunyuan3d-rs)) — Pure Rust engine for Tencent Hunyuan3D-2.1: Generative 3D Asset Creation with PBR Textures.
- 📦 **[`box3d-rs`](https://code.brandonhubbard.com/box3d-rs/)** ([GitHub](https://github.com/bhubbard/box3d-rs)) — High-performance pure Rust 3D physics engine for games and robotics, forked from Erin Catto's Box3D.
- 🌊 **[`clearwater-rs`](https://code.brandonhubbard.com/clearwater-rs/)** ([GitHub](https://github.com/bhubbard/clearwater-rs)) — Real-time, photoreal shallow water physics and rendering engine in Rust.
- 🗿 **[`generate-glb-rs`](https://code.brandonhubbard.com/generate-glb-rs/)** ([GitHub](https://github.com/bhubbard/generate-glb-rs)) — Pure Rust CLI tool and server to generate 3D models in binary GLB format using LLaMA-Mesh AI.
- 🎞️ **[`ffmpeg-skill-rs`](https://code.brandonhubbard.com/ffmpeg-skill-rs/)** ([GitHub](https://github.com/bhubbard/ffmpeg-skill-rs)) — Deterministic FFmpeg tools and Model Context Protocol (MCP) server for AI agents in Rust.
- 🔎 **[`rea-rs`](https://code.brandonhubbard.com/rea-rs/)** ([GitHub](https://github.com/bhubbard/rea-rs)) — Memory-safe pure Rust CLI and MCP server for structured codebase investigation.
- 🖥️ **[`desktop-rs`](https://code.brandonhubbard.com/desktop-rs/)** ([GitHub](https://github.com/bhubbard/desktop-rs)) — Blazingly fast, lightweight pure-Rust fork of GitHub Desktop.
- 🎙️ **[`voicestudio-rs`](https://github.com/bhubbard/voicestudio-rs)** — Open-source, fully-local ElevenLabs alternative in Rust — voice cloning, design, video dubbing, and transcription.
- 🎬 **[`openmontage-rs`](https://github.com/bhubbard/openmontage-rs)** — Open-source, agentic video production system in Rust — pipelines, shot composition, timeline editing, and audio mixing.
- 🏟️ **[`agentarena-rs`](https://github.com/bhubbard/agentarena-rs)** — Dynamic simulation test bench and deterministic benchmark arena for AI agents across traffic, tactical combat, and crowd steering.
- 📡 **[`neteq-rs`](https://github.com/bhubbard/neteq-rs)** — Pure Rust standalone port of WebRTC NetEQ: adaptive audio jitter buffer, PLC, and WSOLA time-stretching.
- 🖼️ **[`upscayl-rs`](https://github.com/bhubbard/upscayl-rs)** — High-performance, pure-Rust native port and drop-in CLI replacement for Upscayl AI image upscaler.
- 🟠 **[`blender-rs`](https://github.com/bhubbard/blender-rs)** — Memory-safe, high-performance Rust port of the Blender 3D creation suite.

---

## 🌐 WordPress Modern Ecosystem & Bridges

- **[`wp-blockmarkup-mcp`](https://github.com/bhubbard/wp-blockmarkup-mcp)** — High-speed Rust Model Context Protocol (MCP) server for WordPress Gutenberg block grammar parsing.
- **[`wp-cloudflare-d1`](https://github.com/bhubbard/wp-cloudflare-d1)** — Native PHP class querying Cloudflare D1 serverless SQL database within WordPress.
- **[`wp-cloudflare-kv`](https://github.com/bhubbard/wp-cloudflare-kv)** — WordPress object and transient cache backend powered by Cloudflare KV edge storage.
- **[`wp-pressable-api`](https://github.com/bhubbard/wp-pressable-api)** & **[`pressable-cli`](https://github.com/bhubbard/pressable-cli)** — PHP SDK and TypeScript CLI for Pressable Cloud management.
- **[`wp-theme-check-cli`](https://github.com/bhubbard/wp-theme-check-cli)** — Automated CI/CD quality gate for WordPress themes checking PHPCS, security, and standards.

---

## 📜 License

MIT © 2026 Brandon Hubbard. Code as Craft. Radical Ownership.
