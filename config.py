import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '57e19ea558d4967a552d03deece34a70'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT=True
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # "postgresql://<username>:<password>@<server>:5432/<db_name>"
    userNameDataBase = os.getenv('USER_DB')
    passwordDataBase = os.getenv('PASSWORD_DB')
    nameDataBase = os.getenv('NAME_DB')
    hostDataBase = os.getenv('HOST_DB')
    SQLALCHEMY_DATABASE_URI= f"postgresql://{userNameDataBase}:{passwordDataBase}@{hostDataBase}:5432/{nameDataBase}"