from rest_framework.exceptions import APIException


class GeneralAPIException(APIException):

    def __init__(self, detail=None, code=None):
        self.status_code = code
        super().__init__(detail, code)
