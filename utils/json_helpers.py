from django.http import JsonResponse


def json_response(status, data):
    return JsonResponse({
        "status": status,
        "data": data
    })