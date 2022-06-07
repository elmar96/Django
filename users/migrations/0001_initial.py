# Generated by Django 4.0.4 on 2022-06-02 17:29

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("FeMale", "FeMale"),
                            ("Other", "Other"),
                        ],
                        max_length=100,
                    ),
                ),
                ("phone_number", models.CharField(max_length=255)),
                ("code_word", models.CharField(max_length=200)),
                (
                    "occupations",
                    models.CharField(
                        choices=[
                            ("Student", "Student"),
                            ("Worker", "Worker"),
                            ("Jobless", "Jobless"),
                            ("Retired", "Retired"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "continents",
                    models.CharField(
                        choices=[
                            ("Asia", "Asia"),
                            ("Africa", "Africa"),
                            ("Europe", "Europe"),
                            ("North America", "North America"),
                            ("South America", "South America"),
                            ("Australia/Oceania", "Australia/Oceania"),
                            ("Antarctica", "Antarctica"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
