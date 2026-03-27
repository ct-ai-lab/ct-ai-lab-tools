---
name: explain
description: Document the Codebase. Use to analyze the codebase and produce or update a comprehensive ARCHITECTURE.md file.
---

# Document the Codebase

## Inputs

- Accept an optional scope path as `$ARGUMENTS` to focus the explanation.
- Document the whole application when no scope is provided.

## Workflow

1. **Explore the project structure.** Identify key files, directory layout, and dependencies.
2. **Identify the tech stack.** Frameworks, CSS/JS strategy, database, AI integrations, deployment target.
3. **Map the architecture.** Trace request flows from frontend to backend logic.
4. **Document key features.** Explain what they do and where the code lives.
5. **Note patterns and conventions.** i18n, navigation, state management, AI patterns.
6. **Write or update `ARCHITECTURE.md`.**
   - Include: Overview, Tech Stack, Project Structure, Request Flow, Key Features, Patterns, Config, Deployment.
   - If it exists, update it and add a "Last updated" note.

## Rules

- Include file paths with line numbers.
- Write for a developer new to the project.
- Keep it factual; describe what IS.
- Avoid long code snippets; point to files instead.
- Note tech debt or inconsistencies in a dedicated section.
