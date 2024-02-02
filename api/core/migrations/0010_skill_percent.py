# Generated by Django 5.0.1 on 2024-02-02 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_typeskill_color_alter_typeskill_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="skill",
            name="percent",
            field=models.IntegerField(
                default=100,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
