"""
Day 3 — application configuration (database URI, secret key, upload limits).
Override the database URL with env var SQLALCHEMY_DATABASE_URI when needed.
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # MySQL (create DB first: CREATE DATABASE lms_db;)
    # Example: mysql+mysqlconnector://USER:PASSWORD@HOST:3306/lms_db
    # If password contains @, URL-encode it as %40
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "mysql+mysqlconnector://root:root@localhost:3306/lms_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-change-me-in-production")

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
