""" Imports """
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Integer, String, Column
from App.ext.database import db


class Checkin(db.Model, SerializerMixin):
    """Tabela principal para marcações"""
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class User(db.Model, SerializerMixin):
    """Tabela de usuários"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
    agree_terms = db.Column(db.Boolean())
