from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_login import LoginManager, login_manager
from flask_mail import Mail


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


photos = UploadSet('photos', IMAGES)
def create_app(config_name):
    app = Flask(__name__)

    #Creating app configurations
    app.config.from_object(config_options[config_name])

    #UploadSet configurations
    configure_uploads(app,photos)

    #Initialize flask extentions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #Register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/aunthenticate')


    return app