"""
Day 1 — Hello Flask
Minimal WSGI app: one route `/` returning simple HTML.
Run: python app.py   OR   flask run
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Learn by Tech — Day 1</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 40rem; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }
        code { background: #f4f4f4; padding: 0.15em 0.4em; border-radius: 4px; }
    </style>
</head>
<body>
    <h1>Hello, Flask</h1>
    <p>This is the <strong>Day 1</strong> deliverable: a running Flask app with a single route <code>/</code>.</p>
    <p>When you open <code>http://127.0.0.1:5000/</code>, the browser sends an HTTP GET; Flask matches the URL to the
    <code>home</code> view and returns this HTML response.</p>
</body>
</html>"""


if __name__ == "__main__":
    app.run(debug=True)
