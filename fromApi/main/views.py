from django.shortcuts import render
# import form 
from .forms import Registration, LoginForm

# Create your views here.

def home(request):
  # creating registration form 
  fm = Registration()
  return render(request, 'main/index.html', {'form':fm})



def login(request):
  # creating object of loginForm
  # format id 
  # fm = LoginForm(auto_id="kc_%s")
  # output
  # <label for="kc_email">Email:</label>
  # <input type="text" name="email" required id="kc_email">

  # both treated as True
  # fm = LoginForm(auto_id="kc") 
  # fm = LoginForm(auto_id=True)
  # output 
  # <label for="email">Email:</label>
  # <input type="text" name="email" required id="email">

  # auto_id = False
  fm = LoginForm(auto_id=False)

  # label-suffix
  # initial
  # field-order
  return render(request, 'main/login.html', {'form':fm})