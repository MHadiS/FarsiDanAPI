# Generated by Django 4.1.3 on 2022-11-24 21:54

import django.core.validators
from django.db import migrations, models
import question.models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_questions_chapter_no_questions_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='title',
            field=models.CharField(default='A beatuful question', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='chapter_no',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='questions',
            name='correct_option',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='questions',
            name='difficulty',
            field=models.CharField(max_length=6, validators=[question.models.difficulty_validator]),
        ),
        migrations.AlterField(
            model_name='questions',
            name='grade',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_1',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_2',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_3',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option_4',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question_type',
            field=models.CharField(max_length=10, validators=[question.models.question_type_validator]),
        ),
        migrations.AlterField(
            model_name='questions',
            name='text',
            field=models.TextField(unique=True),
        ),
    ]
