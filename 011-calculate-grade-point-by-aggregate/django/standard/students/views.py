from django.db.models.aggregates import Avg, Max, Min, Sum
from students.models import Student
from django.http.response import JsonResponse


def aggregate_grade_point(request):

    return JsonResponse(
        Student.objects.aggregate(
            avg=Avg('grade_point'),
            max=Max('grade_point'),
            min=Min('grade_point'),
            sum=Sum('grade_point'),
        ),
    )
