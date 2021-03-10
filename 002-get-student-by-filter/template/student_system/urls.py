from django.contrib import admin
from django.urls import path

from student.views import get_student_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', get_student_detail),
]
