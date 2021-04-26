from django import forms
from .models import *

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publications
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}, ),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }

