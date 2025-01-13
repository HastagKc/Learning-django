from django.shortcuts import render
from .models import Registration
from .forms import RegistrationForm

# Create your views here.
def home(request):
  form = RegistrationForm()
  context = {'form':form}
  return render(request, 'main/index.html',context)
