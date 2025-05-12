from django.urls import path

from mysite.core.error_views import raise_error
from mysite.core.views import HomeView, KitchenSinkView


app_name = "core"
urlpatterns = [
    path("error/<int:http_status>/", raise_error, name="raise_error"),
    path("kitchen-sink/", KitchenSinkView.as_view(), name="kitchen_sink"),
    path("", HomeView.as_view(), name="home"),
]
