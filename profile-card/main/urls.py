from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, single_profile


# 1 st method
# urlpatterns = [
#     path('', home, name="home"),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 2nd method
urlpatterns = [
    path('', home, name="home"),
    path('<int:pk>/', single_profile, name="single_profile"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
