class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    SECRET_KEY = 'secure_production_key'
