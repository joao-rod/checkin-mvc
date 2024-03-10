""" Imports """
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Date
from sqlalchemy import ForeignKey

from App.ext.database import db


class User(db.Model, SerializerMixin):
    """Tabela de usuários"""
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now)
    name = Column(String(50), nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(15), nullable=False)
    agree_terms = Column(Boolean(), nullable=False)
    time_records = db.relationship('Checkin', backref='user')


class Checkin(db.Model, SerializerMixin):
    """Tabela principal para marcações"""
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created = Column(DateTime, default=datetime.now)
    date = Column(Date, default=datetime.now().date)
    is_entry = Column(Boolean, nullable=False)
    description = Column(String(100), nullable=True)


def save_marking(checkin) -> Checkin:
    """ Salva marcação """
    db.session.add(checkin)
    db.session.commit()
    return checkin
