from django.test import TestCase, Client
from django.urls import reverse

from question.models import Questions


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.post_q_url = reverse("post_q")
        self.get_q_url = reverse("get_q")
    
    def test_get_q_url_GET_listing_questions(self):
        data = list(Questions.objects.values())
        response = self.client.get(self.get_q_url, {"format": "json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), data)
    
    def test_post_q_POST_posting_question(self):
        new_question = {
            "title": "testing the API",
            "text": "This question is just for testing the software. Don't worry about it.",
            "option_1": "t1",
            "option_2": "t2",
            "option_3": "t3",
            "option_4": "t4",
            "correct_option": 1,
            "question_type": "vocabulary",
            "difficulty": "hard",
            "from_tizhooshan_exam": True,
            "grade": 9,
            "chapter_no": 1
        }
        self.client.post(self.post_q_url, new_question)
        stored_question = Questions.objects.filter(title=new_question["title"])  # finding the posted question in the database
        stored_question_json = stored_question.values()[0]
        del stored_question_json["id"]
        del stored_question_json["accepted"]
        self.assertEqual(new_question, stored_question_json)
        stored_question.delete()
        
        