import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'verylongboringunimportanttext'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 8025
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or None
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or None
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or None
    ADMINS = ['no-reply@example.com']
