# Generated by Django 4.1.4 on 2023-05-10 11:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question", "0014_registeredbook_difficulty_level_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registeredbook",
            name="name",
            field=models.CharField(max_length=50, verbose_name="اسم"),
        ),
        migrations.AlterField(
            model_name="registeredchapter",
            name="chapter_number",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="شماره ی درس",
            ),
        ),
    ]
