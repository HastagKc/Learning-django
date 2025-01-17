from django.shortcuts import render,redirect
# import messages
from django.contrib import messages
from .forms import StudentForm
from .models import Student

# # Create your views here.
# def home(request):
#   # messages framework
#   # 1st way 
#   # messages.add_message(request, messages.SUCCESS, 'Data is successfully inserted')
#   # messages.add_message(request, messages.INFO, 'This is info')
#   # messages.add_message(request, messages.WARNING, 'This is warning')
#   # messages.add_message(request, messages.ERROR, 'This is error')

#   # # 2nd way
#   # messages.success(request, 'This is success')
#   # messages.info(request, 'This is info')
#   # messages.warning(request, 'This is warning')
#   # messages.error(request, 'This is error')
  
#   # # debug
#   # messages.debug(request,"this is debug")
#   # print(messages.get_level(request)) # 20
#   # messages.set_level(request, messages.DEBUG) #10
#   # messages.debug(request,"this is debug after setting level")

#   return render(request, 'main/index.html')



def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student is added successfully.')
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'main/index.html', {'form': form})
