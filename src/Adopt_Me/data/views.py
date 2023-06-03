from django.shortcuts import render
# from .access import db_objects
from django.contrib.auth.decorators import login_required
from upload.models import upload_img
# Create your views here.

@login_required
def feed_view(request, *args, **kwargs):
    db_objects = upload_img.objects.all()
    context = dict()
    context['data'] = db_objects
    context['user'] = request.user
    print(db_objects)
    return render(request, 'post/display.html', context)