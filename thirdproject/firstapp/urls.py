from django.urls import path
from .views import StudentView, FirstAppView


urlpatterns = [
    path("first/", StudentView, name="first"),
    path("home/", FirstAppView, name="home"),
]
