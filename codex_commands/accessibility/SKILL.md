---
name: accessibility
description: Audit and fix web accessibility issues to WCAG 2.1 AA. Use when asked to review or remediate semantic HTML, keyboard access, focus behavior, forms, ARIA usage, contrast, live regions, or screen reader support.
---

# Accessibility Audit And Remediation

## Inputs

- Accept an optional scope path (file or directory).
- Audit the whole application when no scope is provided.

## Workflow

1. Inventory relevant UI files.
- Read HTML templates/components, CSS, and frontend JS used for interaction patterns.
- Identify forms, navigation, modals, tables, media, and dynamic content regions.

2. Audit semantics and structure.
- Ensure a single logical main content region.
- Ensure heading levels are sequential and meaningful.
- Ensure nav, lists, tables, and landmarks use semantic elements first.

3. Audit keyboard and focus behavior.
- Ensure all interactive controls are reachable by keyboard.
- Ensure focus order follows visual order.
- Replace non-semantic clickable containers with semantic controls.
- Ensure modals trap focus and close on Escape.
- Move focus to new step/view headings after navigation updates.

4. Audit forms and feedback.
- Ensure every input has a visible label tied by for/id.
- Ensure helper text and errors are associated with aria-describedby or aria-errormessage.
- Ensure required fields have visible indicators and programmatic signaling.
- Ensure validation and status messages are announced with focus management or aria-live.

5. Audit media, color, and language.
- Ensure images and icon-only controls have appropriate text alternatives.
- Ensure contrast meets WCAG 2.1 AA thresholds.
- Ensure information is not conveyed by color alone.
- Ensure document language is declared and per-section language is set where needed.

6. Audit responsive and touch accessibility.
- Ensure touch targets are at least 44x44 px.
- Ensure content is usable at 200 percent zoom without horizontal scroll for primary flows.
- Ensure hover-only interactions have keyboard and touch alternatives.

7. Fix issues directly.
- Apply safe, minimal code changes while preserving existing behavior.
- Prefer semantic HTML over ARIA workarounds.
- Avoid adding ARIA that duplicates native semantics.

8. Summarize changes.
- Report fixed items grouped by category.
- Call out any unresolved items that require product or content decisions.

## Quality Bar

- Prioritize correctness over cosmetic consistency.
- Keep behavior stable unless an accessibility fix requires a visible change.
- Flag uncertain alt text/content choices explicitly.
