from django.urls import path

from .views import get_tags, list_syllabuses


urlpatterns = [
    path("get-tags/", get_tags, name="get-tags"),
    path("list/", list_syllabuses, name="get-list"),
    path("list/<str:tag>", list_syllabuses, name="get-filtered-list"),
]


