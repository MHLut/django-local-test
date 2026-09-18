from django.contrib import admin
from django.urls import include, path

from mysite.admin_custom.views import custom as admin_views


app_name = "admin"
urlpatterns = [
    path("zen/", admin_views.ZenOfPythonAdminView.as_view(), name="zen"),
    path("doc/", include("django.contrib.admindocs.urls")),
    path("", include(admin.site.get_urls())),
]
