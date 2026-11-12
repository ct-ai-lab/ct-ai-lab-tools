---
name: ctstyles
description: Apply the CT AI Lab style guide. Use when asked to make a web app match the Connecticut AI Lab apps: CT.GOV chrome, CT logo, colors, type sizes, spacing, control sizes and WCAG 2.2 AA accessibility.
---

# Apply the CT AI Lab style guide

## Workflow

1. **Read the references.**
   - Read `references/lab_style_guide.md` (the rules: chrome, logo, colors, type scale, spacing, controls, accessibility, checks). Where it disagrees with the next file, it wins.
   - Read `references/ct_design_system.md` (raw portal.ct.gov tokens and components).
   - If not found locally, look in `../ct-ai-lab-tools/references/`.

2. **Audit the current app.**
   - Compare the chrome, font stack, type scale, colors, control heights, heading structure and breakpoints with the guide.
   - If the app runs locally, run `references/ui_audit.py` over its main pages and keep the output.

3. **Apply the guide.**
   - **Chrome**: skip link, accessibility bar, CT.GOV bar, header band with the CT logo and a `span` app title, tabs with a white active tab and server-rendered `aria-current="page"`, separator, context row, footer (agency office line for a public single-agency app; "Built by the Connecticut AI Lab" for a staff tool). No search or switchers in the header band.
   - **Logo**: white CT mark, 48px (36px at ≤640px), first in the header, linked to portal.ct.gov; never recolored, stretched or on a light background.
   - **Type and layout**: Poppins only; 14px floor, 18px body, 36px page `h1`; one container width on every page; 24px card padding; breakpoints at 1024px and 640px.
   - **Controls**: 44px minimum targets, 48px inputs, 3px focus outline, underlined links in running text.
   - **Structure**: one `h1` per page, no skipped heading levels, labelled fields, `scope` on table headers.

4. **Language toggle (public, resident-facing apps only).**
   - Add an EN/ES toggle with `data-i18n` attributes and a `switchLanguage()` scaffold if missing.

5. **Preserve functionality.**
   - Do not alter JS behavior, API endpoints or data flow; keep element IDs that scripts use.

6. **Check the result.**
   - `references/ui_audit.py` prints OK for every page at 1440px and 390px; screenshots match the guide; tests, linter and type checker pass.

## Rules

- Use CSS custom properties for all colors (e.g., `var(--brand)`). No inline styles.
- WCAG 2.2 AA: contrast, visible focus, 44px targets, nothing readable under 14px.
- Load Poppins from Google Fonts with `preconnect`.
- Prefer bigger and roomier over denser.
