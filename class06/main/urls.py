from django.urls import path
from .views import learn_django

urlpatterns = [
    path('dj/', learn_django, name="dj"),
]
