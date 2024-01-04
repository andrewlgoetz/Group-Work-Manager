from flask import Blueprint
from imports import *

auth_bp = Blueprint("auth_bp", __name__, template_folder='templates', static_folder = 'static')

# # Login 
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(user_id):
#     pass #return Users.query.get(int(user_id))

# @login_manager.user_loader
# def get_user(ident):
#     pass #return Users.query.get(int(ident))