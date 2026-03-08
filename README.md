# CT AI Lab Tools

Reusable [Claude Code](https://docs.anthropic.com/en/docs/claude-code) custom slash commands for building, styling, auditing, and deploying state government web applications.

Built by the Connecticut AI Lab at the Office of the Healthcare Advocate. Designed to be forked by other states and customized.

## What's in here

### Skills (slash commands)

| Command | What it does |
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

### For a single project

Copy the commands you want into your project's `.claude/commands/` directory:

```bash
# From your project root
mkdir -p .claude/commands

# Copy all skills
cp /path/to/ct-ai-lab-tools/commands/*.md .claude/commands/

# Or copy just the ones you need
cp /path/to/ct-ai-lab-tools/commands/scaffold.md .claude/commands/
cp /path/to/ct-ai-lab-tools/commands/accessibility.md .claude/commands/
```

### For all your projects (user-level)

```bash
# Copy to your user-level commands directory
mkdir -p ~/.claude/commands
cp /path/to/ct-ai-lab-tools/commands/*.md ~/.claude/commands/
```

### Reference docs

Skills like `/ctstyles` and `/scaffold` reference docs in the `references/` folder. Copy the `references/` directory alongside your commands, or update the paths in the command files to point to where you keep them.

## Usage

Once installed, use them in Claude Code like any slash command:

```
> /explain
> /scaffold
> /ctstyles
> /accessibility
> /mobile
> /deploymentprecheck
> /lint
> /hook
```

Some commands accept arguments:

```
> /explain app_web/screener.py
> /scaffold path/to/gradio_app.py
```

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
