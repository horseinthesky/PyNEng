import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

myapp = Flask(__name__)
myapp.config['SECRET_KEY'] = 'super-secret-key'
myapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'myweb_database.db')
myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bootstrap = Bootstrap(myapp)
db = SQLAlchemy(myapp)
login = LoginManager(myapp)
login.login_view = 'login'

from myweb import routes, models
