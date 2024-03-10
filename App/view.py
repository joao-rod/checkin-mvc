""" Imports """
from datetime import datetime
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import session
from flask import flash
from flask import jsonify

from App.ext.authentication import create_user
from App.ext.authentication import edit_user
from App.ext.authentication import verify_login
from App.ext.authentication import is_logged
from App.ext.authentication import get_user
from App.ext.authentication import is_user_already_exist
from App.ext.authentication import check_current_password

from App.model import Checkin
from App.model import save_marking
from App.model import find_markings_by_date
from App.model import find_last_marking
from App.forms import LoginForm, RegisterForm, EditUserForm, MarkingForm


def init_app(app):
    """Definição das rotas"""
    app.add_url_rule("/", view_func=home)
    app.add_url_rule("/home/", view_func=home, methods=['GET', 'POST'])
    app.add_url_rule("/register/", view_func=register, methods=['GET', 'POST'])
    app.add_url_rule("/login/", view_func=login, methods=['GET', 'POST'])
    app.add_url_rule("/logout/", view_func=logout)
    app.add_url_rule('/get_current_date/',
                     view_func=get_current_date, methods=['GET'])
    app.add_url_rule("/preferences/",
                     view_func=preferences, methods=['GET', 'POST'])


def home():
    """ Homepage """
    if not is_logged():
        return redirect(url_for('login'))

    user_logged = get_user()
    markings = find_markings_by_date(user_logged.id, datetime.now().date())

    curret_time = datetime.now()
    form = MarkingForm(time=curret_time)

    if request.method == 'POST' and form.validate_on_submit():
        last_marking = find_last_marking(user_logged.id)
        if last_marking:
            if last_marking.is_entry:
                is_entry = False
            else:
                is_entry = True
        else:
            is_entry = True

        marking = Checkin(user_id=user_logged.id,
                          is_entry=is_entry,
                          description=form.description.data)

        save_marking(marking)
        return redirect(url_for('home', user=user_logged))
    return render_template('home.html',
                           user=user_logged,
                           form=form,
                           markings=markings)


def register():
    """ Register """
    form = RegisterForm()
    message = None

    if form.validate_on_submit():
        message = is_user_already_exist(username=form.username.data)
        if not message:
            user = create_user(name=form.name.data,
                               username=form.username.data,
                               password=form.password.data,
                               agree_terms=form.agree_terms.data)
            session['username'] = request.form['username']
            return redirect(url_for('home', user=user))
    return render_template('register.html', form=form, message=message)


def login():
    """ Login """
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
    """ Logout """
    session.clear()
    return redirect(url_for('login'))


def preferences():
    """ Preferencias  de usuario """
    if not is_logged():
        return redirect(url_for('login'))

    user = get_user()
    form = EditUserForm(obj=user)
    message = None

    if form.validate_on_submit():
        if form.change_password.data:
            current_password = form.current_password.data
            new_password = form.new_password.data

            if not check_current_password(user, current_password):
                message = "Senha atual incorreta"
                return render_template('preferences.html',
                                       form=form,
                                       user=user,
                                       message=message)
        else:
            current_password = None
            new_password = None

        if user.username != form.username.data:
            message = is_user_already_exist(username=form.username.data)
            if not message:
                user.name = form.name.data
                user.username = form.username.data
                user = edit_user(user, current_password, new_password)
                session['username'] = request.form['username']
                flash('Usuário alterado com sucesso', 'success')
                return render_template('preferences.html',
                                       form=form,
                                       user=user,
                                       message=message)
        else:
            if user.name != form.name.data:
                flash('Usuário alterado com sucesso', 'success')
            else:
                flash('Senha alterada com sucesso', 'success')

            user.name = form.name.data
            user = edit_user(user, current_password, new_password)
            session['username'] = request.form['username']

    return render_template('preferences.html',
                           form=form,
                           user=user,
                           message=message)


def get_current_date():
    """ Obtém a data atual """
    current_date = datetime.now().strftime('%d/%m/%Y')
    return jsonify({'current_date': current_date})
