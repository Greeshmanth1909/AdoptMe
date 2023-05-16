from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def login_view(request, *args, **kwargs):
    return render(request, 'registration/login.html', {})


def registration_view(request, *args, **kwargs):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})