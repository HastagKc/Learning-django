from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
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
  return render(request, "main/form.html",{'form':form})


# update
def update_student(request, pk):
   stu = get_object_or_404(Student, pk = pk)
   if request.method == 'POST':
      form = StudentForm(request.POST)
      if form.is_valid():
         for key,value in form.cleaned_data.items():
            setattr(stu, key, value)
         stu.save()
         return redirect("read")
   else:  
      form = StudentForm(
         initial= {
            'name':stu.name,
            'email':stu.email,
            'age':stu.age,
            'enrollment':stu.enrollment,
            'created_at':stu.created_at,
         }
      )
   return render(request, "main/form.html",{'form':form})



# delete

def delete_student(request, id):
    stu = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        stu.delete()
        return redirect('read')
    else:
        return HttpResponse("Method not allowed", status=405)


# student details
def student_details(request, pk):
  stu = get_object_or_404(Student, pk = pk)
  return render(request, 'main/stu_details.html', {'stu':stu})



