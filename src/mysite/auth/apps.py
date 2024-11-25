from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthAppConfig(AppConfig):
    """Configuration for custom authentication app."""

    name = "mysite.auth"
    label = "mysite_auth"
    verbose_name = _("Authentication and Authorization (Custom)")
