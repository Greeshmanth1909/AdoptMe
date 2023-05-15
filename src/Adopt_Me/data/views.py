from django.shortcuts import render
from .access import db_objects
# Create your views here.


def feed_view(request, *args, **kwargs):
    context = dict()
    context['data'] = db_objects
    return render(request, 'post/display.html', context)