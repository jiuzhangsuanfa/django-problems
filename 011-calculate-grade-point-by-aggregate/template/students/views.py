from django.db.models.aggregates import Avg, Max, Min, Sum
from students.models import Student
from django.http.response import JsonResponse


def aggregate_grade_point(request):
    avg_grade_point = Student.objects.aggregate(Avg('grade_point'))
    max_grade_point = Student.objects.aggregate(Max('grade_point'))
    min_grade_point = Student.objects.aggregate(Min('grade_point'))
    sum_grade_point = Student.objects.aggregate(Sum('grade_point'))
    return JsonResponse({
        'avg': avg_grade_point.get('grade_point__avg'),
        'max': max_grade_point.get('grade_point__max'),
        'min': min_grade_point.get('grade_point__min'),
        'sum': sum_grade_point.get('grade_point__sum'),
    })
