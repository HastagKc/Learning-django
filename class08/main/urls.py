from django.urls import path
from main.views import about, collection, shop

urlpatterns = [
    path("aboutme/", about, name="about"),
    path("collection/", collection, name="collection"),
    path("shop/", shop, name="shop"),
]
