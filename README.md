# bhubbard.github.io

[![Live Demo](https://img.shields.io/badge/Live%20Demo-code.brandonhubbard.com-brightgreen?logo=github)](https://code.brandonhubbard.com/)

Official open source software portal and flagship engineering hub for **Brandon Hubbard** ([brandonhubbard.com](https://brandonhubbard.com)).

Built in accordance with strict **Swiss Modernist Grid Design Standards** (dark mode `#0a0a0a`, 0px border-radius, `Plus Jakarta Sans` & `JetBrains Mono` typography).

> 🎮 **Live Interactive Visualizer & Demo:** [bhubbard.github.io on code.brandonhubbard.com](https://code.brandonhubbard.com/)

---

## 🛡️ The Flare Suite (Cloudflare Developer Ecosystem)

A unified suite of high-throughput compiled Rust binaries engineered for Cloudflare Workers, Pages, and edge architectures:

1. 🛡️ **[`flareguard`](https://bhubbard.github.io/flareguard/)** ([GitHub](https://github.com/bhubbard/flareguard)) — Cloudflare Security, Secret Leaks, Binding Validation, Zone Posture, Origin IP Hunting.
   ```bash
   cargo install flareguard
   ```
2. ⚡ **[`flareperf`](https://bhubbard.github.io/flareperf/)** ([GitHub](https://github.com/bhubbard/flareperf)) — Edge Performance, Bundle Budgets, V8 Isolate Cold-Start, 50-Subrequest Limits, D1 Batching.
   ```bash
   cargo install flareperf
   ```
3. 🔍 **[`flarelint`](https://bhubbard.github.io/flarelint/)** ([GitHub](https://github.com/bhubbard/flarelint)) — OXC-Powered AST Static Analysis, Node.js Compatibility, ctx.waitUntil Linter, Durable Objects Safety.
   ```bash
   cargo install flarelint
   ```
4. 🔄 **[`flareops`](https://bhubbard.github.io/flareops/)** ([GitHub](https://github.com/bhubbard/flareops)) — DevEx, Wrangler Binding Sync, .dev.vars Migrations, _routes.json Optimizer.
   ```bash
   cargo install flareops
   ```

---

## 🤖 Astro Chrome Built-in AI Suite (13 Packages)

Zero-cost, zero-latency developer tooling powered directly by on-device **Gemini Nano**:

- **[`astro-client-directive-ai`](./astro-client-directive-ai/)** ([GitHub](https://github.com/bhubbard/astro-client-directive-ai)) — Custom hydration directive (`client:ai-ready`) for Gemini Nano.
- **[`astro-rehype-nano-code`](./astro-rehype-nano-code/)** ([GitHub](https://github.com/bhubbard/astro-rehype-nano-code)) — Zero-JS interactive code explainer and annotations.
- **[`astro-prefetch-ai-brief`](./astro-prefetch-ai-brief/)** ([GitHub](https://github.com/bhubbard/astro-prefetch-ai-brief)) — 15-word AI link hover summaries via Chrome Summarizer API.
- **[`astro-dev-audit-nano`](./astro-dev-audit-nano/)** ([GitHub](https://github.com/bhubbard/astro-dev-audit-nano)) — Dev Toolbar WCAG a11y, heading hierarchy, & SEO live auditor.
- **[`astro-dev-copy-optimizer`](./astro-dev-copy-optimizer/)** ([GitHub](https://github.com/bhubbard/astro-dev-copy-optimizer)) — In-browser copy tuner & tone rewriter with 1-click clipboard copy.
- **[`astro-og-smart-crop`](./astro-og-smart-crop/)** ([GitHub](https://github.com/bhubbard/astro-og-smart-crop)) — Dynamic social card previews & character-budgeted headline optimizer.
- **[`astro-schema-ld-verifier`](./astro-schema-ld-verifier/)** ([GitHub](https://github.com/bhubbard/astro-schema-ld-verifier)) — JSON-LD semantics & microdata auditor against rendered DOM.
- **[`astro-dev-i18n-coverage`](./astro-dev-i18n-coverage/)** ([GitHub](https://github.com/bhubbard/astro-dev-i18n-coverage)) — Dev-time missing translation finder with contextual locale export.
- **[`astro-dev-content-linter`](./astro-dev-content-linter/)** ([GitHub](https://github.com/bhubbard/astro-dev-content-linter)) — Style guide, tone, jargon, & reading level linter.
- **[`astro-dev-schema-scaffolder`](./astro-dev-schema-scaffolder/)** ([GitHub](https://github.com/bhubbard/astro-dev-schema-scaffolder)) — Instant Schema.org JSON-LD microdata generator.
- **[`astro-dev-mock-generator`](./astro-dev-mock-generator/)** ([GitHub](https://github.com/bhubbard/astro-dev-mock-generator)) — Synthetic mock data generator for Content Collections Zod schemas.
- **[`astro-dev-broken-anchor-healer`](./astro-dev-broken-anchor-healer/)** ([GitHub](https://github.com/bhubbard/astro-dev-broken-anchor-healer)) — Smart anchor link validator & semantic heading matcher.
- **[`astro-dev-island-hydration-advisor`](./astro-dev-island-hydration-advisor/)** ([GitHub](https://github.com/bhubbard/astro-dev-island-hydration-advisor)) — Island hydration inspector & below-the-fold advisor.

---

## 🦀 High-Throughput Rust Ports & Verified Benchmark Suite

Native, compiled, SIMD-accelerated Rust ports engineered to replace heavy Python, C++, and Electron runtimes with sub-millisecond execution and fractional memory footprints. Every project features an empirical benchmark report comparing it directly to the original reference implementation:

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
| 🛡️ **`unified-audit-rs`** | ESLint + npm audit | Sub-100ms Security & AST Auditor | **140.9× faster** | [Live Site](https://code.brandonhubbard.com/unified-audit-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/unified-audit-rs/blob/main/BENCHMARKS.md) |
| 📹 **`yt-dlp-rs`** | yt-dlp (Python) | Zero-Python Video Metadata Extractor | **23.3× faster** | [Live Site](https://code.brandonhubbard.com/yt-dlp-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/yt-dlp-rs/blob/main/BENCHMARKS.md) |
| ✂️ **`lossless-cut-rs`** | LosslessCut (Electron) | Zero-Loss Keyframe Video Trimmer | **154× faster** | [Live Site](https://code.brandonhubbard.com/lossless-cut-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/lossless-cut-rs/blob/main/BENCHMARKS.md) |
| 🎞️ **`handbrake-rs`** | HandBrake CLI (C) | Hardware Video Transcode Orchestration | **44.0× faster** | [Live Site](https://code.brandonhubbard.com/handbrake-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/handbrake-rs/blob/main/BENCHMARKS.md) |
| 🫒 **`olive-rs`** | Olive (C++) | Non-Linear Node Compositing Engine | **7.2× faster** | [Live Site](https://code.brandonhubbard.com/olive-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/olive-rs/blob/main/BENCHMARKS.md) |
| 📽️ **`mlt-rs`** | MLT Framework (C) | Real-Time Video Filter Graph Engine | **3.7× faster** | [Live Site](https://code.brandonhubbard.com/mlt-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlt-rs/blob/main/BENCHMARKS.md) |
| 🎨 **`mflux-rs`** | mflux (Python MLX) | Flux.1-schnell Image Generation | **1.89× faster** | [Live Site](https://code.brandonhubbard.com/mflux-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mflux-rs/blob/main/BENCHMARKS.md) |
| 🎙️ **`mlx-audio-rs`** | mlx-audio (Python) | Speech-to-Text & Audio Synthesis | **2.3× faster** | [Live Site](https://code.brandonhubbard.com/mlx-audio-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlx-audio-rs/blob/main/BENCHMARKS.md) |
| 🔍 **`mlx-embeddings-rs`** | sentence-transformers | Vector Embeddings & Similarity | **5.4× faster** | [Live Site](https://code.brandonhubbard.com/mlx-embeddings-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlx-embeddings-rs/blob/main/BENCHMARKS.md) |
| 🌐 **`mlx-serve-rs`** | vLLM / FastAPI (Python) | High-Concurrency Local API Server | **7.8× higher RPS** | [Live Site](https://code.brandonhubbard.com/mlx-serve-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlx-serve-rs/blob/main/BENCHMARKS.md) |
| 👁️‍🗨️ **`mlx-vlm-rs`** | mlx-vlm (Python) | Multimodal Vision-Language Inference | **4.4× faster** | [Live Site](https://code.brandonhubbard.com/mlx-vlm-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/mlx-vlm-rs/blob/main/BENCHMARKS.md) |
| 🏎️ **`tlab-vehicle-physics-rs`**| Vehicle Physics (C++) | Pacejka Magic Formula Vehicle Dynamics | **8.4× faster** | [Live Site](https://code.brandonhubbard.com/tlab-vehicle-physics-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/tlab-vehicle-physics-rs/blob/main/BENCHMARKS.md) |
| 🚗 **`simplecar2-rs`** | SimpleCar (C++) | Arcade Simulation Vehicle Physics | **6.8× faster** | [Live Site](https://code.brandonhubbard.com/simplecar2-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/simplecar2-rs/blob/main/BENCHMARKS.md) |
| 🚦 **`sumo-rs`** | SUMO (C++) | Microscopic Urban Mobility Simulator | **12.1× faster** | [Live Site](https://code.brandonhubbard.com/sumo-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/sumo-rs/blob/main/BENCHMARKS.md) |
| 🚶 **`detour-crowd-rs`** | Recast/Detour (C++) | Navmesh Crowd & Agent Navigation | **5.6× faster** | [Live Site](https://code.brandonhubbard.com/detour-crowd-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/detour-crowd-rs/blob/main/BENCHMARKS.md) |
| 🕹️ **`godot-rs`** | Godot Engine (C++) | Core Math & Scene Tree Traversal | **3.8× faster** | [Live Site](https://code.brandonhubbard.com/godot-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/godot-rs/blob/main/BENCHMARKS.md) |
| 🦹 **`openrw-rs`** | OpenRW (C++) | GTA III Re-implementation Components | **4.1× faster** | [Live Site](https://code.brandonhubbard.com/openrw-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/openrw-rs/blob/main/BENCHMARKS.md) |
| ⚡ **`hyperframes-rs`** | HyperFrames (JS) | 120 FPS Declarative Motion Engine | **8.2× faster** | [Live Site](https://code.brandonhubbard.com/hyperframes-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/hyperframes-rs/blob/main/BENCHMARKS.md) |
| 📡 **`gambetta-netcode-rs`** | Gambetta Netcode | Client-side Prediction & Reconciliation | **14.2× faster** | [Live Site](https://code.brandonhubbard.com/gambetta-netcode-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/gambetta-netcode-rs/blob/main/BENCHMARKS.md) |
| 🔊 **`sfxr-rs`** | sfxr (C++) | 8-bit Procedural Sound Synthesizer | **18.0× faster** | [Live Site](https://code.brandonhubbard.com/sfxr-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/sfxr-rs/blob/main/BENCHMARKS.md) |
| 📐 **`sdf-math-rs`** | Inigo Quilez (GLSL) | 2D & 3D Signed Distance Functions | **24.5× faster** | [Live Site](https://code.brandonhubbard.com/sdf-math-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/sdf-math-rs/blob/main/BENCHMARKS.md) |
| 🎯 **`tactical-ai-rs`** | Tactical AI (C++) | Tactical Cover & Flanking Behavior Trees | **9.2× faster** | [Live Site](https://code.brandonhubbard.com/tactical-ai-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/tactical-ai-rs/blob/main/BENCHMARKS.md) |
| 📹 **`video-use-rs`** | Video Utilities | High-Performance Transcode Pipelines | **12.4× faster** | [Live Site](https://code.brandonhubbard.com/video-use-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/video-use-rs/blob/main/BENCHMARKS.md) |
| 📱 **`npwd-rs`** | NPWD (FiveM / React) | In-Game Smartphone Simulation Backend | **32.0× faster** | [Live Site](https://code.brandonhubbard.com/npwd-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/npwd-rs/blob/main/BENCHMARKS.md) |
| 💬 **`dialogger-rs`** | Dialogger (C#) | Nonlinear Dialogue Graph Traversal | **16.5× faster** | [Live Site](https://code.brandonhubbard.com/dialogger-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/dialogger-rs/blob/main/BENCHMARKS.md) |
| ⭕ **`radial-menu-rs`** | RadialMenu (JS) | 60 FPS Pie & Radial Navigation | **28.0× faster** | [Live Site](https://code.brandonhubbard.com/radial-menu-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/radial-menu-rs/blob/main/BENCHMARKS.md) |
| 🧭 **`minimal-hud-rs`** | Minimal-HUD (Lua) | Low-Latency In-Game HUD Elements | **42.0× faster** | [Live Site](https://code.brandonhubbard.com/minimal-hud-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/minimal-hud-rs/blob/main/BENCHMARKS.md) |
| 🗺️ **`vhud-rs`** | V-HUD (Lua) | Mini-Map Radar & Vector Navigation | **35.0× faster** | [Live Site](https://code.brandonhubbard.com/vhud-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/vhud-rs/blob/main/BENCHMARKS.md) |
| 🤸 **`active-ragdoll-rs`** | Active Ragdoll (Unity) | Physics-Driven Character Ragdolls | **7.8× faster** | [Live Site](https://code.brandonhubbard.com/active-ragdoll-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/active-ragdoll-rs/blob/main/BENCHMARKS.md) |
| 🎥 **`poormans-camera-rs`** | Poor Man's Camera | 3D Cinematic Camera Rigs | **18.5× faster** | [Live Site](https://code.brandonhubbard.com/poormans-camera-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/poormans-camera-rs/blob/main/BENCHMARKS.md) |
| 🛡️ **`defy-rs`** | PoliceTools / Defy | Entity Dispatch & Tracking Logic | **22.0× faster** | [Live Site](https://code.brandonhubbard.com/defy-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/defy-rs/blob/main/BENCHMARKS.md) |
| ⚙️ **`aesir-utils-rs`** | AesirUtils (FiveM) | Memory Buffer & Safezone Utilities | **45.0× faster** | [Live Site](https://code.brandonhubbard.com/aesir-utils-rs/) | [`BENCHMARKS.md`](https://github.com/bhubbard/aesir-utils-rs/blob/main/BENCHMARKS.md) |


---

## 🌐 WordPress Modern Ecosystem & Bridges

- **`wp-cloudflare-d1`** — Native PHP class querying Cloudflare D1 serverless SQL database within WordPress.
- **`wp-cloudflare-kv`** — Modern WordPress library interfacing with Cloudflare KV edge storage.
- **`wp-gemini-cleaner`** — WordPress tool for sanitizing Gemini AI-generated editorial content.
- **`wp-theme-check-cli`** — TypeScript CLI port of the WordPress Theme Check tool.

---

## 📜 License

MIT © 2026 Brandon Hubbard. Code as Craft. Radical Ownership.
