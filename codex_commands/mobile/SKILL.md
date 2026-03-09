---
name: mobile
description: Audit and fix mobile responsiveness issues in web applications. Use when asked to review viewport behavior, breakpoints, touch targets, form usability, responsive layouts, modal behavior, and small-screen CSS regressions.
---

# Mobile Responsiveness Audit

## Inputs

- Accept an optional scope path (file or directory).
- Audit the full UI when scope is not provided.

## Workflow

1. Inspect relevant UI files.
- Read templates/components, CSS, and interaction JS.
- Identify breakpoints and layout systems in use.

2. Validate viewport and base assumptions.
- Ensure viewport meta tag exists and does not disable zoom.
- Ensure content can scale for accessibility.

3. Audit layout behavior.
- Find fixed-width elements that overflow on small screens.
- Ensure multi-column and side-by-side sections stack appropriately.
- Ensure media elements scale to container width.

4. Audit typography and controls.
- Ensure readable font sizing on mobile, including form inputs.
- Ensure tap targets are at least 44x44 px with enough spacing.
- Ensure navigation and critical controls remain reachable.

5. Audit overlays, tables, and sticky/fixed elements.
- Ensure modals fit viewport height and remain scrollable.
- Ensure wide tables are wrapped with horizontal scroll when needed.
- Ensure fixed/sticky UI does not block key content.

6. Fix issues directly.
- Apply minimal, targeted CSS/HTML adjustments.
- Preserve desktop behavior unless it is broken.
- Follow existing media query convention used by the project.

7. Summarize outcomes.
- Report fixes made and remaining design tradeoffs requiring user choice.

## Quality Bar

- Validate across representative widths around 375, 390, 412, and 768 px.
- Avoid framework additions for simple responsive fixes.
