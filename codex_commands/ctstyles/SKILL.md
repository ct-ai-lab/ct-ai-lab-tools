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
- Structural patterns: header band order, footer, navigation, separators, card and section styles.
- Component patterns: buttons, forms, modals, status badges.
- Asset requirements: logos, icons, and any branded lockups called for by the reference.
- Responsive breakpoints and accessibility requirements.

## Workflow

1. Audit current UI implementation against the reference, not against itself.
- Map current colors, fonts, component styles, layout patterns, and page shell structure.
- Compare the actual page composition to the reference in order: accessibility bar, CT.GOV bar, branded header band, nav, separator, content shell, footer.
- Identify custom flourishes that are not in the reference such as glassmorphism, extra gradients, oversized radii, ad hoc shadows, or decorative motion.
- Do not treat "same colors" as sufficient if the page structure still diverges from the reference.

2. Apply styles systematically.
- Implement or normalize CSS custom properties for design tokens using the reference names and values when practical.
- Update header, footer, navigation, forms, buttons, cards, banners, tables, badges, and modal patterns to match the reference.
- Keep styling centralized in CSS files.
- Remove inline styles and presentation-driven HTML where reasonable.
- For dynamic UI states, prefer semantic classes or CSS custom properties over hardcoded colors in JS.
- Keep DOM edits minimal, but do not avoid necessary structural edits when the current markup cannot match the reference.

3. Preserve behavior.
- Do not break existing data flow, route behavior, or API interactions.
- Keep existing JS logic intact unless UI changes require small glue updates.
- When JS currently emits styled HTML fragments, convert it to emit semantic state classes if that is the cleaner path.

4. Keep accessibility intact.
- Maintain visible focus indicators and contrast compliance.
- Preserve keyboard interaction patterns for navigation and modals.
- Keep or add skip links, `aria-live` regions, proper label/input associations, and focusable headings when the reference expects them.

5. Verify responsive behavior.
- Check representative viewport widths (about 375, 390, 412, and 768 px).
- Ensure horizontal layouts collapse predictably on smaller screens.
- Specifically verify header nav, button rows, table containers, filters/selectors, and side-by-side cards at mobile widths.
- If no browser runtime is available, reason through the DOM and CSS breakpoints carefully and state that visual verification is still pending.

6. Summarize changes.
- Report files changed and what was aligned to the design system.
- Note any unresolved decisions requiring product input.
- Call out any temporary asset substitutions when official branded assets were not available.

## Quality Bar

- Use variables/tokens instead of hardcoded colors.
- Keep styling centralized in CSS files, not inline styles.
- Favor consistency with the reference over custom redesign.
- Do not stop at recoloring; align structure, hierarchy, and component behavior to the reference.
- Prefer the reference's token names and component states over inventing parallel naming.
- If official logos or brand assets are missing, use a neutral placeholder only when needed and note the follow-up explicitly.
