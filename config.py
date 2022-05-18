# import os



# class Config():
#     '''
#     General configuration parent class
#     '''
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '') .replace(
#         'postgres://', 'postgresql://') or\
#         'sqlite:///' + os.path.join(basedir, 'blogapp.db')
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    '''
    General configuration parent class
    '''

     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/blogapp'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '') .replace(
         'postgres://', 'postgresql://') or\
         'sqlite:///' + os.path.join(basedir, 'blogapp.db')

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/blogapp'

config_options = {
'development':DevConfig,
'production':ProdConfig,
}