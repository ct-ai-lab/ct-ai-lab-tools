"""Check a running lab app against references/lab_style_guide.md.

Usage (app already running locally):
    python -I references/ui_audit.py http://127.0.0.1:8000 / /contracts /reports
    UI_AUDIT_AUTH=user:pass python -I references/ui_audit.py https://<app>.azurewebsites.net /

Checks every path at 1440px and 390px wide and prints one line per page, then each
finding: text under 14px, controls under 44px tall, h1 count other than one, skipped
heading levels, and sideways scrolling.

Needs Playwright with Chromium (pip install playwright==1.48.0; playwright install
chromium). In a sandbox that gives each shell command its own network namespace, start
the server, run this and stop the server in one command.
"""

from __future__ import annotations

import os
import re
import sys

from playwright.sync_api import sync_playwright

WIDTHS = (1440, 390)

CHECKS = r"""() => {
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'
      && !el.closest('.sr-only,[hidden],.feedback-panel'); };
  const out = {small: [], short: [], skips: [], h1: 0, overflow: 0};
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el)) continue;
    const ownText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (ownText && fs < 14) out.small.push(`${el.tagName.toLowerCase()}.${el.className} ${fs}px "${el.textContent.trim().slice(0, 30)}"`);
  }
  const controls = 'button, .btn, .btn-link, input:not([type=checkbox]):not([type=radio]):not([type=hidden]), '
    + 'select, textarea, .ct-header-nav a, .section-nav a, .agency-btn, summary';
  for (const el of document.querySelectorAll(controls)) {
    if (!vis(el)) continue;
    const h = el.getBoundingClientRect().height;
    if (h < 44) out.short.push(`${el.tagName.toLowerCase()}.${el.className} ${Math.round(h)}px "${(el.textContent || el.name || '').trim().slice(0, 25)}"`);
  }
  let last = 0;
  for (const h of document.querySelectorAll('h1,h2,h3,h4,h5,h6')) {
    if (!vis(h)) continue;
    const level = +h.tagName[1];
    if (level === 1) out.h1++;
    if (last && level > last + 1) out.skips.push(`h${last} -> h${level} "${h.textContent.trim().slice(0, 30)}"`);
    last = level;
  }
  out.overflow = document.documentElement.scrollWidth - window.innerWidth;
  return out;
}"""


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    base, paths = sys.argv[1].rstrip("/"), sys.argv[2:]
    auth = os.environ.get("UI_AUDIT_AUTH", "")
    creds = dict(zip(("username", "password"), auth.split(":", 1))) if ":" in auth else None
    failed = 0
    with sync_playwright() as p:
        # The new headless mode can hang in sandboxed or GPU-less environments; the old one works.
        browser = p.chromium.launch(args=["--headless=old", "--disable-gpu"])
        for width in WIDTHS:
            page = browser.new_page(viewport={"width": width, "height": 900}, http_credentials=creds)
            # Google Fonts may be unreachable; waiting on it hangs the page load.
            page.route(re.compile(r"fonts\.(googleapis|gstatic)\.com"), lambda r: r.abort())
            for path in paths:
                page.goto(base + path, wait_until="domcontentloaded")
                r = page.evaluate(CHECKS)
                issues = []
                if r["h1"] != 1:
                    issues.append(f"{r['h1']} h1 elements (want exactly 1)")
                if r["overflow"] > 0:
                    issues.append(f"scrolls sideways by {r['overflow']}px")
                issues += [f"skipped level {s}" for s in r["skips"]]
                issues += [f"text under 14px: {s}" for s in sorted(set(r["small"]))[:10]]
                issues += [f"control under 44px: {s}" for s in sorted(set(r["short"]))[:10]]
                failed += bool(issues)
                print(f"[{width}px] {path}: {'OK' if not issues else f'{len(issues)} finding(s)'}")
                for issue in issues:
                    print(f"    {issue}")
        browser.close()
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
