from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist

from utils.decorator import check_request_methods
from utils.json_helpers import json_response
from .models import Question, Difficulty, RegisteredChapter, RegisteredBook, QuestionType
from .serializers import QuestionSerializer


class PostQuestionsView(generics.CreateAPIView):
    """The view for posting questions"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def check_queries(queries: dict) -> list:
    """Check the queries( or query-set) of get_questions view

    Args:
        queries (dict): the request queries

    Returns:
        list: errors of the queries
    """

    VALID_QUERIES = ["difficulty_level", "question_type", "chapter"]
    VALID_QUERIES_DATA_TYPE = {
        "difficulty_level": str,
        "question_type": str,
        "chapter": int
    }
    
    errors = []  # a list of errors in queries
    
    for query, data in queries.items():
        # check is the queries valid
        if query not in VALID_QUERIES:
            errors.append(f"'{query}' is not valid (valid queries are {VALID_QUERIES})")        

        current_type = type(data)
        # find the valid type for the query
        try:
            valid_type = VALID_QUERIES_DATA_TYPE[query] 
        except KeyError:
            continue  # if the query isn't valid, it won't exist in VALID_QUERIES_DATA_TYPE so this exception stop the unnecessary errors and continue

        # check is the data type valid
        if current_type is not valid_type:
            errors.append(f"'{query}' query's data type should be {valid_type} not {current_type}")
    
    return errors
    

@check_request_methods(methods=["GET"])
def get_questions(request):
    """Send a list of questions base on your filters

    Args:
        request (HttpRequest): the user request

    Returns:
        json(dict): the questions
    """

    UNNECESSARY_KEYS = ["accepted", "question_type_id", "chapter_id", "difficulty_level_id"]  # the key that going to be deleted
 
    queries = request.GET.dict()  # get the request url queries

    # check the queries
    errors = check_queries(queries)
    if len(errors) != 0: 
        return json_response("error", errors)
    

    # find the values for filtering questions
    try:
        queries["difficulty_level"] = Difficulty.objects.filter(level_name=queries["difficulty_level"]).first()
        queries["question_type"] = QuestionType.objects.filter(question_type=queries["question_type"]).first()
        queries["chapter"] = RegisteredChapter.objects.filter(level_name=queries["chapter"]).first()
    except KeyError:
        pass

    questions = list(Question.objects.filter(**queries).values())  # make a list of filtered questions

    # delete unnecessary keys
    for question in questions:
        for key in UNNECESSARY_KEYS:
            del question[key]
    
    return json_response("success", questions)



@check_request_methods(methods=["GET"])
def get_attributes(request, category, data_id=None):
    """Send the data related to question(object) attributes

    Args:
        request (HttpRequest): the user request
        category (str): the selected attributes categories
        data_id (int, optional): the after selecting category you can select the id of that attribute you want. Defaults to None.

    Returns:
        json: the attribute(s)
    """
    all_of = lambda model : list(model.objects.all().values())  # get all of the records in a table in JSON format
    CATEGORIES = {
        "difficulties": Difficulty,
        "types": QuestionType,
        "chapters": RegisteredChapter,
        "books": RegisteredBook
    }  # registering valid categories

    # check is the category valid or not
    try:
        current_category = CATEGORIES[category]
    except KeyError:
        return json_response("error", f"'{category}' isn't a valid category (valid categories: 'difficulties', 'types', 'chapters', 'books')")

    # if user specified an id, it would return a attribute with that id
    if data_id is not None:
        try:
            data = current_category.objects.get(id=data_id).__dict__  # convert the the data to JSON format
        except ObjectDoesNotExist:
            return json_response("error", "no object found with this id")

        del data["_state"]  # this is an unnecessary key that needs to be removed

        return json_response("success", data)

    return json_response("success", all_of(current_category))
