"""create a django form that enables the user to upload image and description of rescue animal"""

from django.forms import ModelForm
from .models import upload_img

class upload_img_form(ModelForm):
    class Meta:
        model = upload_img
        fields = '__all__'


