from django.db import models


class Questions(models.Model):
    text = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()
    correct_option = models.IntegerField()
    question_type = models.CharField(max_length=10)  # historical, dictation, grammar, vocabulary and books
    difficulty = models.CharField(max_length=6)  # easy, normal and hard
    from_tizhooshan_exam = models.BooleanField()
    accepted = models.BooleanField()

    def __repr__(self):
        return f"Questions({self.question_type})"
