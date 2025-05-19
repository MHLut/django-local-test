from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import pgettext_lazy


class CodeSnippet(models.Model):
    """A code snippet."""

    class Language(models.TextChoices):
        BASH = "bash", pgettext_lazy("Programming language", "Bash")
        CSS = "css", pgettext_lazy("Programming language", "CSS")
        HTML = "html", pgettext_lazy("Programming language", "HTML")
        JAVASCRIPT = "js", pgettext_lazy("Programming language", "JavaScript")
        MAKEFILE = "make", pgettext_lazy("Programming language", "Makefile")
        MARKDOWN = "md", pgettext_lazy("Programming language", "Markdown")
        PLAINTEXT = "txt", pgettext_lazy("Programming language", "Plain text")
        PHP = "php", pgettext_lazy("Programming language", "PHP")
        PYTHON = "py", pgettext_lazy("Programming language", "Python")
        TYPESCRIPT = "ts", pgettext_lazy("Programming language", "TypeScript")

    title = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "title"),
        max_length=64,
    )
    language = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "language"),
        max_length=16,
        choices=Language.choices,
    )
    contents = models.TextField(
        verbose_name=pgettext_lazy("Field verbose name", "contents"),
    )
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        verbose_name=pgettext_lazy("Field verbose name", "created_by"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = pgettext_lazy("Object verbose name (singular)", "code snippet")
        verbose_name_plural = pgettext_lazy("Object verbose name (plural)", "code snippets")

    def __str__(self):
        return self.title or super().__str__()

    def get_absolute_url(self):
        """Return the path to the object's detail page."""
        return reverse("library:code_snippet_detail", kwargs={"pk": self.pk})
