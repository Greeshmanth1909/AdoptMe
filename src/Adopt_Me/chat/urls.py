from django.urls import path
from .views import chat_view, dm_view
urlpatterns = [
    path('chats/', chat_view),
    path('chats/<path:username>_chat/', dm_view, name='dm'),
]