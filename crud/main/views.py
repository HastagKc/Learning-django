from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm



# Create your views here.
 # read
def read(request):
  # querysets 
  students = Student.objects.all()
  print(students)
  context = {'students':students }
  return render(request, 'main/index.html', context)

# create
def add_student(request):
  # empty form 
  if request.method == "POST":
    #  student form with data
     form = StudentForm(request.POST)
     if form.is_valid():
      # 1st way
      # name = form.cleaned_data['name']
      # email = form.cleaned_data['email']
      # age = form.cleaned_data['age']
      # enrollment = form.cleaned_data['enrollment']
      # created_at = form.cleaned_data['created_at']
      # Student.objects.create(
      #    name= name, email= email, age = age, 
      #     enrollment=enrollment, created_at=created_at
      #   )

      # 2nd way
      Student.objects.create(**form.cleaned_data)
      return redirect('read')
      
  else:
    form = StudentForm()
  return render(request, "main/add_student.html",{'form':form})


# update
def update_student(request):
  pass


# delete
def delete_student(request):
  pass


# student details
def student_details(request):
  pass



