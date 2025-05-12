from django.urls import path

from mysite.core.error_views import raise_error
from mysite.core.views import HomeView


app_name = "core"
urlpatterns = [
    path("error/<int:http_status>/", raise_error, name="raise_error"),
    path("", HomeView.as_view(), name="home"),
]
