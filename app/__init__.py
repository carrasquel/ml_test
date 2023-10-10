from flask import Flask


def create_app():

    app = Flask(__name__)
    app.config.from_object("config.Config")

    from . import extensions
    from . import modules

    extensions.init_app(app)
    modules.init_app(app)

    return app
