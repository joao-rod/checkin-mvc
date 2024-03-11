""" Imports """
from datetime import timedelta
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


def find_markings_by_date(user_id, date) -> list:
    """ Busca todas as marcações """
    return Checkin.query.filter_by(user_id=user_id, date=date).all()


def find_last_marking(user_id, date) -> Checkin:
    """ Busca a ultima marcação """
    return Checkin.query.filter_by(user_id=user_id, date=date).order_by(
        Checkin.created.desc()).first()


def find_total_hours_worked(user_id, date):
    """Calcula o total de horas trabalhadas pelo usuário"""
    checkins = Checkin.query.filter_by(
        user_id=user_id, date=date).order_by(Checkin.created).all()
    total_seconds = 0
    for i in range(0, len(checkins), 2):
        if i + 1 < len(checkins):
            entry = checkins[i]
            output = checkins[i + 1]
            total_seconds += (output.created - entry.created).seconds

    return total_seconds / 3600


def find_expected_end_time(user_id, date):
    """Calcula o horário previsto de término"""
    checkin = find_last_marking(user_id, date)

    if checkin is None:
        return None

    total_hours = find_total_hours_worked(user_id, date)
    remaining_hours = 8 - total_hours

    expected_end_time = checkin.created + timedelta(hours=remaining_hours)

    return expected_end_time.time()
