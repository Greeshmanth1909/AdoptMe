from django.shortcuts import render, redirect
from .forms import upload_img_form
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def upload_view(request, *args, **kwargs):
    context = dict()
    form = upload_img_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return render(request, 'upload/success.html', {})

    context['form'] = form
    return render(request, 'upload/upload.html', context)
