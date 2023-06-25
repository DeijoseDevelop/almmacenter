from rest_framework import serializers

from apps.users.models import Supplier
from utils.custom import JWTMaker


class CreateSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            'first_name',
            'surname_name',
            'email',
            'phone',
            'age',
            'password',
            'type_user',
        )


class ValidateSupplierSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField("generate_token")

    class Meta:
        model = Supplier
        fields = (
            'id',
            'email',
            'phone',
            'password',
            'token',
        )

    def generate_token(self, supplier):
        jwt_maker = JWTMaker()
        token = jwt_maker.generate_jwt({"email": supplier.email})
        return token


