# CT AI Lab Tools

Reusable AI coding agent skills for building, styling, auditing, and deploying state government web applications. Supports [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [OpenAI Codex](https://openai.com/index/codex/).

Built by the Connecticut AI Enablement Lab. Designed to be forked by other states and customized.

## Repository structure

```
ct-ai-lab-tools/
├── claude_commands/          # Claude Code custom slash commands (.md)
│   ├── explain.md
│   ├── scaffold.md
│   ├── ctstyles.md
│   ├── accessibility.md
│   ├── mobile.md
│   ├── deploymentprecheck.md
│   ├── lint.md
│   └── hook.md
├── codex_commands/           # OpenAI Codex instructions (.md) — coming soon
├── references/               # Shared reference docs used by skills
│   ├── ct_design_system.md
│   └── fastapi_scaffold.md
└── README.md
```

## Available skills

| Skill | What it does |
|---|---|
| `/explain` | Document the codebase — architecture, key features, file map |
| `/scaffold` | Convert a Gradio prototype to a production FastAPI + Jinja2 app |
| `/ctstyles` | Apply the CT.gov / AI Lab design system to an app |
| `/accessibility` | Audit and fix accessibility (WCAG 2.1 AA) |
| `/mobile` | Check for mobile responsiveness issues |
| `/deploymentprecheck` | Verify the app is ready for Azure deployment |
| `/lint` | Run and fix linting issues |
| `/hook` | Set up pre-commit hooks |

### Reference docs

| File | Purpose |
|---|---|
| `references/ct_design_system.md` | Full CT.gov design tokens, components, and patterns |
| `references/fastapi_scaffold.md` | Standard FastAPI project structure and conventions |

## Installation

### Claude Code

Copy the skills into your project's `.claude/commands/` directory:

```bash
# From your project root
mkdir -p .claude/commands

# Copy all skills
cp /path/to/ct-ai-lab-tools/claude_commands/*.md .claude/commands/

# Or copy just the ones you need
cp /path/to/ct-ai-lab-tools/claude_commands/scaffold.md .claude/commands/
```

For all your projects (user-level):

```bash
mkdir -p ~/.claude/commands
cp /path/to/ct-ai-lab-tools/claude_commands/*.md ~/.claude/commands/
```

### OpenAI Codex

Coming soon. Codex instructions will be available in the `codex_commands/` directory once the format is finalized.

### Reference docs

Skills like `/ctstyles` and `/scaffold` reference docs in the `references/` folder. Copy the `references/` directory alongside your commands, or update the paths in the command files to point to where you keep them.

## Usage

### Claude Code

Once installed, use them like any slash command:

```
> /explain
> /scaffold path/to/gradio_app.py
> /ctstyles
> /accessibility
> /mobile
> /deploymentprecheck
> /lint
> /hook
```

### OpenAI Codex

Instructions TBD — will follow Codex's task/instruction format once available.

## For other states

This repo is designed to be forked and customized:

1. **Fork this repo**
2. **Replace `references/ct_design_system.md`** with your state's design tokens (colors, fonts, header/footer patterns)
3. **Rename `/ctstyles`** to match your state (e.g., `/nystyles`, `/castyles`)
4. **Update deployment targets** in `/deploymentprecheck` if you use AWS, GCP, etc. instead of Azure
5. **Keep everything else** — the scaffold, accessibility, mobile, lint, and hook skills are state-agnostic

## Our workflow

```
Gradio prototype (.py / .ipynb)
        |
        v
/scaffold  ——>  FastAPI + Jinja2 app structure
        |
        v
/ctstyles  ——>  Apply CT.gov design system
        |
        v
/accessibility + /mobile  ——>  Audit and fix
        |
        v
/deploymentprecheck  ——>  Verify Azure readiness
        |
        v
/hook + /lint  ——>  Set up CI guardrails
        |
        v
Deploy to Azure App Service
```

## License

MIT — use it, fork it, improve it.
