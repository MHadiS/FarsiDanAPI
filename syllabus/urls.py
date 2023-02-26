from django.urls import path
from .views import get_syllabuses


urlpatterns = [path("get_s/<int:chapter_no>/", get_syllabuses, name="get_s")]
