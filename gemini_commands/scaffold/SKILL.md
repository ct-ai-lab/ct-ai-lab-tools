---
name: scaffold
description: Gradio to FastAPI Production App. Use to convert a Gradio prototype into a production-ready FastAPI + Jinja2 web application.
---

# Gradio to FastAPI Production App

## Inputs

- `$ARGUMENTS` should be the path to a Gradio app file (.py or .ipynb).

## Workflow

1. **Analyze Gradio prototype.** Extract UI components, callbacks, state, and API calls.
2. **Create project structure.** Set up `app_web/` with `main.py`, logic module, templates, and static files.
3. **Build `main.py`.** FastAPI routes, Jinja2 integration, and API endpoints.
4. **Build logic module.** Extract pure Python logic from callbacks.
5. **Build `index.html`.** Single-page Jinja2 template with `data-i18n` attributes.
6. **Build `app.js`.** Vanilla JS for step navigation and API fetching (or SSE for streaming).
7. **Build `styles.css`.** Mobile-first responsive styles with CSS variables.
8. **Build infrastructure.** `requirements.txt`, `.env.example`, and `startup.sh`.

## Rules

- Preserve ALL functionality from the prototype.
- Every user-facing text must have `data-i18n`.
- Vanilla JS only (no build tools).
- Include basic validation and accessibility from the start.
