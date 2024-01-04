from flask import Flask
from imports import *
import os
from config import Config
from app.extension import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = "abcd"
    app.config['SESSION_TYPE'] = 'memcached'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    @login_manager.user_loader
    def get_user(ident):
        return Users.query.get(int(ident))


    #Auth & New User
    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    #Dashboard
    from .dash.routes import dash_bp 
    app.register_blueprint(dash_bp)
    
    #Models
    db.init_app(app)
    with app.app_context():
        # db.metadata.clear()
        # db.drop_all()
        db.create_all()




    #errors:
    app.register_error_handler(403, forbidden)
    
    return app

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)



def forbidden(e):
    return render_template('403.html'), 403