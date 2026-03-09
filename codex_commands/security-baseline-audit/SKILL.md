---
name: security-baseline-audit
description: Run a security baseline audit for web applications and APIs. Use when asked to assess auth and session handling, input validation, headers, CORS and CSRF, secret management, logging leakage, dependency risk, and pre-release security readiness.
---

# Security Baseline Audit

## Inputs

- Accept an optional scope path (file or directory).
- Accept optional deployment context (public/internal app, auth model, cloud target).
- Default to whole-repo audit when scope is not provided.

## Workflow

1. Inventory attack surface.
- Map entry points: routes, forms, uploads, webhooks, background jobs, admin endpoints.
- Identify trust boundaries between client, server, data stores, and external services.

2. Review authentication and authorization.
- Verify authentication is required where expected.
- Verify authorization checks are resource-aware, not role-name-only shortcuts.
- Verify session/cookie flags and token handling follow secure defaults.

3. Review request and input handling.
- Verify server-side validation for all user-controlled input.
- Check file upload constraints (type, size, path handling, malware pipeline if present).
- Check for injection risks (SQL, command, template, path traversal, SSRF patterns).

4. Review browser and API protections.
- Check CORS scope for least privilege.
- Check CSRF controls for state-changing browser flows.
- Check security headers (for example HSTS, CSP, X-Content-Type-Options, Referrer-Policy).

5. Review secret and config hygiene.
- Search for hardcoded secrets, credentialed URLs, and debug toggles.
- Verify secret loading from environment or secret store, not source code.
- Verify production defaults are safe when env vars are missing.

6. Review observability and error exposure.
- Check logs for sensitive payload leakage.
- Check error responses for stack traces or internal path disclosure.
- Ensure authentication failures are informative but not revealing.

7. Review dependency and supply-chain posture.
- Flag stale or high-risk dependencies if lockfile/version signals exist.
- Note high-risk transitive dependencies and unpinned critical packages.

8. Produce actionable findings.
- Classify each finding as `critical`, `high`, `medium`, `low`.
- Include file path, risk rationale, exploit precondition, and concrete remediation.
- Separate immediate release blockers from backlog hardening tasks.

## Rules

- Perform read-only auditing unless explicitly asked to patch code.
- State assumptions when environment or deployment details are missing.
- Prefer secure defaults and least-privilege recommendations.
