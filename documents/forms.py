from django import forms

from .models import Document


class DocumentUploadForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'})
        )

    class Meta:
        model = Document
        fields = ['document', 'name']

