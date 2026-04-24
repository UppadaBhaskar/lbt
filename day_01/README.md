# lbt/day_01

```powershell
cd lbt\day_01
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create DB `ex-db` in MySQL (or set `SQLALCHEMY_DATABASE_URI`). Password `@` must be `%40` in the URL.

```powershell
python app.py
```

Open `http://127.0.0.1:5000/`. Auth: `/register`, `/login`, `/logout`, `/account`, `/teacher`. **Day 8:** `/courses` (login), `/courses/new` (teacher), `/courses/<id>`, `/courses/<id>/edit`, POST `/courses/<id>/delete` (owner teacher).
