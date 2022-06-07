# Generated by Django 4.0.4 on 2022-06-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Cars",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Eda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
    ]
