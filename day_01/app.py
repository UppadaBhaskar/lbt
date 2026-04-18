from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from config import Config
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from models import User  # noqa: F401 — register model before create_all

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        email = (request.form.get("email") or "").strip()
        password = request.form.get("password") or ""
        role = (request.form.get("role") or "").strip()

        if not username:
            flash("Username is required.", "error")
            return render_template("register.html")
        if not email or "@" not in email:
            flash("Valid email is required.", "error")
            return render_template("register.html", username=username)
        if len(password) < 4:
            flash("Password must be at least 4 characters.", "error")
            return render_template("register.html", username=username, email=email, role=role)
        if role not in ("student", "teacher"):
            flash("Role must be student or teacher.", "error")
            return render_template("register.html", username=username, email=email)
        if User.query.filter_by(username=username).first():
            flash("Username already taken.", "error")
            return render_template("register.html", username=username, email=email, role=role)
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return render_template("register.html", username=username, email=email, role=role)

        try:
            user = User(
                username=username,
                email=email,
                password=generate_password_hash(password),
                role=role,
            )
            db.session.add(user)
            db.session.commit()
            flash("Registration successful.", "success")
            return redirect(url_for("home"))
        except Exception:
            db.session.rollback()
            flash("Something went wrong. Try again.", "error")
            return render_template("register.html", username=username, email=email, role=role)

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
