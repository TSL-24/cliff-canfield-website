# Cliff Canfield Plumbing — website

- `website/` — the live site. This folder is what gets published to `public_html`.
- `site-tools/` — the page generator (`build.py`), page templates (`bodies/`) and `SEO-GUIDE.md`. Never published.
- `.cpanel.yml` — tells cPanel Git Version Control to copy `website/` into `public_html` on deploy.

## Publishing an update
1. Changes are pushed to GitHub.
2. In cPanel → Git Version Control → Manage → Pull or Deploy: click **Update from Remote**, then **Deploy HEAD Commit**.
