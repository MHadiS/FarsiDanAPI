from django.urls import path
from .views import PostQuestionsView, get_questions, get_data


urlpatterns = [
    path("", get_questions, name="questions"),  # get the questions
    path("post_q", PostQuestionsView.as_view(), name="post_q"),  # post questions
]
