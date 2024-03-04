""" Imports """
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Integer, String, Column, Boolean, DateTime
from App.ext.database import db


class Checkin(db.Model, SerializerMixin):
    """Tabela principal para marcações"""
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class User(db.Model, SerializerMixin):
    """Tabela de usuários"""
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now)
    name = Column(String(50), nullable=False)
    username = Column(String(140), unique=True, nullable=False)
    password = Column(String(512), nullable=False)
    agree_terms = Column(Boolean(), nullable=False)
