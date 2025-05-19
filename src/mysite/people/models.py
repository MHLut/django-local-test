from django.db import models
from django.utils.translation import pgettext_lazy

from django_countries.fields import CountryField
from phone_field import PhoneField


class Person(models.Model):
    """A person with their primary contact details and information."""

    name = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "name"),
        max_length=64,
    )
    callsign = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "callsign"),
        max_length=32,
        blank=True,
    )
    pronouns = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "pronouns"),
        max_length=16,
        blank=True,
    )
    date_of_birth = models.DateField(
        verbose_name=pgettext_lazy("Field verbose name", "date of birth"),
        blank=True,
        null=True,
    )

    address_line_1 = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "address line 1"),
        max_length=64,
        blank=True,
    )
    address_line_2 = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "address line 2"),
        max_length=64,
        blank=True,
    )
    city = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "city"),
        max_length=64,
        blank=True,
    )
    state = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "state"),
        max_length=2,
        blank=True,
    )
    zip_code = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "zip code"),
        max_length=10,
        blank=True,
    )
    country = CountryField(
        verbose_name=pgettext_lazy("Field verbose name", "country"),
        blank=True,
        null=True,
    )

    phone_number = PhoneField(
        verbose_name=pgettext_lazy("Field verbose name", "phone number"),
        blank=True,
    )
    email = models.EmailField(
        verbose_name=pgettext_lazy("Field verbose name", "email address"),
        blank=True,
    )

    notes = models.TextField(
        verbose_name=pgettext_lazy("Field verbose name", "notes"),
        blank=True,
    )

    class Meta:
        verbose_name = pgettext_lazy("Object verbose name (singular)", "person")
        verbose_name_plural = pgettext_lazy("Object verbose name (plural)", "people")

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
        to="Person",
        on_delete=models.CASCADE,
        related_name="social_links",
    )
    service_name = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "service name"),
        max_length=32,
    )
    username = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "username"),
        max_length=32,
    )
    profile_url = models.URLField(
        verbose_name=pgettext_lazy("Field verbose name", "profile URL"),
    )

    class Meta:
        verbose_name = pgettext_lazy("Object verbose name (singular)", "social link")
        verbose_name_plural = pgettext_lazy("Object verbose name (plural)", "social links")

    def __str__(self):
        return f"{self.username} @ {self.service_name}"


class ExtraData(models.Model):
    """Extra key/value data linked to a `Person`."""

    person = models.ForeignKey(
        to="Person",
        on_delete=models.CASCADE,
        related_name="extra_data",
    )
    label = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "label"),
        max_length=32,
    )
    value = models.CharField(
        verbose_name=pgettext_lazy("Field verbose name", "value"),
        max_length=32,
    )

    class Meta:
        verbose_name = pgettext_lazy("Object verbose name (singular)", "extra data")
        verbose_name_plural = pgettext_lazy("Object verbose name (plural)", "extra data")

    def __str__(self):
        return f"{self.label}: {self.value}"
