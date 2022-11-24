from django.urls import path
from .views import GetQuestionsView, PostQuestionsView


urlpatterns = [
    path('get_q/', GetQuestionsView.as_view(), name="get_q"),
    path('post_q', PostQuestionsView.as_view(), name="post_q"),
]
