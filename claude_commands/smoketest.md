# /smoketest — Build a Smoke Test Pack

You are a test engineer building a lightweight smoke test suite for core app health and critical user flows.

## If an argument is provided

Focus on the specific service, module, or feature directory passed as `$ARGUMENTS`. Otherwise, select critical paths across the full repository.

## Steps

### 1. Detect existing test strategy

Read the project structure to identify:
- Current test framework (pytest, unittest, jest, etc.)
- Existing test locations, naming conventions, and fixtures
- CI entrypoint (Makefile, package.json scripts, GitHub Actions)

Reuse the existing test stack. Do not introduce a new framework unless none exists.

### 2. Select critical smoke coverage

Choose the smallest set of tests that cover:
- [ ] App boots without error
- [ ] Health/status endpoint responds (if one exists)
- [ ] Highest-value user journey (e.g., submit a form, get a response)
- [ ] One key API endpoint returns expected shape
- [ ] One failure-path guard where risk is highest (e.g., missing required field returns 422, not 500)

Keep scope intentionally small. This is a smoke pack, not a full test suite.

### 3. Set up stable test data

- Use deterministic fixtures and synthetic inputs
- Mock or stub external dependencies (APIs, databases, LLM calls)
- Do not rely on network access, real credentials, or clock-dependent values

### 4. Implement tests

Write tests in project-standard locations and naming patterns. Each test should:
- Focus on one capability
- Assert expected behavior clearly
- Run fast (target under 10 seconds total for the pack)

### 5. Run and verify

Execute the tests locally. Fix flaky selectors, timing assumptions, and environment coupling. Re-run to confirm stability.

### 6. Report coverage

Summarize:
- What is now covered by smoke tests
- What was intentionally excluded and why
- Recommended next tests to add

## Rules

- Prefer fast, deterministic tests over broad but flaky coverage
- Do not add heavy end-to-end or browser-based suites unless explicitly asked
- Do not use real secrets or production data in test fixtures
- Match existing project conventions for file locations, naming, and imports
