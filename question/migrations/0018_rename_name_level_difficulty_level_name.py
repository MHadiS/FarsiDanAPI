# Generated by Django 4.1.4 on 2023-05-27 09:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("question", "0017_alter_difficulty_level_description_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="difficulty",
            old_name="name_level",
            new_name="level_name",
        ),
    ]
