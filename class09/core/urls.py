
from django.urls import path
from core.views import home, add_student
urlpatterns = [
    path("", home, name="home"),
    path("add-student/", add_student, name="add-student"),
]
