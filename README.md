# CT AI Lab Tools

Reusable AI coding agent skills for building, styling, auditing, and deploying state government web applications. Supports [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [OpenAI Codex](https://openai.com/codex/).

Built by the Connecticut AI Enablement Lab. Designed to be forked by other states and customized.

## Repository structure

```
ct-ai-lab-tools/
|- claude_commands/          # Claude custom slash commands (.md)
|  |- explain.md
|  |- scaffold.md
|  |- ctstyles.md
|  |- accessibility.md
|  |- mobile.md
|  |- deploymentprecheck.md
|  |- lint.md
|  `- hook.md
|- codex_commands/           # Codex skills (skill folders)
|  |- accessibility/
|  |- ctstyles/
|  |- deploymentprecheck/
|  |- explain/
|  |- hook/
|  |- lint/
|  |- mobile/
|  |- pii-data-safety/
|  |- security-baseline-audit/
|  |- test-smoke-pack/
|  `- scaffold/
|- references/               # Shared reference docs used by skills
|  |- ct_design_system.md
|  `- fastapi_scaffold.md
`- README.md
```

## Available skills

| Skill | What it does |
|---|---|
| `explain` | Document the codebase: architecture, key features, file map |
| `scaffold` | Convert a Gradio prototype to a production FastAPI + template app |
| `ctstyles` | Apply a design system consistently across UI components |
| `accessibility` | Audit and fix accessibility issues (WCAG 2.1 AA) |
| `mobile` | Audit and fix mobile responsiveness issues |
| `deploymentprecheck` | Verify cloud deployment readiness |
| `lint` | Run linting and fix safe quality issues |
| `hook` | Set up and tune pre-commit hooks |
| `security-baseline-audit` | Run a baseline security review before release |
| `pii-data-safety` | Audit and reduce PII exposure risk |
| `test-smoke-pack` | Build lightweight smoke tests for critical flows |

### Reference docs

| File | Purpose |
|---|---|
| `references/ct_design_system.md` | Design tokens, components, and layout patterns |
| `references/fastapi_scaffold.md` | Standard FastAPI project structure and conventions |

## Installation

### Claude Code

Copy the slash commands into your project's `.claude/commands/` directory:

```bash
# from your project root
mkdir -p .claude/commands
cp /path/to/ct-ai-lab-tools/claude_commands/*.md .claude/commands/
```

For all projects (user-level):

```bash
mkdir -p ~/.claude/commands
cp /path/to/ct-ai-lab-tools/claude_commands/*.md ~/.claude/commands/
```

### OpenAI Codex

Codex skills are the folders in `codex_commands/`.

Copy each skill folder into your Codex skills directory (`$CODEX_HOME/skills` or `~/.codex/skills`):

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/ct-ai-lab-tools/codex_commands/* ~/.codex/skills/
```

PowerShell example:

```powershell
New-Item -ItemType Directory -Force "$HOME/.codex/skills" | Out-Null
Copy-Item -Recurse -Force "C:\path\to\ct-ai-lab-tools\codex_commands\*" "$HOME/.codex/skills"
```

## Usage

### Claude Code

Use slash commands:

```text
/explain
/scaffold path/to/gradio_app.py
/ctstyles
/accessibility
/mobile
/deploymentprecheck
/lint
/hook
```

### OpenAI Codex

Invoke skills explicitly in prompts using `$skill-name`, or rely on skill trigger descriptions.

```text
Use $explain to refresh ARCHITECTURE.md for this repo.
Use $scaffold on app.py and keep feature parity.
Use $ctstyles to align this UI to our design system.
```

## For other states

This repo is designed to be forked and customized:

1. Fork this repo.
2. Replace `references/ct_design_system.md` with your own design tokens and component patterns.
3. Rename `ctstyles` to your state naming if preferred (for example, `nystyles`, `castyles`).
4. Update deployment checks in `deploymentprecheck` for your cloud target if not Azure.
5. Keep scaffold, accessibility, mobile, lint, and hook mostly unchanged.

## Suggested workflow

```text
Gradio prototype (.py / .ipynb)
        |
        v
scaffold -> production FastAPI + template app
        |
        v
ctstyles -> apply design system
        |
        v
accessibility + mobile -> audit and fix
        |
        v
deploymentprecheck -> verify deployment readiness
        |
        v
hook + lint -> add quality guardrails
```

## License

MIT - use it, fork it, improve it.
