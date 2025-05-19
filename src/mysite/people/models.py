from django.db import models
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField
from phone_field import PhoneField


class Person(models.Model):
    """A person with their primary contact details and information."""

    name = models.CharField(
        _("name"),
        max_length=64,
    )
    callsign = models.CharField(
        _("callsign"),
        max_length=32,
        blank=True,
    )
    pronouns = models.CharField(
        _("pronouns"),
        max_length=16,
        blank=True,
    )
    date_of_birth = models.DateField(
        _("date of birth"),
        blank=True,
        null=True,
    )

    address_line_1 = models.CharField(
        _("address line 1"),
        max_length=64,
        blank=True,
    )
    address_line_2 = models.CharField(
        _("address line 2"),
        max_length=64,
        blank=True,
    )
    city = models.CharField(
        _("city"),
        max_length=64,
        blank=True,
    )
    state = models.CharField(
        _("state"),
        max_length=2,
        blank=True,
    )
    zip_code = models.CharField(
        _("zip code"),
        max_length=10,
        blank=True,
    )
    country = CountryField(
        _("country"),
        blank=True,
        null=True,
    )

    phone_number = PhoneField(
        _("phone number"),
        blank=True,
    )
    email = models.EmailField(
        _("email address"),
        blank=True,
    )

    notes = models.TextField(
        _("notes"),
        blank=True,
    )

    class Meta:
        verbose_name = _("person")
        verbose_name_plural = _("people")

    def __str__(self):
        parts = [self.name]

        extra_parts = list(filter(None, [self.callsign, self.pronouns]))
        if extra_parts:
            extra = f"({', '.join(extra_parts)})"
            parts.append(extra)

        return " ".join(parts)


class SocialLink(models.Model):
    """A social profile or service linked to a `Person`."""

    person = models.ForeignKey(
        "Person",
        on_delete=models.CASCADE,
        related_name="social_links",
    )
    service_name = models.CharField(
        _("service name"),
        max_length=32,
    )
    username = models.CharField(
        _("username"),
        max_length=32,
    )
    profile_url = models.URLField(
        _("profile URL"),
    )

    class Meta:
        verbose_name = _("social link")
        verbose_name_plural = _("social links")

    def __str__(self):
        return f"{self.username} @ {self.service_name}"


class ExtraData(models.Model):
    """Extra key/value data linked to a `Person`."""

    person = models.ForeignKey(
        "Person",
        on_delete=models.CASCADE,
        related_name="extra_data",
    )
    label = models.CharField(
        _("label"),
        max_length=32,
    )
    value = models.CharField(
        _("value"),
        max_length=32,
    )

    class Meta:
        verbose_name = _("extra data")
        verbose_name_plural = _("extra data")

    def __str__(self):
        return f"{self.label}: {self.value}"
