# Production-specific settings
class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///production.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
