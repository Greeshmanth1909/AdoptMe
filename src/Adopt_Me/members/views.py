from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
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