from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from os import path


basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = Flask(__name__)

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    # where to store app.db (database file)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
)

db = SQLAlchemy(myapp_obj)
#creating database


def createDatabase(app):
    if not path.exists('websiteProject/' + 'app.db'):
        db.create_all(app=app)
        print("Created db")

createDatabase(myapp_obj)

login = LoginManager(myapp_obj)
# function that is called to login a user
login.login_view = 'login'

from app import routes, models
