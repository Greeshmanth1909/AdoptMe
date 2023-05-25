from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import DirectMessages
from .forms import SendMessage
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your views here.
def chat_view(request, *args, **kwargs):
    # chat stuff here
    context = dict()

    # get list of all chats of user here
    recent_contacts = DirectMessages.objects.filter(sender=request.user) | DirectMessages.objects.filter(receiver=request.user)
    
    return render(request, 'chat/chatHome.html', context)


# this view handles dms.

def dm_view(request, username):

    # get existing chats from db, if any.
    sender = request.user
    receiver = User.objects.get(username=username)
    print(receiver)
    print(sender)
    old_messages = (DirectMessages.objects.filter(sender=sender, receiver=receiver) | DirectMessages.objects.filter(sender=receiver, receiver=sender)).order_by('date', 'time')
    context = dict()
    context['sender'] = sender
    context['receiver'] = receiver
    context['old_messages'] = old_messages
    context['user'] = request.user
    print(old_messages)
    # enable text field and send button
    if request.method == 'GET':
        form = SendMessage()
        context['form'] = form
        return render(request, 'chat/dm.html', context)
    else:
        form = SendMessage(request.POST)
        if form.is_valid():
            form.instance.sender = request.user
            form.instance.receiver = receiver
            form.instance.date = date.today()
            form.instance.time = datetime.now()
            context['form'] = form
            form.save()
            redirect_path = f'/chats/{username}_chat'
            return redirect(redirect_path)