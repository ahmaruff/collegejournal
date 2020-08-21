from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown
from flaskext.markdown import Markdown


pagedown = PageDown()
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    # app.config['BOOTSTRAP_SERVE_LOCAL'] = True #This turns file serving static
    
    db.init_app(app)
    pagedown.init_app(app)
    Markdown(app)

    login_manager.init_app(app)

    #attach custom routes and errors here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #authentication routes
    from  .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # course routes
    from .course import course as course_blueprint
    app.register_blueprint(course_blueprint, url_prefix='/course')

    #journal route
    from .journal import journal as journal_blueprint
    app.register_blueprint(journal_blueprint, url_prefix='/journal')

    return app
