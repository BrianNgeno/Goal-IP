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
    MAIL_USERNAME = os.environ.get("lukemark254@gmail.com")
    MAIL_PASSWORD = os.environ.get("1234qwer,./")
	# SENDER_EMAIL = 'lukemark254@gmail.com'
    SECRET_KEY=os.environ.get('SECRET_KEY') 

 
class ProdConfig(Config):
    '''
    child class production and takes in config from the parent
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


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