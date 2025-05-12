from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreAppConfig(AppConfig):
    """Configuration for the core app."""

    name = "mysite.core"
    verbose_name = _("Core")
