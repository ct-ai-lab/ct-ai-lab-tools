# /ctstyles — Apply the CT AI Lab style guide

You are a frontend developer making a web app look and behave like the other Connecticut AI Lab apps: the same CT.GOV chrome, the CT logo used correctly, large friendly type and spacing, and WCAG 2.2 AA accessibility.

## Steps

### 1. Read the references

Read both files from this tools repo (or from the project, if they were copied there):

1. `references/lab_style_guide.md`: the rules. Chrome, logo, colors, type sizes, spacing, control sizes, accessibility, and how to check the result. **Where the two files disagree, this one wins.**
2. `references/ct_design_system.md`: raw tokens and component patterns scraped from portal.ct.gov.

If they are not found, look in `./references/`, `../ct-ai-lab-tools/references/` and `~/.claude/references/`. If still not found, tell the user and stop.

### 2. Audit the current app

Read the base template(s) and stylesheet(s). Note what differs from the style guide:
- Chrome: accessibility bar, CT.GOV bar, header band, logo, title, tabs, separator, context row, footer
- Font stack and the type scale (anything under 14px, body under 18px)
- Colors not defined as custom properties, and red/amber/green used for amounts
- Control heights under 44px, inputs under 48px, card padding under 24px
- Heading structure: more than one `h1` (often the app name in the header), skipped levels
- Breakpoints other than 1024px and 640px; page widths that change between tabs

If the app runs locally, run `references/ui_audit.py` against its main pages first and keep the output.

### 3. Apply the style guide

#### Chrome (section 1 of the guide)
- Rebuild the header from the guide's markup skeleton: skip link, accessibility bar, CT.GOV bar, header band with the CT logo and a `span` app title, subtitle, optional BETA pill, horizontal tabs with a white active tab and server-rendered `aria-current="page"`, mobile menu button.
- Add the separator and the context row under the header. Move any search box or switcher out of the header band.
- Footer: agency name, address, phone and portal link for a public single-agency app; "Built by the Connecticut AI Lab" plus app notes for an internal staff tool.

#### Logo (section 2)
- White CT mark, 48px tall (36px at ≤640px), first in the header row, linked to portal.ct.gov with `aria-label="CT.GOV home"` and `alt="Connecticut CT.GOV logo"`. Never recolored, stretched, rounded or placed on a light background. Agency and partner logos go in page content, not the header.

#### Tokens, type and layout (sections 3 and 4)
- Define the color tokens as custom properties and replace hard-coded colors.
- Poppins everywhere, 300/400/500/600, loaded from Google Fonts with `preconnect`.
- Apply the type scale: 14px floor, 18px body (20px for public screeners), 36px page `h1`.
- One container width on every page; 24px card padding; KPI numbers that never wrap; grids with `minmax(0, …)` columns so tables scroll inside their panels.
- Breakpoints at 1024px and 640px.

#### Controls (section 5)
- 44px minimum for every button, tab and toggle; 48px inputs and selects; 20px checkboxes and radios.
- 3px focus outline everywhere (white on the blue bands).
- Underline links in running text.

#### Structure (section 6)
- Make the page title the only `h1`; panels become `h2`, their subsections `h3`.
- `scope` on every `th`, visible labels on every field, associated error messages.
- Dialogs: focus in, focus trapped, Escape closes.

#### Public, resident-facing apps only
- Add an EN/ES language toggle in the context row if the app serves residents and has no translations yet: `data-i18n` attributes on user-facing text and a `switchLanguage()` scaffold in JS.

### 4. Preserve functionality

- Do not remove or alter existing JavaScript behavior, API endpoints or data flow. If a script finds an element by ID (agency switcher, menu toggle), keep the ID when you move the element.
- Only change templates, CSS and small presentational JS.
- If tests assert on markup (headings, classes), update them to the new structure and say so.

### 5. Check the result (section 7)

1. Run `references/ui_audit.py` over the main pages. Every page must print OK at 1440px and 390px.
2. Take full-page screenshots at both widths and look at them: chrome as in the guide, nothing under the feedback tab, no amounts broken across lines, no sideways scrolling.
3. Make sure cached static files get a new version when the CSS changes.
4. Run the project's tests, linter and type checker, and report the real output.

## Rules

- Use CSS custom properties for all colors (e.g., `var(--brand)`).
- No inline styles: everything goes in the CSS file.
- WCAG 2.2 AA: 4.5:1 contrast for text (3:1 for 24px+), visible focus on every control, 44px targets.
- Nothing readable under 14px; one `h1` per page; no skipped heading levels.
- Load Poppins from Google Fonts with `preconnect`.
- Prefer bigger and roomier over denser: the apps should feel friendly and easy to use.
