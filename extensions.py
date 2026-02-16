import firebase_admin
from firebase_admin import credentials
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

firebase_app = None

def init_firebase():
    global firebase_app

    if not firebase_admin._apps:
        cred = credentials.Certificate("secrets/firebase_secret.json")
        firebase_app = firebase_admin.initialize_app(cred)
    else:
        firebase_app = firebase_admin.get_app()

    return firebase_app
