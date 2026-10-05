# falakpatel.com

My portfolio site. One page, no build step: GitHub Pages serves `index.html` as it is.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole site: styles at the top, text in the middle, two scripts at the bottom |
| `models/*.bin` | The 3-D parts shown in the viewer, in a small format made from the STL files |
| `CNAME` | Points the site at falakpatel.com. Don't change it |
| `.nojekyll` | Tells GitHub Pages to serve files as they are |

## Inside `index.html`

1. **Styles** (`<style>` in the head). Colours for light and dark mode are the variables at the top (`--bg`, `--fg`, `--link`).
2. **Text.** Plain HTML. Edit it like a document.
3. **Dark / light switch** (first script at the bottom). Remembers the choice in the browser.
4. **3-D viewer** (last script). It uses three.js from a CDN. The script is split into six numbered, commented sections. The `MODELS` list at the top is the only part you normally touch.

## Common changes

**Edit text.** Change it in `index.html`, then open the file in a browser to check.

**Add a 3-D part.** Put `<name>.bin` in `models/` and add one line to `MODELS` in the viewer script, with the button label, the row (`exo` or `other`), and the CAD file name in the Stridemate_3D_files_IITH repo.

**Preview locally.** In this folder run `python3 -m http.server`, then open `http://localhost:8000`. (Opening the file directly won't load the 3-D models.)
