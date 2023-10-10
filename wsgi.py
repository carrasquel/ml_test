
def get_app():
    from app import create_app
    app = create_app()
    return app


app = get_app()