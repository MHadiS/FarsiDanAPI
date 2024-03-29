# Generated by Django 4.1.4 on 2023-05-08 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("question", "0010_question_difficulty_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionType",
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
                (
                    "question_type",
                    models.CharField(max_length=30, verbose_name="نام نوع"),
                ),
            ],
            options={
                "verbose_name": "نوع سوال",
                "verbose_name_plural": "انواع سوال",
            },
        ),
        migrations.AlterField(
            model_name="question",
            name="difficulty_level",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="question.difficulty",
                verbose_name="درجه سختی",
            ),
        ),
    ]
