from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FormsGaloreAppConfig(AppConfig):
    """Configuration for the forms_galore app."""

    name = "mysite.forms_galore"
    verbose_name = _("Forms galore")
