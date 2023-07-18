from django.urls import path, register_converter

from .views import get_tags, list_syllabuses
from utils.converter import ListConverter


register_converter(ListConverter, "list")


urlpatterns = [
    path("get-tags/", get_tags, name="get-tags"),
    path("list/", list_syllabuses, name="get-list"),
    path("list/<list:tags>", list_syllabuses, name="get-filtered-list"),
]


