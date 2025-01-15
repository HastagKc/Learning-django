from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import StudentForm
from .models import Student

# Create your views here.
# read
def home(request):
  students = Student.objects.all()
  context = {'students':students}
  return render(request, 'main/index.html', context)

# create
def add_student(request):
  '''
  This method is use to add student
  '''
  if request.method =='POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    
  form = StudentForm()
  return render(request, 'main/student_form.html',{'form':form})
 
# update
def update_student(request,pk):
  '''
  This method is use to Update student
  '''
  stu = get_object_or_404(Student,pk = pk)
  if request.method == 'POST':
    form = StudentForm(request.POST, instance=stu)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = StudentForm(instance=stu)
  return render(request, 'main/student_form.html', {'form':form})


# Delete
def delete_student(request,pk):
  stu = get_object_or_404(Student, pk = pk)
  if request.method == 'POST':
    stu.delete()
    return redirect('home')
  
  else:
    return HttpResponse("Method not allowed", status=405)

