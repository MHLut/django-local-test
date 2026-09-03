from typing import Self

from django.db import models
from django.db.models import Count, ExpressionWrapper, F, FloatField, Q
from django.db.models.functions import Cast


class TodoListQueryset(models.QuerySet):
    """Custom manager for `TodoList`."""

    def with_item_counts(self) -> Self:
        """
        Add item counts to the queryset.

        * `num_items`; Integer, total number of items.
        * `num_finished`; Integer, number of completed items.
        * `progress`; Float, percentage of completed items.
        """
        return self.annotate(
            num_items=Count("items"),
            num_finished=Count("items", filter=Q(items__is_done=True)),
            progress=ExpressionWrapper(
                Cast(F("num_finished"), FloatField()) / Cast(F("num_items"), FloatField()) * 100,
                output_field=FloatField(),
            ),
        )


class TodoListManager(models.Manager):
    """Custom manager for `TodoList`."""

    def get_queryset(self) -> TodoListQueryset:
        """Override the default queryset with `TodoListQueryset`."""
        return TodoListQueryset(self.model, using=self._db)

    def with_item_counts(self) -> TodoListQueryset:
        """Proxy for `TodoListQueryset.with_item_counts()`."""
        return self.get_queryset().with_item_counts()
