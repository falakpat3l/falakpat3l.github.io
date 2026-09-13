# Putting this site on falakpatel.com

Everything here is ready to publish. Two stages: get it on GitHub, then point the domain at it.

---

## Stage 1 — GitHub (about 10 minutes)

1. Go to https://github.com/new
   - Repository name: **`falakpat3l.github.io`** (must match your username exactly)
   - **Public**
   - Do **not** tick "Add a README"
   - Create

2. From this folder, run:

```bash
cd ~/Documents/falakpat3l.github.io

git init
git add .
git commit -m "Portfolio site"
git branch -M main
git remote add origin https://github.com/falakpat3l/falakpat3l.github.io.git
git push -u origin main
```

If git asks for a password, use a Personal Access Token instead of your account
password: GitHub → Settings → Developer settings → Personal access tokens →
Tokens (classic) → Generate new token → scope `repo`.

3. In the repo: **Settings → Pages**
   - Source: **Deploy from a branch**
   - Branch: **main**, folder: **/ (root)** → Save

4. Wait 1-2 minutes, then check https://falakpat3l.github.io — the site should load.
   Get this working before touching DNS.

---

## Stage 2 — point the domain (about 30 minutes, mostly waiting)

In **Hostinger → Domains → falakpatel.com → DNS / Nameservers**, add these records.
Delete any existing A record for `@` first.

### A records — host `@`, TTL default

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

### CNAME record

```
Host:   www
Points to:   falakpat3l.github.io
```

### Then back in GitHub

5. **Settings → Pages → Custom domain** → enter `falakpatel.com` → Save
   (The `CNAME` file in this folder already contains this, so it may fill itself in.)
6. Wait for the DNS check to pass — minutes to a few hours.
7. Once it passes, tick **Enforce HTTPS**. The certificate is free and automatic.

Done. https://falakpatel.com serves this site.

---

## Notes

- `CNAME` tells GitHub which domain to serve. Don't delete it.
- `.nojekyll` stops GitHub's Jekyll build touching the files. Don't delete it.
- `models/*.json` are the decimated 3D geometries the viewer loads. Keep the folder name.
- To update the site later: edit, then `git add . && git commit -m "update" && git push`.
  Changes appear in about a minute.

## Ignore for now

You do **not** need Cloudflare for this. That only becomes relevant if you transfer
the registrar in November to get the cheaper renewal. The DNS above works fine at Hostinger.

## Timing

Do not put falakpatel.com in the Utrecht application until it is actually loading.
Use the artifact link until then — it works today.
