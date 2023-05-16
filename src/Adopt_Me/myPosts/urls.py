from django.urls import path, include
from .views import my_post_view

urlpatterns = [
    path('my posts/', my_post_view)
]