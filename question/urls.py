from django.urls import path
from .views import get_questions, get_attributes


urlpatterns = [
    path("", get_questions, name="get-questions"),  # get the questions
    path("attributes/<str:category>", get_attributes, name="get-attributes"),  # get some data about filters of questions
    path("attributes/<str:category>/<int:data_id>", get_attributes, name="get-attributes-by-id"),  # get some data about filters of questions
]
