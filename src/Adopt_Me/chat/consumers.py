import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer



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
        print(data)
