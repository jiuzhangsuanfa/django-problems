from django.db.models.aggregates import Avg, Max, Min, Sum
from students.models import Student
from django.http.response import JsonResponse


def aggregate_grade_point(request):
    # write your code here

    # you should return a JsonResponse
