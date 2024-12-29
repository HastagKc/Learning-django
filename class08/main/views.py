from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, 'main/about.html')


def shop(request):
    return render(request, 'main/shop.html')


def collection(request):
    return render(request, 'main/collection.html')
