from django.http import JsonResponse

from .json_helpers import json_response


def error_handling(exceptions: tuple):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as err:
                return JsonResponse({
                   "status": "error",
                   "message": str(err),
                })
        return wrapper
    return inner


def check_request_methods(methods: list):
    def inner(func):
        def wrapper(*args, **kwargs):
            if args[0].method not in methods:
                return json_response("fail", f"accepted method(s): {methods}")
            return func(*args, **kwargs)
        return wrapper
    return inner
