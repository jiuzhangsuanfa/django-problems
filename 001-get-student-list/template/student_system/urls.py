from django.contrib import admin
from django.urls import path

from student.views import get_student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', get_student_list)
]
