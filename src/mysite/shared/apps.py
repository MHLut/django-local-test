from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SharedAppConfig(AppConfig):
    """Configuration for the shared app."""

    name = "mysite.shared"
    verbose_name = _("Shared")
