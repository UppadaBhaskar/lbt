# Day 1–3 — Hello Flask, templates/static, then MySQL + SQLAlchemy

## Setup

1. Create a virtual environment (from this folder):

```powershell
cd lbt\day_01
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. **Day 3 — MySQL**

- Install and start **MySQL** (or MariaDB with a compatible client).
- Create the database (example name from the teaching plan):

```sql
CREATE DATABASE lms_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

- Set `SQLALCHEMY_DATABASE_URI` if your user/password/host differ from the default in `config.py`, e.g. in PowerShell:

```powershell
$env:SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:YOURPASSWORD@localhost:3306/lms_db"
```

(If the password contains `@`, encode it as `%40` in the URL.)

## Run the app

**Option A — `python app.py`**

```powershell
python app.py
```

**Option B — Flask CLI**

```powershell
$env:FLASK_APP = "app:app"
flask run
```

Open `http://127.0.0.1:5000/` in a browser.

## What to understand

- **WSGI**: Flask (or your WSGI server) is the bridge between the HTTP server and your Python functions.
- **Request**: Browser sends GET `/` → Flask finds the route and calls `home()`.
- **Response**: Return value is sent back as HTML (or plain text if you return a string without HTML).

## Deliverable

- Repo runs locally; you can describe what happens when you open `http://127.0.0.1:5000/`.

## Day 2 (this folder)

- `templates/home.html` — single page (no `base.html`; kept simple).
- `static/css/style.css` — linked with `url_for('static', filename='css/style.css')`.
- `app.py` uses `render_template('home.html')`.

## Day 3 (this folder)

- `config.py` — `Config` with `SQLALCHEMY_DATABASE_URI`, `SECRET_KEY`, `UPLOAD_FOLDER`, `MAX_CONTENT_LENGTH`.
- `app.py` — `db = SQLAlchemy()`, `db.init_app(app)`, `db.create_all()` inside `app.app_context()` on startup (no models yet, so no tables until Day 4).
