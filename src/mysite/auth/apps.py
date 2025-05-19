from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class AuthAppConfig(AppConfig):
    """Configuration for custom authentication app."""

    name = "mysite.auth"
    label = "mysite_auth"
    verbose_name = pgettext_lazy("App name", "Authentication and Authorization (Custom)")
