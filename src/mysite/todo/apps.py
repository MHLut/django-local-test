from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class TodoAppConfig(AppConfig):
    """Configuration for the ToDo app."""

    name = "mysite.todo"
    verbose_name = pgettext_lazy("App name", "ToDo")
