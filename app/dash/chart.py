## Special routes associated with chart functionality

from flask import Blueprint
from imports import *

chart_bp = Blueprint("chart_bp", __name__, template_folder='templates', static_folder = 'static')

@chart_bp.route("/chart", methods=['GET', 'POST'])
def chart():
    pass