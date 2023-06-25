from django.contrib import admin
from django.contrib.admin import ModelAdmin, register

from apps.users.models import Supplier


@register(Supplier)
class SupplierAdmin(ModelAdmin):

    list_display = (
        'first_name',
        'surname_name',
        'email',
    )
