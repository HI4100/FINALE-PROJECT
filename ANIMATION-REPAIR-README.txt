ATELIER ANIMATION REPAIR

This patch is based on the uploaded Atelier-Website.zip source.

Changes:
- The welcome flow now renders PublicSections once instead of nesting the old cosmic welcome screen and a second full landing page.
- The landing page includes a cinematic CosmicGalaxy intro overlay using the existing CosmicGalaxy canvas component.
- Hero text animates in with staggered delays.
- An animated daily schedule preview was added immediately after the hero, with staggered row entrances, looping row highlights, a progress ring, pulsing LIVE dot, floating card, and looping progress bar.
- Existing Progress.jsx and Progress.css were preserved.

Install:
1. Extract into a NEW folder.
2. Run npm.cmd install
3. Run npm.cmd run dev

Important:
- Do not copy .env files or secrets into shared folders.
- Build verification could not be completed in the current environment because npm dependency installation timed out. Test in the local VS Code environment.
