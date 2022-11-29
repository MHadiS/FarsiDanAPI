from django.db import models
from django.core.validators import MaxValueValidator


class Syllabuses(models.Model):
    name = models.CharField(max_length=50)
    chapter_no = models.PositiveIntegerField()
    grade = models.PositiveIntegerField(validators=[
        MaxValueValidator(12)
    ])
