from django.shortcuts import render
from upload import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def my_post_view(request, *args, **kwargs):
    # accessing the stored db of uploaded images where stored username is the same as existing users
    post_archieve = models.upload_img.objects.filter(user = request.user)

    context = dict()
    context['total_posts'] = len(post_archieve)
    context['post_archieve'] = post_archieve
    return render(request, 'user_posts/user_posts.html', context)
