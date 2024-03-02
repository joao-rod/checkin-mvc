"""Module providing a function printing python version."""
from flask import Flask
from flask_bootstrap import Bootstrap
from App.ext import authentication, database, configuration, admin, \
    commands
import App.model
import App.view as view


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    configuration.init_app(app)
    database.init_app(app)
    commands.init_app(app)
    view.init_app(app)
    authentication.init_app(app)
    admin.init_app(app)
    return app


# @app.route('/')
# @app.route('/home')
# def home():
#     """Module providing a function printing python version."""
#     return render_template('home.html')


# @app.route('/login')
# def login():
#     return render_template('login.html')


# @app.route('/preferences')
# def preferences():
#     return render_template('preferences.html')


# if __name__ == '__main__':
#     app.run(debug=True)
