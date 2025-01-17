from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={
        'placeholder':'Enter your name',
        'class':'form-control',
      }),
      'roll':forms.TextInput(attrs={
        'placeholder':'Enter your roll',
        'class':'form-control',
      }),

      'email':forms.EmailInput(attrs={
        'placeholder':'Enter your Email',
        'class':'form-control',
      })
    }