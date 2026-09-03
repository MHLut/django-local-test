from typing import TYPE_CHECKING

from django.contrib import admin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.request import HttpRequest
from django.urls import path
from django.utils.text import capfirst
from django.utils.translation import pgettext_lazy
from django.views.generic.detail import DetailView

from mysite.todo.models import TodoItem, TodoList


if TYPE_CHECKING:
    from django.http.request import HttpRequest

    from mysite.todo.managers import TodoListQueryset


class TodoItemInline(admin.TabularInline):
    """Model inline admin for `TodoItem`."""

    model = TodoItem
    extra = 1


class TodoListFullDetailView(PermissionRequiredMixin, DetailView):
    """A read-only admin page showing a list and all its items."""

    permission_required = "todo.view_todolist"
    http_method_names = ["get"]  # noqa: RUF012

    model = TodoList
    context_object_name = "todo_list"
    template_name = "admin/todo/todolist/full.html"

    def get_context_data(self, **kwargs):  # noqa: D102
        opts = self.model._meta
        title = pgettext_lazy(
            "Admin page title, TodoList",
            "Full %(verbose_name)s: %(list_title)s"  # noqa: UP031
            % {"verbose_name": opts.verbose_name, "list_title": self.object.title},
        )

        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "title": title,
            "subtitle": None,
            "module_name": str(capfirst(opts.verbose_name_plural)),
            "opts": opts,
        }


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    """Model admin for `TodoList`."""

    list_display = (
        "title",
        "display_num_items",
        "display_num_finished",
        "display_progress",
    )
    search_fields = (
        "title",
        "items__description",
    )
    search_help_text = pgettext_lazy(
        "Admin `search_help_text`, TodoList",
        "Search through list title and its items.",
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

    def get_urls(self):
        """Add custom `Full list` view."""
        return [
            path(
                "<pk>/full/",
                self.admin_site.admin_view(TodoListFullDetailView.as_view()),
                name="todo_todolist_full",
            ),
            *super().get_urls(),
        ]
