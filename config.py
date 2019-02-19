import os

class Config:
    BASE_URL ='http://quotes.stormconsultancy.co.uk/{}.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ron:3159@localhost/rblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   

class DevConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}