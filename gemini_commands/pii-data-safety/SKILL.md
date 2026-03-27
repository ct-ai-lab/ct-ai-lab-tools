---
name: pii-data-safety
description: Audit PII and Data Safety. Use to audit an application for personally identifiable information risks and data safety, mapping data lifecycles and classifying sensitivity.
---

# Audit PII and Data Safety

## Inputs

- Accept an optional scope path as `$ARGUMENTS`.
- Audit the whole repository when no scope is provided.

## Workflow

1. **Map the data lifecycle.** Trace collection, storage, and display of user data.
2. **Classify sensitive data.** Identify direct identifiers, quasi-identifiers, and sensitive attributes.
3. **Audit collection.** Ensure minimization and necessity.
4. **Audit storage and transport.** Check for plaintext storage and encryption in transit.
5. **Audit logs and AI.** Ensure no PII in logs, telemetry, or AI prompts.
6. **Audit disclosure.** Check for deletion/correction controls and privacy disclosures.
7. **Produce findings.** Report with Severity, File Path, Risk, and Fix.

## Rules

- Read-only audit unless asked to patch.
- Never include real user data in reports.
- Prefer masking/hashing over deletion for fixes.
