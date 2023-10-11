from app.extensions import db


class Element(db.Model):

    __tablename__ ="elements"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    name = db.Column(db.String(50))
