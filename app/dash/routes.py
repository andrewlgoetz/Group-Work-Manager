from flask import Blueprint
from imports import *

dash_bp = Blueprint("dash_bp", __name__, template_folder='templates', static_folder = 'static')



#index

@dash_bp.route("/")
def index():



    return render_template("index.html")
