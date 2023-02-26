from django.db import models
from django.core.validators import MaxValueValidator


class Syllabuses(models.Model):
    name = models.CharField(max_length=50)  # the file path
    chapter_no = models.PositiveIntegerField(unique=True)
    grade = models.PositiveIntegerField(
        validators=[MaxValueValidator(12)]
    )  # 0 < grade < 13
