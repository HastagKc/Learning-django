from django.shortcuts import render
from django.http import HttpResponse
# project logic or business logic
# there ways function based view and class based view

# function based view
# function functionName(parametes)


def StudentView(request):
    return HttpResponse("<h2>Hello world, i am comming<h2>")


def FirstAppView(request):
    return render(request, "firstapp/index.html")
