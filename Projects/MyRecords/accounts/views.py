from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ResgistrationForm

# Create your views here.

def home(request):
  return render(request, 'accounts/index.html')

def user_register(request):
    if request.method == "POST":
        form = ResgistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = ResgistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    pass
