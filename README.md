# Thalassemia Support System

A lightweight web application to help Thalassemia patients and donors connect. This project provides:

- A Django backend to manage donors and patient blood requests.
- A Bootstrap-based frontend with responsive pages and a small chatbot UI.
- Google Maps integration to locate nearby treatment centers.
- WhatsApp integration (via pywhatkit) to notify matched donors.
- PostgreSQL as the production database (sqlite is included for quick local testing).

---

## Features 

- Donor registration and patient blood request forms
- Automatic donor matching by blood group
- WhatsApp notification to matched donors (schedules message using pywhatkit)
- Interactive map using Google Maps Places API to find nearby treatment centers
- Simple, client-side chatbot for basic Thalassemia information

---

## Tech Stack 

- Backend: **Python** + **Django 4.2.x**
- Database: **PostgreSQL** (configured in `thalassemia/settings.py`)
- Frontend: HTML/CSS/JavaScript with **Bootstrap 5** CDN
- Libraries: **pywhatkit** (WhatsApp integration), **psycopg2** (Postgres adapter)
- Maps: **Google Maps JavaScript API (Places library)**

---

## Project Structure 

- `thalassemia/` — Django project settings and WSGI/ASGI
- `blood/` — main Django app (models, views, templates, static files)
- `templates/blood/` — UI templates (homepage, donor/getter forms, map)
- `static/` — project static assets (CSS, images)

---

## Prerequisites 

- Python 3.10+ installed
- PostgreSQL installed and running (or use the included `db.sqlite3` for quick local testing)
- (Optional) A virtual environment tool (venv)
- A Google Maps API key (enable Maps JavaScript API & Places)
- A browser with an active WhatsApp Web session for pywhatkit (it automates the browser)

---

## Setup & Run (Windows — PowerShell) 

1. Clone the repository and change directory:

```powershell
git clone <repo-url>
cd thalassemia
```

2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv venv
# PowerShell
.\venv\Scripts\Activate.ps1
# or CMD
.\venv\Scripts\activate
```

3. Install dependencies (create `requirements.txt` if not present):

```powershell
pip install -r requirements.txt


4. Configure your PostgreSQL database (example using psql):

```sql
-- connect as postgres user
CREATE DATABASE thalassemia;
CREATE USER thalassemia_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE thalassemia TO thalassemia_user;
```

5. Set environment variables or update `thalassemia/settings.py` with your DB credentials and secrets. Recommended environment variables:

- `SECRET_KEY` — Django secret key
- `DEBUG` — `True`/`False`
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `GOOGLE_MAPS_API_KEY` — (used in `map.html`; replace the hard-coded key before pushing)

Tip: Use a `.env` file or `s.env` and load it securely (do NOT commit secrets).

6. Apply migrations and create an admin user:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

7. Run the development server:

```powershell
python manage.py runserver
```

8. Open the site at `http://127.0.0.1:8000/`.

---

## WhatsApp integration (pywhatkit) 

- The project uses `pywhatkit.sendwhatmsg()` which opens WhatsApp Web on your default browser and sends/schedules messages. Make sure:
  - You are logged into WhatsApp Web in that browser session.
  - Pop-ups and the browser automation are allowed.
- Behavior can vary by OS and browser; this is intended for notification automation, not high-volume messaging.

---

## Google Maps 

- The `map.html` template currently includes a Google Maps script tag with an API key. Replace the key with your own and **do not** commit the key to version control. Use an environment variable or templating to keep it secret for production.

---

## Security notes 

- Remove hard-coded secrets from `thalassemia/settings.py` before pushing (e.g., SECRET_KEY, DB passwords, API keys).
- Add `venv/`, `db.sqlite3`, and any environment files (e.g., `.env`, `s.env`) to `.gitignore`.

---

## Testing 

Run Django tests:

```powershell
python manage.py test
```

