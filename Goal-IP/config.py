import os 
class Config:
   
    @staticmethod
    def init__app(app):
        pass
 
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True