import firebase_admin  # Firebase Admin SDK
from firebase_admin import credentials  # credentials loader
from flask_sqlalchemy import SQLAlchemy  # database ORM
from flask_migrate import Migrate  # migration tool
import os  # environment variables read karne ke liye
import json  # JSON parse karne ke liye

db = SQLAlchemy()  # SQLAlchemy instance create
migrate = Migrate()  # migration instance create

firebase_app = None  # global firebase app reference

def init_firebase():
    global firebase_app  # global variable use karne ke liye

    if not firebase_admin._apps:  # agar firebase initialize nahi hua hai
        firebase_json = os.getenv("FIREBASE_CREDENTIALS")  # Render env variable read karo

        if firebase_json:  # production case (Render)
            cred_dict = json.loads(firebase_json)  # JSON string ko dict me convert
            cred = credentials.Certificate(cred_dict)  # credentials object create
        else:
            cred = credentials.Certificate("secrets/firebase_secret.json")  # local dev file

        firebase_app = firebase_admin.initialize_app(cred)  # Firebase Admin init
    else:
        firebase_app = firebase_admin.get_app()  # existing app use karo

    return firebase_app  # initialized app return
