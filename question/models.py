from django.db import models
from django.core.validators import ValidationError, MinValueValidator, MaxValueValidator


# Add some validators
def states_validator(value: any, states: tuple):
    """The data that can be stored in the cell is limited to several states

    Args:
        value (any): a default argument that have to exist
        states (tuple): the validate states

    Raises:
        ValidationError: if the data wasn't valid, error raises
    """
    if value.lower() not in states:
        raise ValidationError(f"'question_type' just can be {', '.join(states)}")


def question_type_validator(value: any):
    """A validator specific for question_type field

    Args:
        value (any): a default argument that have to exist
    """
    states = ("historical", "diction", "grammar", "vocabulary", "books")
    states_validator(value, states)


def difficulty_validator(value: any):
    """A validator specific for difficulty field

    Args:
        value (_type_): a default argument that have to exist
    """
    states = ("easy", "normal", "hard")
    states_validator(value, states)


class Questions(models.Model):
    title = models.CharField(unique=True, max_length=50)
    text = models.TextField(unique=True)
    option_1 = models.TextField(unique=True)
    option_2 = models.TextField(unique=True)
    option_3 = models.TextField(unique=True)
    option_4 = models.TextField(unique=True)
    correct_option = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(1)]
    )
    question_type = models.CharField(
        max_length=10, validators=[question_type_validator]
    )  # historical, dictation, grammar, vocabulary and books
    difficulty = models.CharField(
        max_length=6, validators=[difficulty_validator]
    )  # easy, normal and hard
    from_tizhooshan_exam = models.BooleanField()
    grade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    chapter_no = models.IntegerField(validators=[MinValueValidator(1)])
    accepted = models.BooleanField()

    def __repr__(self):
        return f"Questions({self.question_type})"
