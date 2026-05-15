# Documentation Standards

This file defines the writing and formatting rules for walkthrough output.
Extracted from `SKILL.md` to keep the skill definition focused on process.

## Language

- Write in the same language as the project's documentation
- If project docs are English, write in English
- If project docs are Chinese, write in Chinese
- If mixed, default to Chinese (this is the primary audience)
- **Technical terms:** Keep standard terms in their original form (e.g., "middleware", "hook", "schema"). Don't translate well-known technical vocabulary.
- **Code comments in examples:** Match the style of the actual source code. If source uses English comments, keep English. If Chinese, keep Chinese.
- **Architecture diagrams:** Labels in the same language as the chapter text. Technical identifiers (file names, function names) always stay in English.
- **Audience-specific variants:** `brief-general` uses more analogies and fewer technical terms. `brief-dev` uses precise technical language. This applies regardless of language.

## Structure

- Every chapter starts with a title + one-line subtitle
- Use backend analogies for every concept (middleware, CI/CD, HTTP, databases)
- Include code examples from the actual source (not fabricated)
- **Every code block must have a source citation** — `// Simplified from: path:lines`. Code blocks without source citations are a quality violation.
- Include architecture diagrams in ASCII or CSS flow format
- Every chapter ends with navigation links (← previous | next →)

## Source Verification

All source verification happens in Phase 3A (verify & build manifest) and Phase 3C (validate coverage). See SKILL.md Process section for the complete verification procedure.

## Audience: `general` mode specifics

Add these elements when audience is `general`:

**类比理解 cards** (at every technical term's first appearance):
```
┌─────────────────────────────────────────┐
│ 🔍 类比理解                              │
│                                         │
│ Prompt 注入 ≈ 钓鱼邮件                   │
│                                         │
│ 就像钓鱼邮件伪装成正常邮件骗你点击链接，   │
│ Prompt 注入是伪装成正常网页内容骗 AI 执行  │
│ 恶意指令。防御方式也类似：过滤器 = 垃圾    │
│ 邮件过滤，蜜罐 = 诱饵链接检测。           │
└─────────────────────────────────────────┘
```

**Code block summaries** (before every code block):
```
这段代码的作用：在网页内容中插入一个唯一的"标记"，
如果 AI 被骗后把这个标记说出来了，就说明攻击成功。
```

## Audience: `dev` mode specifics

- No analogy cards
- Code blocks analyzed line by line with inline comments
- Technical terms used directly
- Performance data and benchmarks where available
