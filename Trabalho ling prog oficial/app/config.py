import os
from os.path import basename
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "dados de banco"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '../storage.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True