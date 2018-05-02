from flask import Flask
from flask_bootstrap import Bootstrap


myapp = Flask(__name__)
myapp.config['SECRET_KEY'] = 'super-secret-key'
bootstrap = Bootstrap(myapp)

from myweb import routes
