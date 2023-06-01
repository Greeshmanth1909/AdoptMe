# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chats/(?P<id1>\w+)_(?P<id2>\w+)/$", consumers.ChatConsumer.as_asgi()),
]