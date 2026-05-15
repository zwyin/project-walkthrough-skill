# Exploration Protocol

Step-by-step guide for exploring a project before generating the walkthrough.

## Step 1: Identify Project Type

Read the top-level files to classify the project:

```
Check these files (in order of reliability):
1. package.json — "description" + "keywords" fields
2. README.md — first 50 lines
3. CLAUDE.md / GEMINI.md / AGENTS.md — if present, describes project purpose
4. Directory structure — `ls` the top-level directories
```

**Classification:**

| Type | Indicators | Example |
|------|-----------|---------|
| **AI tool** | Skills/prompts directory, AI model references, plugin system, prompt engineering | superpowers, gstack, cursor |
| **Library** | `src/index.ts` exports, `lib/` directory, API documentation, no `server.js` | React, Lodash, zod |
| **Web app** | Routes/pages directory, server entry point, database migrations, auth | Next.js app, Rails app |
| **CLI tool** | `bin/` directory, commander/yargs dependency, `cli.ts`/`cli.js` entry | git, esbuild, gstack browse |

If the project doesn't fit neatly, pick the closest match and note the hybrid aspects.

## Step 2: Read Core Files

Read these files completely (not just skimming):

### All project types
- `README.md` — project description, installation, usage
- `package.json` — dependencies, scripts, engines
- `CLAUDE.md` / `GEMINI.md` / `AGENTS.md` — AI assistant instructions (if present)
- `ARCHITECTURE.md` — architecture documentation (if present)

### AI tool specific
- `plugin.json` or equivalent manifest
- Skill/prompt files (read at least 3-5 representative ones)
- Entry skill (the one that loads first, e.g. `using-superpowers`)
- Hook scripts (SessionStart, PreToolUse, etc.)

### Library specific
- `src/index.ts` — public API surface
- Types/interfaces file
- At least 3 source files in core modules

### Web app specific
- Router/routes configuration
- Database schema or migrations
- API endpoint handlers (at least 3)
- Authentication/authorization middleware

### CLI tool specific
- CLI entry point (`cli.ts`, `bin/cli.js`)
- Command handlers
- Configuration file handling

## Step 3: Read Key Source Files

Based on the architecture discovered in Step 2, read the most important source files. Prioritize:

1. **Core logic** — the module that does the main work
2. **Configuration** — how the project is configured
3. **Entry points** — where execution begins
4. **Error handling** — how errors are caught and reported
5. **Tests** — what the project considers worth testing (reveals priorities)

**Rule of thumb:** Read at least 5 source files for brief, 10 for medium, 15+ for deep.

### File-size aware reading

Not all files should be read the same way:

| File size | Strategy | Why |
|-----------|----------|-----|
| < 500 lines | Read full file | Small enough to understand completely |
| 500 – 2,000 lines | Read first 100 lines + key sections | Get structure, then target specifics |
| > 2,000 lines | Use outline/symbols first, read only needed sections | Avoid context exhaustion; these files often have traps (e.g., a 4,700-line file with 40+ type literals where counting is unreliable) |

For files > 2,000 lines: if you need to count items (type literals, enum variants, exports), state the count as "approximately N" or "40+" rather than an exact number, unless you can verify programmatically.

### Architecture import verification (do here, not later)

Before moving to Step 4, verify the ACTUAL dependency relationships between modules:

1. For each pair of modules that appear related (e.g., `classic/` and `mini/`), check: does one import from the other? Or do both import from a shared dependency?
2. This prevents the common trap of drawing architecture diagrams based on directory structure alone. Directory nesting ≠ dependency hierarchy.
3. Record findings — they directly determine how you draw architecture diagrams in Phase 3.

## Step 4: Extract Innovations

From the exploration so far, identify 3-5 unique aspects:

**Questions to ask:**
- What does this project do differently from similar tools?
- What design decisions would surprise an experienced developer?
- What problems does it solve that others don't?
- What trade-offs did the authors make, and why?

**Innovation types to look for:**

| Type | Description | Example |
|------|-------------|---------|
| Architecture | Novel way of organizing code/flow | Superpowers' event-driven skill routing |
| Performance | Unusual optimization technique | GStack's persistent Chromium daemon |
| Security | Unique defense mechanism | GStack's 6-layer prompt injection defense |
| UX | Innovative developer experience | Superpowers' Red Flags anti-rationalization |
| Composability | Novel way to combine components | GStack's Host adapter pattern for multi-AI |

## Step 5: Map Architecture

Create a mental model of the project's architecture:

1. **Components** — what are the main modules and what do they do?
2. **Data flow** — how does data move between components?
3. **Dependencies** — what external libraries/services does it use?
4. **Configuration** — what can be customized and how?
5. **State** — what state is maintained and where?

**Output:** This becomes the architecture diagram in Chapter 1/2 of the walkthrough.

**Next step:** The exploration results feed directly into Phase 2 (Plan), where you select a chapter template from `docs/chapter-templates.md` based on the project type identified in Step 1.

## Step 6: Verify Exploration Findings

Before moving to content generation, cross-check your exploration notes:

1. **Re-read key claims** — For every factual statement you plan to make (module responsibilities, API signatures, file existence), go back and verify:
   - `ls` or `find` to confirm directory structures you plan to describe
   - Read the actual function signature, not just the call site
   - Check config files for version numbers, not README

2. **Mark unverified claims** — If you couldn't verify something (file too large, access denied, ran out of context), tag it in your notes as `[UNVERIFIED]`. These claims must either be re-verified during Phase 3, or omitted from the walkthrough.

3. **Source file inventory** — For each code example you plan to include, note the exact file path and line range. If you can't locate the source, you cannot include the code.

4. **Dependency check** — Re-read `package.json` / `Cargo.toml` / `pyproject.toml` dependency lists. Cross-reference any dependency claims (e.g., "uses library X for Y") against the actual imports in source files.

This step takes 3-5 minutes and prevents the #1 quality issue: fabricated content.

## Common Pitfalls

| Pitfall | How to avoid |
|---------|-------------|
| Reading too many files, running out of context | Stick to the priority order above. Use `smart_outline` or `get_symbols_overview` (Serena MCP tools — if not available, use grep/find or LSP documentSymbol) before reading full files. |
| Fabricating details not in source | If you can't find evidence for a claim, tag it [UNVERIFIED] per Step 6. If it remains unverifiable during Phase 3, omit it from the walkthrough. |
| Missing the project's own docs | Many projects have ARCHITECTURE.md, CONTRIBUTING.md, DESIGN.md. Check for these first. |
| Ignoring the test suite | Tests reveal what the authors consider important. Read at least 2-3 test files. |
| Treating all projects the same | Adjust exploration based on project type. A library's API surface is more important than its CLI parsing. |

## Time Budget

| Phase | Brief | Medium | Deep |
|-------|-------|--------|------|
| Step 1: Identify type | 2 min | 2 min | 2 min |
| Step 2: Read core files | 5 min | 8 min | 12 min |
| Step 3: Read source files | 5 min | 15 min | 25 min |
| Step 4: Extract innovations | 3 min | 5 min | 8 min |
| Step 5: Map architecture | 3 min | 5 min | 8 min |
| Step 6: Verify findings | 3 min | 4 min | 8 min |
| **Total** | **~21 min** | **~39 min** | **~63 min** |
