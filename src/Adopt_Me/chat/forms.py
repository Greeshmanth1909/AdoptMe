from django.forms import ModelForm
from .models import DirectMessages
from django import forms

class SendMessage(ModelForm):
    class Meta:
        model = DirectMessages
        exclude = ['sender', 'receiver', 'time', 'date']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2, 'placeholder': 'message'})
        }