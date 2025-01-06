from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
  # querysets 
  # read
  students = Student.objects.all()
  context = {'students':students}
  return render(request, 'main/index.html', context)

  return render(request, 'main/index.html')
