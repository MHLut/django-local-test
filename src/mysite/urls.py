"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import include, path

from mysite.core import error_views


urlpatterns = [
    path("forms-galore/", include("mysite.forms_galore.urls")),
    path("library/", include("mysite.library.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("", include("mysite.core.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

handler400 = error_views.http_400_bad_request_view
handler403 = error_views.http_403_forbidden_view
handler404 = error_views.http_404_not_found_view
handler500 = error_views.http_500_internal_server_error_view
