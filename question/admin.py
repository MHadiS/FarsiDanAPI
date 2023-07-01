from django.contrib import admin
from .models import Question, Difficulty, QuestionType, RegisteredBook, RegisteredChapter


admin.site.site_header = "مدیریت فارسیدان"
admin.site.register(Difficulty)
admin.site.register(QuestionType)

# Register some models

@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ("title", "difficulty_level", "chapter", "question_type", "accepted_for_exam")
    search_fields = ("title", "text")
    list_filter = ["accepted_for_exam", "difficulty_level", "chapter", "question_type"]


@admin.register(RegisteredBook)
class AdminRegisteredBook(admin.ModelAdmin):
    list_display = ("name", "grade")
    search_fields = ("name",)
    list_filter = ("grade",)


@admin.register(RegisteredChapter)
class AdminRegisteredChapter(admin.ModelAdmin):
    list_display = ("chapter_name", "chapter_number")
    search_fields = ("chapter_name",)
    list_filter = ["chapter_number"]