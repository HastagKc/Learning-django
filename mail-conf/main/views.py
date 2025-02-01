from django.shortcuts import render
from .forms import FeedbackForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from decouple import config

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Get validated form data
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            contact_number = form.cleaned_data['contact_number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email content
            subject = f"Feedback from Mrs/Miss {name}"
            full_message = f"""
            Name: {name}
            Address: {address}
            Contact Number: {contact_number}
            Email: {email}
            Message: {message}
            """

            # Send mail
            try:
                send_mail(
                    subject=subject,
                    message=full_message,
                    from_email=config('EMAIL_HOST_USER'),
                    recipient_list=[
                        config('RECIPIENT_EMAIL'),
                        'chaudharykshittiz950@gmail.com',
                        'unnatidhakal0@gmail.com'
                                     ],
                    fail_silently=False,
                )
                # Redirect to a success page or render a success template
                return render(request, 'main/msg_sent.html')
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            except Exception as e:
                # Log the error if needed and show an error message
                print(f"Error sending email: {e}")
                return HttpResponse("Failed to send email. Please try again later.")

    else:
        form = FeedbackForm()
    return render(request, 'main/index.html', {'form': form})