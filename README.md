# falakpatel.com

My portfolio site. One page, no build step: GitHub Pages serves `index.html` as it is.

The look: a quiet, near-black page with a serif (Libre Baskerville) for reading and a monospace (JetBrains Mono) for the editor bits. At the top, a small editor types real excerpts from my own repos, with a vim-style status line. The logo is the Gujarati letter ફ (pha), my initial, turned on its side.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole site: styles at the top, text in the middle, scripts at the bottom |
| `fonts/` | Libre Baskerville and JetBrains Mono, cut down to Latin letters (woff2), with their OFL licence files. No Google Fonts call |
| `models/*.bin` | The 3-D parts shown in the viewer, in a small format made from the STL files |
| `projects/` | Pictures for the project browser (one per project, for example `aushadhi-drishti.jpg`) |
| `me.jpg` | Optional round profile photo (square, about 400 x 400). Until you add it, the initials FP show instead |
| `og.png` | The picture shown when the link is shared (1200 x 630) |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png` | The tab and home-screen icons (the logo) |
| `404.html` | The page GitHub shows for a wrong address, in the same theme as the main page |
| `robots.txt`, `sitemap.xml` | Tell search engines the site has one page, at falakpatel.com |
| `tools/update-csp.py` | Refreshes the security fingerprints after a script or style change (see Security below) |
| `CNAME` | Points the site at falakpatel.com. Don't change it |
| `.nojekyll` | Tells GitHub Pages to serve files as they are |

## Colour themes

Three themes: **night** (black with soft blue, like my apps), **paper** (warm off-white, like a printed report) and **clinic** (cool white with teal). The first visit follows the phone or computer (dark gives night, light gives paper). The switch in the top bar, the `:theme` button in the footer, or the command line changes it, and the choice is remembered in the browser. The colours are the variables at the top of the `<style>` block, one group per theme.

## Command line

Press `:` anywhere on a computer, type a command, press Enter:
`:theme paper`, `:theme` (next theme), `:e anukalpa` (open a project), `:projects`, `:stridemate`, `:writing`, `:top`, `:help`.

## Inside `index.html`

1. **Styles** (`<style>` in the head): fonts, the three themes, then one block per part of the page.
2. **Text.** Plain HTML. Edit it like a document.
3. **Photo spot** (first script): shows `me.jpg`, or the initials if it is missing.
4. **Themes** (second script).
5. **Editor** (third script). `FILES` holds the code excerpts and their paths. Paste a new excerpt between the backticks to change one. It pauses when it is off screen, and with "reduce motion" switched on it shows the first file already typed. Screen readers get a one-line description instead.
6. **Project browser.** The `projects` list holds each project's name, short tag, text, facts, links and pictures. Arrow keys, Home and End move through it. The GitHub numbers in its bottom line are optional: if GitHub does not answer, the plain link stays.
7. **3-D viewer.** It uses three.js from a CDN. Without internet (or WebGL) it shows a still picture of the shell instead. The `MODELS` list at the top is the only part you normally touch.
8. **Menu** and **command line** (last two scripts). The menu builds its project list from the browser, so a new project shows up there by itself.

## Common changes

**Edit text.** Change it in `index.html`, then open the page in a browser to check.

**Add a project.** Put its picture in `projects/` and add an entry to `projects` in the browser script.

**Add a 3-D part.** Put `<name>.bin` in `models/` and add one line to `MODELS` in the viewer script, with the button label, the row (`exo` or `other`), and the CAD file name in the Stridemate_3D_files_IITH repo.

**Changed a script or the style block?** Run `python3 tools/update-csp.py` in this folder, then preview. Without it, the changed part is blocked (see Security).

**Preview locally.** In this folder run `python3 -m http.server`, then open `http://localhost:8000`. (Opening the file directly may skip the fonts and won't load the 3-D models.)

## Security

- **Content-Security-Policy** (a meta line at the top of `index.html` and `404.html`). The page may only run its own inline scripts, three.js from jsDelivr (version 0.169.0 only), load images and fonts from this site, and ask api.github.com for the stats. Each inline script and the style block is allowed by its sha256 fingerprint, so after editing one, run `python3 tools/update-csp.py`. If you forget, the browser console says which part was blocked. `python3 tools/update-csp.py --check` only checks.
- **three.js integrity.** The seven three.js files have sha384 fingerprints (in the import map and the `modulepreload` lines). If jsDelivr ever served a changed file, the browser refuses it and the still picture shows instead. To move to a newer three.js, change the version everywhere and put in the new fingerprints.
- **GitHub numbers** are added as plain text, never as HTML.
- **Referrer policy:** other sites see only `falakpatel.com`, not the full address.
