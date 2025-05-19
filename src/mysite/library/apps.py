from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class LibraryAppConfig(AppConfig):
    """Configuration for the library app."""

    name = "mysite.library"
    verbose_name = pgettext_lazy("App name", "Library")
