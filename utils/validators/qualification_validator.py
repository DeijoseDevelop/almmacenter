from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def qualification_validator(value: float):
    if 0.0 < value > 5.0:
        raise ValidationError(
            _('Value must be between 0.0 and 5.0'),
            params={'value': value}
        )
