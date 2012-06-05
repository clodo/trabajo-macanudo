# -*- coding: utf-8 -*-

from setuptools import setup

setup(
  name='Trabajo Macanudo',
  version='0.1',
  description='Trabajo Macanudo',
  author='Banquito',
  author_email='hola@elgalpondebanquito.com.ar',
  packages=['frontend'],
  include_packages_data=True,
  zip_safe=False,
  install_requires=[
    'Flask',
    'Flask-SQLAlchemy',
    'Flask-WTF',
    'Flask-Script',
    'Flask-Testing',
    'Flask-DebugToolbar',
    'python-twitter',
    'nose',
    'factory-boy',
    'psycopg2',
  ]
)
