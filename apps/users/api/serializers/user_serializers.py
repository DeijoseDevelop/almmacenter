from rest_framework import serializers

from apps.users.models import User
from utils.custom import JWTMaker


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'phone',
            'password',
        )


class ValidateUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField("generate_token")

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'phone',
            'password',
            'token',
        )

    def generate_token(self, user):
        jwt_maker = JWTMaker()
        token = jwt_maker.generate_jwt({"email": user.email})
        return token


