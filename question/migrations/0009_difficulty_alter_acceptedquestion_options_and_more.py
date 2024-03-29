# Generated by Django 4.1.4 on 2023-05-08 12:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("question", "0008_acceptedquestion_question_delete_questions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Difficulty",
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
                    "name_level",
                    models.CharField(max_length=20, verbose_name="نام درجه"),
                ),
            ],
            options={
                "verbose_name": "درجه سختی",
                "verbose_name_plural": "درجه های سختی",
            },
        ),
        migrations.AlterModelOptions(
            name="acceptedquestion",
            options={
                "verbose_name": "سوال قبول شده",
                "verbose_name_plural": "سوالات قبول شده",
            },
        ),
        migrations.AlterModelOptions(
            name="question",
            options={"verbose_name": "سوال", "verbose_name_plural": "سوالات"},
        ),
        migrations.AlterField(
            model_name="acceptedquestion",
            name="question_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="question.question",
                verbose_name="سوال",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="correct_option",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(4),
                    django.core.validators.MinValueValidator(1),
                ],
                verbose_name="گزینه صحیح",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="option_1",
            field=models.TextField(verbose_name="گزینه یک"),
        ),
        migrations.AlterField(
            model_name="question",
            name="option_2",
            field=models.TextField(verbose_name="گزینه دو"),
        ),
        migrations.AlterField(
            model_name="question",
            name="option_3",
            field=models.TextField(verbose_name="گزینه سه"),
        ),
        migrations.AlterField(
            model_name="question",
            name="option_4",
            field=models.TextField(verbose_name="گزینه چهار"),
        ),
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.TextField(unique=True, verbose_name="متن سوال"),
        ),
        migrations.AlterField(
            model_name="question",
            name="title",
            field=models.CharField(max_length=49, unique=True, verbose_name="عنوان"),
        ),
    ]
