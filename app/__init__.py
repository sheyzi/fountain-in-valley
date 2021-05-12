from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, migrate

from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    migrate.init_app(app, db=db)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    bcrypt.init_app(app)
    mail.init_app(app)

    from app.auth.views import auth

    app.register_blueprint(auth, url_prefix='/')

    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    db.create_all(app=app)

    return app