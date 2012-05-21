import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'db/db.sqlite')
BABEL_DEFAULT_LOCALE = 'es_AR'
BABEL_DEFAULT_TIMEZONE = 'America/Argentina/Buenos_Aires'