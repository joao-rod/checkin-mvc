""" Importações """
from flask import session
from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from App.model import db, User


def verify_login(username, password):
    """ Valida o usuario e senha para efetuar o login """
    if not username or not password:
        return False
    existing_user = User.query.filter_by(username=username).first()

    if not existing_user:
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


def create_user(name, username, password, agree_terms) -> User:
    """ Registra um novo usuario caso nao esteja cadastrado """
    user = User(name=name, username=username, password=generate_password_hash(
        password), agree_terms=agree_terms)
    db.session.add(user)
    db.session.commit()
    return user


def edit_user(user) -> User:
    """ Edita um usuario caso o nao esteja cadastrado """
    db.session.add(user)
    db.session.commit()
    return user


def is_user_already_exist(username):
    """ Verifica se usuário já está cadastrado e retorna mensagem de erro """
    if User.query.filter_by(username=username).first():
        return f"{username} já está cadastrado!"
    else:
        return None


def is_logged():
    """ Verifica se o usuário """
    return 'username' in session


def get_user() -> User:
    """ Retorna usuário logado """
    return User.query.filter_by(username=session['username']).first()


def init_app(app):
    """  Inicia o SimpleLogin no app """
    SimpleLogin(app, login_checker=verify_login)
