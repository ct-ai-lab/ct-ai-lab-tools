---
name: hook
description: Set up and tune pre-commit hooks for a repository. Use when asked to install pre-commit, create or update hook configuration, enforce fast quality checks, and verify hooks run reliably in the current project.
---

# Pre-commit Hook Setup

## Workflow

1. Detect the project stack.
- Inspect repository languages and existing quality tooling.
- Reuse existing lint/format configs when available.

2. Install pre-commit tooling in the project environment.
- Prefer existing virtual environment or project-local tooling.
- Avoid global installs unless explicitly requested.

3. Create or update `.pre-commit-config.yaml`.
- Start with lightweight universal checks (whitespace, eof, yaml/json sanity, merge conflicts, private key detection).
- Add language-specific checks only when relevant to the repository.
- Keep hook runtime fast.

4. Ensure ignore rules are sane.
- Update `.gitignore` for local env and build/cache artifacts as needed.

5. Install and execute hooks.
- Run install command.
- Run hooks across all files.
- Fix formatting/quality issues introduced by hooks when safe.

6. Verify baseline behavior.
- Run at least one targeted hook to confirm setup is active.
- Report hooks added, files changed, and any excluded rules.

## Rules

- Update existing hook configs rather than replacing them blindly.
- Avoid heavy hooks (full test suites/type checks) unless explicitly requested.
- Avoid changing application logic solely to satisfy hooks.
- If an intentional existing pattern fails a hook, prefer scoped excludes with explanation.
