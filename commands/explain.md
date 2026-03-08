# /explain — Document the Codebase

You are a technical documentation expert. Your job is to analyze the current codebase and produce (or update) a clear, comprehensive `ARCHITECTURE.md` file in the project root.

## If an argument is provided

Focus your explanation on the specific file or directory passed as `$ARGUMENTS`. Still produce a complete document, but center the narrative around that component.

## Steps

1. **Explore the project structure.** Use Glob and Read to understand the directory layout, key files, and dependencies (requirements.txt, package.json, etc.).

2. **Identify the tech stack.** Framework (FastAPI, Flask, Django, etc.), templating engine, CSS approach, JS strategy, database, AI/LLM integrations, deployment target.

3. **Map the architecture.** Trace how a request flows through the system — from the user clicking a button, to the frontend JS, to the API route, to the business logic, and back.

4. **Document key features.** For each major feature, explain:
   - What it does from the user's perspective
   - Where the relevant code lives (file paths + line numbers)
   - How the pieces connect

5. **Note patterns and conventions.** Things like:
   - How translations/i18n works
   - How navigation between views works
   - How modals or overlays are structured
   - How AI/LLM calls are made and streamed
   - How state is managed (frontend and backend)

6. **Write `ARCHITECTURE.md`.** Structure it as:

```markdown
# [Project Name] — Architecture

## Overview
[2-3 sentence summary]

## Tech Stack
[Table of technologies and their roles]

## Project Structure
[Directory tree with annotations]

## Request Flow
[How a typical user interaction flows through the system]

## Key Features
[Feature-by-feature breakdown with file references]

## Patterns & Conventions
[Reusable patterns someone new to the codebase should know]

## Configuration & Environment
[Environment variables, config files, secrets management]

## Deployment
[How the app is built and deployed]
```

7. **If `ARCHITECTURE.md` already exists**, read it first and update it to reflect the current state of the codebase. Preserve any manually-written sections. Add a "Last updated" note at the top.

## Rules

- Always include file paths with line numbers (e.g., `app_web/screener.py:42`) so readers can jump to the code
- Write for a developer who is new to the project but not new to programming
- Keep it factual — describe what IS, not what should be
- Don't include code snippets longer than 5 lines; point to the file instead
- If you find something confusing or inconsistent in the codebase, note it in a "Known Issues / Tech Debt" section at the bottom
