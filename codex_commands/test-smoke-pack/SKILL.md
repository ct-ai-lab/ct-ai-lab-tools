---
name: test-smoke-pack
description: Build or improve a lightweight smoke test pack for core app health and critical user flows. Use when asked to add fast CI checks for startup, key endpoints, and top-priority journey regressions.
---

# Test Smoke Pack

## Inputs

- Accept optional scope path (service, module, or feature directory).
- Accept optional priority flow list from product or release context.
- Default to repository-wide critical path selection when no scope is provided.

## Workflow

1. Detect existing test strategy.
- Identify current test framework, conventions, fixtures, and CI entrypoints.
- Reuse existing structure instead of introducing new test stack unless required.

2. Select critical smoke coverage.
- Include boot/startup sanity check.
- Include at least one health/status endpoint check if available.
- Include highest-value user journeys or API workflows that must not regress.
- Keep scope intentionally small and fast.

3. Design stable test data and setup.
- Use deterministic fixtures and synthetic inputs.
- Isolate external dependencies via mocks/stubs/fakes where feasible.
- Avoid relying on network access or unstable clock randomness.

4. Implement smoke tests.
- Add tests in project-standard locations and naming patterns.
- Assert success-path behavior plus one failure-path guard where high risk exists.
- Keep each test focused on one capability.

5. Integrate with existing CI commands.
- Ensure tests run from existing test script or command path.
- Keep runtime short enough for commit and pull request feedback loops.

6. Execute and harden.
- Run tests locally.
- Fix flaky selectors, timing assumptions, and environment coupling.
- Re-run to confirm stability.

7. Report coverage and gaps.
- Summarize what is now covered.
- List intentional exclusions and recommended next tests.

## Rules

- Prefer fast, deterministic tests over broad but flaky coverage.
- Avoid adding heavy end-to-end suites unless explicitly requested.
- Do not use real secrets or production data in test fixtures.
