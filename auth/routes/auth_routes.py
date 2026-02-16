from flask import Blueprint, request, jsonify
from auth.validators.token_validator import extract_bearer_token
from auth.services.auth_service import authenticate_user, update_username

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    token = extract_bearer_token(request)

    if not token:
        return jsonify({"error": "Authorization token missing"}), 401

    try:
        user = authenticate_user(token)
    except Exception:
        return jsonify({"error": "Invalid token"}), 401

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "signup_method": user.signup_method,
        "is_email_verified": user.is_email_verified
    })

@auth_bp.route("/username", methods=["PUT"])
def change_username():
    data = request.json
    user_id = data.get("user_id")
    new_username = data.get("username")

    user = update_username(user_id, new_username)

    return jsonify({
        "id": user.id,
        "username": user.username
    })
