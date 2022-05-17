from ensurepip import bootstrap
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap



db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'
bootstrap = Bootstrap()


def createapp(config_class=Config):
    app = Flask(__name__)
    # Setting up configuration
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://smhnlzawyswsou:f9f02fb0abe68b32afdfeabac823d2fbfc249e464a9cd85c225177b871caefd5@ec2-3-229-252-6.compute-1.amazonaws.com:5432/ddp651snc9mj3g'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SECRET_KEY"] = '885b966eda440980c4db'

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    if not app.debug and not app.testing:
        # heroku logs to stdout
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
            # End of Heroku stdout logs

    return app
