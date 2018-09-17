import os 
class Config:
    '''
    parent class config 
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY= os.environ.get('SECRET_KEY') 
	 # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

 
class ProdConfig(Config):
    '''
    child class production and takes in config from the parent
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bknngeno:123@localhost/pitches'
    DEBUG = True

# defining our config options
class TestConfig(Config):
    pass

config_options = { 
    'production':ProdConfig,
    'development' :DevConfig,
    'test':TestConfig
}