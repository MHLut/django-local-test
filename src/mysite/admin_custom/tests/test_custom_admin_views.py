from contextlib import suppress
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from mysite.core.logging import MissingVariableError


class CustomAdminViewsTestCase(TestCase):
    """Test case for custom admin views."""

    def setUp(self):  # noqa: D102
        self.admin_user = get_user_model().objects.create(
            username="admin_user",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        self.regular_user = get_user_model().objects.create(
            username="regular_user",
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )

        self.custom_view_paths = [
            ("admin:zen", None),
        ]

    def test_custom_views_load(self):
        """Check if custom admin views load without errors."""
        self.client.force_login(self.admin_user)

        for path_info in self.custom_view_paths:
            with self.subTest(path_name=path_info[0]):
                path = reverse(path_info[0], kwargs=path_info[1])
                response = self.client.get(path)

                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_custom_views_are_protected(self):
        """Check if non-admin user gets redirected away from custom admin views."""
        self.client.force_login(self.regular_user)

        for path_info in self.custom_view_paths:
            with self.subTest(path_name=path_info[0]), suppress(MissingVariableError):
                path = reverse(path_info[0], kwargs=path_info[1])
                response = self.client.get(path)

                self.assertEqual(response.status_code, HTTPStatus.FOUND)
