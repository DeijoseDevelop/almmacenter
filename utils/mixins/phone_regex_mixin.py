from django.core.validators import RegexValidator


class PhoneRegexMixin(object):
    phone_regex = RegexValidator(
        regex=r'^\+?57\d{9}$',
        message="The telephone number must be in the format '+573xxxxxxxx'."
    )