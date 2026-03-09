---
name: deploymentprecheck
description: Run a deployment readiness audit for a web application. Use when asked to verify cloud deployment safety, startup configuration, dependency readiness, static asset handling, environment variables, security settings, and large-file risks.
---

# Deployment Readiness Precheck

## Inputs

- Accept deployment target details if provided.
- Default to cloud app-service style deployment assumptions when target is unspecified.

## Workflow

1. Validate project deployment files.
- Confirm presence and quality of core files (`requirements.txt`, startup command/script, `.env.example`, `.gitignore`).
- Ensure dependency versions are pinned where required by team policy.

2. Check for secrets and sensitive configuration issues.
- Scan for hardcoded keys, tokens, passwords, and credentialed URLs.
- Ensure secrets are loaded from environment variables.
- Ensure `.env` is ignored and not committed.

3. Validate environment-variable hygiene.
- Ensure runtime-required variables are documented in `.env.example`.
- Ensure missing required variables fail fast with clear errors.
- Ensure server-side env vars are not leaked to client code.

4. Validate startup behavior.
- Confirm app module path and process command are valid.
- Confirm bind host/port align with target platform expectations.
- Confirm startup scripts use correct line endings and executable mode where needed.

5. Validate dependency and runtime compatibility.
- Ensure required web/runtime packages are present.
- Flag packages likely to fail due to missing build tools/system libraries.
- Flag Python/runtime version compatibility risks.

6. Validate static assets and networking assumptions.
- Ensure static files are served correctly by the app stack.
- Remove localhost-only URLs and hardcoded dev ports from production paths.
- Review CORS and debug settings for production safety.

7. Validate repository hygiene.
- Flag oversized files and non-deployable artifacts.
- Ensure transient directories and caches are ignored.

8. Run a local startup check when possible.
- Start the app with the expected runtime command.
- Capture import/runtime failures and include exact fix guidance.

9. Produce a readiness report.
- Classify findings as PASS, FAIL, or WARN.
- Include file paths and exact remediation steps for each FAIL.

## Rules

- Perform a read-only audit unless explicitly asked to fix issues.
- Be explicit about assumptions when deployment target details are missing.
