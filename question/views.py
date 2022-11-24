from django.http import JsonResponse, HttpRequest
from django.core.exceptions import FieldError, ValidationError
from .models import Questions
from utils.decorator import check_methods, error_handling

from random import randint


def question_to_json(question) -> dict:
    """Convert a question object data to json
        Args:
            question: the question objects

        Return:
            dict: the json result
    """
    return {
        "id": question.id,
        "text": question.text,
        "options": (question.option_1,
                    question.option_2,
                    question.option_3,
                    question.option_4),
        "correct_option_index": question.correct_option - 1,
        "question_type": question.question_type,
        "difficulty": question.difficulty,
        "tizhooshan": question.from_tizhooshan_exam,
        "accepted": question.accepted
    }


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
    return dict_query


@error_handling(exceptions=(FieldError, ValidationError))
@check_methods(methods=["GET"])
def get_question(request: HttpRequest):
    """Get a question from database with the mentioned attributes in request's parameters
        Args:
            request (django.http.HttpRequest): the request

        Return:
            Json: a json response that include the question data
    """

    dict_query = preprocess_prams(request.GET.dict())  # process the parameters
    query = Questions.objects.filter(**dict_query).all()  # filter the mentioned record
    results_number = query.count()
    if results_number == 0:
        return JsonResponse({
            "status": "error",
            "message": "There is no results"
        })
    # choosing a random result
    index = randint(0, results_number - 1)
    question = query[index]

    return JsonResponse({
        "status": "success",
        "data": {"question": question_to_json(question)}
    })


@error_handling(exceptions=(FieldError, ValidationError))
@check_methods(methods=["POST"])
def post_question(request: HttpRequest):
    question_json = request.POST.dict()
    question_json["accepted"] = False

    new_question = Questions(**question_json)
    new_question.save()

    return JsonResponse({
        "status": "success",
        "data": question_json
    })
