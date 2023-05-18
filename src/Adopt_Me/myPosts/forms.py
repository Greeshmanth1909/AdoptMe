"""edit post form here"""

from upload import models
from django.forms import ModelForm

class edit_form(ModelForm):
    class Meta:
        model = models.upload_img
        fields = ['__all__']