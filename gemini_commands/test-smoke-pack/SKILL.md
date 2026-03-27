---
name: test-smoke-pack
description: Build a Smoke Test Pack. Use to build a lightweight smoke test suite for core app health and critical user flows, reusing existing frameworks.
---

# Build a Smoke Test Pack

## Inputs

- Accept an optional scope path as `$ARGUMENTS`.
- Select critical paths across the repository when no scope is provided.

## Workflow

1. **Detect existing test strategy.** Identify frameworks (pytest, jest, etc.) and CI entrypoints.
2. **Select critical coverage.** Boot check, health endpoint, high-value user journey, key API endpoint.
3. **Set up stable test data.** Use fixtures and mocks; avoid network or real credential dependencies.
4. **Implement tests.** Follow project-standard naming and locations; ensure they run fast.
5. **Run and verify.** Confirm stability locally.
6. **Report coverage.** Summarize what is covered and what was excluded.

## Rules

- Prefer fast, deterministic tests.
- No real secrets or production data.
- Match existing project conventions.
