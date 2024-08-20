# Flask application factory
from flask import Flask

# DevelopmentConfig
from app.blueprints.main import main as main_blueprint
from app.config.development import DevelopmentConfig
from app.models.user import *
from app.utils.database import db


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    # Register blueprints/
    app.register_blueprint(main_blueprint)

    return app
