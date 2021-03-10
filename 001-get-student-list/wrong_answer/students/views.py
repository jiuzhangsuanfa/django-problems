from django.http import JsonResponse

from student.models import StudentsModel


def get_student_list(request):
    queryset = StudentsModel.object.all()
    data = queryset.values()
    res = {
        "data": list(data)
    }

    return JsonResponse(res)
