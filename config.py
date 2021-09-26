import os

class Config:
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.environ.get('SECRET_KEY')

     #Database configurations
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patrick:patrick@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    #email configurations
    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','')
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://',1)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patrick:patrick@localhost/blogs'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}