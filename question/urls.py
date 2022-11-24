from django.urls import path
from .views import get_question, post_question


urlpatterns = [
    path('get_q/', get_question, name="get_q"),
    path('post_q', post_question, name="post_q"),
]
