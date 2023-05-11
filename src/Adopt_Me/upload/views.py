from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages

# Create your views here.


def upload_view(request, *args, **kwargs):
    if request.method == "POST":
        form = forms.upload_form(request.POST, request.FILES)
        if form.is_valid():
            animal = form.cleaned_data['animal']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']

            user_img =  models.upload_img(animal=animal, image=image, description=description)
            user_img.save()
            messages.success(request, 'upload successful')
            return redirect('')
    else:
        form = forms.upload_form()
        return render(request, 'upload/upload.html', {'form': form})
    