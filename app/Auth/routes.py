from flask import Blueprint
from imports import *


auth_bp = Blueprint("auth_bp", __name__, template_folder='templates', static_folder = 'static')

#login
#logout
#new user
#delete user



@auth_bp.route("/new_user")
def new_user():
    return render_template("new_user.html")
