# This makes the whole folder a package which can be imported in main.py file
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Setting Up our database
from os import path


db = SQLAlchemy()   # Defining the database
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ASDHFAL;SANVOVALSV;N'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # It will make a database folder to store all the data
    db.init_app(app)
    
    # Registering our blueprints in init.py
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Note, User
        
    create_database(app)

    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')