from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PeopleAppConfig(AppConfig):
    """Configuration for the people app."""

    name = "mysite.people"
    verbose_name = _("People")
