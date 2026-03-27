---
name: ctstyles
description: Apply CT.gov / AI Lab Design System. Use when asked to apply Connecticut state government design tokens, component patterns, and layout conventions to a web application.
---

# Apply CT.gov / AI Lab Design System

## Workflow

1. **Read the design system reference.**
   - Read `references/ct_design_system.md`. This contains design tokens, component patterns, and layout conventions.
   - If not found locally, look in `../ct-ai-lab-tools/references/ct_design_system.md`.

2. **Audit the current app.**
   - Identify current color scheme, font stack, header/footer structure, and component styles.

3. **Apply the design system.**
   - **Header**: Add accessibility bar, CT.GOV top bar, agency header band, and navigation bar.
   - **Footer**: Add agency footer (office name, address, phone, portal link).
   - **Colors & Typography**: Use CSS custom properties from the design system. Set font to Poppins.
   - **Components**: Style buttons (`.btn-primary`, `.btn-secondary`, etc.), forms, and cards according to the reference.
   - **Responsive**: Ensure mobile breakpoint at 700px and proper stacking.

4. **Add the language toggle.**
   - Implement EN/ES toggle with `data-i18n` attributes and `switchLanguage()` scaffold.

5. **Preserve functionality.**
   - Do not alter existing JS behavior or API endpoints. Only modify HTML structure and CSS.

## Rules

- Use CSS custom properties for all colors (e.g., `var(--color-primary)`).
- No inline styles.
- Maintain WCAG 2.1 AA contrast ratios.
- All interactive elements must have visible focus indicators.
- Load Poppins font from Google Fonts.
