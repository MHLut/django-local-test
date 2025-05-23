# Generated by Django 5.2.dev20241120122318 on 2024-11-25 15:16

import django.db.models.deletion
from django.db import migrations, models

import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=64, verbose_name="name")),
                ("callsign", models.CharField(blank=True, max_length=32, verbose_name="callsign")),
                ("pronouns", models.CharField(blank=True, max_length=16, verbose_name="pronouns")),
                (
                    "date_of_birth",
                    models.DateField(blank=True, null=True, verbose_name="date of birth"),
                ),
                (
                    "address_line_1",
                    models.CharField(blank=True, max_length=64, verbose_name="address line 1"),
                ),
                (
                    "address_line_2",
                    models.CharField(blank=True, max_length=64, verbose_name="address line 2"),
                ),
                ("city", models.CharField(blank=True, max_length=64, verbose_name="city")),
                ("state", models.CharField(blank=True, max_length=2, verbose_name="state")),
                ("zip_code", models.CharField(blank=True, max_length=10, verbose_name="zip code")),
                (
                    "country",
                    django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name="country"),
                ),
                (
                    "phone_number",
                    phone_field.models.PhoneField(blank=True, max_length=31, verbose_name="phone number"),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="email address"),
                ),
                ("notes", models.TextField(blank=True, verbose_name="notes")),
            ],
            options={
                "verbose_name": "person",
                "verbose_name_plural": "people",
            },
        ),
        migrations.CreateModel(
            name="ExtraData",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("label", models.CharField(max_length=32, verbose_name="label")),
                ("value", models.CharField(max_length=32, verbose_name="value")),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="extra_data",
                        to="people.person",
                    ),
                ),
            ],
            options={
                "verbose_name": "extra data",
                "verbose_name_plural": "extra data",
            },
        ),
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("service_name", models.CharField(max_length=32, verbose_name="service name")),
                ("username", models.CharField(max_length=32, verbose_name="username")),
                ("profile_url", models.URLField(verbose_name="profile URL")),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="social_links",
                        to="people.person",
                    ),
                ),
            ],
            options={
                "verbose_name": "social link",
                "verbose_name_plural": "social links",
            },
        ),
    ]
