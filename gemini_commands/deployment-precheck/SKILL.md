---
name: deployment-precheck
description: Azure Deployment Readiness Check. Use to verify that a FastAPI web application is ready to deploy to Azure App Service, checking for structure, secrets, environment variables, and dependencies.
---

# Azure Deployment Readiness Check

## Workflow

1. **Check project structure.**
   - Verify `requirements.txt`, `startup.sh`, `.env.example`.
   - Ensure `.env` is not committed and is in `.gitignore`.

2. **Check for hardcoded secrets.**
   - Search for API keys, passwords, connection strings.
   - All secrets must be loaded via `os.getenv()`.

3. **Check environment variable usage.**
   - Ensure sensible defaults or "fail fast" logic.
   - Verify `.env.example` is complete.

4. **Check `startup.sh`.**
   - Verify gunicorn command, module path, workers, and port 8000.
   - Ensure Unix line endings and executable permissions.

5. **Check dependencies.**
   - Ensure `gunicorn` and `uvicorn[standard]` are in `requirements.txt`.
   - Check for system-level dependencies or compilation issues.

6. **Check static files and CORS.**
   - Verify `StaticFiles` mount and relative URLs.
   - Ensure CORS is not `*` in production.
   - Ensure `DEBUG = False`.

7. **Check for large files.**
   - Ensure no files over 50MB and proper `.gitignore` exclusions.

8. **Summary.**
   - Produce a checklist with **PASS**, **FAIL**, and **WARN** items.

## Rules

- Read-only audit; do not modify files.
- Be specific about file paths and line numbers for failures.
