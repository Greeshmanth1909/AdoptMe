from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import DirectMessages
from .forms import SendMessage
from django.contrib.auth.models import User

# Create your views here.
def chat_view(request, *args, **kwargs):
    # chat stuff here
    context = dict()
    
    return render(request, 'chat/chatHome.html', context)


# this view handles dms.

def dm_view(request, username):

    messages.success(request, "Welcome to chat!")

    # get existing chats from db, if any.
    sender = request.user
    receiver = User.objects.filter()
    old_messages = (DirectMessages.objects.filter(sender=sender) | DirectMessages.objects.filter(receiver=receiver)).order_by('date', 'time')
    context = dict()
    context['sender'] = sender
    context['receiver'] = receiver
    context['old_messages'] = old_messages
    # enable text field and send button
    if request.method == 'GET':
        form = SendMessage()
        context['form'] = form
        return render(request, 'chat/dm.html', context)
    else:
        form = SendMessage(request.POST)
        if form.is_valid():
            form.save()
            render(request, 'chat/dm.html', context)
    return render(request, 'chat/dm.html', context)