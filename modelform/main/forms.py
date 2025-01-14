from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    # custom field
    confirm_password = forms.CharField(
        max_length=200,
        label="Enter Your confirm password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Confirm Password',
            }
        )
    )

    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'roll': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your Roll',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email',
                }
            ),
            'age': forms.NumberInput(  # Use NumberInput for age
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your age',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your Password',
                }
            ),
        }

        labels = {
            'name': 'Enter your name',
            'roll': 'Enter your roll',
            'email': 'Enter your email',
            'password': 'Enter your password',
            'age': 'Enter your age',
        }

        error_messages = {
            'name': {
                'required': 'Incorrect name field',
                'max_length': 'More than max length',
            }
        }

    # Field-level validation for age
    def clean_age(self):
        data = self.cleaned_data.get('age')
        if data is None or data <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        return data

    # Form-level validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data  
