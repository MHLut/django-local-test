from django.contrib.admin.apps import AdminConfig


class CustomAdminAppConfig(AdminConfig):
    """Configuration for the custom admin app."""

    default_site = "mysite.admin_custom.admin_site.CustomAdminSite"
