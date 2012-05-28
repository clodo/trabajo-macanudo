import os
_basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'frontend'

class BaseConfig(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = 'nestor ancel'
  CSRF_ENABLED = True
  RECAPTCHA_USE_SSL = True
  RECAPTCHA_PUBLIC_KEY = '6Lco79ESAAAAAPKyci6r9mVxKzXu9QbSICcRWRnE'
  RECAPTCHA_PRIVATE_KEY = '6Lco79ESAAAAAE6_QrNDFzb9S2J979gk5fDsgDWj'
  RECAPTCHA_OPTIONS = {'theme': 'clean', 'lang': 'es'}
  DEBUG_TB_PROFILER_ENABLED = True
  DEBUG_TB_INTERCEPT_REDIRECTS = False
  
class DefaultConfig(BaseConfig):
  DEBUG = True
  database_uri = os.environ.get('DATABASE_URL', 'sqlite:///%s/db/db.sqlite' % os.path.dirname(__file__))
  SQLALCHEMY_DATABASE_URI = database_uri

class TestConfig(BaseConfig):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/test.sqlite' % os.path.dirname(__file__)