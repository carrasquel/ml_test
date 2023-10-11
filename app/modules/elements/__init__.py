from app.extensions.api import api

from .models import Element

def init_app(app):
    from .resources import ns

    api.add_namespace(ns, "/elements")