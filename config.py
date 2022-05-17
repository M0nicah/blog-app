# import os

# basedir = os.path.abspath(os.path.dirname(__file__))


# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
#         'postgresql://', 'postgres://') or \
#         'sqlite:///' + os.path.join(basedir, 'blogapp.db')


#     LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

import os

class Config:
    '''
    General configuration parent class
    '''
    #  email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/blogapp'




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

# class TestConfig(Config):
#     # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brian:new_password@localhost/watchlist_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost/blogapp'

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}
