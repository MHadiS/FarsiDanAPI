# Generated by Django 4.1.4 on 2023-07-01 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("question", "0021_question_chapter_question_difficulty_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="chapter",
            field=models.ForeignKey(
                db_column="chapter",
                on_delete=django.db.models.deletion.CASCADE,
                to="question.registeredchapter",
                verbose_name="درس",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="correct_option",
            field=models.IntegerField(
                choices=[
                    (1, "گزینه یک"),
                    (2, "گزینه دو"),
                    (3, "گزینه سه"),
                    (4, "گزینه چهار"),
                ],
                verbose_name="گزینه صحیح",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="difficulty_level",
            field=models.ForeignKey(
                db_column="difficulty_level",
                on_delete=django.db.models.deletion.CASCADE,
                to="question.difficulty",
                verbose_name="درجه سختی",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_type",
            field=models.ForeignKey(
                db_column="question_type",
                on_delete=django.db.models.deletion.CASCADE,
                to="question.questiontype",
                verbose_name="نوع سوال",
            ),
        ),
        migrations.AlterField(
            model_name="registeredbook",
            name="grade",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "اول"),
                    (2, "دوم"),
                    (3, "سوم"),
                    (4, "چهارم"),
                    (5, "پنجم"),
                    (6, "ششم"),
                    (7, "هفتم"),
                    (8, "هشتم"),
                    (9, "نهم"),
                    (10, "دهم"),
                    (11, "یازدهم"),
                    (12, "دوازدهم"),
                ],
                verbose_name="مقطع تحصیلی",
            ),
        ),
    ]
