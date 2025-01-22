from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        required=True, 
        label="Enter Your Name", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )
    address = forms.CharField(
        max_length=100, 
        required=True, 
        label="Enter Your Address", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'})
    )
    contact_number = forms.CharField(
        max_length=100, 
        required=True, 
        label="Enter Your Contact Number", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your contact number'})
    )
    email = forms.EmailField(
        required=True, 
        label="Enter Your Email", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        required=True, 
        label="Enter Your Feedback", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your feedback', 'rows': 5})
    )
