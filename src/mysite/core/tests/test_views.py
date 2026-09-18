from contextlib import suppress
from http import HTTPStatus

from django.test import TestCase, override_settings
from django.urls import reverse


class ViewsTestCase(TestCase):
    """Test case for core views."""

    def setUp(self):  # noqa: D102
        self.error_view_codes = [400, 403, 404, 500]

    def test_home_view_loads(self):
        """Check if the home view loads."""
        path = reverse("core:home")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_kitchen_sink_view_loads(self):
        """Check if the kitchen sink view loads."""
        path = reverse("core:kitchen_sink")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    @override_settings(DEBUG=False)
    def test_error_views_load(self):
        """Check if custom error views load without (template) errors."""
        for code in self.error_view_codes:
            with self.subTest(code=code), suppress(RuntimeError):
                path = reverse("core:raise_error", kwargs={"http_status": code})
                response = self.client.get(path)

                self.assertEqual(response.status_code, code)
