

def init_app(app):

    from . import elements

    modules = (elements,)

    for module in modules:
        module.init_app(app)
