import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
SECRET_KEY = '_5#y2L"F4Q8zdkhvybksjnkbxjshfcgfsa\n\xec]'
WTF_CSRF_ENABLED = True
DB_NAME = "data.db"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'xbid.info@gmail.com'
MAIL_DEFAULT_SENDER = 'xbid.info@gmail.com'
MAIL_PASSWORD = 'Password@2020'

MAIL_USE_TLS = False
MAIL_USE_SSL = True