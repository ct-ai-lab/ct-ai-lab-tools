---
name: pii-data-safety
description: Identify and reduce personally identifiable information risk across application code and data flows. Use when asked to audit collection, storage, logging, analytics, prompts, exports, and retention of sensitive user data.
---

# PII Data Safety

## Inputs

- Accept optional scope path (file or directory).
- Accept optional policy context (state policy, federal program constraints, retention rules).
- Default to full-repo audit when scope is not provided.

## Workflow

1. Map data lifecycle.
- Identify where user data is collected, transformed, stored, displayed, exported, and deleted.
- Trace flows across frontend, backend, queues, third-party APIs, logs, and analytics.

2. Identify sensitive data classes.
- Classify fields as direct identifiers, quasi-identifiers, sensitive attributes, or low-risk metadata.
- Include uploaded files, free text, and model prompt/response content in classification.

3. Audit collection and minimization.
- Check whether each collected field is necessary for the user outcome.
- Flag over-collection and duplicate collection.
- Recommend minimizing scope, granularity, and retention window.

4. Audit storage, transport, and access controls.
- Check for plaintext storage of sensitive fields.
- Check for insufficient access boundaries around sensitive datasets.
- Check for risky replication into caches, exports, and backups.

5. Audit logs, telemetry, and prompts.
- Search server logs, client logs, analytics events, traces, and error payloads.
- Flag raw PII leakage in logs and monitoring attributes.
- Flag prompt construction that unnecessarily injects sensitive user data.

6. Audit disclosure and lifecycle controls.
- Verify deletion and correction workflows exist where expected.
- Verify retention settings and archival policies are explicit.
- Verify user-visible disclosures match actual data behavior.

7. Remediate with safe patterns.
- Replace raw identifiers in logs with masked, hashed, or tokenized forms.
- Add field-level redaction helpers for logs and error handlers.
- Restrict outbound payloads to required minimum fields.
- Add explicit data handling comments where behavior is non-obvious.

8. Produce findings and follow-ups.
- Classify each finding as `blocker`, `high`, `medium`, or `low`.
- Include affected files, risk explanation, and concrete fix steps.
- Separate immediate remediation from policy/legal confirmation items.

## Rules

- Never include real user data in reports or examples.
- Use synthetic placeholders when demonstrating patterns.
- Perform read-only auditing unless explicitly asked to patch code.
