from .models import Tag, Syllabus
from utils.decorator import check_request_methods
from utils.json_helpers import json_response


def tag_id(tag_name):
    """Get a tag's id base on it's name

    Args:
        tag_name (str): the tag name

    Returns:
        int: the tag id
    """

    # try to find a tag with name 'tag_name'
    try:
        tag_obj = Tag.objects.filter(name=tag_name).first()
    except AttributeError:
        return None

    # if the wanted tag exist return it
    if tag_obj is not None:
        return tag_obj.pk   


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
def list_syllabuses(request, tag=None):
    """List all of the syllabuses

    Args:
        request (HttpRequest): client request
        tag (str): a tag name. Defaults to None.

    Returns:
        json: a list of syllabuses with wanted tag
    """
    syllabuses = None

    # if tag is None return all of syllabuses
    if tag is None:
        syllabuses = Syllabus.objects.all()

    # if there is a tag return all of syllabuses with that tag
    else:
        syllabus_tag = tag_id(tag)

        # if wanted tag doesn't exist return an error massage
        if syllabus_tag is None:
            return json_response("error", "No tag found with this name")

        syllabuses = Syllabus.objects.filter(tags=syllabus_tag)  # find syllabuses with wanted tag
    
    response = list(syllabuses.values())  # convert 'syllabuses' to serializable data 

    # change some values of syllabuses
    for syllabus in response:
        syllabus_obj = Syllabus.objects.filter(**syllabus).first()
        syllabus["tags"] = list(syllabus_obj.tags.values())
        syllabus["pdf_file"] = syllabus_obj.pdf_file.url
        syllabus["banner"] = syllabus_obj.banner.url
    
    return json_response("success", response)