# CT.gov / AI Lab Design System Reference

This document defines the design tokens, component patterns, and layout conventions used in Connecticut state government web applications built by the CT AI Lab.

Derived from [portal.ct.gov](https://portal.ct.gov) and the CT Office of the Healthcare Advocate's applications.

---

## Design Tokens (CSS Custom Properties)

```css
:root {
    /* Primary */
    --color-primary: #0046AD;
    --color-primary-dark: #003478;

    /* Text */
    --color-body-text: #0a0a0a;
    --color-text: #212529;
    --color-text-muted: #495057;

    /* Borders */
    --color-border: #CED4DA;
    --color-border-light: #E0E0E0;

    /* Backgrounds */
    --color-bg-light: #F0F4FA;
    --color-white: #FFFFFF;

    /* Status: Eligible */
    --color-eligible-bg: #D4EDDA;
    --color-eligible-text: #155724;

    /* Status: Not eligible / Warning */
    --color-not-eligible-bg: #FFF3CD;
    --color-not-eligible-text: #856404;

    /* Beta badge */
    --color-beta-bg: #FFC107;
    --color-beta-text: #664D03;

    /* Disclaimer banner */
    --color-disclaimer-bg: #FFF8E1;

    /* Spacing & Shape */
    --radius: 4px;
    --shadow-card: 0 1px 3px rgba(0,0,0,0.08);

    /* Typography */
    --font-family: 'Poppins', Arial, sans-serif;
}
```

## Typography

**Font:** Poppins (Google Fonts) with Arial/sans-serif fallback.

Load via:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
```

**Heading styles:**
| Element | Size | Weight | Color |
|---------|------|--------|-------|
| h1 | 2.25rem | 300 (light) | `--color-primary-dark` |
| h2 | 2rem | 400 (regular) | `--color-primary-dark` |
| h3 | 1.5rem | 500 (medium) | `#333` |

**Body:** 16px base, line-height 1.5, color `--color-body-text`.

---

## Page Layout

### Header (top to bottom)

1. **Accessibility bar** — `#2a2a2a` background, 32px tall, right-aligned "Report an accessibility issue" link
2. **CT.GOV bar** — `--color-primary-dark` background, 40px tall, "CT.GOV | State of Connecticut" left-aligned
3. **OHA header band** — `--color-primary` background, contains:
   - Top row: CT logo (32px tall SVG) + app title (h1, white, light weight) + BETA badge + subtitle line
   - Banner: descriptive paragraph in white/92% opacity, max-width 900px
   - Navigation: horizontal tab bar, white text, `border-top: 1px solid rgba(255,255,255,0.2)`, tabs separated by vertical borders
4. **Separator** — 1px `--color-border-light` line, 16px bottom margin

### Content area

- `max-width: 1200px`, centered, `padding: 0 32px`
- Language toggle (EN/ES) right-aligned at top
- Step-based sections shown/hidden with JS

### Footer

- `--color-primary-dark` background, white text
- Centered: "Office of the Healthcare Advocate | [address] | [phone] | [portal link]"
- 20px padding, `margin-top: 2rem`

---

## Components

### Buttons

**Primary** (`.btn-primary`):
```css
background: var(--color-primary-dark);
color: white;
border: none;
border-radius: var(--radius);
padding: 12px 32px;
font-weight: 600;
cursor: pointer;
```
Hover: `background: var(--color-primary)`

**Secondary** (`.btn-secondary`):
```css
background: white;
color: var(--color-primary-dark);
border: 2px solid var(--color-primary);
```
Hover: `background: var(--color-bg-light)`

**Large variant** (`.btn-lg`):
```css
font-size: 1.1rem;
padding: 18px 32px;
width: 100%;
text-align: left;
```

**Back button** (`.btn-back`):
```css
background: none;
border: 2px solid var(--color-primary);
color: var(--color-primary-dark);
padding: 12px 32px;
border-radius: var(--radius);
font-weight: 600;
```

### Button layouts

**Horizontal row** (`.btn-row`): `display: flex; gap: 12px; flex-wrap: wrap`
**Vertical stack** (`.btn-row-vertical`): `flex-direction: column`

### Forms

- Labels: `font-weight: 600`, `margin-bottom: 6px`
- Required indicator: red `*` with `aria-hidden="true"`
- Inputs: full width, `padding: 10px 14px`, `border: 2px solid --color-border`, `border-radius: var(--radius)`
- Focus: `border-color: var(--color-primary)`, `outline: 2px solid var(--color-primary)`, `outline-offset: 2px`
- Helper text: `<small>` with `font-size: 0.92rem`, `color: --color-text-muted`
- Radio groups: `role="radiogroup"` with `aria-labelledby`

### Cards

**Resource card** (`.resource-card`):
```css
background: var(--color-bg-light);
border: 1px solid var(--color-border-light);
border-radius: var(--radius);
padding: 16px;
margin-bottom: 12px;
```

**Organization card** (`.resource-org-card`): side-by-side logo + info layout, flexbox with gap.

### Educational sections

`.edu-section`: content blocks with `border-bottom: 1px solid --color-border-light`, `padding-bottom: 16px`, `margin-bottom: 16px`.

### Modals

```html
<div class="modal-overlay" onclick="if(event.target===this)closeModal()">
    <div class="modal-content" role="dialog" aria-modal="true" aria-labelledby="heading-id">
        <button class="modal-close" aria-label="Close">&times;</button>
        <h3 id="heading-id">Title</h3>
        <!-- content -->
    </div>
</div>
```

Modal overlay: `position: fixed`, full viewport, `background: rgba(0,0,0,0.5)`, `z-index: 9999`.
Modal content: `max-width: 560px`, centered, white background, `border-radius: 10px`, `max-height: 90vh`, `overflow-y: auto`.

### Status badges

**Eligible**: `background: --color-eligible-bg`, `color: --color-eligible-text`, `padding: 6px 16px`, `border-radius: 20px`
**Not eligible**: `background: --color-not-eligible-bg`, `color: --color-not-eligible-text`

### Disclaimer banner

```css
.ai-disclaimer-banner {
    background: var(--color-disclaimer-bg);
    border-left: 4px solid var(--color-beta-bg);
    padding: 12px 16px;
    font-size: 0.92rem;
    border-radius: var(--radius);
    margin: 16px 0;
}
```

### Did-you-know banner

Blue-tinted info banner: `background: --color-bg-light`, `border-left: 4px solid --color-primary`, same padding pattern.

### Language toggle

Two buttons, right-aligned. Active button: `background: --color-primary`, `color: white`. Inactive: `background: white`, `color: --color-primary`, `border: 2px solid --color-primary`.

---

## Responsive Design

**Breakpoint:** `@media (max-width: 700px)`

Key changes at mobile:
- Header nav: `flex-direction: column`, full-width links
- Button rows: stack vertically
- Side-by-side layouts (results + map): stack vertically
- Container padding reduces to 12-16px
- Cards: full width, no side-by-side

---

## Accessibility Patterns

- Skip link as first focusable element
- `aria-live` regions for dynamic content
- Step headings have `tabindex="-1"` and receive focus via JS on navigation
- All form inputs linked to labels via `for`/`id`
- Required fields: `aria-required="true"` + visible `*`
- Helper text linked via `aria-describedby`
- Radio groups: `role="radiogroup"` + `aria-labelledby`
- Modals: focus trap, Escape to close, backdrop click to close

---

## i18n Pattern

- All user-facing text has `data-i18n="key_name"` attribute
- Translations stored as a Python dict, passed to template as JSON
- `switchLanguage(lang)` in JS iterates `[data-i18n]` elements and updates `.textContent`
- HTML content uses `data-i18n-html` (sets `.innerHTML`)
- Placeholders use `data-i18n-placeholder`
- Language toggle buttons update `aria-pressed`

---

## Navigation Pattern

- Single-page app with step-based navigation
- `ALL_STEPS` array lists all section IDs
- `showStep(stepId)` hides all sections, shows the target, scrolls to top, focuses heading
- Back buttons on every step
- Triage gate on step0 routes to different flows via `choosePath(path)`
