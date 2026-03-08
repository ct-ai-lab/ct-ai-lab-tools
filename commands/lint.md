# /lint — Run and Fix Linting Issues

You are a code quality engineer. Run linting checks on the codebase and fix any issues found.

## Steps

### 1. Detect the tech stack

Read the project files to determine what languages and tools are in use:
- Python (.py files) → use `ruff` (preferred) or `flake8`
- JavaScript (.js files) → manual lint checks (no build tools assumption)
- HTML (.html files) → structural checks
- CSS (.css files) → structural checks

### 2. Python linting

If Python files exist:

**Check if ruff is available:**
```bash
ruff check . 2>/dev/null || pip install ruff && ruff check .
```

**If ruff is not installable, do manual checks:**
- [ ] No unused imports
- [ ] No unused variables
- [ ] Consistent string quotes (single or double — match the project's convention)
- [ ] No bare `except:` clauses (should catch specific exceptions)
- [ ] No mutable default arguments (e.g., `def foo(bar=[])`)
- [ ] f-strings preferred over `.format()` or `%` formatting
- [ ] No `print()` statements (should use `logging` in production code)
- [ ] Line length under 120 characters
- [ ] Consistent indentation (4 spaces for Python)
- [ ] No trailing whitespace
- [ ] Files end with a newline

**Auto-fix with ruff if available:**
```bash
ruff check --fix .
ruff format .
```

### 3. JavaScript linting (manual — no ESLint dependency)

For each .js file:
- [ ] No `var` declarations (use `const` or `let`)
- [ ] No unused variables or functions
- [ ] Consistent semicolons (match project convention)
- [ ] No `console.log` left in production code (except intentional debug)
- [ ] No `==` comparisons (use `===` unless intentional)
- [ ] No unreachable code after `return`, `break`, or `continue`
- [ ] Event listeners use named functions where practical (for removeEventListener)
- [ ] No global variable pollution (use `const`/`let`, IIFEs, or modules)
- [ ] Template literals preferred over string concatenation for multi-part strings

### 4. HTML linting

For each .html file:
- [ ] All tags are properly closed
- [ ] No duplicate `id` attributes
- [ ] All `<img>` tags have `alt` attributes
- [ ] No inline `style` attributes (should be in CSS)
- [ ] No inline `onclick` handlers using complex logic (simple function calls are OK)
- [ ] All external links have `target="_blank"` with `rel="noopener"`
- [ ] `data-i18n` attributes on user-facing text (if i18n is used in the project)

### 5. CSS linting

For each .css file:
- [ ] No duplicate selectors
- [ ] No `!important` (unless overriding third-party styles)
- [ ] Colors use CSS custom properties where a design system exists
- [ ] No vendor prefixes that aren't needed for modern browsers
- [ ] Media queries are consistent (all `min-width` or all `max-width`, not mixed)
- [ ] No unused CSS classes (cross-reference with HTML)

### 6. Fix and report

- Fix all issues directly in the code
- For issues that require a judgment call, note them and explain the options
- Produce a brief summary of what was found and fixed

## Rules

- Match the existing code style — do not impose a new style on the project
- If the project has a linter config (ruff.toml, .flake8, etc.), respect it
- Do not add linter config files unless asked
- Do not install packages globally — use the project's virtual environment if one exists
- Prioritize: errors > warnings > style nits
