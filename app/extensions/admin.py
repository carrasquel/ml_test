from flask_admin import Admin

admin = Admin(name="ML", template_mode="bootstrap4")


def init_app(app):

    app.config["FLASK_ADMIN_SWATCH"] = "pulse"

    admin.init_app(app)
