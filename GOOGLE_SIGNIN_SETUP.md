# Enable Google sign-in for Atelier

The React button calls Supabase OAuth correctly, but Supabase returns `Unsupported provider: provider is not enabled` until Google is enabled in the Supabase dashboard. This cannot be switched on by frontend code alone.

1. Open the correct Supabase project.
2. Go to **Authentication → Sign In / Providers → Google** (the exact label may vary).
3. Enable Google.
4. In Google Cloud Console, configure an OAuth client for a Web application and add the Supabase callback URL shown by Supabase to **Authorized redirect URIs**.
5. Paste the Google Client ID and Client Secret into Supabase's Google provider settings and save.
6. In **Authentication → URL Configuration**, add your local development URL (for example `http://127.0.0.1:5173`) and your production website URL to the allowed redirect URLs.
7. Restart Vite and test both new-user and returning-user Google flows.

Do not put the Google Client Secret in `.env` or frontend code. It belongs in Supabase provider settings only.

## Current flow
- New email/password account: seven onboarding questions → summary → personalised roadmap → create account.
- Existing account: sign in directly.
- Google button appears on both create-account and login screens. New Google signups from the account creation step attach the local seven-question answers to the authenticated user's metadata after the OAuth redirect.
- Username uniqueness is checked by the existing `is_username_available` RPC. The SQL setup from the existing project must be installed for this to work.
