# Chapter Templates

Starting point for planning chapters. Adapt to each project's specifics.

## AI Tool Template

For projects that are AI coding assistants, prompt engineering tools, AI agents, or AI workflow engines.

### Brief (7-8 chapters)

| # | Chapter | Source files to read |
|---|---------|---------------------|
| 1 | Overview — what it does, tech stack, key numbers | README, package.json |
| 2 | Architecture — component diagram, data flow | ARCHITECTURE.md or main source files |
| 3 | Core mechanism — the main innovation | Entry skill / core module |
| 4 | Skill/plugin system — how capabilities are organized | Skills directory, manifest |
| 5 | Key technical highlights — 3-5 innovations | Core source files |
| 6 | Comparison with alternatives | README alternatives section, industry knowledge |
| 7 | Innovation summary + impact | Synthesized from above |

### Medium (12-15 chapters, extends Brief)

All Brief chapters (expanded), plus:

| # | Additional Chapter | Source files to read |
|---|-------------------|---------------------|
| 8 | Hook/event system | Hook scripts, event handlers |
| 9 | Prompt engineering deep dive | Key skill files, prompt templates |
| 10 | Multi-model / cross-review (if applicable) | Review-related source |
| 11 | Security model | Security-related source, safety checks |
| 12 | Cross-platform support | Platform adapters, tool mappings |
| 13 | Developer workflow & testing | Test files, CI config |
| 14 | Design philosophy / ethos | ETHOS.md, CONTRIBUTING.md, code comments |

### Deep (15-20 chapters, extends Medium)

All Medium chapters (expanded), plus:

| # | Additional Chapter | Source files to read |
|---|-------------------|---------------------|
| 15 | Design evolution — version history | Git history, CHANGELOG, code comments |
| 16 | Line-by-line analysis of core algorithm | Core module (full read) |
| 17 | Complete security model with attack scenarios | Security source, threat analysis |
| 18 | Error handling & edge cases | Error handling code, fallback logic |
| 19 | Build your own — reimplementation guide | Synthesized from understanding |
| 20 | Industry impact & predictions | Synthesized from analysis |

---

## Library Template

For projects that are reusable libraries, frameworks, or SDKs.

### Brief (7-8 chapters)

| # | Chapter | Source files to read |
|---|---------|---------------------|
| 1 | Overview — what problem it solves, API surface | README, src/index.ts |
| 2 | Architecture — module structure, public vs internal | Directory structure, exports |
| 3 | Core API walkthrough | Main source files |
| 4 | Configuration & customization | Config files, options types |
| 5 | Key technical highlights | Core algorithm source |
| 6 | Comparison with alternatives | README, npm/registry comparison |
| 7 | Getting started + recommended patterns | README, examples |

### Medium (12-15 chapters)

All Brief chapters (expanded), plus:

| # | Additional Chapter |
|---|-------------------|
| 8 | Type system design (if TypeScript) |
| 9 | Plugin/extension API |
| 10 | Error handling strategy |
| 11 | Performance characteristics |
| 12 | Testing strategy |
| 13 | Migration & backwards compatibility |
| 14 | Internal implementation details for key features |

### Deep (15-20 chapters)

All Medium chapters (expanded), plus:

| # | Additional Chapter |
|---|-------------------|
| 15 | Design evolution — API changes over versions |
| 16 | Line-by-line analysis of core algorithm |
| 17 | Edge cases & corner cases |
| 18 | Bundle size & tree-shaking analysis |
| 19 | Build your own — minimal reimplementation |
| 20 | Contribution guide & community patterns |

---

## Web App Template

For projects that are web applications, SaaS products, or full-stack projects.

### Brief (7-8 chapters)

| # | Chapter | Source files to read |
|---|---------|---------------------|
| 1 | Overview — what it does, tech stack, users | README, package.json |
| 2 | Architecture — frontend/backend split, services | Directory structure |
| 3 | Data model — database schema, key entities | Migrations, schema files |
| 4 | API surface — endpoints, auth model | Routes, controllers |
| 5 | Key technical highlights | Core feature source |
| 6 | Deployment & infrastructure | Docker, CI config, deploy scripts |
| 7 | Comparison with similar apps | Synthesized |

### Medium (12-15 chapters)

All Brief chapters (expanded), plus:

| # | Additional Chapter |
|---|-------------------|
| 8 | Authentication & authorization flow |
| 9 | State management (frontend) |
| 10 | Database access patterns |
| 11 | Caching strategy |
| 12 | Error handling & monitoring |
| 13 | Testing strategy |
| 14 | CI/CD pipeline |

### Deep (15-20 chapters)

All Medium chapters (expanded), plus:

| # | Additional Chapter |
|---|-------------------|
| 15 | Design evolution — feature history |
| 16 | Line-by-line analysis of core feature |
| 17 | Security model — threat analysis |
| 18 | Performance optimization techniques |
| 19 | Build your own — minimal version |
| 20 | Scaling considerations & bottlenecks |

---

## CLI Tool Template

For projects that are command-line tools, build tools, or developer utilities.

### Brief (7-8 chapters)

| # | Chapter | Source files to read |
|---|---------|---------------------|
| 1 | Overview — what it does, installation, usage | README, package.json |
| 2 | Architecture — command structure, plugin system | Directory structure, bin/ |
| 3 | Command handling — how commands are parsed and executed | CLI entry point |
| 4 | Configuration system | Config files, options parsing |
| 5 | Key technical highlights | Core module |
| 6 | Comparison with alternatives | Synthesized |
| 7 | Extensibility — plugins, hooks | Plugin directory, hook system |

### Medium (12-15 chapters)

All Brief chapters (expanded), plus:

| # | Additional Chapter |
|---|-------------------|
| 8 | Output formatting & user experience |
| 9 | File system operations |
| 10 | Error handling & exit codes |
| 11 | Testing strategy |
| 12 | Cross-platform support |
| 13 | Performance — startup time, memory |
| 14 | Distribution & packaging |

### Deep (15-20 chapters)

All Medium chapters (expanded), plus:

| # | Additional Chapter |
|---|-------------------|
| 15 | Design evolution — command history |
| 16 | Line-by-line analysis of core command |
| 17 | Security model — input validation, sandboxing |
| 18 | Edge cases — unusual inputs, large files |
| 19 | Build your own — minimal CLI tool |
| 20 | Internal APIs — for plugin authors |

---

## Adapting Templates

These templates are starting points. When adapting:

1. **Remove irrelevant chapters.** If the project has no security model, don't force one.
2. **Add unique chapters.** If the project does something unusual (e.g. browser automation, ML inference), add a dedicated chapter.
3. **Merge overlapping chapters.** If two template chapters cover the same ground in a specific project, merge them.
4. **Respect the project's own organization.** If the project has a clear module structure, mirror it in chapters.

### What makes a good chapter

- **One clear topic** — not "Miscellaneous features"
- **Source-backed** — you can point to specific files that inform this chapter
- **Stand-alone readable** — makes sense without reading other chapters
- **Non-trivial** — not just "this file has 200 lines of code"

### Source citation rules (all depth levels)

Every code block must have a `<!-- Simplified from: -->` comment. This applies to all depth levels including deep chapters like "Build your own" and "Line-by-line analysis":

- All code blocks ≥20 chars: `<!-- Simplified from: path/to/file.ext:lines -->`
- Never use `// Source:` — always `Simplified from:` since walkthrough code is always simplified
- For "Build your own" chapters: cite the original source file being reimplemented
- For "Line-by-line analysis" chapters: cite the exact file and line range being analyzed
