# /ctstyles — Apply CT.gov / AI Lab Design System

You are a frontend developer applying the Connecticut state government design system to a web application.

## Steps

### 1. Read the design system reference

Read the file `references/ct_design_system.md` in this tools repo (or in the project if it's been copied there). This contains the full design tokens, component patterns, and layout conventions.

If the reference file is not found, search for it at these paths:
- `./references/ct_design_system.md`
- `~/.claude/references/ct_design_system.md`
- `../ct-ai-lab-tools/references/ct_design_system.md`

If still not found, inform the user and stop.

### 2. Audit the current app

Read the HTML template(s) and CSS file(s). Identify:
- Current color scheme
- Font stack
- Header/footer structure
- Button styles
- Form element styles
- Card/container patterns
- Responsive breakpoints
- Any existing CT.gov branding

### 3. Apply the design system

#### Header
- Add the accessibility bar (report accessibility issue link)
- Add the CT.GOV top bar (CT.GOV | State of Connecticut)
- Add the agency header band (CT logo, app title, subtitle, optional BETA tag)
- Add the resource banner (yellow/info banner below header, if applicable)
- Add the navigation bar (horizontal tabs with proper order)

#### Footer
- Add the agency footer (office name, address, phone, portal link)

#### Colors & Typography
- Replace all colors with CSS custom properties from the design system
- Set font-family to Poppins (with system font fallback)
- Apply proper heading sizes and weights

#### Buttons
- `.btn-primary` — solid dark blue with white text
- `.btn-secondary` — outlined, dark blue border and text
- `.btn-back` — text-style back button
- `.btn-lg` — large variant for prominent CTAs
- Consistent border-radius, padding, and hover states

#### Forms
- Consistent label styling with required-field star indicators
- Input/select styling with proper focus states
- Radio button groups with clear spacing
- Range slider with synced number input pattern

#### Cards & Sections
- `.edu-section` — content sections with bottom border
- `.resource-card` — bordered info cards
- `.resource-org-card` — logo + info side-by-side layout
- Step groups with consistent padding and spacing

#### Modals
- `.modal-overlay` — semi-transparent backdrop, click-outside-to-close
- `.modal-content` — centered white card with close button
- Focus trapping and Escape key handling

#### Responsive
- Mobile breakpoint at 700px
- Stack horizontal layouts vertically on mobile
- Navigation collapses to vertical list
- Button rows stack vertically
- Map/results columns stack

### 4. Add the language toggle

If not already present:
- EN/ES toggle buttons at top of content area
- `data-i18n` attributes on all user-facing text
- `switchLanguage()` function scaffold in JS

### 5. Preserve functionality

- Do not remove or alter any existing JavaScript behavior
- Do not change API endpoints or data flow
- Only modify HTML structure, CSS, and add the language toggle JS if missing

## Rules

- Use CSS custom properties for all colors (e.g., `var(--color-primary)`)
- Do not use inline styles — everything goes in the CSS file
- Maintain WCAG 2.1 AA contrast ratios (4.5:1 for text, 3:1 for large text)
- All interactive elements must have visible focus indicators
- Test that the header and footer look correct before finishing
- Load Poppins font from Google Fonts (with preconnect)
