"""
Custom logging to raise exceptions when template variables are missing.

Original:
https://adamj.eu/tech/2022/03/30/how-to-make-django-error-for-undefined-template-variables/#with-a-logging-filter-that-raises-exceptions
"""

import logging


class MissingVariableError(Exception):
    """
    A variable was missing from a template.

    Used as an alternative to `django.template.base.VariableDoesNotExist`,
    because that exception has some meaning within the template engine.
    """


class MissingVariableErrorFilter(logging.Filter):
    """Turn log messages about missing template variables into exceptions."""

    ignored_prefixes = (
        "unknown",
        # "admin/",
        "auth/",
        "debug_toolbar/",
        "django/",
        "wagtail/",
        "wagtailadmin/",
        "wagtailblog/",
        "wagtailembeds/",
        "wagtailimages/",
        "wagtailsites/",
        "wagtailusers/",
    )

    def filter(self, record):
        """Exclude third-party messages from errors."""
        if record.msg.startswith("Exception while resolving variable "):
            variable_name, template_name = record.args
            if not template_name.startswith(self.ignored_prefixes):
                msg = f"{variable_name!r} missing in {template_name!r}"
                raise MissingVariableError(msg) from None
        return False
