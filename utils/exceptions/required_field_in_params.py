from rest_framework.exceptions import ValidationError


class RequiredFieldInParams(ValidationError):

    default_code = 400

    def __init__(self, field):
        message = {
            field: ["This field in the parameters is required."]
        }
        super().__init__(message)
