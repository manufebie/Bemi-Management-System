from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Project
from .models import Division

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
    division = forms.ModelChoiceField(
        help_text = 'Division',
        queryset = Division.objects.all()
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
        fields = ['employees', 'division', 'client', 'name', 'description', 'deadline']
        