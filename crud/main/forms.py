from django import forms
from datetime import datetime

class StudentForm(forms.Form):
  name = forms.CharField(max_length=20)
  email = forms.EmailField()
  age = forms.IntegerField()
  enrollment = forms.ChoiceField(
    choices=[
      ('Full-time', 'Full-time'),
      ('Part-time', 'Part-time'),
    ]
  )
  created_at = forms.DateTimeField(
    disabled=True, 
    initial=datetime.now
  )
