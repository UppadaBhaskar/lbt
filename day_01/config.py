import os
from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "mysql+mysqlconnector://root:9848%40Mysql@localhost:3306/ex-db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-change-me")
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
