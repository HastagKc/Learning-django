from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            print(form.errors)  # Debugging: Print errors to the console
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()

    return render(request, 'main/index.html', {'form': form})
