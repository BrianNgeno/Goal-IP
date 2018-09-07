import os 
class Config:
    '''
    parent class config 
    '''
   
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