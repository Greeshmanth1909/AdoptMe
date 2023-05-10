"""create a django form that enables the user to upload image and description of rescue animal"""

from django import forms

class upload_form(forms.Form):
    animal = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField()
    