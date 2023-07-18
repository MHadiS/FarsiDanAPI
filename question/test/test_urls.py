import pytest
from django.urls import reverse, resolve

from question.urls import urlpatterns
from question.views import get_attributes, get_questions


@pytest.fixture(scope="session")
def urls():
    URLS = {url.name: url.callback for url in urlpatterns}  # all of urls in question app : {'questions': '/questions/', ....}
    print(URLS)
    return URLS
    

def test_urls_name(urls):
    ACCEPTED_URLS = {
        "get-questions": get_questions,
        "get-attributes": get_attributes,
        "get-attributes-by-id": get_attributes
    }
    
    assert ACCEPTED_URLS == urls