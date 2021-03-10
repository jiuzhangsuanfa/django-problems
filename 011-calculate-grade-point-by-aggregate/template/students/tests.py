from django.db.models.aggregates import Avg, Max, Min, Sum
from django.test import TestCase

from students.models import Student


class StudentsTestCase(TestCase):

    def setUp(self):
        pass

    def test_should_return_response(self):
        body = self.client.get('/students/').json()
        avg_grade_point = Student.objects.aggregate(Avg('grade_point'))
        max_grade_point = Student.objects.aggregate(Max('grade_point'))
        min_grade_point = Student.objects.aggregate(Min('grade_point'))
        sum_grade_point = Student.objects.aggregate(Sum('grade_point'))
        self.assertEqual(
            body.get('avg'),
            avg_grade_point.get('grade_point__avg'),
        )
        self.assertEqual(
            body.get('max'),
            max_grade_point.get('grade_point__max'),
        )
        self.assertEqual(
            body.get('min'),
            min_grade_point.get('grade_point__min'),
        )
        self.assertEqual(
            body.get('sum'),
            sum_grade_point.get('grade_point__sum'),
        )
