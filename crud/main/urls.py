from django.urls import path

from .views import read, add_student, update_student , delete_student, student_details

urlpatterns = [
  path("",read, name="read"),
  path("add-student/", add_student, name="add-student"),
]
