from flask import Flask
from imports import *

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
    app.config['SECRET_KEY'] = "abcd"
    app.config['SESSION_TYPE'] = 'memcached'

    db = SQLAlchemy(app)



    #Models

    #Auth & New User
    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    #Dashboard
    from .dash.routes import dash_bp 
    app.register_blueprint(dash_bp)
    
    
    return app

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)