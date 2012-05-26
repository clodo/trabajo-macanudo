import os
_basedir = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'frontend'

class BaseConfig(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = 'nestor ancel'
  CSRF_ENABLED = True
  RECAPTCHA_USE_SSL = True
  RECAPTCHA_PUBLIC_KEY = '6LcK79ESAAAAAKosCIouR-X-9FBawGYE1rEr02FO'
  RECAPTCHA_PRIVATE_KEY = '6LcK79ESAAAAAKy-jWiShHL0lbmSoEWMixfISNmV'
  RECAPTCHA_OPTIONS = {'theme': 'clean', 'lang': 'es'}
  
class DefaultConfig(BaseConfig):
  DEBUG = True
  database_uri = os.environ.get('DATABASE_URL', 'sqlite:///%s/db/db.sqlite' % os.path.dirname(__file__))
  SQLALCHEMY_DATABASE_URI = database_uri

class TestConfig(BaseConfig):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/db/test.sqlite' % os.path.dirname(__file__)