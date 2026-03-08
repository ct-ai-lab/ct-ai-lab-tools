# /accessibility — Audit & Fix Accessibility (WCAG 2.1 AA)

You are an accessibility specialist auditing a web application against WCAG 2.1 Level AA standards.

## If an argument is provided

Focus the audit on the specific file or component passed as `$ARGUMENTS`. Otherwise, audit the entire application.

## Steps

### 1. Read all HTML templates and CSS files

Identify every interactive element, form, navigation pattern, modal, and dynamic content area.

### 2. Audit each category and fix issues as you go

#### Semantic HTML
- [ ] Page has exactly one `<main>` element
- [ ] Headings follow a logical hierarchy (h1 → h2 → h3, no skipped levels)
- [ ] Navigation is wrapped in `<nav>` with an `aria-label`
- [ ] Lists use `<ul>`, `<ol>`, or `<dl>` (not divs with visual bullets)
- [ ] Sections use `<section>`, `<article>`, or `<aside>` where appropriate
- [ ] Tables (if any) have `<thead>`, `<th>` with `scope`, and `<caption>`

#### Skip Link
- [ ] "Skip to main content" link exists as the first focusable element
- [ ] It targets `#main-content` (or equivalent) with matching `id`
- [ ] It's visually hidden until focused

#### Keyboard Navigation
- [ ] All interactive elements are reachable via Tab key
- [ ] Focus order follows visual order (no `tabindex` > 0)
- [ ] Custom buttons use `<button>`, not `<div>` or `<span>` with click handlers
- [ ] Links that act as buttons use `role="button"` or are actual `<button>` elements
- [ ] Modals trap focus (Tab cycles within modal, Escape closes)
- [ ] Focus is moved to new content when steps/views change (e.g., `heading.focus()`)

#### Forms
- [ ] Every input has a visible `<label>` with matching `for`/`id`
- [ ] Required fields have `aria-required="true"` and a visible indicator
- [ ] Helper text is linked via `aria-describedby`
- [ ] Error messages are linked via `aria-describedby` or `aria-errormessage`
- [ ] Radio groups use `role="radiogroup"` with `aria-labelledby`
- [ ] Form validation errors are announced (via `aria-live` region or focus management)

#### Images & Icons
- [ ] All `<img>` elements have `alt` text (or `alt=""` for decorative images)
- [ ] Icon-only buttons have `aria-label`
- [ ] SVGs have `role="img"` and `aria-label` or `<title>`

#### Color & Contrast
- [ ] Text meets 4.5:1 contrast ratio against background
- [ ] Large text (18px+ bold or 24px+) meets 3:1
- [ ] Focus indicators meet 3:1 against adjacent colors
- [ ] Information is not conveyed by color alone (add icons, text, or patterns)

#### Dynamic Content
- [ ] Status messages use `aria-live="polite"` or `aria-live="assertive"`
- [ ] Loading states are announced to screen readers
- [ ] Content that appears/disappears is announced or focus is managed
- [ ] Chat messages use `role="log"` with `aria-live="polite"`

#### Language
- [ ] `<html>` has a `lang` attribute
- [ ] If the page has content in multiple languages, those sections have their own `lang`

#### Touch & Mobile
- [ ] Touch targets are at least 44x44px
- [ ] No content requires hover to access (tooltips have focus-triggered alternatives)
- [ ] Page is usable at 200% zoom without horizontal scrolling

### 3. Write a summary

After fixing issues, create a brief summary of what was found and fixed. List any issues that require user judgment (e.g., alt text for domain-specific images) separately.

## Rules

- Fix issues directly in the code as you find them — don't just report them
- If a fix would change visible behavior or layout, note it but still make the fix
- Prefer semantic HTML over ARIA attributes (e.g., use `<button>` instead of `<div role="button">`)
- Do not add ARIA attributes that duplicate native semantics (e.g., don't add `role="button"` to a `<button>`)
- Do not remove existing accessibility features, even if they seem redundant
- If you're unsure about alt text for a specific image, use a descriptive placeholder and flag it for the user
