from django.urls import path
from .views import get_question


urlpatterns = [
    path('get_q/', get_question, name="get_q")
]
