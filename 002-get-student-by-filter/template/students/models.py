from django.db import models


class Student(models.Model):
    GENDER_CHOICE = [
        (1, "male"),
        (0, "female")
    ]
    name = models.CharField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICE)
