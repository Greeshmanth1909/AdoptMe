import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from .models import DirectMessages
from django.contrib.auth.models import User
from datetime import date, datetime


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        text = 'hello ws'
        jsontxt = {
            'text': text
        }
        self.send(json.dumps(jsontxt))
        print('hello world')


    def receive(self, text_data=None, bytes_data=None):
        msg = json.loads(text_data)
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