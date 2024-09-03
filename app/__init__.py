# Flask application factory
from flask import Flask

# DevelopmentConfig
from app.config.development import DevelopmentConfig
from app.utils.database import db
from app.blueprints.user import user as user_blueprint


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    # Register blueprints/
    app.register_blueprint(user_blueprint, url_prefix="/api/users")

    return app
