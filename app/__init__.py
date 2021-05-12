from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    login_manager.init_app(app)

    # login_manager.login_view = 'auth.login'
    # login_manager.login_message_category = 'info'

    bcrypt.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        pass
        # return User.query.get(user_id)

    from app.auth.views import auth

    app.register_blueprint(auth, url_prefix='/')

    db.create_all(app=app)

    return app