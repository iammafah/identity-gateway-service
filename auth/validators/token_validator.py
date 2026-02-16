from flask import Request

def extract_bearer_token(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None

    if not auth_header.startswith("Bearer "):
        return None

    return auth_header.split("Bearer ")[1]
