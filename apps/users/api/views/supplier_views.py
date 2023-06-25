import json

from django.db.models import Q
from django.contrib.auth.hashers import (
    make_password,
    check_password,
)
from rest_framework import generics, views, status
from rest_framework.response import Response

from utils.exceptions import (
    GeneralAPIException,
    RequiredFieldInParams,
    InvalidPassword,
)
from utils.custom import JWTMaker
from utils.mixins import *
from apps.users.api.serializers import (
    CreateSupplierSerializer,
    ValidateSupplierSerializer,
)
from apps.users.models import (
    User,
    Supplier,
)


class CreateSupplierAPIView(APIKeyRequiredMixin, generics.CreateAPIView):
    serializer_class = CreateSupplierSerializer

    def create(self, request, *args, **kwargs):
        jwt_maker = JWTMaker()

        request.data["password"] = make_password(request.data["password"])
        print(request.data)
        if not 'type_user' in request.data:
            raise RequiredFieldInParams('type_user')

        if not 'age' in request.data:
            raise RequiredFieldInParams('age')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response = {
            "token": jwt_maker.generate_jwt({
                "email": serializer.data.get("email")
            }),
            **serializer.data
        }

        self._create_type_user(request.data)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        # return Response({'email': "Login"}, status=status.HTTP_201_CREATED)

    def _create_type_user(self, user: dict):
        user = User.objects.get_or_create(
            first_name=user['first_name'],
            last_name=user['surname_name'],
            email=user['email'],
            phone=user['phone'],
            password=user['password'],
            type_user=user['type_user'],
        )

class ValidateIfSupplierAlreadyExist(APIKeyRequiredMixin, generics.GenericAPIView):

    serializer_class = ValidateSupplierSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')

        if not (email or phone) or not password:
            raise RequiredFieldInParams('email or phone, password')

        try:
            supplier = Supplier.objects.get(Q(email=email) | Q(phone=phone))
            serializer = self.get_serializer(supplier)

            if not supplier.check_password(password):
                raise InvalidPassword()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Supplier.DoesNotExist:
            raise GeneralAPIException(
                detail="Supplier does not exist",
                code=status.HTTP_404_NOT_FOUND,
            )
