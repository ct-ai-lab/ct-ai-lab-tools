---
name: explain
description: Generate or update architecture documentation for a codebase. Use when asked to explain project structure, request flow, feature mapping, technology choices, conventions, configuration, and deployment details.
---

# Architecture Documentation

## Inputs

- Accept an optional scope path (file or directory).
- Focus analysis on the scope if provided while still documenting overall architecture.

## Workflow

1. Inspect project structure.
- Enumerate major directories and high-signal files.
- Identify config and dependency files that define stack and runtime.

2. Identify tech stack and runtime model.
- Determine backend framework, frontend architecture, data layer, integrations, and deployment target.
- Note key libraries and their roles.

3. Trace request/interaction flows.
- Map user actions through frontend handlers, API routes, business logic, and response rendering.
- Include async/streaming patterns where present.

4. Map major features.
- Describe each key feature from user perspective.
- Link each feature to concrete implementation files.

5. Document conventions and patterns.
- Capture reusable patterns for i18n, state handling, navigation, forms, and error handling.
- Capture any team-specific architecture conventions discovered in the repo.

6. Write or update `ARCHITECTURE.md` in project root.
- Use concise factual sections:
  - Overview
  - Tech Stack
  - Project Structure
  - Request Flow
  - Key Features
  - Patterns and Conventions
  - Configuration and Environment
  - Deployment
  - Known Issues or Tech Debt
- Preserve existing manual sections when updating.
- Add a last-updated date near the top.

## Rules

- Describe current behavior, not aspirational design.
- Cite concrete file paths for each claim.
- Keep code snippets short; prefer references over long excerpts.
- Flag inconsistencies and ambiguous flows clearly.
