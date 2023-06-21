from typing import Iterable, Optional
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Difficulty(models.Model):
    class Meta:
        verbose_name = "درجه سختی"
        verbose_name_plural = "درجه های سختی"

    level_name = models.CharField(verbose_name="نام درجه", max_length=20, unique=True)
    level_description= models.TextField(verbose_name="توضیحات مربوط به درجه", blank=True)

    def __str__(self) -> str:
        return self.level_name


class RegisteredBook(models.Model):
    class Meta:
        verbose_name = "کتاب ثبت شده"
        verbose_name_plural = "کتاب های ثبت شده"

    name = models.CharField(max_length=50, verbose_name="اسم", unique=True)
    grade = models.PositiveIntegerField(
        verbose_name="مقطع تحصیلی",
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    
    def __str__(self) -> str:
        return f"کتاب : {self.name}"


class QuestionType(models.Model):
    class Meta:
        verbose_name = "نوع سوال"
        verbose_name_plural = "انواع سوال"

    question_type = models.CharField(verbose_name="نام نوع", max_length=30, unique=True)

    def __str__(self) -> str:
        return self.question_type


class RegisteredChapter(models.Model):
    class Meta:
        verbose_name = "درس ثبت شده"
        verbose_name_plural = "درس های ثبت شده"

    chapter_name = models.CharField(max_length=50, verbose_name="نام درس")
    chapter_number = models.PositiveIntegerField(
        verbose_name="شماره ی درس",
        validators=[MinValueValidator(1)]
    )
    referenced_book = models.ForeignKey(RegisteredBook, on_delete=models.CASCADE, verbose_name="کتاب مرجع")
    
    def __str__(self) -> str:
        return f"{self.referenced_book.name} : درس {self.chapter_number}"



class Question(models.Model):
    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوالات"

    title = models.CharField(unique=True, max_length=49, verbose_name="عنوان")
    text = models.TextField(unique=True, verbose_name="متن سوال")
    option_1 = models.TextField(verbose_name="گزینه یک")
    option_2 = models.TextField(verbose_name="گزینه دو")
    option_3 = models.TextField(verbose_name="گزینه سه")
    option_4 = models.TextField(verbose_name="گزینه چهار")
    correct_option = models.IntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(1)],
        verbose_name="گزینه صحیح"
    )
    difficulty_level = models.ForeignKey(Difficulty, on_delete=models.CASCADE, verbose_name="درجه سختی")
    chapter = models.ForeignKey(RegisteredChapter, on_delete=models.CASCADE, verbose_name="درس")
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE, verbose_name="نوع سوال")
    accepted = models.BooleanField(verbose_name="تایید شده", default=False)

    def __str__(self) -> str:
        return f"سوال : {self.title}"
