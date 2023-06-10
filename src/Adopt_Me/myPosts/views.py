from django.shortcuts import render, get_object_or_404, redirect
from upload import models, forms
from django.contrib.auth.decorators import login_required
from django .contrib import messages

# Create your views here.
@login_required
def my_post_view(request, *args, **kwargs):
    # accessing the stored db of uploaded images where stored username is the same as existing users
    post_archieve = models.upload_img.objects.filter(user = request.user)

    context = dict()
    context['total_posts'] = len(post_archieve)
    context['post_archieve'] = post_archieve
    messages.error(request, "You can post details about your rescue animal here.")
    return render(request, 'user_posts/user_posts.html', context)


@login_required
def edit_view(request, post_id):
    post = get_object_or_404(models.upload_img, id=post_id)

    if request.method == "POST":
        form = forms.upload_img_form(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/my posts/')
    else:
        form = forms.upload_img_form(instance=post)
        return render(request, 'post/editPost.html', {'form': form})