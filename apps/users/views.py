from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from apps.users.forms import EmailAuthenticationForm
from apps.users.forms import ExternalAuthForm


class EmailLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'material/admin/auth/login.html'

