# Generated by Django 4.1.3 on 2022-11-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_questions_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='chapter_no',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='grade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='accepted',
            field=models.BooleanField(),
        ),
    ]
