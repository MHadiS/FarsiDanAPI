from django.db import models
from django.core.validators import ValidationError, MinValueValidator, MaxValueValidator


def categorise_validator(value, categories):
    if value.lower() not in categories:
        raise ValidationError(f"'question_type' just can be {', '.join(categories)}")


class Questions(models.Model):
    text = models.TextField(unique=True)
    option_1 = models.TextField(unique=True)
    option_2 = models.TextField(unique=True)
    option_3 = models.TextField(unique=True)
    option_4 = models.TextField(unique=True)
    correct_option = models.IntegerField(validators=[MaxValueValidator(4),
                                                     MinValueValidator(1)])
    question_type = models.CharField(max_length=10, validators=[
        lambda value: categorise_validator(
            value,
            ("historical", "diction", "grammar", "vocabulary", "books")
        )
    ])  # question just type can be : historical, dictation, grammar, vocabulary and books
    difficulty = models.CharField(max_length=6, validators=[
        lambda value: categorise_validator(
            value,
            ("easy", "normal", "hard")
        )
    ])  # easy, normal and hard
    from_tizhooshan_exam = models.BooleanField()
    grade = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(12)])
    chapter_no = models.IntegerField(validators=[MinValueValidator(1)])
    accepted = models.BooleanField()

    def __repr__(self):
        return f"Questions({self.question_type})"
