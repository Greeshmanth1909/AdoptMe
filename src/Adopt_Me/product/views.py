from django.shortcuts import render
from django.http import HttpResponse
from upload import models

# Create your views here.
def home_view(request, *args, **kwargs):
    # the root page is where the user loggs in or registers their account.
    return render(request, 'welcome.html', {})


def post_view(request, *args, **kwargs):
    # this is where the user can put a rescue animal for adoption.
    return render(request, 'post.html', {})


def about_view(request, *args, **kwargs):
    # about page.
    number_adopted = models.upload_img.objects.filter(adopted=True).count()

    return render(request, 'about.html', {'number': number_adopted})