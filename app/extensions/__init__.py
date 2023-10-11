
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):

    from . import admin, api

    extensions = (admin, api, db)

    for extension in extensions:
        extension.init_app(app)
