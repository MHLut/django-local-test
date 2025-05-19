from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class CoreAppConfig(AppConfig):
    """Configuration for the core app."""

    name = "mysite.core"
    verbose_name = pgettext_lazy("App name", "Core")
