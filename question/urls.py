from django.urls import path
from .views import PostQuestionsView, get_questions, get_attributes


urlpatterns = [
    path("", get_questions, name="questions"),  # get the questions
    path("attributes/<str:category>", get_attributes, name="attributes"),  # get some data about filters of questions
    path("attributes/<str:category>/<int:data_id>", get_attributes, name="attributes_by_id"),  # get some data about filters of questions
    path("post_q", PostQuestionsView.as_view(), name="post_q"),  # post questions
]
