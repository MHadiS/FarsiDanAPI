# Generated by Django 4.1.7 on 2023-06-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("question", "0018_rename_name_level_difficulty_level_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="accepted_for_exam",
            field=models.BooleanField(
                default=False, verbose_name="تایید شده برای آزمون"
            ),
        ),
    ]