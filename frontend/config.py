import os
_basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'frontend'

class BaseConfig(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = 'nestor ancel'
  
class DefaultConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/db.sqlite' % os.path.dirname(__file__)

class TestConfig(BaseConfig):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/test.sqlite' % os.path.dirname(__file__)
