# CT AI Lab app style guide

How every CT AI Lab web app should look, so someone who has used one lab app already knows the
next. The `ctstyles` skill follows this guide; read it before any UI work.

- **This guide** sets the page chrome, the CT logo, color use, type sizes, spacing, control
  sizes and the accessibility checks. It reflects the lab's apps as of November 2026.
- **`ct_design_system.md`** (same folder) holds the raw tokens and component patterns
  scraped from portal.ct.gov. Where the two disagree (body size, breakpoint), this guide wins.

The goal is **friendly and easy to use**: big type, generous spacing, large click targets,
plain words. When in doubt, go bigger and leave more room, not denser.

## 1. Page chrome, top to bottom

Every page has the same bands in this order. Do not restyle them per app.

| Band | Spec |
|---|---|
| Skip link | First in `<body>`, hidden until focused: "Skip to main content" → `#main-content` |
| Accessibility bar | `#2a2a2a`, min 32px tall, right-aligned link "Report an accessibility issue" (`mailto:` the team's address with the app name in the subject), 14px `#d0d0d0` |
| CT.GOV bar | `#1F64E5`, 40px tall, 32px side padding. Text "**CT.GOV** &nbsp;\|&nbsp; State of Connecticut", 15px white, links to `https://portal.ct.gov` |
| Header band | `#003D9C`. Row padding `24px 32px 16px`, gap 16px: CT logo, then the title link |
| App title | A `span`, **not a heading**: Poppins 300, 3.375rem (54px), white, line-height 1.2. Optional `BETA` pill: `#FFC107` on `#664D03`, 18px 600, radius 10px |
| Subtitle | One plain sentence of what the app is for, 22px, white at 90% |
| Tabs | Inside the header band, top border white at 20%. Each tab min 48px tall, 1.1rem 500, padding `12px 20px`, divider white at 15%. **The active tab is white with `#003478` text** and `aria-current="page"` rendered by the server. Secondary tabs (Getting started, Admin) sit at the right after a flexible spacer |
| Separator | 1px `#E0E0E0`, 16px below |
| Context row | Right-aligned under the separator: language toggle, agency switcher, or the current agency. **Never put search boxes or switchers in the header band.** Search goes on a page or a tab |
| Main | `<main id="main-content">` with one `.container` |
| Footer | `#1F64E5`, white 16px text, padding `20px 32px`, centered, items separated by `&nbsp;\|&nbsp;`. **Public app for one agency:** agency name, office address, phone, `portal.ct.gov/<agency>` link. **Internal staff tool:** "Built by the Connecticut AI Lab" plus app notes (signed-in user, sign-out) |
| Feedback+ | The lab's fixed right-edge feedback tab, `#e87722`. Keep content clear of it (section 4) |

Markup skeleton (class names as used in the lab's apps):

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
<header>
  <div class="accessibility-bar"><a href="mailto:...?subject=App%20accessibility%20issue">Report an accessibility issue</a></div>
  <div class="ct-gov-bar"><a href="https://portal.ct.gov" target="_blank" rel="noopener"><strong>CT.GOV</strong> &nbsp;|&nbsp; <span>State of Connecticut</span></a></div>
  <div class="ct-header">
    <div class="ct-header-top">
      <a href="https://portal.ct.gov" target="_blank" rel="noopener" class="ct-logo-link" aria-label="CT.GOV home">
        <img src="/static/images/ct-logo.svg" alt="Connecticut CT.GOV logo" class="ct-logo">
      </a>
      <a href="/" class="ct-title-link">
        <span class="ct-site-title">App name <span class="ct-beta">BETA</span></span>
        <span class="ct-subtitle">One sentence on what the app is for</span>
      </a>
    </div>
    <button type="button" class="mobile-menu-toggle" aria-expanded="false" aria-controls="primary-navigation" hidden>Menu</button>
    <nav id="primary-navigation" class="ct-header-nav" aria-label="Primary navigation">
      <a href="/" class="active" aria-current="page">Overview</a>
      <a href="/items">Items</a>
      <span class="ct-nav-spacer"></span>
      <a href="/guide">Getting started</a>
    </nav>
  </div>
</header>
<div class="ct-separator"></div>
<main id="main-content"><div class="container">
  <div class="context-row"><!-- language toggle or agency switcher --></div>
  <!-- page: eyebrow, one h1, description, content -->
</div></main>
<footer class="ct-footer">...</footer>
```

## 2. The CT logo

- **File:** `static/images/ct-logo.svg`, the white CT mark.
- **Placement:** only in the header band, first item in the header row, before the title.
- **Size:** `height: 48px; width: auto` on desktop, `36px` at ≤640px. Never stretch it, round its
  corners, add a shadow or a background tile, or recolor it. It is white because it sits on the
  dark header blue; do not put the white mark on a light background.
- **Link and text:** it links to `https://portal.ct.gov` (new tab, `rel="noopener"`) with
  `aria-label="CT.GOV home"` and `alt="Connecticut CT.GOV logo"`. The app title next to it links
  to the app's home page.
- **Agency and partner logos** never go in the header. Put them in page content, such as a
  resources card, with real alt text.
- **Print:** grayscale (`filter: grayscale(1)`) on a white header.

## 3. Color

Define these as CSS custom properties and use them everywhere; never hard-code a hex value in a
template or inline style.

| Token | Value | Use |
|---|---|---|
| `--brand` | `#0046AD` | Links, primary buttons, focus ring |
| `--brand-dark` | `#003478` | Headings, hover, active tab text |
| `--portal-utilbar` | `#1F64E5` | CT.GOV bar, footer |
| `--portal-header` | `#003D9C` | Header band |
| `--brand-tint` / `-2` | `#E9F0FA` / `#D3E1F5` | Callout backgrounds, hover rows |
| `--ink` / `--ink-2` / `--ink-muted` | `#0a0a0a` / `#212529` / `#495057` | Body text / secondary / hints |
| `--line` / `--line-2` | `#E0E0E0` / `#CED4DA` | Card borders / input borders |
| `--page-bg` | `#FFFFFF` | Page background: white, as on portal.ct.gov |
| `--ok`, `--warn`, `--danger`, `--neutral` (+ `-bg`) | `#1B7F52`, `#8A5300`, `#A3231C`, `#475569` | **States only**: done or approved, needs review or due soon, overdue or error, not started |

Red, amber and green mean a state, never an amount. Amounts (spend, scores, counts) use one hue
stepped light to dark. All text meets WCAG AA contrast (4.5:1, or 3:1 for 24px+).

## 4. Type, spacing and layout

**Font:** Poppins everywhere (UI and headings), weights 300/400/500/600 from Google Fonts with
`preconnect`, falling back to Arial. No second typeface.

| Token | Size | Used for |
|---|---|---|
| `--fs-xs` | 14px | **The floor.** Table headers, badges, eyebrows, fine print. Nothing readable is smaller |
| `--fs-sm` | 16px | Buttons, inputs, hints, secondary text |
| `--fs-base` | 18px | Body text, table cells. Public, resident-facing screeners may use 20px |
| `--fs-md` | 20px | Subsection headings, lead paragraphs |
| `--fs-lg` | 22px | Card and panel titles (`h2` inside a panel, weight 600) |
| `--fs-xl` | 28px | Section headings (`h2`, weight 400) |
| `--fs-2xl` | 36px | The page `h1` (weight 300) and big KPI numbers (600) |

Body line-height 1.6. Reading text (descriptions, guides, intros) stops at `max-width: 76ch`.
Headings are `--brand-dark`.

**Layout:**
- One `.container` width on every page, so the layout never jumps between tabs: up to 1520px for
  data-heavy staff tools, 1200px for public screeners. Side padding 32px; 56px at ≥1025px if
  buttons sit at the right edge, so the Feedback+ tab never covers them; 12px at ≤640px.
- Page head: eyebrow (14px uppercase, letter-spacing 0.1em, muted), then `h1`, then a one-line
  description, then actions; 24px below.
- Cards and panels: white, 1px `--line`, radius 4px, light shadow, **padding 24px**, 20px between
  them. Panel header strip: padding `16px 24px`, light gray background.
- KPI tiles: grid `repeat(auto-fit, minmax(180px, 1fr))`, gap 16px, padding `18px 20px`. Numbers
  never wrap mid-amount (`white-space: nowrap`); give long dollar figures a smaller size or the
  full row on phones.
- Grids that hold tables use `minmax(0, …)` columns, so a wide table scrolls inside its own
  wrapper instead of making the page scroll sideways.
- Breakpoints: 1024px (tablet: smaller tabs, one-column dashboards) and **640px** (phone: menu
  button, stacked tabs, two KPI tiles per row, full-width buttons).

## 5. Controls

- **Every control is at least 44px tall**: buttons, small buttons, selects, tabs, link-style
  buttons, `summary` toggles. Text inputs and selects are 48px with `12px 14px` padding;
  checkboxes and radios are 20px with `accent-color: var(--brand)`.
- Buttons: radius 4px, padding `10px 24px`, 16px 500. Primary is solid `--brand`; secondary is
  white with a `--brand` border and text; destructive is `--danger`. One primary button per area.
- Labels sit above fields, 18px 500, 6px gap; hints 16px muted below. Required fields get a red `*`
  and the word "required" for screen readers. Errors are red text under the field, linked with
  `aria-describedby`.
- Focus: `outline: 3px solid var(--brand); outline-offset: 2px` everywhere; white on the blue
  bands. Never remove an outline without replacing it.
- Links inside running text (`p`, `li`, `td`, callouts) are underlined, not only colored
  (WCAG 1.4.1). Tab-like rows of links are not.

## 6. Structure and accessibility (WCAG 2.2 AA)

These are pass/fail. `ui_audit.py` (same folder) checks the first five automatically.

1. Exactly one `h1` per page: the page title. The app name in the header is a `span`.
2. No skipped heading levels: panels under the `h1` are `h2`, their subsections `h3`.
3. No readable text under 14px.
4. No control under 44px tall.
5. No sideways scrolling at 390px wide.
6. Every `th` has `scope`; tables without visible headers get a `caption` or a visually hidden
   header row.
7. Every field has a visible, associated `<label>`; no placeholder-only fields.
8. `aria-current="page"` on the active tab, rendered by the server, not added by JavaScript.
9. Dialogs move focus in, trap it, and close on Escape.
10. Respect `prefers-reduced-motion`; include a print stylesheet (no chrome, grayscale logo).
11. Write at about a grade-6 reading level: short sentences, plain words, no jargon in labels.
    Say what a button does ("Record invoice", not "Submit").

## 7. Checking your work

1. Run the app locally with demo data and run the audit over its main pages:
   `python references/ui_audit.py http://127.0.0.1:8000 / /page2 ...`. Every page must print OK
   at both widths.
2. Take full-page screenshots at 1440px and 390px and look at them: the chrome matches this
   guide, nothing is covered by the feedback tab, no amounts break across lines, and tables
   scroll inside their panels.
3. If static files are cached with a version query (`?v=`), make sure the version changes when
   the CSS changes (for example, a hash of the static files at startup), or users keep the old
   styles.
4. Run the app's tests, linter and type checker.
