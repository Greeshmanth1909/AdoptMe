"""edit post form here"""

from upload import models
from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe




class edit_form(ModelForm):
    class Meta:
        model = models.upload_img
        exclude = ["user", "dateTime"]
        widgets = {
            'animal': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'adopted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }