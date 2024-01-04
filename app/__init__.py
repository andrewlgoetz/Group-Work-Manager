from flask import Flask
from imports import *
import os
from config import Config
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)



   

    #Auth & New User
    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    #Dashboard
    from .dash.routes import dash_bp 
    app.register_blueprint(dash_bp)
    
    #Models
    db.init_app(app)

    
    return app

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


