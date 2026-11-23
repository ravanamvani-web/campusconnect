# CampusConnect API

Flask API backed by Supabase. The `backend` directory is self-contained and can be deployed as a Render web service.

## Deploy to Render

1. Push this repository to GitHub and create a **Web Service** in Render from that repository.
2. Set **Root Directory** to `backend` (or deploy the `backend` folder as its own repository).
3. Render can use `render.yaml` for the build, start, and health-check settings. If entering settings manually, use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Health check path: `/health`
4. Add `SUPABASE_URL` and `SUPABASE_KEY` in the service's Environment settings. Set `CORS_ORIGINS` to the frontend origin(s), comma-separated. For example: `https://campusconnect.example,https://www.campusconnect.example`.

Keep the Supabase key in Render's environment settings; do not commit it. Use a least-privileged key appropriate for the API's access policies.

## Endpoints

- `GET /` and `GET /health` report service status.
- `GET /api/users` reads rows from the Supabase `users` table.

For local development, copy `.env.example` to `.env`, fill in the values, install `requirements.txt`, and run `flask --app app run` from this directory.
