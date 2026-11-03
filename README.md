# Atelier ✨ — Personal Life Management System

atelier. helps users organise tasks, track goals, check in on daily habits, and save notes in one personal workspace. It is built with React and Vite. Supabase handles authentication and email verification; workspace content is currently saved in browser localStorage.

## Run the project

1. Install Node.js (LTS recommended).
2. Open a terminal in this folder.
3. Run `npm install`.
4. Copy `.env.example` to `.env` and fill in your own Supabase URL and publishable key.
5. Run `npm run dev` and open the local URL printed by Vite.
6. Run `npm run build` to create a production build.

## Source-code map

- `src/main.jsx` — React entry point.
- `src/App.jsx` — app coordinator, shared state, navigation, authentication, and callbacks.
- `src/components/Icon.jsx` — reusable SVG icon.
- `src/features/overview/Overview.jsx` — daily summary.
- `src/features/tasks/Tasks.jsx` — task list, search, and task form.
- `src/features/goals/Goals.jsx` — goal cards and progress controls.
- `src/features/habits/Habits.jsx` — daily habit check-in and list.
- `src/features/notes/Notes.jsx` — note editor and saved notes.
- Each feature has a matching CSS file for feature-specific styles; shared/responsive rules remain in `src/App.css`.
- `src/utils/workspaceData.js` — sample data, safe localStorage loading, ID generation, and date helpers.
- `src/supabase.js` — Supabase client.
- `src/index.css` — base styles.
- `scripts/startup.js` — decorative terminal startup sequence.
- `docs/PROJECT_GUIDE.md` — architecture and viva preparation.

## Architecture

`App.jsx` owns the shared workspace state so Overview and the feature pages read from the same source of truth. Each feature receives the data and event handlers it needs through props. This is an example of lifting state up in React. It avoids separate, conflicting copies of tasks, goals, habits, or notes.

## Storage note

Tasks, goals, habits, notes, and habit check-ins use browser `localStorage`. They persist in the same browser on the same device and are not yet synchronised to a database. Supabase is used for authentication in this version.

## Viva introduction

“I built atelier., a personal life management web application using React and Vite. It helps users organise tasks, monitor goals, build daily habits, and keep notes in one workspace. I divided the interface into reusable feature components so each section is easier to maintain. React state keeps the sections in sync, local storage preserves workspace data in the browser, and Supabase provides authentication and email verification.”

Only describe functionality that is implemented and tested; the terminal startup animation is decorative and does not run real health checks.


## Final release notes

- Run `npm install` and `npm run dev` from this project root.
- The local `.env.local` is configured for the Supabase project supplied in the uploaded archive and is git-ignored. Before publishing to a public repository, do not commit local environment files. Configure the same public URL and publishable key in the hosting provider instead.
- Run `backend/supabase/atelier-auth.sql` in the intended Supabase project's SQL Editor. Review it if that project already has a `profiles` table or an auth-user trigger.
- Run `backend/supabase/migrations/202610290001_user_workspaces.sql` for per-user workspace cloud storage.
- Configure Google OAuth in Supabase and Google Cloud, including production callback/redirect URLs.
- Admin Command Center password gate is a **demo-only client-side gate**, not real server-side authorization. Do not use it to protect live admin data. Production admin privileges must be enforced by server-side authorization and database RLS.
- The temporary app-state reset button and its dialog have been removed.

Admin demo access password: `finaldestination`. This unlocks only the client-side demo dashboard; it is not a secure production admin credential.
