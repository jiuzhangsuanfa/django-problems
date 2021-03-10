from django.db.models.aggregates import Avg, Max, Min, Sum
from django.test import TestCase

from students.models import Student


class StudentsTestCase(TestCase):

    def setUp(self):
        pass

    def test_should_return_avg(self):
        result = self.client.get('/students/').json().get('avg')
        avg_grade_point = Student.objects.aggregate(Avg('grade_point'))
        self.assertEqual(
            result,
            avg_grade_point.get('grade_point__avg'),
        )

    def test_should_return_max(self):
        result = self.client.get('/students/').json().get('max')
        max_grade_point = Student.objects.aggregate(Max('grade_point'))
        self.assertEqual(
            result,
            max_grade_point.get('grade_point__max'),
        )

    def test_should_return_min(self):
        result = self.client.get('/students/').json().get('min')
        min_grade_point = Student.objects.aggregate(Min('grade_point'))
        self.assertEqual(
            result,
            min_grade_point.get('grade_point__min'),
        )

    def test_should_return_sum(self):
        result = self.client.get('/students/').json().get('sum')
        sum_grade_point = Student.objects.aggregate(Sum('grade_point'))
        self.assertEqual(
            result,
            sum_grade_point.get('grade_point__sum'),
        )
