from firebase_admin import auth
from extensions import init_firebase

init_firebase()

def verify_firebase_token(id_token: str):
    return auth.verify_id_token(id_token)
