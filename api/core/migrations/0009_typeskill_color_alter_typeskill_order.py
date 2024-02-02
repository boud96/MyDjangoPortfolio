# Generated by Django 5.0.1 on 2024-02-02 10:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_skill_order_typeskill_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="typeskill",
            name="color",
            field=models.CharField(default="#000000", max_length=7),
        ),
        migrations.AlterField(
            model_name="typeskill",
            name="order",
            field=models.IntegerField(
                default=1,
                unique=True,
                validators=[django.core.validators.MinValueValidator(1)],
            ),
        ),
    ]
