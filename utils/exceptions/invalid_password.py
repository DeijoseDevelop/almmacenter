from rest_framework.exceptions import ValidationError


class InvalidPassword(ValidationError):

    default_code = 400

    def __init__(self):
        message = {
            "password": ["Password is invalid."]
        }
        super().__init__(message)
