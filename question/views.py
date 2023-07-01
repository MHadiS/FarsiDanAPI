from django.core.exceptions import ObjectDoesNotExist

from utils.decorator import check_request_methods
from utils.json_helpers import json_response
from .models import Question, Difficulty, RegisteredChapter, RegisteredBook, QuestionType


def check_queries(queries: dict, valid_queries: list, valid_queries_data_type: dict) -> list:
    """Check the queries( or url parameters) of get_questions view

    Args:
        queries (dict): the request queries

    Returns:
        list: errors of the queries
    """
    
    errors = []  # a list of errors in queries
    
    for query, data in queries.items():
        # check is the queries valid
        if query not in valid_queries:
            errors.append(f"'{query}' is not valid (valid queries are {valid_queries})")        
            continue

        current_type = type(data)
        
        # find the valid type for the query
        valid_type = valid_queries_data_type[query] 

        # check is the data type valid
        try:
            queries[query] = valid_type(data)
        except ValueError:
            errors.append(f"'{query}' query's data type should be {valid_type[0].__name__} or {valid_type[1].__name__} not {current_type.__name__} (if the type should be bool use 'True' or 'False')")

    return [errors, queries]


def advanced_filter(model, **filters):
    """Filter a model's data

    Args:
        model (Model): model class

    Returns:
        list: filtered questions
    """
    objects = list(model.objects.all().values())  # an copy of model's data in JSON format

    # filter the data
    for obj in objects:
        for key, value in filters.items():
            # remove the records that need to be removed
            if obj[key] not in value:
                objects.remove(objects)

    return objects
    

@check_request_methods(methods=["GET"])
def get_questions(request):
    """Send a list of questions base on your filters

    Args:
        request (HttpRequest): the user request

    Returns:
        json(dict): the questions
    """

    VALID_QUERIES = ["difficulty_level", "question_type", "chapter", "accepted_for_exam"]
    VALID_QUERIES_DATA_TYPE = {
        "difficulty_level": str,
        "question_type": str,
        "chapter": list,
        "accepted_for_exam": bool
    }
 
    queries = request.GET.dict()  # get the request url queries

    # check the queries
    errors, queries = check_queries(queries, VALID_QUERIES, VALID_QUERIES_DATA_TYPE)
    if len(errors) != 0: 
        return json_response("error", errors)

    questions = advanced_filter(Question, **queries)  # make list of filtered questions

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
