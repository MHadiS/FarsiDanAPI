from typing import Iterable, Optional
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Difficulty(models.Model):
    class Meta:
        verbose_name = "درجه سختی"
        verbose_name_plural = "درجه های سختی"

    level_name = models.CharField(verbose_name="نام درجه", max_length=20)
    level_description= models.TextField(verbose_name="توضیحات مربوط به درجه", blank=True)

    def __str__(self) -> str:
        return self.level_name


class RegisteredBook(models.Model):
    GRADES = (
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
    )
    class Meta:
        verbose_name = "کتاب ثبت شده"
        verbose_name_plural = "کتاب های ثبت شده"

    name = models.CharField(max_length=50, verbose_name="اسم")
    grade = models.PositiveIntegerField(
        verbose_name="مقطع تحصیلی",
        choices=GRADES
    )
    
    def __str__(self) -> str:
        return f"کتاب : {self.name}"


class QuestionType(models.Model):
    class Meta:
        verbose_name = "نوع سوال"
        verbose_name_plural = "انواع سوال"

    question_type = models.CharField(verbose_name="نام نوع", max_length=30)

    def __str__(self) -> str:
        return self.question_type


class RegisteredChapter(models.Model):
    class Meta:
        verbose_name = "درس ثبت شده"
        verbose_name_plural = "درس های ثبت شده"

    chapter_name = models.CharField(max_length=50, verbose_name="نام درس")
    chapter_number = models.PositiveIntegerField(
        verbose_name="شماره ی درس",
        validators=[MinValueValidator(1)],
    )
    referenced_book = models.ForeignKey(RegisteredBook, on_delete=models.CASCADE, verbose_name="کتاب مرجع")
    
    def __str__(self) -> str:
        return f"{self.referenced_book.name} : درس {self.chapter_number}"



class Question(models.Model):
    OPTIONS = (
        (1, "گزینه یک"),
        (2, "گزینه دو"),
        (3, "گزینه سه"),
        (4, "گزینه چهار"),
    )
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
        verbose_name="گزینه صحیح",
        choices=OPTIONS
    )
    difficulty_level = models.ForeignKey(Difficulty, on_delete=models.CASCADE, verbose_name="درجه سختی", db_column="difficulty_level")
    chapter = models.ForeignKey(RegisteredChapter, on_delete=models.CASCADE, verbose_name="درس", db_column="chapter")
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE, verbose_name="نوع سوال", db_column="question_type")
    accepted_for_exam = models.BooleanField(verbose_name="تایید شده برای آزمون", default=False)

    def __str__(self) -> str:
        return f"سوال : {self.title}" # type: ignore
