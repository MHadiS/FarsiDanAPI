from django.db import models

from question.models import RegisteredBook


class Tag(models.Model):
    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ ها"

    name = models.CharField(max_length=10, unique=True, verbose_name="نام")

    def __str__(self) -> str:
        return self.name


class Syllabus(models.Model):
    class Meta:
        verbose_name = "جزوه"
        verbose_name_plural = "جزوه ها"
    
    title = models.CharField(max_length=20, verbose_name="عنوان")
    book = models.ForeignKey(RegisteredBook, on_delete=models.CASCADE, verbose_name="کتاب")
    tags = models.ManyToManyField(Tag, verbose_name="تگ ها")
    pdf_file = models.FileField(upload_to="syllabuses", verbose_name="فایل pdf")
    banner = models.ImageField(default="banners/default.jpg", upload_to="banners", verbose_name="بنر")

    def __str__(self) -> str:
        return f"جزوه : {self.title}"