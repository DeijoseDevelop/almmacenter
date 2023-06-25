from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.validators.phone_validator import phone_validator


class AbstractTypeUser(models.Model):

    class Meta:
        abstract = True

    class Gender(models.TextChoices):
        MALE = _("MALE"), _('male')
        FEMALE = _("FEMALE"), _('female')
        OTHER = _("OTHER"), _('other')

    document_number = models.PositiveIntegerField(
        _('Document Number'),
        primary_key=True,
    )

    first_name = models.CharField(
        _('First Name'),
        max_length=100,
    )

    last_name = models.CharField(
        _('Last Name'),
        max_length=100,
    )

    born_date = models.DateField(
        _("Born Date"),
    )

    address = models.TextField(
        _("Address"),
    )

    email = models.EmailField(
        _("Email"),
        unique=True,
    )

    phone = models.CharField(
        _("Phone"),
        max_length=13,
        validators=[phone_validator]
    )

    gender = models.CharField(
        _("Gender"),
        max_length=6,
        choices=Gender.choices,
        default=Gender.OTHER,
    )

    profile_picture = models.ImageField(
        _("Profile Picture"),
        upload_to='media/profile/',
        null=True,
        blank=True,
    )
