from rest_framework import generics

from .models import Questions
from .serializers import QuestionSerializer


def preprocess_prams(dict_query: dict = {}) -> dict:
    """Preprocess the get request's parameter and format it to a dict
    Args:
        dict_query (dict): the get request's parameters in a dict format

    Return:
        dict: processed parameters
    """
    for key, value in dict_query.items():
        value = value.lower()
        if value == "true":
            dict_query[key] = True
        elif value == "false":
            dict_query[key] = False
        elif value in "".join([str(i) for i in range(1, 5)]):
            dict_query[key] = int(value)
    try:
        del dict_query["format"]
    except KeyError:
        pass
    return dict_query


class GetQuestionsView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """Allow user to use url queries for searching in questions

        Returns:
            any: the question user was looking for
        """
        query = preprocess_prams(
            self.request.query_params.dict()
        )  # get the urls prams in dict format
        return Questions.objects.filter(**query).all()


class PostQuestionsView(generics.CreateAPIView):
    """The view for posting questions"""

    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
