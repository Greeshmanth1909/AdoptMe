from django.shortcuts import render
from .access import db_objects
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def feed_view(request, *args, **kwargs):
    context = dict()
    context['data'] = db_objects
    context['user'] = request.user
    return render(request, 'post/display.html', context)