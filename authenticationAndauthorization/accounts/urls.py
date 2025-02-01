from django.urls import path
# from .views import user_login, user_logout, user_register, dashboard
# from accounts.views import user_login, user_logout ,user_register, dashboard
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]



