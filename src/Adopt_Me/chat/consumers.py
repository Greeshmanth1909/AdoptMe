import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from .models import DirectMessages
from django.contrib.auth.models import User
from datetime import date, datetime
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):

    def connect(self):

        self.id1 = self.scope["url_route"]["kwargs"]["id1"]
        self.id2 = self.scope["url_route"]["kwargs"]["id2"]

        # assigning unique group id
        self.chat_id = f"chat_{self.id1 + self.id2}"
        async_to_sync(self.channel_layer.group_add)(
            self.chat_id, self.channel_name
        )

        self.accept()
        

    def receive(self, text_data=None, bytes_data=None):
        msg = json.loads(text_data)

        # echo message to the group
        sender = msg['sender']
        message = msg['message']

        async_to_sync(self.channel_layer.group_send)(
            self.chat_id, {'type': 'chat_message',
                           'sender': sender, 
                           'message': message,}
        )
        self.process(msg)


    def disconnect(self, code):
        pass

    def process(self, data):
        # save data to data base
        print(data)
        sender = User.objects.get(username=data['sender'])
        receiver = User.objects.get(username=data['receiver'])
        message = DirectMessages()
        message.sender = sender
        message.receiver = receiver
        message.message = data['message']
        message.time = datetime.now()
        message.date = date.today()
        message.save()
        print("save successful")


    def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "sender": sender}))