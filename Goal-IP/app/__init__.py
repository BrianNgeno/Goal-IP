from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    #initializing the flask extensions
    bootstrap.init_app(app)

    #Registering the bluprint
    from . main import as main_bluprint
    app.register_blueprint(main_blueprint)