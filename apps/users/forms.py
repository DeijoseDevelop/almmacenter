from django.contrib.auth.forms import AuthenticationForm


class EmailAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.fields['username'].label = "Email"
