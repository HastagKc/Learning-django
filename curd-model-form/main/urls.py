from django.urls import path
from .views import home,add_student, update_student,delete_student

urlpatterns = [
    path('', home , name='home'),
    path('add/', add_student, name='add'),
    path('update/<int:pk>/',update_student, name='update'),
    path('delete/<int:pk>/',delete_student, name='delete'),
]
