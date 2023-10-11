from app.extensions import db

from .models import Element

class ElementDAO:

    def create(self, status, name):
        element = Element(status=status, name=name)
        db.session.add(element)
        db.session.commit()

        return element

    def read(self, element_id):
        element = Element.query.filter_by(id=element_id).first()

        return element

    def read_all(self):
        elements = Element.query.all()

        return elements

    def update(self):
        pass

    def delete(self):
        pass
