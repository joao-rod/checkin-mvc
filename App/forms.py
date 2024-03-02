from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import DataRequired, Email
from wtforms import StringField
from wtforms import SubmitField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(),
                           Email("Preencha com um email válido")])
    password = PasswordField('Password', validators=[DataRequired()])
    # submit = SubmitField('Sign In')
