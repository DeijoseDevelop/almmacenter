from django.urls import path
from apps.users.api.views import (
    CreateUserAPIView,
    ValidateIfUserAlreadyExist,
    CreateSupplierAPIView,
    ValidateIfSupplierAlreadyExist,
)


urlpatterns = [
    path(
        "create/",
        CreateUserAPIView.as_view(),
        name="Create User"
    ),
    path(
        "validate/",
        ValidateIfUserAlreadyExist.as_view(),
        name="Validate User"
    ),
    path(
        "supplier/create/",
        CreateSupplierAPIView.as_view(),
        name="Create Supplier"
    ),
    path(
        "supplier/validate/",
        ValidateIfSupplierAlreadyExist.as_view(),
        name="Validate Supplier"
    ),
]

