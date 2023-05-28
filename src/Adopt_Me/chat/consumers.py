import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from django.db import database_sync_to_async
from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):

    async def connect(self):
        self.username = self.scope['url_route']['kwargs']['username']
        await self.accept()

        await self.send(text_data=json.dumps({
            'message': 'connection successful'
        }))

    async def disconnect(self):
        pass

    async def receive(self, text_data):
        pass
