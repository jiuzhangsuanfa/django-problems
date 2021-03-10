from django.http import HttpRequest, HttpResponse


def get_all_students(request):
    return HttpResponse(request)
