from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class CodeSnippet(models.Model):
    """A code snippet."""

    class Language(models.TextChoices):
        BASH = "bash", _("Bash")
        CSS = "css", _("CSS")
        HTML = "html", _("HTML")
        JAVASCRIPT = "js", _("JavaScript")
        MAKEFILE = "make", _("Makefile")
        MARKDOWN = "md", _("Markdown")
        PLAINTEXT = "txt", _("Plain text")
        PHP = "php", _("PHP")
        PYTHON = "py", _("Python")
        TYPESCRIPT = "ts", _("TypeScript")

    title = models.CharField(_("title"), max_length=64)
    language = models.CharField(_("language"), max_length=16, choices=Language.choices)
    contents = models.TextField(_("contents"))
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("created_by"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("code snippet")
        verbose_name_plural = _("code snippets")

    def __str__(self):
        return self.title or super().__str__()
