import jwt
import enum

from django.conf import settings
from django.utils import timezone

from utils.constants import *


class TokenStatus(enum.Enum):

    valid = "Valid"
    expired = "Expired"
    invalid = "Invalid"

class JWTMaker(object):

    def generate_jwt(self, data: dict):

        payload = {
            "exp": timezone.datetime.now(tz=timezone.utc) + timezone.timedelta(days=365),
            **data,
        }
        encoded_jwt = jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm="HS256",
        )
        return encoded_jwt

    def decode_jwt(self, data: str):

        try:
            decoded_jwt = jwt.decode(
                data,
                settings.JWT_SECRET_KEY,
                algorithms=["HS256"],
                options={"verify_signature": True},
            )
            return decoded_jwt
        except jwt.ExpiredSignatureError:
            return TokenStatus.expired
        except jwt.InvalidSignatureError:
            return TokenStatus.invalid
