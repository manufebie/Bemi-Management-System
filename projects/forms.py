from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Project

from clients.models import Company
from employees.models import Employee


class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        help_text = 'Project name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '...'})
    )
    employees = forms.ModelMultipleChoiceField(
            help_text = 'Project Team',
            queryset = Employee.objects.all(),
        )
    client = forms.ModelChoiceField(
        help_text = 'Client',
        queryset = Company.objects.all()
    )
    description = forms.CharField(
        help_text='Describe what the client wants',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '...',})
        )
    deadline = forms.DateField(
        help_text = 'Project deadline',
        widget=forms.SelectDateWidget()
        )

    class Meta:
        model = Project
        fields = ['employees', 'client', 'division', 'name', 'description', 'deadline']
        