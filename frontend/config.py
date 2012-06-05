import os
_basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'frontend'

class BaseConfig(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = 'nestor ancel'
  CSRF_ENABLED = True
  
  RECAPTCHA_USE_SSL = True
  RECAPTCHA_PUBLIC_KEY = ''
  RECAPTCHA_PRIVATE_KEY = ''
  RECAPTCHA_OPTIONS = {'theme': 'clean', 'lang': 'es'}
  
  DEBUG_TB_PROFILER_ENABLED = True
  DEBUG_TB_INTERCEPT_REDIRECTS = False
  
  TWITTER_CONSUMER_KEY = ''
  TWITTER_CONSULER_SECRET = ''
  TWITTER_TOKEN = ''
  TWITTER_SECRET = ''

class DefaultConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/db.sqlite' % os.path.dirname(__file__)

class TestingConfig(BaseConfig):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/test.sqlite' % os.path.dirname(__file__)

class HerokuConfig(BaseConfig):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  RECAPTCHA_PUBLIC_KEY = ''
  RECAPTCHA_PRIVATE_KEY = ''
