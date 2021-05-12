import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
SECRET_KEY = '_5#y2L"F4Q8zdkhvybksjnkbxjshfcgfsa\n\xec]'
WTF_CSRF_ENABLED = True
DB_NAME = "data.db"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False