# Career Factory public API

Base URL: https://api.careerfactorynd.org

Read-only public career information; no API key, AI service, or personal assessment responses are used.

- `GET /` lists endpoints and usage notes.
- `GET /v1/careers?q=welder&area=skilled-trades&limit=20&offset=0` searches career names, subtitles, areas and tags. All filters are optional. Limit is 1–100; offset is a nonnegative integer. Results are alphabetical.
- `GET /v1/careers/skilled-trades/electrician` returns a single career.
- `GET /v1/areas` lists published career areas and counts.

Results include the supplied wage and outlook fields and an absolute `assessmentUrl` for context and source links. Missing values remain null; annual-contract pay is not converted to hourly pay. Pay is a median, not a starting wage or guarantee.

The Worker reads the public search index from the repository's main branch. Source and API responses can each be cached for five minutes. This follows published updates; it does not independently refresh school, wage, licensing, or program information.

Cloudflare dashboard service: `aged-forest-1ddb` in the owner's account. `worker.mjs` is its deployed source. Update it through Edit code and deploy; deploying the website does not automatically deploy this Worker. The API reads the website index dynamically, so routine career data releases require no Worker code update.

Run regression checks with `node api/test.mjs`.

The website's custom domain is configured in GitHub Pages settings. Cloudflare DNS has four GitHub Pages A records at the apex and a www CNAME to shariwhittyphi-collab.github.io. The API subdomain is independently attached to the Worker.
