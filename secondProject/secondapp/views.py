from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def TeacherView(request):
    return HttpResponse("From Teacher app")
