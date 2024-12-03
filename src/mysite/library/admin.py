from django.contrib import admin

from mysite.library.models import CodeSnippet


@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    """Primary admin for the `CodeSnippet` model."""

    list_display = ("title", "language")
    list_filter = ("language",)
