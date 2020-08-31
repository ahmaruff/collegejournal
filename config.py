import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ 
    A class used to create basic app configuration
    
    Key:
    SECRET KEY : str 
        Constanta that used to protect client-side sessions (also used to salt-hash), 
        it can be assign using environment variable "SECRET_KEY"
    
    SQLALCHEMY_TRACK_MODIFICATION : Boolean
        constanta that used to set Track modification on sqlalchemy (default :False)

    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'veryhardtoguessstring'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    A class to create app configuration (for Development)
    this configuration also inherited from class Config

    Key:
    DEBUG : Boolean
        set DEBUG MODE on flask app, (for development purpose, default : True)

    SQL_ALCHEMY_DATABASE_URI : database path/url
        set Database path/url, using environment variable "DEV_DATABASE_URL" or
        using default Database url. 
    
    MAIL_SERVER : str
        set mail url server, ex: smtp.googlemail.com (gmail)
    
    MAIL_PORT : int
        set mail server port, ex: 587 (gmail)

    MAIL_USE_TLS : int/bool
        set using TLS or not

    MAIL_USERNAME : str
        set mail account that want to used
        set using environmet variable "MAIL_USERNAME"

    MAIL_PASSWORD : str
        set mail account password (for login into its account),
        set using environment variable "MAIL_PASSWORD"

    MAIL_DEFAULT_SENDER :
        set default account that want to used,
        default : same as MAIL_USERNAME value.

    note, if you want to use gmail, you have to enable "less secure app to access gmail" setting
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:@localhost/jurnalkuliah'
        # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = f'{MAIL_USERNAME}'

class TestingConfig(Config):
    """
    A class to create app configuration (for Testing)
    this configuration also inherited from class Config

    Key:
    TESTING: Boolean
        set Testing mode on flask, default : True

    SQL_ALCHEMY_DATABASE_URI : str
        set database url for testing, default using SQLite.

    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

class ProductionConfig(Config):
    """
    A class to create app configuration (for production)
    this configuration also inherited from class Config

    Key:
    DEBUG : Boolean
        set DEBUG MODE on flask app, (for production, you have to disable it, default : False)

    SQL_ALCHEMY_DATABASE_URI : database path/url
        set Database path/url, using environment variable "DATABASE_URL"
    
    MAIL_SERVER : str
        set mail url server, ex: smtp.googlemail.com (gmail)
    
    MAIL_PORT : int
        set mail server port, ex: 587 (gmail)

    MAIL_USE_TLS : int/bool
        set using TLS or not

    MAIL_USERNAME : str
        set mail account that want to used
        set using environmet variable "MAIL_USERNAME"

    MAIL_PASSWORD : str
        set mail account password (for login into its account),
        set using environment variable "MAIL_PASSWORD"

    MAIL_DEFAULT_SENDER :
        set default account that want to used,
        default : same as MAIL_USERNAME value.
        
    note, if you want to use gmail, you have to enable "less secure app to access gmail" setting
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
        # 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = f'{MAIL_USERNAME}'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}