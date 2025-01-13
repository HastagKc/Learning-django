from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
  # custom field
  confirm_password = forms.CharField(
    max_length=200,
    label="Enter Your confirm password",
    widget= forms.PasswordInput(
      attrs={
        'class':'form-control',
        'placeholder':'Enter Your Confirm Password',
      }
    )
  )

  # address = forms.CharField(max_length=200)
  class Meta:
    model = Registration
    # fields = ()
    # specific fields
    # fields = ['name','age','email','password']
    fields = '__all__'
    # exclude = ['roll','age']
    # widgets
    widgets = {
        'roll':forms.TextInput(
        attrs={
          'class':'form-control',
          'placeholder':'Enter your Roll ',
        }
      ),
        'name':forms.TextInput(
        attrs={
          'class':'form-control',
          'placeholder':'Enter your name',
        }
      ),
         'email':forms.TextInput(
        attrs={
          'class':'form-control',
          'placeholder':'Enter your email',
        }
      ),
         'age':forms.TextInput(
        attrs={
          'class':'form-control',
          'placeholder':'Enter your age',
        }
      ),

      'password':forms.PasswordInput(
        attrs={
          'class':'form-control',
          'placeholder':'Enter your Password',
        }
      ),

    }

    # label
    labels = {
      'name':'Enter your name',
      'roll':'Enter your roll',
      'email':'Enter your email',
      'passwod':'Enter your passwod',
       'age':'Enter your passwod',
    }

    # error messages
    error_messages = {
      'name': {
        'required':'incorrect name field',
        'max_length':'More than max length',
      }
    }









   


  




 

