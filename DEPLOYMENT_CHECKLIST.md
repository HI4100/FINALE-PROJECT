# Atelier deployment checklist

## Before deploy
1. Confirm `VITE_SUPABASE_URL` and `VITE_SUPABASE_PUBLISHABLE_KEY` in the host environment. Never add service-role keys or Google client secrets to frontend variables.
2. Run `backend/supabase/atelier-auth.sql` in the correct Supabase project; inspect for conflicts if `profiles` or an auth trigger already exists.
3. Run `backend/supabase/migrations/202610290001_user_workspaces.sql`.
4. Configure Google OAuth provider in Supabase and the OAuth client in Google Cloud. Add the production Supabase callback URI and the production site's allowed redirect URL.
5. Set Vercel root directory to project root; build command `npm run build`; output directory `dist`.
6. Test sign-up, duplicate username rejection, email/password login, Google login, password reset, sign-out, profile/settings, light mode, task/goal/habit/note CRUD, achievements, admin demo screen, mobile layout, and cross-user isolation.
7. Verify browser console and network requests have no errors.
8. Review Privacy Policy/Terms against actual data practices before public launch.

## Admin warning
The admin panel in this project is a demo UI behind a client-side password hash check. Client code can be inspected or bypassed. Do not use this as production access control or connect it to privileged live operations until authorization is moved server-side and enforced by RLS.
