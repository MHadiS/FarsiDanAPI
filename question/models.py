from django.db import models
from django.core.validators import ValidationError, MinValueValidator, MaxValueValidator


def categorise_validator(value, categories):
    if value.lower() not in categories:
        raise ValidationError(f"'question_type' just can be {', '.join(categories)}")


def question_type_validator(value):
    categorise = ("historical", "diction", "grammar", "vocabulary", "books")
    categorise_validator(value, categorise)


def difficulty_validator(value):
    categorise = ("easy", "normal", "hard")
    categorise_validator(value, categorise)


class Questions(models.Model):
    title = models.CharField(unique=True, max_length=50)
    text = models.TextField(unique=True)
    option_1 = models.TextField(unique=True)
    option_2 = models.TextField(unique=True)
    option_3 = models.TextField(unique=True)
    option_4 = models.TextField(unique=True)
    correct_option = models.IntegerField(validators=[MaxValueValidator(4),
                                                     MinValueValidator(1)])
    question_type = models.CharField(max_length=10, validators=[
        question_type_validator
    ])  # historical, dictation, grammar, vocabulary and books"""
    difficulty = models.CharField(max_length=6, validators=[
        difficulty_validator
    ])  # easy, normal and hard
    from_tizhooshan_exam = models.BooleanField()
    grade = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(12)])
    chapter_no = models.IntegerField(validators=[MinValueValidator(1)])
    accepted = models.BooleanField()

    def __repr__(self):
        return f"Questions({self.question_type})"
