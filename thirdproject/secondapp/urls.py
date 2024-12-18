from django.urls import path
from .views import SecondView, GlobalView

urlpatterns = [
    path('second/', SecondView, name="second"),
    path('global/', GlobalView, name="global"),
]
