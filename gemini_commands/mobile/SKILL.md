---
name: mobile
description: Check Mobile Responsiveness. Use to audit and fix web applications for mobile responsiveness, ensuring proper viewport, layout, touch targets, and form behavior.
---

# Check Mobile Responsiveness

## Inputs

- Accept an optional scope path as `$ARGUMENTS`.
- Audit the whole application when no scope is provided.

## Workflow

1. **Audit Viewport and Meta.** Ensure proper `viewport` tag and no zoom restrictions.
2. **Check Layout.** No horizontal scroll, single-column collapse, `max-width: 100%` on media.
3. **Check Typography.** Base size >= 16px, appropriate heading scaling.
4. **Check Touch Targets.** Minimum 44x44px, adequate spacing.
5. **Check Forms.** Correct `inputmode`, `autocomplete`, and native behavior.
6. **Check Navigation.** Usable on small screens, reachable back buttons.
7. **Check Modals and Tables.** Ensure they fit and scroll properly.
8. **Fix Issues.** Apply fixes directly in CSS/HTML. Prefer mobile-first CSS.

## Rules

- Fix issues directly.
- Do not add new frameworks (Tailwind, etc.) unless requested.
- Do not change desktop layout unless broken.
- Target common viewports (e.g., 375px wide).
