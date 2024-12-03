# Generated by Django 5.2.dev20241203005448 on 2024-12-03 11:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CodeSnippet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=64, verbose_name="title")),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("bash", "Bash"),
                            ("css", "CSS"),
                            ("html", "HTML"),
                            ("js", "JavaScript"),
                            ("make", "Makefile"),
                            ("md", "Markdown"),
                            ("txt", "Plain text"),
                            ("php", "PHP"),
                            ("py", "Python"),
                            ("ts", "TypeScript"),
                        ],
                        max_length=16,
                        verbose_name="language",
                    ),
                ),
                ("contents", models.TextField(verbose_name="contents")),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="created_by",
                    ),
                ),
            ],
            options={
                "verbose_name": "code snippet",
                "verbose_name_plural": "code snippets",
            },
        ),
    ]
