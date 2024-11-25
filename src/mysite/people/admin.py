from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mysite.people.models import ExtraData, Person, SocialLink


class SocialLinkInlineAdmin(admin.StackedInline):
    """Inline admin for the `SocialLink` model."""

    model = SocialLink
    extra = 1
    classes = ("collapse",)

    fieldsets = (
        (
            None,
            {
                "fields": ["service_name"],
            },
        ),
        (
            _("Username"),
            {
                "fields": ["username"],
            },
        ),
        (
            _("Profile URL"),
            {
                "classes": ["collapse"],
                "fields": ["profile_url"],
            },
        ),
    )


class ExtraDataInlineAdmin(admin.TabularInline):
    """Inline admin for the `ExtraData` model."""

    model = ExtraData
    extra = 1
    classes = ("collapse",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Primary admin for the `Person` model."""

    fieldsets = (
        (
            None,
            {
                "classes": [],
                "fields": ["name", "callsign", "pronouns", "date_of_birth"],
            },
        ),
        (
            _("Address"),
            {
                "classes": ["collapse"],
                "fields": [
                    "address_line_1",
                    "address_line_2",
                    "city",
                    "state",
                    "zip_code",
                    "country",
                ],
                "description": "Optional description.",
            },
        ),
        (
            _("Contact details"),
            {
                "classes": ["collapse"],
                "fields": ["phone_number", "email"],
            },
        ),
        (
            _("Notes"),
            {
                "classes": ["collapse", "wide"],
                "fields": ["notes"],
            },
        ),
    )

    inlines = (
        SocialLinkInlineAdmin,
        ExtraDataInlineAdmin,
    )
