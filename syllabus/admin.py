from django.contrib import admin

from .models import Syllabus, Tag


# Register some models
@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ("title", "book")
    search_fields = ("title",)
    list_filter = ["book", "tags"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
