from django.urls import path
from .views import about, service

urlpatterns = [
    path("about/", about, name="about"),
    path("service/", service, name="service")
]
