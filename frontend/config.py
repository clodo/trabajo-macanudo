import os
_basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'frontend'

class BaseConfig(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = 'nestor ancel'
  CSRF_ENABLED = True
  
class DefaultConfig(BaseConfig):
  DEBUG = True
  database_uri = os.environ.get('DATABASE_URL', 'sqlite:///%s/db/db.sqlite' % os.path.dirname(__file__))
  SQLALCHEMY_DATABASE_URI = database_uri

class TestConfig(BaseConfig):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/test.sqlite' % os.path.dirname(__file__)
