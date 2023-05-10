from django.shortcuts import render
from . import forms

# Create your views here.


def upload_view(request, *args, **kwargs):
    form = forms.upload_form()
    return render(request, 'upload/upload.html', {'form': form}) 