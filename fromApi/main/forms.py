from django import forms

class Registration(forms.Form):
  name = forms.CharField()
  age = forms.IntegerField()
  address = forms.CharField()
  phone = forms.CharField()
  


class LoginForm(forms.Form):
  email = forms.CharField()
  password = forms.CharField()
