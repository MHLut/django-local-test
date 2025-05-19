from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class PeopleAppConfig(AppConfig):
    """Configuration for the people app."""

    name = "mysite.people"
    verbose_name = pgettext_lazy("App name", "People")
