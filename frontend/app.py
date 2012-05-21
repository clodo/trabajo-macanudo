import os

from flask import Flask, render_template
from frontend.config import DefaultConfig, APP_NAME
from frontend.views import main
from frontend.extensions import db

__all__ = ['create_app']

def create_app(config=None, app_name=None):
  if app_name is None:
    app_name = APP_NAME
  
  app = Flask(app_name)
  
  configure_app(app, config)
  configure_extensions(app)
  configure_error_handlers(app)

  app.register_blueprint(main.mod)
  
  return app

def configure_app(app, config):
  app.config.from_object(DefaultConfig)
  if config is not None:
    app.config.from_object(config)

def configure_extensions(app):
  # sqlalchemy
  db.init_app(app)

def configure_error_handlers(app):
  @app.errorhandler(404)
  def not_found(error):
    return render_template('404.html'), 404
