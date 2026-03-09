---
name: scaffold
description: Convert a UI prototype into a production-ready web app skeleton. Use when asked to migrate Gradio-style prototypes into FastAPI plus templates plus static assets, preserving behavior while organizing code for deployment and maintainability.
---

# Prototype To Production Scaffold

## Inputs

- Accept a path to the prototype file (`.py` or `.ipynb`).
- If no path is provided, locate likely prototype files in the repository.

## Workflow

1. Analyze prototype behavior.
- Enumerate UI components, callback functions, state flow, data sources, and external API usage.
- Summarize expected user flows before implementation.

2. Create or update project structure.
- Separate web app entrypoint, templates, static assets, and business logic modules.
- Keep non-UI logic in framework-light modules for testability.

3. Build backend app layer.
- Implement root page render route and API endpoints matching prototype capabilities.
- Implement streaming response pattern when prototype behavior requires incremental output.
- Load configuration from environment variables.

4. Build frontend template and scripts.
- Map prototype widgets to semantic HTML controls.
- Implement client-side handlers for each backend API interaction.
- Keep implementation framework-free unless project standards require otherwise.

5. Build base styling and accessibility scaffolding.
- Provide clear baseline styles with responsive behavior.
- Keep tokens/theming ready for later design-system pass.
- Include accessible labels, keyboard behavior, and focus management.

6. Create deployment-oriented support files.
- Build pinned dependency manifest.
- Build `.env.example` documenting required variables.
- Build startup command/script aligned to target runtime.

7. Validate feature parity.
- Confirm each prototype capability exists in the scaffolded app.
- Do not add unrelated features.

8. Summarize migration output.
- Report architecture decisions, file layout, and known follow-up items.

## Rules

- Preserve prototype functionality end to end.
- Keep API responses structured and error handling explicit.
- Avoid unnecessary framework additions and build complexity.
