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


    def disconnect(self, code):
        pass
