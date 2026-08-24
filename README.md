# bhubbard.github.io

Official open source software portal and flagship engineering hub for **Brandon Hubbard** ([brandonhubbard.com](https://brandonhubbard.com)).

Built in accordance with strict **Swiss Modernist Grid Design Standards** (dark mode `#0a0a0a`, 0px border-radius, `Plus Jakarta Sans` & `JetBrains Mono` typography).

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

## 🦀 Rust & Edge Developer Tools

- **`oxc-astro-cf`** — Static AST linter detecting illegal Cloudflare binding access.
- **`edge-bundle-budget`** — Gzip/Brotli bundle size analyzer auditing quotas against Cloudflare limits.
- **`cf-origin-hunter`** — Discovers unmasked origin IPs behind Cloudflare proxies via CT logs & DNS records.
- **`cf-zone-auditor`** — Multi-zone Cloudflare security auditor verifying SSL/TLS, HSTS, and DNSSEC.
- **`astro-binding-sync`** — Synchronizes `wrangler.jsonc` bindings with TypeScript `App.Locals`.
- **`cf-secret-leak-guard`** — High-throughput scanner preventing secrets leaking into client bundles.
- **`wp-blockmarkup-mcp`** — High-performance Rust Model Context Protocol (MCP) server for Gutenberg block schemas.

---

## 🌐 WordPress Modern Ecosystem & Bridges

- **`wp-cloudflare-d1`** — Native PHP class querying Cloudflare D1 serverless SQL database within WordPress.
- **`wp-cloudflare-kv`** — Modern WordPress library interfacing with Cloudflare KV edge storage.
- **`wp-gemini-cleaner`** — WordPress tool for sanitizing Gemini AI-generated editorial content.
- **`wp-theme-check-cli`** — TypeScript CLI port of the WordPress Theme Check tool.

---

## 📜 License

MIT © 2026 Brandon Hubbard. Code as Craft. Radical Ownership.
