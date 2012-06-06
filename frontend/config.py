import os
_basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'frontend'

class BaseConfig(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = 'nestor ancel'
  CSRF_ENABLED = True
  
  RECAPTCHA_USE_SSL = True
  RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY', None)
  RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY', None)
  RECAPTCHA_OPTIONS = {'theme': 'clean', 'lang': 'es'}
  
  DEBUG_TB_PROFILER_ENABLED = True
  DEBUG_TB_INTERCEPT_REDIRECTS = False
  
  TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', None)
  TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', None)
  TWITTER_TOKEN = os.environ.get('TWITTER_TOKEN', None)
  TWITTER_SECRET = os.environ.get('TWITTER_SECRET', None)

class DefaultConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/db.sqlite' % os.path.dirname(__file__)

class TestingConfig(BaseConfig):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/test.sqlite' % os.path.dirname(__file__)

class HerokuConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class ProductionConfig(BaseConfig):
  DEBUG = False
