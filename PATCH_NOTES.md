# Atelier authentication/onboarding patch

Changes in this copy:
- The "Create an account" link from the login screen now starts onboarding questions.
- Returning email/password users go to their workspace after successful login.
- Adds a Google OAuth button and first-time Google onboarding path.
- Adds a clear "Back to website" control on the authentication screen.
- Replaces remaining UI wordmarks that said `atelier.` with `atelier 🍀` in the main app flows.
- Saves profile fields and onboarding answers to Supabase `profiles` when the SQL setup is applied.
- Improves the light-theme contrast of feature and contact text.
- Adds `supabase/atelier-auth.sql` and `AUTH_SETUP.md`.

Before using:
1. Create `.env` from `.env.example` and add your own Supabase URL and publishable/anon key.
2. Run `supabase/atelier-auth.sql` in the Supabase SQL Editor.
3. Enable Google provider and configure OAuth redirect URLs as described in `AUTH_SETUP.md`.
4. Run `npm.cmd install` and `npm.cmd run dev`.

Verification:
- All JS/JSX files passed a TypeScript parser/transpile syntax check.
- A full Vite production build could not be run here because dependency installation timed out.
- Existing workspace tasks/goals/habits/notes remain browser-local in this stage; they are not yet synced to Supabase.
