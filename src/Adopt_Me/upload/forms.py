"""create a django form that enables the user to upload image and description of rescue animal"""

from django import forms
from .models import upload_img

class upload_img_form(forms.ModelForm):
    class Meta:
        model = upload_img
        exclude = ['user', 'dateTime', 'adopted']
        widgets = {
            'animal': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),

        }


