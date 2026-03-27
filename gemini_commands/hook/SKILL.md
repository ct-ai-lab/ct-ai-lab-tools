---
name: hook
description: Set Up Pre-Commit Hooks. Use to install and configure pre-commit hooks for a project to catch common issues.
---

# Set Up Pre-Commit Hooks

## Workflow

1. **Detect the tech stack.** Determine languages and appropriate checks.
2. **Install pre-commit.** `pip install pre-commit`.
3. **Create/Update `.pre-commit-config.yaml`.**
   - Include general checks (trailing whitespace, end-of-file, YAML/JSON check, large files, merge conflicts, private keys).
   - Add language-specific checks (e.g., `ruff` for Python).
4. **Update `.gitignore`.** Ensure `.env`, `__pycache__`, `.venv`, etc., are ignored.
5. **Install and run.**
   - `pre-commit install`.
   - `pre-commit run --all-files`.
6. **Verify.** Confirm hooks catch intentional issues (e.g., trailing whitespace).

## Rules

- Do not break existing workflows.
- Keep hook set minimal and fast (<5 seconds).
- Do not modify application code except for formatting/whitespace.
- Exclude intentional "failures" rather than changing code.
