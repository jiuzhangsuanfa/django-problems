from django.http import JsonResponse

from student.models import Student


def get_student_detail(request):
    gender = request.GET.get("gender")
    queryset = Student.objects.filter(gender=gender)
    data = queryset.values()
    res = {
        "data": list(data)
    }

    return JsonResponse(res)