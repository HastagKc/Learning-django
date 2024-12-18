from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def SecondView(request):
    return HttpResponse("From Second app")


def GlobalView(request):
    return render(request, 'global.html')
