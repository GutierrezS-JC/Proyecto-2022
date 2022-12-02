from os import environ


class Config(object):
    """Base configuration."""

    SECRET_KEY = "secret"
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = "secret_key"
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_COOKIE_NAME = "access_token_cookie"
    JWT_ACCESS_CSRF_HEADER_NAME = "X-Xsrf-Token"


class ProductionConfig(Config):
    """Production configuration"""

    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    # Session values
    SESSION_TYPE = 'filesystem'
    # JWT
    JWT_COOKIE_SAMESITE = "None"
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_DOMAIN = ".proyecto2022.linti.unlp.edu.ar"


class DevelopmentConfig(Config):
    """Development configuration."""

    # Database values
    DEBUG = True
    DB_USER = environ.get("DB_USER", "postgres")
    DB_PASS = environ.get("DB_PASS", "935root935")
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_NAME = environ.get("DB_NAME", "club")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    # Session values
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = '40c17c4ff739c52983ba31b49fb17c62',
    JWT_COOKIE_SECURE = True,
    JWT_COOKIE_SAMESITE = "None"


class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True


config = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": ProductionConfig,
}
