from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

from apps.users.managers import UserManager


class User(AbstractUser):

    username = None

    email = models.EmailField(
        _("email address"),
        unique=True,
        validators=[
            EmailValidator(),
        ],
    )

    phone = PhoneNumberField(
        unique=True,
        verbose_name=_("phone number"),
    )

    type_user = models.CharField(
        _('Type user'),
        max_length=50,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
