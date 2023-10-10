from flask_restx import Namespace, Resource, fields


from app.extensions.api import api
from app.modules.elements.dao import ElementDAO


ns = Namespace("elements", description="Namespace for elements")

element_model = api.model(
    "element_model", {
        "status": fields.Integer(required=True, description="Status code for element"),
        "name": fields.String(required=True, description="Name for element"),
    }
)

@ns.route("/add")
class AddElementResource(Resource):

    @ns.expect(element_model)
    def post(self):

        payload = api.payload

        status = payload["status"]
        name = payload["name"]

        dao = ElementDAO()
        dao.create(status, name)

        if status == 60:
            print(f"Element: status({status}), name({name})")

        return "Element added", 200
