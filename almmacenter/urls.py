from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView


urlpatterns_endpoints = [
    path(
        "api/v1/users/",
        include("apps.users.api.urls")
    ),
]

urlpatterns = [
    path('', RedirectView.as_view(url="/admin/", permanent=True)),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    *urlpatterns_endpoints,

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

