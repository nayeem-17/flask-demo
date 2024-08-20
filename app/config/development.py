class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:pass@localhost:5432/demo"  # import this from .env
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
