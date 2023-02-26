from django.http import HttpResponse, Http404
import os
import mimetypes

from .models import Syllabuses
from utils.decorator import check_methods


@check_methods(methods=["GET"])
def get_syllabuses(request, chapter_no: int):
    """Send the syllable(in .pdf format) of a specific chapter

    Args:
        request (any): the user request
        chapter_no (int): the chapter number

    Raises:
        Http404: when the file doesn't exist

    Returns:
        response: the syllable pdf
    """
    directory = os.path.abspath("syllabus") + "\\syllabuses\\"
    syllabus = Syllabuses.objects.filter(chapter_no=chapter_no).first()

    try:
        file_path = directory + syllabus.name
    except AttributeError:
        raise Http404()

    if not os.path.exists(file_path):
        raise Http404

    mime_type, _ = mimetypes.guess_type(file_path)
    with open(file_path, "rb") as f:
        response = HttpResponse(f.read(), content_type=mime_type)
        response["Content-Disposition"] = f"inline; filename={syllabus.name}"
    return response
