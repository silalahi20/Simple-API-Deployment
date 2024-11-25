from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "EUrRSnwrBlbAE4aLQ7iibR98EB0GkZjGMqLQwubFVRs",
}

users = {
    "EUrRSnwrBlbAE4aLQ7iibR98EB0GkZjGMqLQwubFVRs": {
        "name": "ParMusic",
        "message": "Semoga TST dapat A. A for Aminn",
        "email": "parmusic@example.com",
        "password": pwd_context.hash("securepassword"),
    }
}

def check_api_key(api_key: str):
    return api_key in api_keys

def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]

def authenticate_user(email: str, password: str):
    for user in users.values():
        if user["email"] == email and pwd_context.verify(password, user["password"]):
            return user
    return None
