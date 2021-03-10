from django.http import JsonResponse

from student.models import Student


def get_student_list(request):
    queryset = Student.objects.all()
    data = queryset.values()
    res = {
        "data": list(data)
    }

    return JsonResponse(res)
