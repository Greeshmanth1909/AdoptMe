from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import DirectMessages
from .forms import SendMessage
from django.contrib.auth.models import User
from datetime import date, datetime
from django.contrib.auth import get_user_model

# Create your views here.
def chat_view(request, *args, **kwargs):
    # chat stuff here
    context = dict()
    recent_chats_set = set()
    # get messages from db where logged in user is a sender and add the receiver members to a set
    recent_chats1 = set(DirectMessages.objects.filter(sender=request.user).values_list('receiver', flat=True))
    # same but the other way around.
    recent_chats2 = set(DirectMessages.objects.filter(receiver=request.user).values_list('sender', flat=True))
    recent_chats_list = list(recent_chats1.union(recent_chats2))
    current_users = [get_user_model().objects.get(id=user_id) for user_id in recent_chats_list]
    context['users'] = current_users
    return render(request, 'chat/chatHome.html', context)


# this view handles dms.
def dm_view(request, username):

    # get existing chats from db, if any.
    sender = request.user
    receiver = User.objects.get(username=username)

    old_messages = (DirectMessages.objects.filter(sender=sender, receiver=receiver) | DirectMessages.objects.filter(sender=receiver, receiver=sender)).order_by('date', 'time')

    # dumb way to ensure a newly created chat doesnt crash the server..
    if len(old_messages) == 0:
        chat = DirectMessages(sender=request.user, receiver=receiver, message='', date=date.today(), time=datetime.now())
        chat.save()
        old_messages = (DirectMessages.objects.filter(sender=sender, receiver=receiver) | DirectMessages.objects.filter(sender=receiver, receiver=sender)).order_by('date', 'time')

    chat_id_ref = old_messages.first()
    chat_id_ref1 = chat_id_ref.sender
    chat_id_ref2 = chat_id_ref.receiver

    context = dict()
    context['sender'] = sender
    context['receiver'] = receiver
    context['old_messages'] = old_messages
    context['user'] = request.user
    context['id1'] = chat_id_ref1
    context['id2'] = chat_id_ref2

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