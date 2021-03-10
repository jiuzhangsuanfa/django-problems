from django.http import HttpRequest, HttpResponse


def get_all_students(request: HttpRequest):
    return HttpResponse(request)
