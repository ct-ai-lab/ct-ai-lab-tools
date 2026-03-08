# /deploymentprecheck — Azure Deployment Readiness Check

You are a DevOps engineer verifying that a FastAPI web application is ready to deploy to Azure App Service.

## Steps

### 1. Check project structure

Verify these files exist and are properly configured:

- [ ] **`requirements.txt`** — exists, has all imports used in the code, versions are pinned
- [ ] **`startup.sh`** — exists, uses gunicorn with uvicorn workers, binds to `0.0.0.0:8000`
- [ ] **`.env.example`** — exists, documents all required environment variables
- [ ] **No `.env` file committed** — check `.gitignore` includes `.env`

### 2. Check for hardcoded secrets

Search the entire codebase for:
- [ ] API keys (patterns like `sk-`, `key-`, `api_key=`, `OPENAI`, `ANTHROPIC`, `AZURE`)
- [ ] Hardcoded passwords or tokens
- [ ] Database connection strings with credentials
- [ ] Any string that looks like a secret

All secrets must be loaded from environment variables via `os.getenv()`.

### 3. Check environment variable usage

- [ ] Every `os.getenv()` call has a sensible default OR the app fails fast with a clear error if the variable is missing
- [ ] `.env.example` lists every variable used in the code
- [ ] No environment variables are used in client-side JavaScript (they'd be exposed)

### 4. Check `startup.sh`

The file should look like:
```bash
#!/bin/bash
gunicorn app_web.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

Verify:
- [ ] The module path (`app_web.main:app`) matches the actual FastAPI app location
- [ ] Worker count is reasonable (2-4 for most apps)
- [ ] Binds to `0.0.0.0:8000` (Azure expects port 8000)
- [ ] File has Unix line endings (not Windows `\r\n`)
- [ ] File is executable (`chmod +x`)

### 5. Check dependencies

- [ ] `requirements.txt` includes `gunicorn`
- [ ] `requirements.txt` includes `uvicorn[standard]`
- [ ] No system-level dependencies that need `apt-get` (if so, note them — Azure needs a custom Docker image or startup command)
- [ ] No packages that require compilation without available wheels (e.g., some C extensions)
- [ ] Python version compatibility — check if any packages require a specific Python version

### 6. Check static files

- [ ] Static files are served via FastAPI's `StaticFiles` mount, not a separate server
- [ ] All static file paths use relative URLs (`/static/...`) not absolute filesystem paths
- [ ] No references to `localhost` or `127.0.0.1` in the codebase
- [ ] No hardcoded port numbers in frontend code

### 7. Check CORS and security

- [ ] If CORS middleware is used, origins are configured (not `allow_origins=["*"]` in production)
- [ ] No `DEBUG = True` or equivalent left on
- [ ] Error responses don't leak stack traces or internal paths

### 8. Check for large files

- [ ] No files over 50MB in the repo (Azure has deployment size limits)
- [ ] `.gitignore` excludes `__pycache__/`, `*.pyc`, `.env`, `venv/`, `node_modules/`
- [ ] No data files that should be in blob storage instead of the repo

### 9. Check the app starts

If possible, verify the app can start locally:
```bash
cd [project_root]
uvicorn app_web.main:app --host 0.0.0.0 --port 8000
```

Check for import errors, missing modules, or startup crashes.

### 10. Summary

Produce a checklist with:
- **PASS**: Items that are good
- **FAIL**: Items that need fixing (with specific instructions)
- **WARN**: Items that aren't blocking but should be addressed

## Rules

- Do not modify any files — this is a read-only audit
- If you find a FAIL item, explain exactly what needs to change and where
- Be specific about file paths and line numbers
- If the app uses a different deployment target (not Azure), note what would need to change
