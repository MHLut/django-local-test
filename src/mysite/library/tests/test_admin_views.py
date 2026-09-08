from contextlib import suppress
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from mysite.core.logging import MissingVariableError
from mysite.library.models import CodeSnippet


class TodoListAdminViewsTestCase(TestCase):
    """Test case for `CodeSnippet` admin views."""

    def setUp(self):  # noqa: D102
        self.admin_user = get_user_model().objects.create(
            username="admin_user",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        self.snippet = CodeSnippet.objects.create(
            title="Hello",
            language=CodeSnippet.Language.PYTHON,
            contents='print("Hello world!")',
            created_by=self.admin_user,
        )

        self.default_view_paths = [
            ("admin:library_codesnippet_changelist", None),
            ("admin:library_codesnippet_add", None),
            ("admin:library_codesnippet_change", {"object_id": self.snippet.pk}),
            ("admin:library_codesnippet_delete", {"object_id": self.snippet.pk}),
            ("admin:library_codesnippet_history", {"object_id": self.snippet.pk}),
        ]

    def test_default_views_load(self):
        """Check if default admin views load without errors."""
        self.client.force_login(self.admin_user)

        for path_info in self.default_view_paths:
            with self.subTest(path_name=path_info[0]), suppress(MissingVariableError):
                path = reverse(path_info[0], kwargs=path_info[1])
                response = self.client.get(path)

                self.assertEqual(response.status_code, HTTPStatus.OK)
