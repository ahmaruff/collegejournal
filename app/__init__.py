"""
package that contains all of flask program.

this  package contains module (blueprint): 
    auth :  authentication (login/register/reset password)
    course : course (add/delete/view)
    journal : journal (add/edit/delete/view)
    main : main function (index/about/markdown-guide)

Function:
create_app(config_name)
    create flask app using configuration that set on "config_name" value.
    ex: create_app('development')
        this function will create flask app using "development" configuration
        based on config.py setting (it will be DevelopmentConfig class)
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown
from flaskext.markdown import Markdown
from flask_mail import Mail
from flask_moment import Moment


pagedown = PageDown()
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
mail = Mail()
moment = Moment()


def create_app(config_name):
    """
    create_app(config_name)
        function to create flask app using configuration that set on "config_name" value.
    ex: create_app('development')
        this function will create flask app using "development" configuration
        based on config.py setting (it will be DevelopmentConfig class)
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    
    db.init_app(app)
    pagedown.init_app(app)
    Markdown(app)
    mail.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)

    # attach custom routes and errors here,

    # main routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # authentication routes
    from  .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # course routes
    from .course import course as course_blueprint
    app.register_blueprint(course_blueprint, url_prefix='/course')

    # journal routes
    from .journal import journal as journal_blueprint
    app.register_blueprint(journal_blueprint, url_prefix='/journal')

    return app
