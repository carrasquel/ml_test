import os

from flask import Flask
from flask_migrate import Migrate

def create_app():

    app = Flask(__name__)
    # app.config.from_object("config.Config")

    from . import extensions
    from . import modules
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')

    extensions.init_app(app)
    modules.init_app(app)

    from app.extensions import db

    Migrate(app, db)

    return app
