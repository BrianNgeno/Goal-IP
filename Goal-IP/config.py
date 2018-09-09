import os 
class Config:
    '''
    parent class config 
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bknngeno:123@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("lukemark@gmail.com")
    MAIL_PASSWORD = os.environ.get("1234qwer,./")

    @staticmethod
    def init__app(app):
        pass
 
class ProdConfig(Config):
    '''
    child class production and takes in config from the parent
    '''
    pass

class DevConfig(Config):
    DEBUG = True

# defining our config options
class TestConfig(Config):
    pass

config_options = { 
    'production':ProdConfig,
    'development' :DevConfig,
    'test':TestConfig
}