---
name: security-baseline-audit
description: Security Baseline Audit. Use to perform a baseline security audit of a web application and its APIs, reviewing authentication, input handling, and secrets.
---

# Security Baseline Audit

## Inputs

- Accept an optional scope path as `$ARGUMENTS`.
- Audit the whole repository when no scope is provided.

## Workflow

1. **Inventory attack surface.** Map routes, handlers, and trust boundaries.
2. **Review AuthN/AuthZ.** Check authentication, resource-aware authorization, and session security.
3. **Review input handling.** Check for injection risks (SQL, Command, Template, Path Traversal, SSRF).
4. **Review browser protections.** CSRF, CORS, and security headers.
5. **Review secrets.** Ensure no hardcoded keys; check environment variable usage.
6. **Review observability.** Ensure no sensitive data in logs or error messages.
7. **Review dependencies.** Check for known vulnerabilities and version pinning.
8. **Produce findings.** Report with Severity, File Path, Risk, and Remediation.

## Rules

- Read-only audit unless asked to patch.
- Focus on code-level review; no actual exploit attempts.
