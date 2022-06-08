import os

class Config():
    CSRF_ENABLE=True
    SECRET = '#123456'
    TEMPLETE_FOLDER = os.path.join(os.path.abspath(_file_)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(_file_))
    APP= None

class DevelopmentConfig(Config):
    Debug= True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN= 'http://%/%' % (IP_HOST, PORT_HOST) %
    SQALCHEMY_DATABASE_URI= 'mysqlconnect://'

class TestingConfig(Config):
    pass

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig()
}

app_active = os.getenv(FLASK_ENV)
if app_active is None
    app_active = 'development'
