""" Module providing a function printing python version. """
from flask import Flask
from flask_bootstrap import Bootstrap
from App.ext import authentication
from App.ext import database
from App.ext import configuration
from App.ext import admin
from App.ext import commands

import App.view as view


def create_app():
    """
    Function creating and returning a Flask application.
    :return: Flask application.
    """
    app = Flask(__name__)
    Bootstrap(app)
    configuration.init_app(app)
    database.init_app(app)
    commands.init_app(app)
    view.init_app(app)
    authentication.init_app(app)
    admin.init_app(app)
    return app
