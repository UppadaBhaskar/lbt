# Day 1 — Environment, Python recap, and Hello Flask

## Setup

1. Create a virtual environment (from this folder):

```powershell
cd learn_by_tech\day_01
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

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
