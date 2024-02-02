# Generated by Django 5.0.1 on 2024-02-02 15:05

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="photos/")),
                (
                    "order",
                    models.IntegerField(
                        default=1,
                        unique=True,
                        validators=[django.core.validators.MinValueValidator(1)],
                    ),
                ),
            ],
            options={
                "ordering": ["-order"],
            },
        ),
    ]
