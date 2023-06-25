from rest_framework.exceptions import ValidationError


class RequiredField(ValidationError):

    default_code = 400

    def __init__(self, field):
        message = {
            field: ["This field is required."]
        }
        super().__init__(message)
