# Generated by Django 5.0.1 on 2024-02-02 18:38

import markdownfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_project_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="title",
            new_name="company",
        ),
        migrations.AlterField(
            model_name="education",
            name="description",
            field=markdownfield.models.MarkdownField(default=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="job",
            name="description",
            field=markdownfield.models.MarkdownField(),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="about_me",
            field=markdownfield.models.MarkdownField(),
        ),
        migrations.AlterField(
            model_name="skill",
            name="description",
            field=markdownfield.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="skill",
            name="description_cs",
            field=markdownfield.models.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="skill",
            name="description_en",
            field=markdownfield.models.MarkdownField(blank=True, null=True),
        ),
    ]