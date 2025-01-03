from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse

# Create your views here.


def home(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            # Process form data
            var_name = form.cleaned_data['name']
            var_email = form.cleaned_data['email']
            var_message = form.cleaned_data['message']

            # model.objects.create(name, email, message)
            Contact.objects.create(
                name=var_name, email=var_email, message=var_message
            )

            # form.clean()
            # form = ContactForm()

            # return HttpResponse(f"Thank you {var_name}. Your message sent successfully")
            return render(request, "main/sucess.html")

    return render(request, "main/index.html", {'form': form})
