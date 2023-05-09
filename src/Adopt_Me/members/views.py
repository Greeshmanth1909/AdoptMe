from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login_view(request, *args, **kwargs):
    return render(request, 'registration/login.html', {})


def registration_view(request, *args, **kwargs):
    form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})