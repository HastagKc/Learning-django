from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm

# Create your views here.
def user_register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # automatically login after saving form
      login(request, user)
      return redirect('dashboard')
  else:
    form = RegistrationForm()
  return render(request, 'accounts/register.html', {'form':form})


def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None: 
      login(request, user)
      return redirect('dashboard')
    
    else:
      return render(request, 'accounts/login.html', {'error':'Invalid Username or Password'})
  return render(request, 'accounts/login.html')

def user_logout(request):
  logout(request)
  return redirect('dashboard')

def dashboard(request):
  return render(request, 'accounts/index.html')