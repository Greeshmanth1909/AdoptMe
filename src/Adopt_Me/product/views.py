from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def damn(request, *args, **kwargs):
    # the root page is where the user loggs in or registers their account.
    return render(request, 'base.html', {})


def home_view(request, *args, **kwargs):
    # the user will then be routed to their homepage.
    return render()

def search_view(request, *args, **kwargs):
    # this is where the user can search for a rescue animal.
    return render()


def put_view(request, *args, **kwargs):
    # this is where the user can put a rescue animal for adoption.
    return render()


def about_view(request, *args, **kwargs):
    # about page.
    return render()