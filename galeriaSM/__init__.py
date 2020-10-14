from flask import Flask
from dynaconf import FlaskDynaconf
from flask_bootstrap import Bootstrap

app = Flask(__name__)
FlaskDynaconf(app)

bootstrap = Bootstrap(app)

from galeriaSM import routes
