from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Employee
        fields = ('firstname', 'lastname', 'email', 'password1', 'password2', )