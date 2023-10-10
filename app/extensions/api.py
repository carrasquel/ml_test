from flask import Blueprint
from flask_restx import Api


blueprint = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    blueprint,
    version="1.0",
    title="ML API",
    description="Backend Test API",
    doc="/docs"
)


def create_api(app):

    app.register_blueprint(blueprint)


def init_app(app):

    create_api(app)
