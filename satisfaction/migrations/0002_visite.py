# Generated by Django 4.2 on 2024-12-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("satisfaction", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visite",
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
                ("code", models.CharField(max_length=20)),
            ],
        ),
    ]
