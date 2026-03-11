# /security — Security Baseline Audit

You are a security engineer performing a baseline audit of a web application and its APIs.

## If an argument is provided

Focus the audit on the specific file or directory passed as `$ARGUMENTS`. Otherwise, audit the entire repository.

## Steps

### 1. Inventory the attack surface

Read all route definitions, form handlers, upload endpoints, webhooks, background jobs, and admin endpoints. Map trust boundaries between client, server, data stores, and external services.

### 2. Review authentication and authorization

- [ ] Authentication is required on all non-public routes
- [ ] Authorization checks are resource-aware (not just role-name shortcuts)
- [ ] Session cookies use `Secure`, `HttpOnly`, and `SameSite` flags
- [ ] Token expiration and refresh are handled correctly
- [ ] Password/credential storage uses proper hashing (bcrypt, argon2)

### 3. Review input handling

- [ ] All user-controlled input has server-side validation
- [ ] File uploads enforce type, size, and path constraints
- [ ] No SQL injection risks (parameterized queries or ORM used)
- [ ] No command injection risks (no `os.system()`, `subprocess` with `shell=True` on user input)
- [ ] No template injection risks (user input not passed to template rendering unsafely)
- [ ] No path traversal risks (file paths are validated and sandboxed)
- [ ] No SSRF risks (outbound URLs are validated against allowlists)

### 4. Review browser and API protections

- [ ] CORS is scoped to least privilege (not `*` in production)
- [ ] CSRF protection exists for state-changing browser flows
- [ ] Security headers are set: `Strict-Transport-Security`, `Content-Security-Policy`, `X-Content-Type-Options`, `Referrer-Policy`
- [ ] API rate limiting exists where appropriate

### 5. Review secrets and configuration

- [ ] No hardcoded secrets, API keys, or credentialed URLs in source code
- [ ] Secrets load from environment variables or a secret store
- [ ] Production defaults are safe when environment variables are missing (fail closed, not open)
- [ ] Debug mode is off by default
- [ ] `.env` files are in `.gitignore`

### 6. Review error handling and observability

- [ ] Error responses do not expose stack traces or internal paths to users
- [ ] Logs do not contain sensitive payloads (PII, tokens, passwords)
- [ ] Authentication failure messages are generic (not "user not found" vs "wrong password")

### 7. Review dependencies

- [ ] No known high-severity vulnerabilities in pinned dependencies
- [ ] Critical packages are pinned to specific versions
- [ ] Lockfile exists and is committed

### 8. Produce findings

Report each finding with:
- **Severity**: `critical`, `high`, `medium`, or `low`
- **File path** and line reference
- **Risk rationale** and exploit precondition
- **Concrete remediation** steps

Separate immediate release blockers from backlog hardening tasks.

## Rules

- Perform read-only auditing unless explicitly asked to patch code
- State assumptions when environment or deployment details are missing
- Prefer secure defaults and least-privilege recommendations
- Do not run actual exploit attempts — this is a code-level review
