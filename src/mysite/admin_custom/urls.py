from django.contrib import admin
from django.urls import include, path


app_name = "admin"
urlpatterns = [
    path("doc/", include("django.contrib.admindocs.urls")),
    path("", include(admin.site.get_urls())),
]
