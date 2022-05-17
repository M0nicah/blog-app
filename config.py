import os

basedir = os.path.abspath(os.path.dirname(__file__))

from sqlalchemy import create_engine,exc

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/blogapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = create_engine(os.environ.get("DATABASE_URL").replace("://", "ql://", 1), pool_recycle=3600)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgresql://') or \
       'sqlite:///' + os.path.join(basedir, 'blogapp.db')
    

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/blogapp'   

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
