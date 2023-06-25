from rest_framework_api_key.permissions import HasAPIKey
from utils.custom import JWTMaker, CustomIsAuthenticated
from apps.users.models import User


class APIKeyRequiredMixin(object):
    permission_classes = [HasAPIKey]

class APIKeyAndTokenRequiredMixin(object):
    permission_classes = [HasAPIKey, CustomIsAuthenticated]

    def __init__(self):
        self.jwt_maker = JWTMaker()

    def get_user(self, request):
        headers = request.META
        payload = self.jwt_maker.decode_jwt(
            headers.get("HTTP_AUTHORIZATION")
        )
        user = User.objects.get(email=payload["email"])
        return user
