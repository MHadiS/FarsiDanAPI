from django.test import SimpleTestCase
from django.urls import reverse, resolve

from question.views import GetQuestionsView, PostQuestionsView


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.post_q_url = reverse("post_q")
        self.get_q_url = reverse("get_q")
        

    def test_get_q_url_resolved(self):
        self.assertEqual(resolve(self.get_q_url).func.view_class, GetQuestionsView)
    
    def test_post_q_url_resolved(self):
        self.assertEqual(resolve(self.post_q_url).func.view_class, PostQuestionsView)