from  flask import Flask

def create_app(config):
    app = Flask(_name_)
    app.secret_key = config.SECRET
    app.config.from_object(DevelomentConfig)
    app.config.from_pyfile('config.py')
    app.config['SQALCHEMY_DATABASE_URI']= config.SQALCHEMY_DATABASE_URI
    app.config['SQALCHEMY_TRACK_MODIFICATION'] = False

    config.APP= app

    @app.route('/')
    def index():
        return 'oi'