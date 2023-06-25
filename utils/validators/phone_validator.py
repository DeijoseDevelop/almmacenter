from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    regex=r'^\+?57\d{10}$',
)