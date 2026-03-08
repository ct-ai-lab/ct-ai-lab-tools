# /mobile — Check Mobile Responsiveness

You are a frontend developer auditing a web application for mobile responsiveness issues.

## If an argument is provided

Focus on the specific file or component passed as `$ARGUMENTS`. Otherwise, audit the full application.

## Steps

### 1. Read all HTML templates and CSS files

Understand the layout structure, responsive breakpoints, and any mobile-specific styles.

### 2. Check each category

#### Viewport & Meta
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1.0">` is present
- [ ] No `maximum-scale=1` or `user-scalable=no` (these break accessibility zoom)

#### Layout
- [ ] No fixed-width containers that would cause horizontal scroll on small screens
- [ ] Flexbox/grid layouts collapse to single-column on mobile
- [ ] Side-by-side layouts (results + map, logo + text, etc.) stack vertically below the mobile breakpoint
- [ ] No elements with `width` set in pixels that exceed ~360px (smallest common viewport)
- [ ] `max-width: 100%` on images, iframes, and embedded content

#### Typography
- [ ] Base font size is at least 16px (prevents iOS auto-zoom on input focus)
- [ ] Line lengths don't exceed ~80 characters on any viewport
- [ ] Headings scale down appropriately (no giant h1 on mobile)

#### Touch Targets
- [ ] Buttons and links are at least 44x44px
- [ ] Adequate spacing between touch targets (at least 8px gap)
- [ ] No tiny close buttons or icon-only buttons below 44px

#### Forms
- [ ] Inputs use the correct `inputmode` attribute (`numeric`, `email`, `tel`, etc.)
- [ ] Inputs use appropriate `autocomplete` values
- [ ] Select dropdowns work natively on mobile (no custom dropdowns that break)
- [ ] Form labels are visible (not hidden above a scrolled-away area)
- [ ] Input font size is at least 16px (prevents iOS zoom)

#### Navigation
- [ ] Nav bar is usable on mobile (wraps, collapses, or scrolls horizontally)
- [ ] Back buttons are easily reachable
- [ ] No hover-dependent interactions without a touch alternative

#### Modals & Overlays
- [ ] Modals don't exceed viewport height (use `max-height: 90vh` with `overflow-y: auto`)
- [ ] Modal close buttons are reachable without scrolling
- [ ] Backdrop click-to-close works on touch devices

#### Tables (if any)
- [ ] Tables scroll horizontally in a wrapper, or reflow for mobile
- [ ] No tables wider than the viewport without a scroll container

#### Images & Media
- [ ] Images have `max-width: 100%` and `height: auto`
- [ ] No images wider than the viewport
- [ ] Embedded iframes (maps, videos) are responsive

#### CSS Issues to Check
- [ ] No `position: fixed` elements that cover content on small screens
- [ ] No negative margins that push content off-screen
- [ ] `overflow: hidden` on body/main doesn't prevent scrolling
- [ ] Sticky elements don't consume too much vertical space on mobile

### 3. Check responsive breakpoints

Look at all `@media` queries in the CSS. Verify:
- There is at least one breakpoint for mobile (typically 600-768px)
- All major layout shifts happen at that breakpoint
- No components are missed (e.g., a card layout that doesn't stack)

### 4. Fix issues

For each issue found:
- Fix it directly in the CSS or HTML
- Prefer mobile-first CSS (`min-width` media queries) but match the existing project's convention
- If a fix requires a judgment call on design (e.g., should this element be hidden on mobile?), note it and suggest options

### 5. Summary

List what was checked, what was fixed, and any design decisions left for the user.

## Rules

- Fix issues directly — don't just report them
- Don't add a CSS framework (Bootstrap, Tailwind, etc.) to fix mobile issues
- Don't change the desktop layout unless it's broken
- Test mental model: imagine a 375px wide screen (iPhone SE) — does everything fit and work?
- Common viewport widths to consider: 375px (iPhone SE), 390px (iPhone 14), 412px (Pixel), 768px (iPad)
