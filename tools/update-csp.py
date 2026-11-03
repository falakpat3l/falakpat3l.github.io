#!/usr/bin/env python3
"""Refresh the script and style fingerprints in the Content-Security-Policy.

The pages only run scripts and styles whose sha256 fingerprint is listed in
their Content-Security-Policy line. Change one character in a script or in
the style block and the browser blocks it. After any such change, run this
from the site folder:

    python3 tools/update-csp.py

It rewrites the fingerprints in index.html and 404.html. With --check it only
reports whether they are up to date (exit code 1 if not).
"""
import base64, hashlib, re, sys
from pathlib import Path

PAGES = ["index.html", "404.html"]
SITE = Path(__file__).resolve().parent.parent

SCRIPT = re.compile(r"<script(\s[^>]*)?>(.*?)</script>", re.S | re.I)
STYLE = re.compile(r"<style(\s[^>]*)?>(.*?)</style>", re.S | re.I)
META = re.compile(r'(<meta http-equiv="Content-Security-Policy" content=")([^"]*)(")', re.I)


def sha(text):
    # Browsers turn Windows line endings into plain ones before hashing.
    data = text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return "'sha256-" + base64.b64encode(hashlib.sha256(data).digest()).decode() + "'"


def hashes(pattern, html):
    out = []
    for m in pattern.finditer(html):
        if m.group(1) and re.search(r"\bsrc\s*=", m.group(1)):
            continue  # a script file, not inline code
        h = sha(m.group(2))
        if h not in out:
            out.append(h)
    return out


def rebuild(policy, name, new):
    parts = [p.strip() for p in policy.split(";") if p.strip()]
    for i, p in enumerate(parts):
        words = p.split()
        if words[0] == name:
            keep = [w for w in words[1:] if not w.startswith("'sha256-")]
            parts[i] = " ".join([name] + keep + new)
            break
    else:
        raise SystemExit("No %s in the policy" % name)
    return "; ".join(parts)


def main():
    check = "--check" in sys.argv
    stale = False
    for page in PAGES:
        path = SITE / page
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        m = META.search(html)
        if not m:
            print(page + ": no Content-Security-Policy line, skipped")
            continue
        policy = rebuild(m.group(2), "script-src", hashes(SCRIPT, html))
        policy = rebuild(policy, "style-src", hashes(STYLE, html))
        if policy == m.group(2):
            print(page + ": up to date")
            continue
        stale = True
        if check:
            print(page + ": out of date, run python3 tools/update-csp.py")
        else:
            path.write_text(html[:m.start(2)] + policy + html[m.end(2):], encoding="utf-8")
            print(page + ": updated")
    if check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
