---
name: lint
description: Run linting and fix safe code quality issues across a repository. Use when asked to execute linters, apply auto-fixes, clean structural issues in Python/JavaScript/HTML/CSS, and summarize remaining judgment-based decisions.
---

# Lint And Remediate

## Workflow

1. Detect lint stack.
- Identify languages present and linter configs already in the project.
- Prefer project-defined tools and settings.

2. Run linters with project-preferred commands.
- Use configured scripts/tools first.
- Use sane defaults only when no project lint command exists.

3. Auto-fix safe issues.
- Apply formatter and linter auto-fixes where supported.
- Keep fixes scoped to lint quality and formatting.

4. Perform targeted manual checks when tooling is absent.
- Python: unused imports/variables, broad exceptions, mutable defaults, style consistency.
- JavaScript: dead code, equality pitfalls, globals, obvious debug leftovers.
- HTML/CSS: structural validity, duplicate ids/selectors, obvious accessibility/style anti-patterns.

5. Re-run checks to confirm clean state.
- Ensure fixes do not introduce regressions.
- Summarize unresolved items requiring product or architecture decisions.

## Rules

- Respect existing style and lint configs; do not impose unrelated style changes.
- Do not add new lint frameworks/config files unless requested.
- Prefer local project environments over global package installs.
- Prioritize correctness issues first, style nits last.
