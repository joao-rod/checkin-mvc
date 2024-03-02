def init_app(app):
    app.config["TITLE"] = "CheckIn"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///checkin.db"
    app.config['SECRET_KEY'] = 'something-secret'
    app.config['SIMPLELOGIN_LOGIN_URL'] = '/signin'
    app.config['SIMPLELOGIN_LOGOUT_URL'] = '/logout'
    app.config['SIMPLELOGIN_HOME_URL'] = '/'
