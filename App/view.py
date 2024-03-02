""" Imports """
from flask import render_template, redirect, url_for, request, session

from App.forms import LoginForm, RegisterForm
from App.ext.authentication import create_user
from App.ext.authentication import verify_login
from App.ext.authentication import is_logged
from App.ext.authentication import get_user
from App.ext.authentication import is_user_already_exist


def init_app(app):
    """Definição das rotas"""
    app.add_url_rule("/", view_func=home)
    app.add_url_rule("/home", view_func=home)
    app.add_url_rule("/register/", view_func=register, methods=['GET', 'POST'])
    app.add_url_rule("/login/", view_func=login, methods=['GET', 'POST'])
    app.add_url_rule("/logout/", view_func=logout)


def home():
    """Homepage"""
    if not is_logged():
        return redirect(url_for('login'))
    user_logged = get_user()
    return render_template('home.html', user=user_logged)


def register():
    """Register"""
    form = RegisterForm()
    message = None

    if form.validate_on_submit():
        message = is_user_already_exist(username=form.username.data)
        if not message:
            user = create_user(name=form.name.data,
                               username=form.username.data,
                               password=form.password.data,
                               agree_terms=form.agree_terms.data)
            return render_template('home.html', user=user)
    return render_template('register.html', form=form, message=message)


def login():
    """Login"""
    form = LoginForm()
    message = None

    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if verify_login(username, password):
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            message = "Email ou senha incorretos."
    return render_template('login.html', form=form, message=message)


def logout():
    """Logout"""
    session.clear()
    return redirect(url_for('simplelogin.login'))
