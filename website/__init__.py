from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'training app for melo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialize the db by giving it our flask app.
    db.init_app(app)

    # Importing the Blueprints from view and auth file.
    from .views import views
    from .auth import auth

    # Registering our Blueprints with our Flask application.
    app.register_blueprint (views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Make sure we load database files before we initialize/create our database.
    from .models import User, Note, Dogs
    
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    # Only creates the DB if it does not exists.
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)