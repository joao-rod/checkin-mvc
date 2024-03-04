""" Imports """
from flask_admin import Admin
from flask_admin.contrib import sqla
from werkzeug.security import generate_password_hash

from App.model import db, Checkin, User

# from flask_simplelogin import login_required
# from flask_admin.base import AdminIndexView
# Proteger o admin com login via Monkey Patch
# AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
# sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)

admin = Admin()


class UserAdmin(sqla.ModelView):
    """ UserAdmin """
    can_edit = False

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)


def init_app(app):
    """ Inicializa perfil Admin """
    admin.name = 'Checkin-Admin'
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.add_view(sqla.ModelView(Checkin, db.session))
    admin.add_view(UserAdmin(User, db.session))
