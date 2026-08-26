from django.contrib.admin import AdminSite
from django.utils.translation import pgettext_lazy


class CustomAdminSite(AdminSite):
    """Custom Django admin site for this project."""

    site_title = pgettext_lazy("Admin site title", "Django Local site admin")
    site_header = pgettext_lazy("Admin site header", "Django Local administration")


admin_site = CustomAdminSite()
