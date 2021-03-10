from django.http import JsonResponse

from student.models import Student


def get_student_list(request):
    # write your code here, to get all informations of student

    data = queryset.values()
    res = {
        "data": list(data)
    }

    return JsonResponse(res)
