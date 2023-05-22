from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def chat_view(request, *args, **kwargs):
    # chat stuff here
    context = dict()
    
    return render(request, 'chat/chatHome.html', context)


# this view handles dms.

def dm_view(request, username):
    print(username)
    print(request.user)
    if username == request.user:
        messages.success(request, "Cant talk to yourself!")
        return redirect('search')
    else:
        messages.success(request, "Welcome to chat!")
        return render(request, 'chat/dm.html', {})