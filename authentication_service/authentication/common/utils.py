import datetime
import jwt

from django.conf import settings


DEFAULT_EXPIREY_DAYS = 1

def generate_token():
    """
    Generate JWT token
    """
    token = jwt.encode(
        {'exp': datetime.datetime.utcnow() + datetime.timedelta(days=DEFAULT_EXPIREY_DAYS)},
        settings.SECRET_KEY, algorithm='HS256')
    return token


def validate_token(token):
    """
    Validate JWT token
    """
    try:
        decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except Exception as e:
        return False
    return True
