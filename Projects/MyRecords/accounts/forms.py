from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class ResgistrationForm(UserCreationForm):
  '''
   This form is responsible for user registration
  '''
 
  email = forms.EmailField(required=True)
  class Meta:
    model = User
    fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists:
      raise forms.ValidationError("They email is already exists")
    return email

  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields.values():
          field.widget.attrs.update({'class': 'form-control'})



class Login(forms.Form):
   username = forms.CharField(
      required=True, 
      widget=forms.TextInput('place')
  )
   password = forms.CharField(
      required=True, 
      label="Password",
      widget=forms.PasswordInput(
         attrs={'placeholder':'Enter your password'}
      )
   ) 
