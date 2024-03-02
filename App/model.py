from sqlalchemy_serializer import SerializerMixin
from App.ext.database import db, Integer, String, Column


class Checkin(db.Model, SerializerMixin):
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
