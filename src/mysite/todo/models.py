from typing import ClassVar

from django.db import models
from django.utils.translation import pgettext_lazy

from mysite.todo.managers import TodoListManager


class TodoList(models.Model):
    """A list for items that need to be done."""

    title = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name, TodoList", "title"),
        max_length=32,
    )

    created_at = models.DateTimeField(
        verbose_name=pgettext_lazy("Field verbose name", "created at"),
        auto_now_add=True,
    )

    objects = TodoListManager()

    class Meta:
        indexes: ClassVar = [
            models.Index(fields=["created_at"], name="todo_list_created_at_idx"),
        ]
        verbose_name = pgettext_lazy("Object verbose name (singular)", "to-do list")
        verbose_name_plural = pgettext_lazy("Object verbose name (plural)", "to-do lists")

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    """An item that needs to be done."""

    todo_list = models.ForeignKey(
        to="TodoList",
        verbose_name=pgettext_lazy("Object verbose name (singular)", "to-do list"),
        on_delete=models.CASCADE,
        related_name="items",
    )

    description = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name, TodoItem", "description"),
    )

    completed_at = models.DateTimeField(
        verbose_name=pgettext_lazy("Field verbose name, TodoItem", "completed at"),
        null=True,
        blank=True,
    )

    is_done = models.GeneratedField(
        verbose_name=pgettext_lazy("Field verbose name, TodoItem", "is done"),
        expression=models.Case(
            models.When(completed_at__isnull=False, then=models.Value(True)),
            default=models.Value(False),
            output_field=models.BooleanField(),
        ),
        output_field=models.BooleanField(),
        db_persist=True,
    )

    created_at = models.DateTimeField(
        verbose_name=pgettext_lazy("Field verbose name", "created at"),
        auto_now_add=True,
    )

    class Meta:
        indexes: ClassVar = [
            models.Index(fields=["completed_at"], name="todo_todoitem_completed_at_idx"),
            models.Index(fields=["created_at"], name="todo_todoitem_created_at_idx"),
            models.Index(fields=["is_done"], name="todo_todoitem_is_done_idx"),
        ]
        verbose_name = pgettext_lazy("Object verbose name (singular)", "to-do item")
        verbose_name_plural = pgettext_lazy("Object verbose name (plural)", "to-do items")

    def __str__(self):
        suffix = "(done)" if self.is_done else "(to-do)"
        return f"{self.description} {suffix}"
