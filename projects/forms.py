from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Project
from employees.models import Employee


class ProjectForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(
            queryset = Employee.objects.all(),
            widget=forms.SelectMultiple(attrs={'id': 'exampleFormcontrolSelect2'})
        )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'})
        )
    deadline = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Project
        fields = ['employees', 'division', 'client', 'description', 'deadline', 'active']
        