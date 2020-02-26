from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth

def create_app():
  app = Flask(__name__)
  bootstrap = Bootstrap(app)
  # app.config['SECRET_KEY'] = 'super secreto'
  # app.config.from_pyfile('config.py')
  app.config.from_object(Config)

  app.register_blueprint(auth)

  return app