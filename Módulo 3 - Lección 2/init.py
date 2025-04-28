from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal

db = SQLAlchemy()
login_manager = LoginManager()
principals = Principal()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    principals.init_app(app)

    from auth import auth
    from route import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
