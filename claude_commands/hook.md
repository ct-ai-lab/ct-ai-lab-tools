# /hook — Set Up Pre-Commit Hooks

You are a DevOps engineer setting up pre-commit hooks to catch issues before they reach the repository.

## Steps

### 1. Detect the tech stack

Read the project to determine what languages are in use and what checks make sense.

### 2. Install pre-commit framework

```bash
pip install pre-commit
```

### 3. Create `.pre-commit-config.yaml`

Generate a config appropriate for the project. Start with this base and adjust:

```yaml
repos:
  # General file checks
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
        args: ['--maxkb=500']
      - id: check-merge-conflict
      - id: detect-private-key

  # Python
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

Adjust based on what's in the project:
- If no Python → remove ruff hooks
- If the project already has a `.pre-commit-config.yaml` → update it, don't replace it
- If ruff config exists (ruff.toml, pyproject.toml [tool.ruff]) → respect it

### 4. Create or update `.gitignore`

Ensure these entries exist:
```
.env
__pycache__/
*.pyc
.ruff_cache/
venv/
.venv/
```

### 5. Install the hooks

```bash
pre-commit install
```

### 6. Run against all files

```bash
pre-commit run --all-files
```

Fix any issues that come up. If ruff reformats files, stage and note the changes.

### 7. Verify it works

Make a small whitespace change to a file and verify the hook catches it:
```bash
pre-commit run trailing-whitespace
```

### 8. Summary

Report:
- What hooks were installed
- What issues were auto-fixed on the initial run
- Any hooks that were skipped and why

## Rules

- Do not add hooks that would break the existing workflow
- Keep the hook set minimal — only add checks that the project actually needs
- If pre-commit is already set up, update rather than replace
- Do not add slow hooks (type checkers, test runners) unless specifically asked — pre-commit hooks should run in under 5 seconds
- Do not modify any application code to satisfy hooks — only fix formatting/whitespace issues
- If a hook fails on existing code that was intentional, add it to the hook's `exclude` list rather than changing the code
