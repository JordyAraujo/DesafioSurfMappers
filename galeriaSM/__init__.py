from flask import Flask
from dynaconf import FlaskDynaconf
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
FlaskDynaconf(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bootstrap = Bootstrap(app)

login = LoginManager(app)
login.login_view = 'login'

from galeriaSM import routes, models
