from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.


def home(request):
    # Querysets
    # syntax to querysets or all table data
    # ModelName.objects.all()
    all_students = Student.objects.all()
    print(all_students)
    context = {'students': all_students}
    # return render(request, 'core/index.html', context)
    return render(request=request, context=context, template_name="core/index.html")


def add_student(request):
    if request.method == "POST":
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')

        data_added = Student.objects.create(
            roll=roll, name=name,
            address=address, email=email
        )
        if data_added:
            return HttpResponse("Data Inserted")

        else:
            return HttpResponse("Something went wrong")

    return render(request, 'core/addstudent.html')
