---
name: lint
description: Run and Fix Linting Issues. Use to check code quality and automatically fix linting errors across Python, JS, HTML, and CSS.
---

# Run and Fix Linting Issues

## Workflow

1. **Detect the tech stack.** Identify languages and tools.
2. **Python Linting.**
   - Use `ruff` if available (`ruff check --fix .`, `ruff format .`).
   - Manual checks: unused imports/vars, no bare `except`, 4-space indent, no `print`.
3. **JavaScript Linting.**
   - Manual checks: `const`/`let` instead of `var`, no `console.log` in prod, `===`, no unused vars.
4. **HTML/CSS Linting.**
   - HTML: closed tags, unique IDs, `alt` on images, no inline styles.
   - CSS: no duplicates, no `!important`, use design system variables.
5. **Fix and report.**
   - Apply fixes directly.
   - Summarize findings and fixes.

## Rules

- Match existing code style; do not impose new ones.
- Respect existing linter configs (ruff.toml, etc.).
- Prioritize errors over style nits.
