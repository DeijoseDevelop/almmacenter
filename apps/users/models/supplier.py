from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import check_password
from phonenumber_field.modelfields import PhoneNumberField

from .user import User


class Supplier(models.Model):

    first_name = models.CharField(
        _("First Name"),
        max_length=100,
    )

    middle_name = models.CharField(
        _("Middle Name"),
        max_length=100,
        null=True,
        blank=True,
    )

    surname_name = models.CharField(
        _("Surname Name"),
        max_length=100,
    )

    last_name = models.CharField(
        _("Last Name"),
        max_length=100,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
        validators=[
            EmailValidator(),
        ],
    )

    age = models.PositiveIntegerField(
        _("Age"),
        null=True,
        blank=True,
    )

    phone = PhoneNumberField(
        unique=True,
        verbose_name=_("phone number"),
    )

    password = models.CharField(
        _('Password'),
        max_length=128,
    )

    type_user = models.CharField(
        _('Type user'),
        max_length=50,
        default='suplier',
    )

    def get_full_name(self):
        return f"{self.first_name} {self.surname_name}"

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


# @receiver(pre_save, sender=Supplier)
# def update_user_from_supplier(sender, instance, **kwargs):
#     if instance.id is None:
#         try:
#             user = User.objects.get(username=instance.get_full_name())
#         except User.DoesNotExist:
#             user = User.objects.create(
#                 username=instance.get_full_name(),
#                 first_name=instance.first_name,
#                 last_name=instance.surname_name,
#                 email=instance.email,
#                 type_user=instance.type_user,
#             )
#         user.set_password(instance.password)
#         user.is_staff = True
#         # try:
#         #     group = Group.objects.get(name='resort')
#         # except Group.DoesNotExist:
#         #     group = Group.objects.create(name='resort')
#         #     group.permissions.set()
#         # user.groups.add(group)
#         user.save()

