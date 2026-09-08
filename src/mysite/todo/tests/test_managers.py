from unittest import mock

from django.test import TestCase

from mysite.todo.managers import TodoListManager, TodoListQueryset
from mysite.todo.models import TodoList


class TodoListManagerTestCase(TestCase):
    """Test case for `TodoListManager`."""

    def test_objects_instance(self):
        """Check if `TodoList.objects` is a `TodoListManager`."""
        self.assertIsInstance(TodoList.objects, TodoListManager)

    def test_get_queryset_instance(self):
        """Check if `TodoListManager.get_queryset()` returns a `TodoListQueryset`."""
        qs = TodoList.objects.all()
        self.assertIsInstance(qs, TodoListQueryset)

    def test_with_item_counts_is_proxy(self):
        """Check if `TodoListManager.with_item_counts()` calls its `TodoListQueryset` counterpart."""
        mock_target = "mysite.todo.managers.TodoListQueryset.with_item_counts"

        with mock.patch(mock_target) as mocked_queryset_method:
            TodoList.objects.with_item_counts()

        self.assertEqual(mocked_queryset_method.call_count, 1)


class TodoListQuerysetTestCase(TestCase):
    """Test case for `TodoListQueryset`."""

    fixtures = ["todolist-test-data"]  # noqa: RUF012

    def test_with_item_counts(self):
        """Test output of `TodoListQueryset.with_item_counts()`."""
        qs = TodoList.objects.with_item_counts()

        self.assertEqual(qs[0].num_items, 5)
        self.assertEqual(qs[0].num_finished, 2)
        self.assertAlmostEqual(qs[0].progress, 40)

        self.assertEqual(qs[1].num_items, 7)
        self.assertEqual(qs[1].num_finished, 2)
        self.assertAlmostEqual(qs[1].progress, 2 / 7 * 100)

        self.assertEqual(qs[2].num_items, 3)
        self.assertEqual(qs[2].num_finished, 2)
        self.assertAlmostEqual(qs[2].progress, 2 / 3 * 100)

        self.assertEqual(qs[3].num_items, 0)
        self.assertEqual(qs[3].num_finished, 0)
        self.assertAlmostEqual(qs[3].progress, 0)

        self.assertEqual(qs[4].num_items, 3)
        self.assertEqual(qs[4].num_finished, 3)
        self.assertAlmostEqual(qs[4].progress, 100)
