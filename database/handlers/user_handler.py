from database.models.user_model import User
from database.queries.user_query import (
    get_user_by_firebase_uid,
    create_user,
    update_user
)
from auth.services.username_services import generate_username

def handle_firebase_login(firebase_data):
    user = get_user_by_firebase_uid(firebase_data["uid"])

    if not user:
        user = User(
            firebase_uid=firebase_data["uid"],
            email=firebase_data["email"],
            username=generate_username(),
            signup_method=firebase_data["sign_in_provider"],
            is_email_verified=firebase_data["email_verified"]
        )
        create_user(user)
        return user

    user.email = firebase_data["email"]
    user.is_email_verified = firebase_data["email_verified"]
    update_user(user)

    return user
