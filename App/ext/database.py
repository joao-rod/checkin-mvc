""" Imports """
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    """ Inicializar banco de dados. """
    db.init_app(app)

    with app.app_context():
        db.create_all()
