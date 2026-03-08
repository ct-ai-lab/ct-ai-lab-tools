# /scaffold — Gradio to FastAPI Production App

You are a software architect converting a Gradio prototype into a production-ready FastAPI + Jinja2 web application.

## Input

`$ARGUMENTS` should be the path to a Gradio app file (.py or .ipynb). If not provided, search the current directory for Gradio files.

## Steps

### 1. Analyze the Gradio prototype

Read the Gradio file and extract:
- **All UI components** (textboxes, dropdowns, sliders, buttons, radio buttons, checkboxes, file uploads, etc.)
- **All callback functions** and what they do
- **State variables** and how data flows between components
- **Any API calls** (LLM, database, external services)
- **User-facing text** (labels, descriptions, placeholder text)

Create a brief summary of what the app does before proceeding.

### 2. Create the project structure

```
app_web/
├── main.py              # FastAPI app, routes, API endpoints
├── [app_logic].py       # Business logic extracted from Gradio callbacks
├── [data].json           # Static data files, if applicable
├── templates/
│   └── index.html       # Single-page Jinja2 template
├── static/
│   ├── css/
│   │   └── styles.css   # Application styles
│   ├── js/
│   │   └── app.js       # Client-side logic
│   └── images/          # Static assets
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
└── startup.sh           # Azure App Service startup script
```

### 3. Build `main.py`

- FastAPI app with Jinja2Templates
- Mount `/static` for static files
- `GET /` renders the template, passing any server-side data (translations, config, etc.)
- One `POST /api/` endpoint per Gradio callback function
- If the Gradio app has streaming (e.g., chatbot), use SSE (Server-Sent Events) via `StreamingResponse`
- Include CORS middleware if needed
- Environment variables via `os.getenv()` with sensible defaults

### 4. Build the business logic module

- Extract all non-UI logic from the Gradio callbacks into a pure Python module
- No web framework imports in this file — keep it testable
- Preserve the same function signatures where practical

### 5. Build `index.html`

- Single-page app using step-based navigation (show/hide sections)
- Map each Gradio "tab" or "accordion" to a `<section>` with a unique ID
- Map each Gradio component to its HTML equivalent:
  - `gr.Textbox` → `<input type="text">` or `<textarea>`
  - `gr.Number` → `<input type="number">`
  - `gr.Dropdown` → `<select>`
  - `gr.Radio` → radio button group
  - `gr.Checkbox` → `<input type="checkbox">`
  - `gr.Slider` → `<input type="range">`
  - `gr.Button` → `<button>` with onclick handler
  - `gr.Markdown` → rendered HTML section
  - `gr.Chatbot` → chat container with input + send button
  - `gr.File` → `<input type="file">`
- Add `data-i18n` attributes to all user-facing text for future translation support
- Include a language toggle scaffold (EN/ES buttons) even if translations aren't written yet

### 6. Build `app.js`

- Step navigation: `ALL_STEPS` array, `showStep(stepId)` function
- One async function per API call (fetch → render response)
- If streaming: SSE reader pattern with `ReadableStream`
- Form validation before API calls
- No build tools, no npm, no frameworks — vanilla JS only

### 7. Build `styles.css`

- Start with a clean, accessible base (system fonts, good contrast, readable line heights)
- Mobile-first responsive design
- Use CSS custom properties for colors so `/ctstyles` can restyle easily later
- Include sensible defaults for forms, buttons, cards, and step containers

### 8. Build `requirements.txt`

- `fastapi`
- `uvicorn[standard]`
- `jinja2`
- `python-multipart` (if file uploads)
- `python-dotenv`
- Any domain-specific packages from the Gradio prototype
- Pin versions

### 9. Build `.env.example` and `startup.sh`

`.env.example`: list every environment variable with placeholder values and comments.

`startup.sh`:
```bash
#!/bin/bash
gunicorn app_web.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Rules

- Preserve ALL functionality from the Gradio prototype — do not drop features
- Every piece of user-facing text must have a `data-i18n` attribute
- No inline styles — all styling in the CSS file
- All API endpoints should return JSON with an `error` key on failure
- Include basic input validation on both client and server
- Add aria labels, roles, and keyboard navigation support from the start
- Do not add features that weren't in the Gradio prototype
