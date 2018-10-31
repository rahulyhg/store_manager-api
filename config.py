"""config file"""
import datetime
import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """environment configurations """
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret'
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'


class DevelopmentConfig(BaseConfig):
    """development environment """
    ENV = 'development'
    DATABASE = 'storemanager'
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    """ enables testing environment """
    ENV = 'testing'
    DATABASE = 'storemanager_test_db'
    DEBUG = True
    TESTING = True

config = dict(
    development = DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig
)
