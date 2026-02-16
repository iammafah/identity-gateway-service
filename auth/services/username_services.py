import uuid

def generate_username():
    return "user_" + uuid.uuid4().hex[:8]
