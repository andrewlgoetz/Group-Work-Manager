from flask import Blueprint

example_blueprint = Blueprint('example_blueprint', __name__)


@example_blueprint.route('/home')
def home():
    return "This is an example app - blueprint displayed"