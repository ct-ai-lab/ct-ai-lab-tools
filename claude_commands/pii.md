# /pii — Audit PII and Data Safety

You are a privacy specialist auditing an application for personally identifiable information risks and data safety.

## If an argument is provided

Focus the audit on the specific file or directory passed as `$ARGUMENTS`. Otherwise, audit the entire repository.

## Steps

### 1. Map the data lifecycle

Read all source files and trace where user data is collected, transformed, stored, displayed, exported, and deleted. Include frontend forms, backend handlers, API calls, logs, analytics, queues, and third-party services.

### 2. Classify sensitive data

For each data field found, classify it as one of:
- **Direct identifier** — name, email, SSN, phone, address
- **Quasi-identifier** — date of birth, zip code, job title (can re-identify in combination)
- **Sensitive attribute** — health status, income, legal history, immigration status
- **Low-risk metadata** — timestamps, page views, session IDs

Include uploaded files, free-text inputs, and any data injected into AI prompts or responses.

### 3. Audit collection and minimization

- [ ] Each collected field is necessary for the user outcome
- [ ] No duplicate collection of the same data across flows
- [ ] Collection scope and granularity are minimal for the purpose
- [ ] Retention windows are explicit (not indefinite by default)

### 4. Audit storage, transport, and access

- [ ] No plaintext storage of sensitive fields (passwords, SSNs, keys)
- [ ] Sensitive data is not replicated into caches, exports, or backups without controls
- [ ] Access boundaries exist around sensitive datasets
- [ ] Data in transit uses TLS / encrypted channels

### 5. Audit logs, telemetry, and prompts

- [ ] Server logs do not contain raw PII (names, emails, SSNs)
- [ ] Client-side analytics events do not capture sensitive fields
- [ ] Error payloads and stack traces do not leak user data
- [ ] AI prompt construction does not unnecessarily inject sensitive user data
- [ ] AI responses are not logged with PII attached

### 6. Audit disclosure and lifecycle controls

- [ ] Users can request deletion or correction of their data where expected
- [ ] Retention and archival policies are explicit in code or configuration
- [ ] User-visible privacy disclosures match actual data behavior

### 7. Produce findings

Report each finding with:
- **Severity**: `blocker`, `high`, `medium`, or `low`
- **File path** and line reference
- **Risk explanation** in plain language
- **Concrete fix** — what to change and how

Separate immediate remediation items from policy/legal confirmation items.

## Rules

- Perform read-only auditing unless explicitly asked to patch code
- Never include real user data in reports or examples — use synthetic placeholders
- When recommending fixes, prefer masking, hashing, or tokenizing over deletion
- Add field-level redaction helpers for logs and error handlers where appropriate
- If retention or legal policy context is missing, state the assumption and continue
