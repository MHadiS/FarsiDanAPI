from django.contrib import admin
from .models import Questions


# Register some models
@admin.register(Questions)
class AdminQuestions(admin.ModelAdmin):
    list_display = (
        "title",
        "question_type",
        "difficulty",
        "chapter_no",
        "from_tizhooshan_exam",
        "grade",
        "accepted",
    )
    search_fields = ("title", "text")
    list_filter = (
        "question_type",
        "difficulty",
        "chapter_no",
        "from_tizhooshan_exam",
        "grade",
        "accepted",
    )
