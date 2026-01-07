# Portfolio — Static site

This repository contains a small static portfolio page for GitHub Pages.

Features
- Minimal black & white design
- About section and contact link
- Two project cards (Discord bot, Minecraft Fabric plugin)

Quick start
1. Edit `index.html` and `assets/css/styles.css` to update content.
2. Place a copy of your CV at `assets/Luke_McGarvey_06_01.pdf` (the site links to that file).
3. Push to GitHub. In repository Settings -> Pages, set the source to `main` branch (root) and your site will be published.

Notes
- Replace placeholder repo/demo links with the real links to your projects.
- If you prefer, you can publish from the `gh-pages` branch or add a GitHub Actions workflow to deploy.
If you prefer, you can publish from the `gh-pages` branch or add a GitHub Actions workflow to deploy.

Automatic deployment (GitHub Actions) ✅

This repository includes a workflow at `.github/workflows/deploy.yml` that runs on every push to `main` and publishes the repository root to the `gh-pages` branch using `peaceiris/actions-gh-pages`.

After the first successful run, go to **Settings → Pages** and set the source to:

- **Branch**: `gh-pages`
- **Folder**: `/ (root)`

The site will then be available at `https://<your-username>.github.io/<repo>`.
