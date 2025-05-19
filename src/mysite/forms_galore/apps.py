from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class FormsGaloreAppConfig(AppConfig):
    """Configuration for the forms_galore app."""

    name = "mysite.forms_galore"
    verbose_name = pgettext_lazy("App name", "Forms galore")
