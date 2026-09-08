from typing import TYPE_CHECKING

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import pgettext_lazy

from mysite.todo.models import TodoItem, TodoList


if TYPE_CHECKING:
    from django.http.request import HttpRequest
    from django.utils.safestring import SafeString

    from mysite.todo.managers import TodoListQueryset


class TodoItemInline(admin.TabularInline):
    """Model inline admin for `TodoItem`."""

    model = TodoItem
    extra = 1


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    """Model admin for `TodoList`."""

    list_display = (
        "title",
        "display_num_items",
        "display_num_finished",
        "display_progress",
        "created_at",
    )
    search_fields = (
        "title",
        "items__description",
    )
    search_help_text = pgettext_lazy(
        "Admin `search_help_text`, TodoList",
        "Search through list titles and item descriptions.",
    )
    date_hierarchy = "created_at"

    inlines = (TodoItemInline,)

    def get_queryset(self, request: "HttpRequest") -> "TodoListQueryset":
        """Add item counts to the queryset."""
        qs: TodoListQueryset = super().get_queryset(request)
        return qs.with_item_counts()

    @admin.display(
        description=pgettext_lazy("Field admin display, TodoList", "num. items"),
        ordering="num_items",
    )
    def display_num_items(self, obj: "TodoList") -> int:
        """Display the number of items in a list."""
        return obj.num_items

    @admin.display(
        description=pgettext_lazy("Field admin display, TodoList", "num. finished"),
        ordering="num_finished",
    )
    def display_num_finished(self, obj: "TodoList") -> int:
        """Display the number of finished items in a list."""
        return obj.num_finished

    @admin.display(
        description=pgettext_lazy("Field admin display, TodoList", "progress"),
        ordering="progress",
    )
    def display_progress(self, obj: "TodoList") -> str:
        """Display the percentage of finished items in a list."""
        precision = 1 if obj.progress % 1 > 0 else 0
        return f"{obj.progress:.{precision}f}%"


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    """Model admin for `TodoItem`."""

    list_display = (
        "description",
        "display_todo_list",
        "is_done",
        "created_at",
    )
    list_filter = (
        "is_done",
        "todo_list",
    )
    search_fields = (
        "description",
        "todo_list__title",
    )
    search_help_text = pgettext_lazy(
        "Admin `search_help_text`, TodoItem",
        "Search through item descriptions and list titles.",
    )
    list_select_related = ("todo_list",)
    date_hierarchy = "created_at"

    @admin.display(
        description=pgettext_lazy("Field admin display, TodoItem", "list"),
        ordering="todo_list",
    )
    def display_todo_list(self, obj: "TodoItem") -> "SafeString":
        """Display a link to the parent `TodoList`."""
        url = reverse("admin:todo_todolist_change", args=(obj.todo_list.pk,))
        return format_html('<a href="{}">{}</a>', url, obj.todo_list.title)
