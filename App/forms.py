""" Imports """
from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import StringField
from wtforms import BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """ Formulário de login """
    username = StringField('Email', validators=[
                           DataRequired(),
                           Email("Preencha com um email válido")])
    password = PasswordField('Senha', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    """ Formulário de registro """
    name = StringField('Nome', validators=[DataRequired()])
    username = StringField('Email', validators=[
                           DataRequired(),
                           Email("Preencha com um email válido")])
    password = PasswordField('Senha', validators=[DataRequired()])
    agree_terms = BooleanField(
        'Aceito as condições de uso e política de privacidade.',
        validators=[DataRequired()])


class EditUserForm(FlaskForm):
    """ Formulário de edição de usuario """
    name = StringField('Nome', validators=[DataRequired()])
    username = StringField('Email', validators=[
                           DataRequired(),
                           Email("Preencha com um email válido")])
    change_password = BooleanField('Alterar senha')
    current_password = PasswordField('Senha atual')
    new_password = PasswordField('Nova senha')
