import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# function to return generated tokens


def token_response(token: str):
    return {
        "access_token": token
    }

# signing and generating tokens


def generate_token(email: str):
    payload = {
        "email": email,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


# function to decode token
def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decoded_token if decoded_token["expiry"] >= time.time() else None
    except:
        return {}
