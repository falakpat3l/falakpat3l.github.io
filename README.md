# falakpatel.com

My portfolio site. One page, no build step: GitHub Pages serves `index.html` as it is.

The look: a quiet, near-black page with a serif (Newsreader) for reading and a monospace (JetBrains Mono) for the editor bits. At the top, a small editor types real excerpts from my own repos, with a vim-style status line. The logo is an eye whose iris is a capsule ("drishti" means vision).

## Files

| File | What it is |
|---|---|
| `index.html` | The whole site: styles at the top, text in the middle, scripts at the bottom |
| `fonts/` | Newsreader and JetBrains Mono, cut down to Latin letters (woff2), with their OFL licence files. No Google Fonts call |
| `models/*.bin` | The 3-D parts shown in the viewer, in a small format made from the STL files |
| `projects/` | Pictures for the project browser (one per project, for example `aushadhi-drishti.jpg`) |
| `me.jpg` | Optional round profile photo (square, about 400 x 400). Until you add it, the initials FP show instead |
| `og.png` | The picture shown when the link is shared (1200 x 630) |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png` | The tab and home-screen icons (the eye) |
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

**Preview locally.** In this folder run `python3 -m http.server`, then open `http://localhost:8000`. (Opening the file directly may skip the fonts and won't load the 3-D models.)
