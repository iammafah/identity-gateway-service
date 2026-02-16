from database.models.user_model import User
from extensions import db

def get_user_by_firebase_uid(firebase_uid):
    return User.query.filter_by(firebase_uid=firebase_uid).first()

def create_user(user):
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user):
    db.session.commit()
    return user
