from contextlib import suppress
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from mysite.core.logging import MissingVariableError
from mysite.todo.models import TodoItem, TodoList


class TodoListAdminViewsTestCase(TestCase):
    """Test case for `TodoList` admin views."""

    def setUp(self):  # noqa: D102
        self.admin_user = get_user_model().objects.create(
            username="admin_user",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        self.list = TodoList.objects.create(title="Testing tasks")
        TodoItem.objects.create(todo_list=self.list, description="One")
        TodoItem.objects.create(todo_list=self.list, description="Two", completed_at=timezone.now())
        TodoItem.objects.create(todo_list=self.list, description="Three")

        pk = self.list.pk
        self.default_view_paths = [
            ("admin:todo_todolist_changelist", None),
            ("admin:todo_todolist_add", None),
            ("admin:todo_todolist_change", {"object_id": pk}),
            ("admin:todo_todolist_delete", {"object_id": pk}),
            ("admin:todo_todolist_history", {"object_id": pk}),
        ]

    def test_default_views_load(self):
        """Check if default admin views load without errors."""
        self.client.force_login(self.admin_user)

        for path_info in self.default_view_paths:
            with self.subTest(path_name=path_info[0]), suppress(MissingVariableError):
                path = reverse(path_info[0], kwargs=path_info[1])
                response = self.client.get(path)

                self.assertEqual(response.status_code, HTTPStatus.OK)
