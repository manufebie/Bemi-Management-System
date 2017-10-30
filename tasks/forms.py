import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget

from .models import Task


class TaskCreateForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'})
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'})
    )
    obstacles = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'obsctacles'})
    )
    deadline = forms.DateField(widget=forms.SelectDateWidget())


    class Meta:
        model = Task
        fields = ['name', 'description', 'obstacles', 'deadline']