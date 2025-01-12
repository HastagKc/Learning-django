from django.urls import path

from .views import read, add_student, update_student , delete_student, student_details

urlpatterns = [
  path("",read, name="read"),
  path("add-student/", add_student, name="add-student"),
  path("update-student/<int:pk>/", update_student, name="update-student"),
  path("delete/<int:id>/",delete_student, name="delete"),
    path("student_details/<int:pk>/",student_details, name="student_details"),
]
