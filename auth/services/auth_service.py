from auth.services.firebase_service import verify_firebase_token
from database.handlers.user_handler import handle_firebase_login
from database.models.user_model import User
from extensions import db

def authenticate_user(id_token: str):
    decoded = verify_firebase_token(id_token)

    firebase_data = {
        "uid": decoded["uid"],
        "email": decoded.get("email"),
        "email_verified": decoded.get("email_verified", False),
        "sign_in_provider": decoded.get("firebase", {})
        .get("sign_in_provider", "email")
    }

    return handle_firebase_login(firebase_data)

def update_username(user_id: int, new_username: str):
    user = User.query.get(user_id)

    if not user:
        raise Exception("User not found")

    user.username = new_username
    db.session.commit()

    return user
