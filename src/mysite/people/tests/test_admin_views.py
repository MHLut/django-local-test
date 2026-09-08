from contextlib import suppress
from datetime import date
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from mysite.core.logging import MissingVariableError
from mysite.people.models import ExtraData, Person, SocialLink


class TodoListAdminViewsTestCase(TestCase):
    """Test case for `CodeSnippet` admin views."""

    def setUp(self):  # noqa: D102
        self.admin_user = get_user_model().objects.create(
            username="admin_user",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        self.person = Person.objects.create(
            name="Tester McPerson",
            callsign="McTestFace",
            pronouns="they/them/theirs",
            date_of_birth=date(year=2026, month=9, day=8),
        )
        self.social_link = SocialLink.objects.create(
            person=self.person,
            service_name="django",
            username="McTester",
            profile_url="https://www.djangoproject.com/",
        )
        self.extra_data = ExtraData.objects.create(
            person=self.person,
            label="hello",
            value="world",
        )

        self.default_view_paths = [
            ("admin:people_person_changelist", None),
            ("admin:people_person_add", None),
            ("admin:people_person_change", {"object_id": self.person.pk}),
            ("admin:people_person_delete", {"object_id": self.person.pk}),
            ("admin:people_person_history", {"object_id": self.person.pk}),
        ]

    def test_default_views_load(self):
        """Check if default admin views load without errors."""
        self.client.force_login(self.admin_user)

        for path_info in self.default_view_paths:
            with self.subTest(path_name=path_info[0]), suppress(MissingVariableError):
                path = reverse(path_info[0], kwargs=path_info[1])
                response = self.client.get(path)

                self.assertEqual(response.status_code, HTTPStatus.OK)
