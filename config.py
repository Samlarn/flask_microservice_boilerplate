import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'make-this-hard-to-guess'

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'make-this-hard-to-guess-also'

    JWT_BLACKLIST_ENABLED = True

    JWT_BLACKLIST_TOKEN_CHECKS =  ['access', 'refresh']

    DEBUG = os.environ.get('DEBUG') or 'False'

    MS_NAME = os.environ.get('MS_NAME') or 'ms_template'

    MS_ID = os.environ.get('MS_ID') or '1337'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://foo:bar@localhost/ms_template_db'#os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///databaseModels/msApp.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False