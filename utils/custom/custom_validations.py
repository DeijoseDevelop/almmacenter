from django.conf import settings
from django.utils import timezone
from rest_framework import permissions

from apps.users.models import User
from utils.custom import JWTMaker, TokenStatus
from utils.constants import *


class CustomIsAuthenticated(permissions.BasePermission):

    def __init__(self):
        self.jwt_maker = JWTMaker()

    def has_permission(self, request, view):
        headers = request.META

        if (not "HTTP_AUTHORIZATION" in headers):
            return False

        payload = self.jwt_maker.decode_jwt(
            headers.get("HTTP_AUTHORIZATION")
        )

        if payload == TokenStatus.expired or payload == TokenStatus.invalid:
            return False

        if not User.objects.filter(email=payload["email"]).exists():
            return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

