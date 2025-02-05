from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('our-history/', our_history, name='our-history'),
    path('services/', services, name='services'),
    path('news-notice/',news_notices, name='news-notice'),
    path('contact-us/', contactus, name='contact-us'),
]
