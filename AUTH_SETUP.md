# Atelier authentication setup

## 1. Environment variables

Create a local `.env` file in the project root (do not commit or share it):

```env
VITE_SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
VITE_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_OR_ANON_KEY
```

Restart Vite after changing `.env`.

## 2. Create the profile table and username checker

In Supabase Dashboard, open **SQL Editor**, create a new query, paste the contents of `supabase/atelier-auth.sql`, and run it. This creates the profile table, a case-insensitive unique username index, row-level security policies, and `is_username_available`.

The table stores each user's display name, unique username, email, onboarding answers, and onboarding-completed status. Users can access only their own profile through the client policies. Do not add a Supabase service-role key to the frontend.

## 3. Enable Google sign-in

1. In Supabase Dashboard, open **Authentication → Sign In / Providers → Google** and enable Google.
2. Create OAuth credentials in Google Cloud Console and add the client ID and client secret in Supabase's Google provider settings.
3. In Supabase **Authentication → URL Configuration**, add your local callback origin (for example `http://127.0.0.1:5173/`) to the allowed redirect URLs. Add your production URL before deployment.
4. In Google Cloud's OAuth client settings, add the Supabase callback URL shown by Supabase as an authorised redirect URI.
5. Save both dashboards and restart the app.

Google sign-in routes a first-time Google account through onboarding. Returning Google accounts with saved onboarding metadata go to the dashboard. The app cannot complete Google OAuth until the provider and redirect URLs are configured in Supabase and Google Cloud.

## 4. Flow

- Landing page → **Open your Space** → onboarding questions → summary/roadmap → create account.
- Sign-in page → **Create an account** → onboarding questions (not directly to email/username).
- Returning user → email/password login or Google sign-in → dashboard.
- New Google user → Google sign-in → onboarding → save username/profile → dashboard.
- Email and phone links on the Contact section use `mailto:` and `tel:` handlers.

## 5. Important current limitation

The profile and onboarding metadata are persisted to Supabase. The existing task/goal/habit/note workspace still uses browser `localStorage` in this project; this SQL does not make those workspace items sync between devices. Cloud-syncing workspace data and adding an admin console require additional tables, role-safe server-side admin controls, and a separate implementation. Do not grant admin permissions based on client-side metadata alone.
