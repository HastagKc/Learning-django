from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  class Meta:
    model = User
    fields = ['first_name','last_name', 'username' ,'email' ,'password1', 'password2']

  # clean function is used to validate fields
  # syntax
  # def clean_email(self):
  #   pass
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
      raise forms.ValidationError("This Email is already exists")
    return email
  
  # init function 
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs.update({'class':'form-control'})