---
name: ctstyles
description: Apply an organization design system to a web application. Use when asked to restyle an app to match brand tokens, layout patterns, typography, components, responsive behavior, and accessibility requirements.
---

# Design System Application

## Inputs

- Accept an optional scope path (file or directory).
- Prefer a design system reference document if provided by the user.

## Resolve The Reference

1. Locate a design reference before editing.
- Prefer user-provided reference paths first.
- Otherwise check common project paths such as:
  - `./references/ct_design_system.md`
  - `./references/design_system.md`
  - `../references/ct_design_system.md`
- Stop and request the reference if none is available.

2. Extract required design rules.
- Token system: colors, spacing, radius, shadows, typography.
- Structural patterns: header, footer, navigation, card and section styles.
- Component patterns: buttons, forms, modals, status badges.
- Responsive breakpoints and accessibility requirements.

## Workflow

1. Audit current UI implementation.
- Map current colors, fonts, component styles, and layout patterns.
- Identify mismatches against the reference.

2. Apply styles systematically.
- Implement or normalize CSS custom properties for design tokens.
- Update header, footer, navigation, forms, buttons, cards, and modal patterns.
- Keep DOM edits minimal and structural.

3. Preserve behavior.
- Do not break existing data flow, route behavior, or API interactions.
- Keep existing JS logic intact unless UI changes require small glue updates.

4. Keep accessibility intact.
- Maintain visible focus indicators and contrast compliance.
- Preserve keyboard interaction patterns for navigation and modals.

5. Verify responsive behavior.
- Check representative viewport widths (about 375, 390, 412, and 768 px).
- Ensure horizontal layouts collapse predictably on smaller screens.

6. Summarize changes.
- Report files changed and what was aligned to the design system.
- Note any unresolved decisions requiring product input.

## Quality Bar

- Use variables/tokens instead of hardcoded colors.
- Keep styling centralized in CSS files, not inline styles.
- Favor consistency with the reference over custom redesign.
