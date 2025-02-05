from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm


def user_register(request):
  '''
  user register function is responsible of registration
  '''
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = RegistrationForm()
  return render(request, 'accounts/registration.html', {'form':form})


def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username1')
    password = request.POST.get('password1')
    user = authenticate(request, username=username, password=password)

    if user is not None: 
      login(request, user)
      return redirect('dashboard')
    else:
      return render(request, 'accounts/login.html', {'error':'Invalid Username or Password'})
  return render(request, 'accounts/login.html')

def user_logout(request):
  logout(request)
  return redirect('home')
