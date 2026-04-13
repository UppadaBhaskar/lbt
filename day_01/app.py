"""
Day 1–3 — Flask + templates/static + MySQL (Flask-SQLAlchemy)
Run: python app.py   OR   flask run

Requires: MySQL server, database `lms_db`, and a valid SQLALCHEMY_DATABASE_URI (see config.py).
"""

import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import Config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database: db.create_all() finished (no models yet — no tables until Day 4).")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
