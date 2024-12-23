from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LibraryAppConfig(AppConfig):
    """Configuration for the library app."""

    name = "mysite.library"
    verbose_name = _("Library")
