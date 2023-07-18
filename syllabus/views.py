from .models import Tag, Syllabus
from utils.decorator import check_request_methods
from utils.json_helpers import json_response


def tags_id(tags_name: list):
    """Get tag's id base on it's name

    Args:
        tags_name (list): the tags names

    Returns:
        list: the tags id
    """
 
    tags = Tag.objects.filter(name__in=tags_name)  # find tags with wanted names

    ids = [tag.pk for tag in tags]  # get their id 

    return ids
    


@check_request_methods(methods=["GET"])
def get_tags(request):
    """Get a list of tags

    Args:
        request (HttpRequest): the client request

    Returns:
        json: an organized list of every tag name and tag id 
    """
    tags = Tag.objects.all()
    return json_response("success", list(tags.values()))


@check_request_methods(methods=["GET"])
def list_syllabuses(request, tags=None):
    """List all of the syllabuses

    Args:
        request (HttpRequest): client request
        tag (str): a tag name. Defaults to None.

    Returns:
        json: a list of syllabuses with wanted tag
    """
    syllabuses = None

    # if 'tags' is None return all of syllabuses
    if tags is None:
        syllabuses = Syllabus.objects.all()

    # if 'tags' isn't 'None' return all of syllabuses with those tags
    else:
        tags = tags_id(tags)

        # if the wanted tags don't exist return an error massage
        if len(tags) == 0:
            return json_response("error", "No syllabus found with this tag")

        syllabuses = Syllabus.objects.filter(tags__in=tags)  # find syllabuses with wanted tags
    
    response = list(syllabuses.values())  # convert 'syllabuses' to serializable data 

    # change some values of syllabuses
    for syllabus in response:
        syllabus_obj = Syllabus.objects.filter(**syllabus).first()
        syllabus["tags"] = list(syllabus_obj.tags.values())
        syllabus["pdf_file"] = syllabus_obj.pdf_file.url
        syllabus["banner"] = syllabus_obj.banner.url
    
    return json_response("success", response)