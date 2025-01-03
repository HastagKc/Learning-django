from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Enter your name")
    email = forms.EmailField(label="Enter your Email")
    message = forms.CharField(
        widget=forms.Textarea,
        label="Enter Your message"
    )
