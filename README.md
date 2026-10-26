# falakpatel.com

My portfolio site. One page, no build step: GitHub Pages serves `index.html` as it is.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole site: styles at the top, text in the middle, scripts at the bottom |
| `models/*.bin` | The 3-D parts shown in the viewer, in a small format made from the STL files |
| `projects/` | Pictures for the project browser (one per project, for example `aushadhi-drishti.jpg`) |
| `og.png` | The picture shown when the link is shared (1200 x 630) |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png` | The tab and home-screen icons |
| `CNAME` | Points the site at falakpatel.com. Don't change it |
| `.nojekyll` | Tells GitHub Pages to serve files as they are |

## Menu

The bar at the top has the name (back to the top), section links, the menu button (three lines) and the dark / light switch. The menu lists every section and every project; a project link such as `#project-anukalpa` opens that project in the project browser. The menu script is the last `<script>` in `index.html`, and it builds the project list from the browser, so a new project shows up in the menu by itself.

## Inside `index.html`

1. **Styles** (`<style>` in the head). The last block, marked "Modern look", sets the font (Inter), colours, rounded cards and spacing; change the look there. Colours for light and dark mode are the variables at the top (`--bg`, `--fg`, `--link`).
2. **Text.** Plain HTML. Edit it like a document.
3. **Dark / light switch** (first script at the bottom). Follows the phone or computer setting until the visitor picks one, then remembers the choice.
4. **Project browser** (second script). The `projects` list at the top holds each project's text, facts, links and pictures. Arrow keys move through it, and the GitHub numbers in its bottom line are optional: if GitHub does not answer, the plain link stays.
5. **3-D viewer** (last script). It uses three.js from a CDN. Without internet (or WebGL) it shows a still picture of the shell instead. The script is split into six numbered, commented sections. The `MODELS` list at the top is the only part you normally touch.

## Common changes

**Edit text.** Change it in `index.html`, then open the file in a browser to check.

**Add a project.** Put its picture in `projects/` and add an entry to `projects` in the browser script.

**Add a 3-D part.** Put `<name>.bin` in `models/` and add one line to `MODELS` in the viewer script, with the button label, the row (`exo` or `other`), and the CAD file name in the Stridemate_3D_files_IITH repo.

**Preview locally.** In this folder run `python3 -m http.server`, then open `http://localhost:8000`. (Opening the file directly won't load the 3-D models.)
